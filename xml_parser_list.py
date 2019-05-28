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

#writing lists to new file and printing number of lists to console
with open('information.txt','w',encoding="utf-8") as info:
  for city_value_list in city_value:
    info.write('{}\n'.format(city_value_list))
  
print("Total number of lists: {}.".format(city_num))
