#xml_parser.py: Simple XML parser using ElementTree

import xml.etree.ElementTree as ET

#parsing dataMay-24-2019.xml
tree = ET.parse('dataMay-24-2019.xml')
root = tree.getroot()

for record in root.findall('record'):
  value = record.find('city').text
  print(value)
  root.clear()
