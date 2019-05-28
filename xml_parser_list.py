#xml_parser_list.py: Simple XML parser writing list

import xml.etree.ElementTree as ET

#parsing dataMay-27-2019.xml
tree = ET.parse('dataMay-27-2019.xml')
root = tree.getroot()
