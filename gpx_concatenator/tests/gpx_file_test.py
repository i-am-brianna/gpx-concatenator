import unittest
from gpx_concatenator.gpx_concatenator import GPXConcatenator
import xml.etree.ElementTree as ET
import os


class GPXConcatenatorTests(unittest.TestCase):

    def test_create_gpx_root(self):
        concatenator = GPXConcatenator([], '', False)

        root = concatenator._create_gpx_root()

        self.assertIsNotNone(root)
        self.assertEqual(root.tag, 'gpx')

    def test_prettify_xml(self):
        concatenator = GPXConcatenator([], '', False)
        xml_string = '<root><element1>Value1</element1><element2>Value2</element2></root>'

        prettified_xml = concatenator._prettify_xml(xml_string)

        self.assertIsInstance(prettified_xml, str)
        self.assertIn('<root>', prettified_xml)
        self.assertIn('<element1>Value1</element1>', prettified_xml)
        self.assertIn('<element2>Value2</element2>', prettified_xml)