import unittest
import xml.etree.ElementTree as ET
from gpx_concatenator.gpx_colorizer import GPXColorizer


class GPXColorizerTests(unittest.TestCase):

    def test_colorize_tracks(self):
        colorizer = GPXColorizer()
        tracks = [
            ET.Element('trk', attrib={'id': '1'}),
            ET.Element('trk', attrib={'id': '2'}),
            ET.Element('trk', attrib={'id': '3'})
        ]
        tracks[0].append(ET.Element('name'))
        tracks[1].append(ET.Element('name'))
        tracks[2].append(ET.Element('name'))
        tracks[0].find('name').text = 'Track 1'
        tracks[1].find('name').text = 'Track 2'
        tracks[2].find('name').text = 'Track 3'

        colorizer.colorize_tracks(tracks)

        self.assertEqual(len(colorizer.color_dict), 3)
        self.assertEqual(colorizer.color_index, 3)

    def test_generate_distinct_colors(self):
        colorizer = GPXColorizer()
        num_colors = 5

        distinct_colors = colorizer._generate_distinct_colors(num_colors)

        self.assertEqual(len(distinct_colors), num_colors)

    def test_add_color_extensions(self):
        colorizer = GPXColorizer()
        trk = ET.Element('trk')
        color = '#FF0000'

        colorizer._add_color_extensions(trk, color)

        extensions = trk.find('extensions')
        gpx_style_line = extensions.find('gpx_style:line')
        color_element = gpx_style_line.find('color')

        self.assertIsNotNone(extensions)
        self.assertIsNotNone(gpx_style_line)
        self.assertIsNotNone(color_element)
        self.assertEqual(color_element.text, color)

    def test_add_coloring_metadata(self):
        colorizer = GPXColorizer()
        root = ET.Element('root')

        colorizer.add_coloring_metadata(root)

        self.assertEqual(len(root.attrib), 7)
        self.assertIn('xmlns:xsi', root.attrib)
        self.assertIn('xmlns', root.attrib)
        self.assertIn('xsi:schemaLocation', root.attrib)
        self.assertIn('xmlns:gpxtpx', root.attrib)
        self.assertIn('xmlns:gpxx', root.attrib)
        self.assertIn('xmlns:gpx_style', root.attrib)
        self.assertIn('version', root.attrib)

if __name__ == '__main__':
    unittest.main()