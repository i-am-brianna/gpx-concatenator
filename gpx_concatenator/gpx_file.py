import xml.etree.ElementTree as ET
from typing import List

class GPXFile:
    """
    A class that represents a GPX file and provides methods for extracting metadata and tracks.
    """

    def __init__(self, file_path: str):
        """
        Initializes an instance of GPXFile.

        Args:
            file_path (str): The path to the GPX file.
        """
        self.file_path = file_path
        self.tree = ET.parse(file_path)

    def extract_metadata(self) -> ET.Element:
        """
        Extracts the metadata element from the GPX file.

        Returns:
            ET.Element: The metadata element if found, otherwise an empty metadata element.
        """
        metadata = self.tree.find("metadata")
        if metadata is not None:
            return metadata
        return ET.Element("metadata")

    def extract_tracks(self) -> List[ET.Element]:
        """
        Extracts the track elements from the GPX file.

        Returns:
            List[ET.Element]: A list of track elements.
        """
        return self.tree.findall(".//trk")
