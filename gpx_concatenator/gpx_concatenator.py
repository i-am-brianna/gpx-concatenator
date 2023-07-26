import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from typing import List
from gpx_concatenator.gpx_file import GPXFile
from gpx_concatenator.gpx_colorizer import GPXColorizer

class GPXConcatenator:
    """
    A class that concatenates multiple GPX files into a single GPX file.
    """

    def __init__(self, input_files: List[str], output_file: str, enable_metadata: bool, enable_coloring: bool = False):
        """
        Initializes an instance of GPXConcatenator.

        Args:
            input_files (List[str]): List of input file paths to concatenate.
            output_file (str): Output file path to save the concatenated GPX.
            enable_metadata (bool): Flag to enable metadata in the output GPX.
            enable_coloring (bool, optional): Flag to enable track coloring. Defaults to False.
        """
        self.input_files = input_files
        self.output_file = output_file
        self.enable_metadata = enable_metadata
        self.enable_coloring = enable_coloring

    def concatenate_files(self):
        """
        Concatenates the input GPX files into a single GPX file.

        Returns:
            None
        """
        root = self._create_gpx_root()
        colorizer = GPXColorizer()  # Create a single colorizer instance

        for file_path in self.input_files:
            gpx_file = GPXFile(file_path)
            if self.enable_coloring:
                tracks = gpx_file.extract_tracks()
                colorizer.colorize_tracks(tracks)

            tracks = gpx_file.extract_tracks()
            for trk in tracks:
                trkpt_elements = trk.findall(".//trkpt")
                if len(trkpt_elements) >= 2:  # Check if "trk" has at least 2 "trkpt" elements
                    root.append(trk)

        if self.enable_coloring:
            colorizer.add_coloring_metadata(root)

        xml_string = ET.tostring(root, encoding="utf-8")
        prettified_xml = self._prettify_xml(xml_string)

        with open(self.output_file, "w") as f:
            f.write(prettified_xml)

    def _create_gpx_root(self) -> ET.Element:
        """
        Creates the root element of the GPX XML.

        Returns:
            ET.Element: The root element of the GPX XML.
        """
        root = ET.Element("gpx")
        return root

    def _prettify_xml(self, xml_string: str) -> str:
        """
        Prettifies the XML string.

        Args:
            xml_string (str): The XML string to prettify.

        Returns:
            str: The prettified XML string.
        """
        parsed_xml = minidom.parseString(xml_string)
        pretty_xml = parsed_xml.toprettyxml(indent="  ")
        compact_xml = "\n".join(
            line for line in pretty_xml.split("\n") if line.strip())
        return compact_xml
