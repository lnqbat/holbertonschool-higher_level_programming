#!/usr/bin/env python3
"""
Serialization and deserialization using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Convert a Python dictionary into XML.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Read an XML file and convert.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
