#!/usr/bin/python3
"""Module:."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str) -> None:
    """Save dictionary to xml file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = value

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename: str) -> dict:
    """Load python dictionary from xml file.

    Returns:
        python dictionary created from xml file

    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
