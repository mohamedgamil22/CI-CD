# import json
import os
# import logging
import FELibrary


USER = os.environ['UserName_API']
PASSW = os.environ['Pass_API']

# USER="MohamedGamil"
# PASSW="Test1234_"
# print ("Hello "+USER)





''' Body of the request'''
BODY= "{\"auth\":{\"identity\":{\"methods\":[\"password\"],\"password\":{\"user\":{\"name\":\""+USER+"\",\"password\":\""+PASSW+"\",\"domain\":{\"name\":\"MohamedGamil\"}}}},\"scope\":{\"project\":{\"name\":\"eu-west-0\"}}}}"

try:
	#_http = urllib3.PoolManager()
	#tokenReq = _http.request('POST',url,body=_body,headers={"Content-Type" : "application/json"})
	tokenReq = FELibrary.CALL_FEAPI(Verb="POST", URI="/v3/auth/tokens", Body=BODY)
except:
	print("Issue with request sent")

# print (tokenReq)
STATUS = tokenReq.status_code
# resBody = dict(json.loads(tokenReq.data))
RESP_BODY = tokenReq.json()
# resHeader = tokenReq.headers()
print("Token will expire at: ", RESP_BODY['token']['expires_at'])
# print(resHeader)

if int(str(STATUS)[:1]) == 2 :
    print("Token Request succeeded", "Return code", STATUS)
    print("Generated Token:", tokenReq.headers["X-Subject-Token"])
    # print ("Expiration Date", resBody["token"]["issued_at"])
    MYTOKEN = (tokenReq.headers["X-Subject-Token"])
else:
    print("Token Request failed","Return Code", STATUS)


print ("Github build works ;)")