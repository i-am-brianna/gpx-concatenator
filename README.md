# GPX File Concatenator

This code is a Python script that concatenates multiple GPX (GPS Exchange Format) files into a single GPX file. It utilizes the `xml.etree.ElementTree` and `xml.dom.minidom` modules for parsing and manipulating XML data.

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
```

The script imports necessary modules: `xml.etree.ElementTree` for XML parsing, `xml.dom.minidom` for XML prettifying, `List` for type hinting, `listdir` and `join` from `os` for working with file paths.

### Concatenate GPX Files

```python
def concatenate_gpx_files(input_files: List[str], output_file: str, enable_metadata: bool) -> None:
    root = ET.Element("gpx")
    first_file = input_files[0]
    tree = ET.parse(first_file)

    if enable_metadata:
        add_metadata(tree, root)

    track_segment = ET.Element("trkseg")
    root.append(track_segment)

    for file in input_files:
        tree = ET.parse(file)
        for trkpt in tree.findall(".//trkpt"):
            track_segment.append(trkpt)

    xml_string = ET.tostring(root, encoding="utf-8")
    prettified_xml = prettify_xml(xml_string)

    with open(output_file, "w") as f:
        f.write(prettified_xml)
```

The `concatenate_gpx_files` function takes a list of input file paths (`input_files`), an output file path (`output_file`), and a boolean flag (`enable_metadata`) to determine whether to include metadata in the output file.

The function creates a root element for the new GPX file and parses the first input file to obtain the base structure. If `enable_metadata` is `True`, the `add_metadata` function is called to add metadata to the root element.

A track segment element is created and appended to the root. The function iterates over each input file, parses it, and appends all `trkpt` elements to the track segment.

The root element is converted to an XML string and prettified using the `prettify_xml` function. The prettified XML is then written to the output file.

### Add Metadata

```python
def add_metadata(tree: ET.ElementTree, output: ET.Element) -> None:
    metadata = tree.find("metadata")
    if metadata is not None:
        output.append(metadata)
```

The `add_metadata` function takes an `ET.ElementTree` object (`tree`) and an `ET.Element` object (`output`). It finds the metadata element in the input tree and appends it to the output element if it exists.

### Prettify XML

```python
def prettify_xml(xml_string: str) -> str:
    parsed_xml = minidom.parseString(xml_string)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    compact_xml = "\n".join(line for line in pretty_xml.split("\n") if line.strip())
    return compact_xml
```

The `prettify_xml` function takes an XML string (`xml_string`) and returns a prettified version of it. It parses the XML string using `minidom.parseString`, applies

 pretty printing using `toprettyxml`, and removes unnecessary blank lines using a list comprehension.

### File Paths and Execution

```python
input_files = [join("input", file) for file in listdir("input")]
output_file = "output.gpx"

concatenate_gpx_files(input_files, output_file, True)
```

The script constructs a list of input file paths by joining the "input" directory path with the files present in it. The output file path is set to "output.gpx". Finally, the `concatenate_gpx_files` function is called with the appropriate arguments to perform the concatenation and generate the output file.

Feel free to modify the script as per your needs and file paths.
     _                 _          _                         
    (_)               | |        (_)                        
     _  __ _ _ __ ___ | |__  _ __ _  __ _ _ __  _ __   __ _ 
    | |/ _` | '_ ` _ \| '_ \| '__| |/ _` | '_ \| '_ \ / _` |
    | | (_| | | | | | | |_) | |  | | (_| | | | | | | | (_| |
    |_|\__,_|_| |_| |_|_.__/|_|  |_|\__,_|_| |_|_| |_|\__,_|
                                                        
                                                        