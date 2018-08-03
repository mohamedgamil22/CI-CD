import json
import urllib3


_http = urllib3.PoolManager()

'''forming the URL of the Request ( BaseURL + URI )'''

baseURL= 'https://iam.eu-west-0.prod-cloud-ocb.orange-business.com'
uri= '/v3/auth/tokens'
url= baseURL + uri

''' Body of the request'''

_body='{"auth":{"identity":{"methods":["password"],"password":{"user":{"name":"MohamedGamil","password":"Test1234_","domain":{"name":"MohamedGamil"}}}},"scope":{"project":{"name":"eu-west-0"}}}}'

tokenReq = _http.request('POST',url,body=_body,headers={"Content-Type" : "application/json"})

status=tokenReq.status
resBody= dict(json.loads(tokenReq.data))
resHeader=tokenReq.headers


if int(str(status)[:1]) == 2 :
    print ("Token Request succeeded", "Return code" , status)
    print ("Generated Token:", resHeader["x-subject-token"])
    print ("Expiration Date", resBody["token"]["issued_at"])
else:
    print ("Token Request failed", "Return Code", tokenReq.status )

print ("Github build works ;)")
print ("Output success")
print ("Thanks for using my repo")
