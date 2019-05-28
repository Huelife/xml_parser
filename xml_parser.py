#xml_parser.py: Simple XML parser using ElementTree

import xml.etree.ElementTree as ET

#parsing dataMay-24-2019.xml
tree = ET.parse('dataMay-24-2019.xml')
root = tree.getroot()

city_num = 0
city_value = ""

#loops through record to find city, print city name, and add total
for record in root.findall('record'):
  value = record.find('city').text
  print(value)
  city_num += 1
  city_value += "[" + value + "]\n"

#write parsed values to information.txt
with open('information.txt','w') as info:
  info.write(city_value)
  
print("Total number of cities: {}.".format(city_num))
