#  Extracting Data from XML 
import xml.etree.ElementTree as ET

link = sampledata.xml

stuff = ET.fromstring(link)
lst = stuff.findall("comments/comment")
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('count').text)
