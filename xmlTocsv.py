import xml.etree.ElementTree as ET
import csv

finaltree = ET.parse('DLTINS_20210117_01of01.xml')
finalroot = finaltree.getroot()

print(finalroot.tag)
for x in finalroot[0]:
    print(x.tag,x.attrib)
for x in finalroot[0]:
    print(x.text)
