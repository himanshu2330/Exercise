import requests
import json
from requests.auth import HTTPBasicAuth
import sys
from urllib3.exceptions import InsecureRequestWarning


Response_json= []
serverip = sys.argv[1]

url = 'https://' + serverip + '/latest/api/token' 
print ('Getting Token : ',url)
response = requests.put(url,verify=False)
print(response.status_code)
if response.status_code < 300:
    print(response.text)
else:
    raise Exception("ERROR:: Unable to get token")


url1 = 'https://' + serverip + '/latest/metadata'
response1 = requests.get(url1,verify=False,headers={'Authorization': 'response'})
print(response.status_code)
if response.status_code < 300:
    print(response.text)
else:
    raise Exception("ERROR:: Unable to top level metadata")
Response_json.append(response1)


url3 = 'https://' + serverip + '/latest/metadata/ami-id'
response2 = requests.get(url3,verify=False,headers={'Authorization': 'response'})
print(response.status_code)
if response.status_code < 300:
    print(response.text)
else:
    raise Exception("ERROR:: Unable to fetch ami  metadata")
Response_json.append(response2)


url4 = 'https://' + serverip + '/latest/metadata/reservation-id'
response3 = requests.get(url4,verify=False,headers={'Authorization': 'response'})
print(response.status_code)
if response.status_code < 300:
    print(response.text)
else:
    raise Exception("ERROR:: Unable to fetch reservation-id metadata")
Response_json.append(response3)


url5 = 'https://' + serverip + '/latest/metadata/local-hostname'
response4 = requests.get(url4,verify=False,headers={'Authorization': 'response'})
print(response.status_code)
if response.status_code < 300:
    print(response.text)
else:
    raise Exception("ERROR:: Unable to fetch reservation-id localhostname")
Response_json.append(response4)




