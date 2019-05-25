#xml_parser.py: Simple XML parser using ElementTree

import xml.etree.ElementTree as ET

#parsing dataMay-24-2019.xml
tree = ET.parse('dataMay-24-2019.xml')
root = tree.getroot()

city_num = 0

for record in root.findall('record'):
  value = record.find('city').text
  print(value)
  cit_num += 1
  root.clear()
  
print("Total number of cities: {}.".format(city_num))
