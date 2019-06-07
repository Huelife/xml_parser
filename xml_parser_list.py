#xml_parser_list.py: Simple XML parser writing multiple lists

import xml.etree.ElementTree as ET

tree = ET.parse('dataMay-27-2019.xml')
root = tree.getroot()

set_num = 0

#writing lists to new file and printing number of lists to console
#loops through record to find longitude,latitude,country,city
with open('information_list.txt','w',encoding="utf-8") as info:
  for record in root.findall('record'):
    value = [[record.find('longitude').text,record.find('latitude').text,
              record.find('country').text,record.find('city').text]]
    print(value)    #remove print command to increase parsing speed
    set_num += 1
    [info.write('{}\n'.format(value_list)) for value_list in value]
  
print("Total number of lists: {}.".format(set_num))
