import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from typing import List
from gpx_file import GPXFile
from gpx_colorizer import GPXColorizer


class GPXConcatenator:
    def __init__(self, input_files: List[str], output_file: str, enable_metadata: bool, enable_coloring: bool = False):
        self.input_files = input_files
        self.output_file = output_file
        self.enable_metadata = enable_metadata
        self.enable_coloring = enable_coloring

    def concatenate_files(self):
        root = self._create_gpx_root()
        colorizer = GPXColorizer()  # Create a single colorizer instance

        for file_path in self.input_files:
            gpx_file = GPXFile(file_path)
            if self.enable_coloring:
                tracks = gpx_file.extract_tracks()
                colorizer.colorize_tracks(tracks)

            tracks = gpx_file.extract_tracks()
            for trk in tracks:
                root.append(trk)

        if self.enable_coloring:
            colorizer.add_coloring_metadata(root)

        xml_string = ET.tostring(root, encoding="utf-8")
        prettified_xml = self._prettify_xml(xml_string)

        with open(self.output_file, "w") as f:
            f.write(prettified_xml)

    def _create_gpx_root(self) -> ET.Element:
        root = ET.Element("gpx")
        return root

    def _prettify_xml(self, xml_string: str) -> str:
        parsed_xml = minidom.parseString(xml_string)
        pretty_xml = parsed_xml.toprettyxml(indent="  ")
        compact_xml = "\n".join(
            line for line in pretty_xml.split("\n") if line.strip())
        return compact_xml
