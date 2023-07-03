import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from typing import List

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

def add_metadata(tree: ET.ElementTree, output: ET.Element) -> None:
    metadata = tree.find("metadata")
    if metadata is not None:
        output.append(metadata)

def prettify_xml(xml_string: str) -> str:
    parsed_xml = minidom.parseString(xml_string)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    compact_xml = "\n".join(line for line in pretty_xml.split("\n") if line.strip())
    return compact_xml

input_files = ["file1.gpx", "file2.gpx"]
output_file = "concatenated.gpx"

concatenate_gpx_files(input_files, output_file, True)
