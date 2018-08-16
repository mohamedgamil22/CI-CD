import json
import urllib3
import os
import logging
import FELibrary


#user=os.environ['UserName_API']
#passw=os.environ['Pass_API']

user="MohamedGamil"
passw="Test1234_"
print ("Hello "+user)



'''forming the URL of the Request ( BaseURL + URI )'''

baseURL= FELibrary.GET_SRVCURL("iam","eu-west-0")
uri= '/v3/auth/tokens'
url= baseURL + uri
print (url)

''' Body of the request'''
headers={'Content-Type' : 'application/json'}
_body= "{\"auth\":{\"identity\":{\"methods\":[\"password\"],\"password\":{\"user\":{\"name\":\""+user+"\",\"password\":\""+passw+"\",\"domain\":{\"name\":\"MohamedGamil\"}}}},\"scope\":{\"project\":{\"name\":\"eu-west-0\"}}}}"
try:
	#_http = urllib3.PoolManager()
	#tokenReq = _http.request('POST',url,body=_body,headers={"Content-Type" : "application/json"})
	tokenReq = FELibrary.CALL_FEAPI(Verb="POST",URI="/v3/auth/tokens",Body=_body)
except:
	print ("Issue with request sent")

# print (tokenReq)
status = tokenReq.status_code
# resBody = dict(json.loads(tokenReq.data))
resBody = tokenReq.json()
# resHeader = tokenReq.headers()
print("Token will expire at: ",resBody['token']['expires_at'])
# print(resHeader)

if int(str(status)[:1]) == 2 :
    print ("Token Request succeeded","Return code",status)
    print ("Generated Token:", tokenReq.headers["X-Subject-Token"])
    # print ("Expiration Date", resBody["token"]["issued_at"])
    mytoken=(tokenReq.headers["X-Subject-Token"])
else:
    print ("Token Request failed","Return Code", tokenReq.status_code)


print ("Github build works ;)")