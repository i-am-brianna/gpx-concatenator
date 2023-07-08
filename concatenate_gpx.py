import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from typing import List, Dict
from os import listdir
from os.path import join
import colorsys


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


def add_color_extensions(trk: ET.Element, color: str) -> None:
    extensions = ET.Element('extensions')
    gpx_style_line = ET.SubElement(extensions, 'gpx_style:line')
    color_element = ET.SubElement(gpx_style_line, 'color')
    color_element.text = color
    trk.append(extensions)


def add_coloring_metadata(root: ET.Element) -> None:
    namespace_mapping = {
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xmlns': 'http://www.topografix.com/GPX/1/1',
        'xsi:schemaLocation': (
            'http://www.topografix.com/GPX/1/1 '
            'http://www.topografix.com/GPX/1/1/gpx.xsd '
            'http://www.garmin.com/xmlschemas/GpxExtensions/v3 '
            'http://www.garmin.com/xmlschemas/GpxExtensionsv3.xsd '
            'http://www.garmin.com/xmlschemas/TrackPointExtension/v1 '
            'http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd '
            'http://www.topografix.com/GPX/gpx_style/0/2 '
            'http://www.topografix.com/GPX/gpx_style/0/2/gpx_style.xsd'
        ),
        'xmlns:gpxtpx': 'http://www.garmin.com/xmlschemas/TrackPointExtension/v1',
        'xmlns:gpxx': 'http://www.garmin.com/xmlschemas/GpxExtensions/v3',
        'xmlns:gpx_style': 'http://www.topografix.com/GPX/gpx_style/0/2',
        'version': '1.1',
    }
    root.attrib.update(namespace_mapping)


def create_gpx_root(enable_coloring: bool) -> ET.Element:
    root = ET.Element("gpx")
    if enable_coloring:
        add_coloring_metadata(root)
    return root


def add_metadata(tree: ET.ElementTree, output: ET.Element) -> None:
    metadata = tree.find("metadata")
    if metadata is not None:
        output.append(metadata)


def concatenate_gpx_files(input_files: List[str], output_file: str, enable_metadata: bool, enable_coloring: bool = False) -> None:
    root = create_gpx_root(enable_coloring)

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
            if len(trkpt_elements) >= 2 and enable_coloring:
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


def prettify_xml(xml_string: str) -> str:
    parsed_xml = minidom.parseString(xml_string)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    compact_xml = "\n".join(
        line for line in pretty_xml.split("\n") if line.strip())
    return compact_xml


input_files = sorted([join("input", file) for file in listdir("input")])
output_file = "output.gpx"

concatenate_gpx_files(input_files, output_file,
                      enable_metadata=True, enable_coloring=True)
