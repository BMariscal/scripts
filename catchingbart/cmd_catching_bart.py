#Idea: change api url from the command line
#It will change route and time
#Project titled: Reading Command Line Arguments and Making a Script
import sys
import urllib.request
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
    raise SystemExit('Usage: cmd_catching_bart.py route time(time formated like this: 00:00+am or 00:00+pm)')
    #e.g, python3 cmd_catching_bart.py 2 08:00+pm

route= sys.argv[1]
time =  sys.argv[2]



u = urllib.request.urlopen('http://api.bart.gov/api/sched.aspx?cmd=routesched&route={}&key=QHZJ-PKEH-9PWT-DWE9&time={}'.format(route,time))
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




