import xml.etree.ElementTree as ET
from typing import List


class GPXFile:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.tree = ET.parse(file_path)

    def extract_metadata(self) -> ET.Element:
        metadata = self.tree.find("metadata")
        if metadata is not None:
            return metadata
        return ET.Element("metadata")

    def extract_tracks(self) -> List[ET.Element]:
        return self.tree.findall(".//trk")
