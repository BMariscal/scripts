#This script gives you the route schedule times for the route 1 bart (PITT station to MLBR)
import urllib.request
from xml.etree.ElementTree import XML


u = urllib.request.urlopen('http://api.bart.gov/api/sched.aspx?cmd=routesched&route=1&key=QHZJ-PKEH-9PWT-DWE9&time=07:30+am')
data = u.read()
doc = XML(data)#ElementTree usage

p=doc.findall(".//stop")#findall from ElementTree
q=doc.findall("./date")
# r=doc.findall(".//train")
for j in q:
    print('date ',end='')
    print(j.text)

count = 1
for i in p:
    items=i.attrib
    if items['station']== 'PITT':
        print('__','Train', str(count),'__')
        print('station |' + 'time')
        count+=1
    print(items.get('station',''),end='    ')
    print(items.get('origTime','N/A'))



"""I got the bart API key from http://www.bart.gov/schedules/developers
looked at the bart API documentation
used urllib to access api data
used ElementTree library to manipulate XML, used ElementTree documentation #https://docs.python.org/3/library/xml.etree.elementtree.html"""
