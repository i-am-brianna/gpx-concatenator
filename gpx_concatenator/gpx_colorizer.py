import xml.etree.ElementTree as ET
import colorsys
from typing import List

class GPXColorizer:
    """
    A class that colorizes GPX tracks in XML format.
    """

    def __init__(self):
        """
        Initializes an instance of GPXColorizer.
        """
        self.color_dict = {}
        self.color_index = 0

    def colorize_tracks(self, tracks: List[ET.Element]) -> None:
        """
        Colorizes the tracks with distinct colors.

        Args:
            tracks (List[ET.Element]): A list of track elements.

        Returns:
            None
        """
        num_distinct_colors = len(tracks) + 1
        distinct_colors = self._generate_distinct_colors(num_distinct_colors)

        for trk in tracks:
            name_element = trk.find('name')
            if name_element is not None:
                trk_name = name_element.text
                if trk_name not in self.color_dict:
                    self.color_dict[trk_name] = distinct_colors[self.color_index]
                    self.color_index += 1
                color = self.color_dict[trk_name]
                self._add_color_extensions(trk, color)

    def _generate_distinct_colors(self, num_colors: int) -> List[str]:
        """
        Generates a list of distinct colors.

        Args:
            num_colors (int): Number of distinct colors to generate.

        Returns:
            List[str]: A list of distinct colors in hexadecimal format.
        """
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

    def _add_color_extensions(self, trk: ET.Element, color: str) -> None:
        """
        Adds color extensions to a track element.

        Args:
            trk (ET.Element): The track element.
            color (str): The color value to add.

        Returns:
            None
        """
        extensions = ET.Element('extensions')
        gpx_style_line = ET.SubElement(extensions, 'gpx_style:line')
        color_element = ET.SubElement(gpx_style_line, 'color')
        color_element.text = color
        trk.append(extensions)

    def add_coloring_metadata(self, root: ET.Element) -> None:
        """
        Adds coloring metadata to the root element.

        Args:
            root (ET.Element): The root element of the GPX XML.

        Returns:
            None
        """
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
