import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from typing import List
from os import listdir
from os.path import join

def concatenate_gpx_files(input_files: List[str], output_file: str, enable_metadata: bool) -> None:
    root = ET.Element("gpx")
    first_file = input_files[0]
    tree = ET.parse(first_file)
    
    if enable_metadata:
        add_metadata(tree, root)

    for file in input_files:
        tree = ET.parse(file)
        for trk in tree.findall(".//trk"):
            trkpt_elements = trk.findall(".//trkpt")
            if len(trkpt_elements) >= 2:  # Check if "trk" has at least 2 "trkpt" elements
                root.append(trk)

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

input_files = sorted([join("input", file) for file in listdir("input")])
output_file = "output.gpx"

concatenate_gpx_files(input_files, output_file, True)
