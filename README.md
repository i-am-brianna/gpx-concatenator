# GPX File Concatenator

This Python script allows you to concatenate multiple GPX (GPS Exchange Format) files into a single GPX file. The script utilizes the `xml.etree.ElementTree` and `xml.dom.minidom` modules for parsing and manipulating XML data.

## Requirements

- Python 3.x

## Usage

1. Place the GPX files you want to concatenate in the `input` directory.
2. Run the script using Python: `python concatenate_gpx.py`.

## Code Explanation

### Importing Modules

```python
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from typing import List
from os import listdir
from os.path import join
import colorsys
```

The script imports the necessary modules:

- `xml.etree.ElementTree` for XML parsing and manipulation.
- `xml.dom.minidom` for prettifying the XML output.
- `List` for type hinting the input file list.
- `listdir` and `join` from `os` for working with file paths.
- `colorsys` for generating distinct colors.

### Generate Distinct Colors

```python
def generate_distinct_colors(num_colors: int) -> List[str]:
    distinct_colors = []
    for i in range(num_colors):
        hue = i / num_colors
        saturation = 0.7
        lightness = 0.5
        rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
        hex_color = '{:02x}{:02x}{:02x}'.format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )
        distinct_colors.append(hex_color)
    return distinct_colors
```

The `generate_distinct_colors` function generates a list of distinct colors in hexadecimal format. It takes the number of colors (`num_colors`) as input and uses the `colorsys` module to convert each color's hue, saturation, and lightness values to an RGB tuple. The RGB values are then converted to hexadecimal format and added to the list of distinct colors.

### Add Color Extensions

```python
def add_color_extensions(trk: ET.Element, color: str) -> None:
    extensions = ET.Element('extensions')
    gpx_style_line = ET.SubElement(extensions, 'gpx_style:line')
    color_element = ET.SubElement(gpx_style_line, 'color')
    color_element.text = color
    trk.append(extensions)
```

The `add_color_extensions` function adds color extensions to a `<trk>` element. It takes an `ET.Element` object (`trk`) and a color string (`color`) as input. The function creates the necessary XML structure for color extensions and appends it to the `<trk>` element.

### Add Coloring Metadata

```python
def add_coloring_metadata(root: ET.Element) -> None:
    namespace_mapping = {
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xmlns': 'http://www.topografix.com/GPX/1/1',
        'xsi:schemaLocation': 'http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd http://www.topografix.com/GPX/gpx_style/0/2 http://www.topografix.com/GPX/gpx_style/0/2/gpx_style.xsd',
        'xmlns:gpxtpx': 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1',
        'xmlns:gpxx': 'http://www.garmin.com/xmlschemas/GpxExtensions/v3',
        'xmlns:gpx_style': 'http://www.topografix.com/GPX/gpx_style/0/2',
        'version': '1.1',
    }
    root.attrib.update(namespace_mapping)
```

The `add_coloring_metadata` function adds coloring metadata to the root element of the GPX file. It takes an `ET.Element` object (`root`) as input and updates its attributes with the appropriate namespace mappings for coloring.

### Concatenate GPX Files

```python
def concatenate_gpx_files(input_files: List[str], output_file: str, enable_metadata: bool, enable_coloring: bool = False) -> None:
    root = ET.Element("gpx")

    if enable_coloring:
        add_coloring_metadata(root)

    first_file = input_files[0]
    tree = ET.parse(first_file)

    if enable_metadata:
        add_metadata(tree, root)

    color_dict: Dict[str, str] = {}
    num_distinct_colors = len(input_files)
    distinct_colors = generate_distinct_colors(num_distinct_colors)
    color_index = 0

    for file in input_files:
        tree = ET.parse(file)
        for trk in tree.findall(".//trk"):
            trkpt_elements = trk.findall(".//trkpt")
            if len(trkpt_elements) >= 2:
                if enable_coloring:
                    name_element = trk.find('name')
                    if name_element is not None:
                        trk_name = name_element.text
                        if trk_name not in color_dict:
                            color_dict[trk_name] = distinct_colors[color_index]
                            color_index += 1
                        color = color_dict[trk_name]
                        add_color_extensions(trk, color)

                root.append(trk)

    xml_string = ET.tostring(root, encoding="utf-8")
    prettified_xml = prettify_xml(xml_string)

    with open(output_file, "w") as f:
        f.write(prettified_xml)
```

The `concatenate_gpx_files` function is responsible for concatenating the GPX files. It takes the following parameters as input:

- `input_files` (List[str]): A list of input file paths.
- `output_file` (str): The output file path.
- `enable_metadata` (bool): A flag indicating whether to include metadata in the output.

The function performs the following steps:

1. Creates the root element for the new GPX file.
2. If `enable_coloring` is `True`, adds coloring metadata to the root.
3. Parses the first input file to obtain the base structure.
4. If `enable_metadata` is `True`, calls the `add_metadata` function to add metadata to the root.
5. Initializes dictionaries and variables for color management.
6. Iterates over each input file and each `<trk>` element.
7. Checks if the `<trk>` element contains at least 2 `<trkpt>` elements.
8. If `enable_coloring` is `True` and a track name is available, assigns a distinct color to the track and adds color extensions.
9. Appends the `<trk>` element to the root.
10. Converts the root element to an XML string and prettifies

it using the `prettify_xml` function.
11. Writes the prettified XML to the output file.

### Add Metadata

```python
def add_metadata(tree: ET.ElementTree, output: ET.Element) -> None:
    metadata = tree.find("metadata")
    if metadata is not None:
        output.append(metadata)
```

The `add_metadata` function takes an `ET.ElementTree` object (`tree`) and an `ET.Element` object (`output`) as input. It finds the metadata element in the input tree and appends it to the output element if it exists.

### Prettify XML

```python
def prettify_xml(xml_string: str) -> str:
    parsed_xml = minidom.parseString(xml_string)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    compact_xml = "\n".join(line for line in pretty_xml.split("\n") if line.strip())
    return compact_xml
```

The `prettify_xml` function takes an XML string (`xml_string`) as input and returns a prettified version of it. It parses the XML string using `minidom.parseString`, applies pretty printing using `toprettyxml`, and removes unnecessary blank lines using a list comprehension.

### File Paths and Execution

```python
input_files = sorted([join("input", file) for file in listdir("input")])
output_file = "output.gpx"

concatenate_gpx_files(input_files, output_file, enable_metadata=True, enable_coloring=True)
```

The script constructs a sorted list of input file paths by joining the "input" directory path with the files present in it. The output file path is set to "output.gpx". Finally, the `concatenate_gpx_files` function is called with the appropriate arguments to perform the concatenation and generate the output file.

Feel free to modify the script as per your needs and file paths.


     _                 _          _                         
    (_)               | |        (_)                        
     _  __ _ _ __ ___ | |__  _ __ _  __ _ _ __  _ __   __ _ 
    | |/ _` | '_ ` _ \| '_ \| '__| |/ _` | '_ \| '_ \ / _` |
    | | (_| | | | | | | |_) | |  | | (_| | | | | | | | (_| |
    |_|\__,_|_| |_| |_|_.__/|_|  |_|\__,_|_| |_|_| |_|\__,_|
                                                        
                                                        