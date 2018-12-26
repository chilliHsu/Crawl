from Naked.toolshed.shell import execute_js, muterun_js 
import sys
import json
import demjson

response = muterun_js('myRunNodeJS.js')
   
if response.exitcode == 0:
    result = response.stdout
    #print(result)
    reviews = demjson.decode(result)
else:
    print('Error')
    

for r in reviews:
    print(r['text'])
