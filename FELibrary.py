"""" BaseFE :  a libaray used to help create API calls for Flexbile Engine"""

import requests


REGION_LIST = ["eu-west-0", "na-east-0", "as-south-0"]
SERVICE_LIST = ["iam", "ecs" ,"evs" ,"ims" ]

"""

def FE_Param():
	FE_Param.REGION_LIST = ["eu-west-0" , "na-east-0" , "as-south-0" ]

"""
def CALL_FEAPI(Verb="GET", URI="/", Body=None,Token=None, Service="iam", Region="eu-west-0"):
	""" Function for Calling FE APIs 
	"""
	#First Generating the Service URL
	URL = GET_SRVCURL(Service , Region)
	ReqURL = URL + URI
	print (Body)
	#Checking if token is inserted.
	if Token is None:
		Headers = {'Content-Type': 'application/json'}
	else:
		Headers = {'Content-Type': 'application/json' , 'X-Auth-Token':Token}
	if Verb == "GET":
		req = requests.get(ReqURL, headers= Headers )
		return r.text
		##
	elif Verb == "POST":
		req= requests.post(ReqURL, data=Body, headers=Headers)
        
	elif Verb == "PATCH":
		req= requests.patch(ReqURL, data=Body, headers=Headers)
	elif Verb == "DELETE":
		req= requests.delete(ReqURL, Headers)
	elif Verb == "PUT":
		req = requests.put(ReqURL, data=Body, headers=Headers)
	else:
		print("The Verb used is not supported, Please use on the following:")
		print("GET , POST , PATCH , DELETE , PUT")
	return req




def Get_SrvcURL (service , region):	
	""" To Add Help for this module"""
	#Confirm correct Region name entered:
	if not(region in REGION_LIST):
		print (" The region name is wrong, Availble regions:" , REGION_LIST)
		return 1
	#Confirm correct Service Name:
	if not(service in SERVICE_LIST):
		print (" The service id is wrong, Availble Services are:" , SERVICE_LIST)
		return 1
	else:
		service_url = "https://" + service + "." + region + ".prod-cloud-ocb.orange-business.com"
		return service_url