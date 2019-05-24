#xml_parser.py: Simple XML parser using ElementTree

import xml.etree.ElementTree as ET

#file.xml is currently a placeholder
tree = ET.parse('file.xml')
root = tree.getroot()
