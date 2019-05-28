#xml_parser_list.py: Simple XML parser writing list

import xml.etree.ElementTree as ET

#parsing dataMay-27-2019.xml
tree = ET.parse('dataMay-27-2019.xml')
root = tree.getroot()

city_num = 0
city_value = []

#loops through record to find longitude,latitude,country,city
for record in root.findall('record'):
  value = [[record.find('longitude').text,record.find('latitude').text,
           record.find('country').text,record.find('city').text]]
  print(value)
  city_num += 1
  city_value += value
