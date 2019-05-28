#xml_parser_list.py: Simple XML parser writing multiple lists

import xml.etree.ElementTree as ET

#parsing dataMay-27-2019.xml
tree = ET.parse('dataMay-27-2019.xml')
root = tree.getroot()

set_num = 0
set_value = []

#loops through record to find longitude,latitude,country,city
for record in root.findall('record'):
  value = [[record.find('longitude').text,record.find('latitude').text,
           record.find('country').text,record.find('city').text]]
  print(value)
  set_num += 1
  set_value += value

#writing lists to new file and printing number of lists to console
with open('information_list.txt','w',encoding="utf-8") as info:
  for set_value_list in set_value:
    info.write('{}\n'.format(set_value_list))
  
print("Total number of lists: {}.".format(set_num))
