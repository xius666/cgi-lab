#!/usr/bin/env python3
import os,json
print('Content-Type: text/html\r\n\r\n')

#Q1
#print('Content-Type: application/json')
#print(json.dumps(dict(os.environ), indent = 4))
#Q2
#for param in os.environ['QUERY_STRING'].split('&'):
     #name = param.split('=')[0]
     #value = param.split('=')[1]
     #print(f"<li>QUERY_STRING: {name} = {value}</li>")
#Q3
#for param in os.environ.keys():
    #if (param == "HTTP_USER_AGENT"):
        #print(f"<p> HTTP_USER_AGENT: {os.environ[param]}</p>")
        

