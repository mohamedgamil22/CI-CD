"""" fe_library
a library created to easier the API call for FE services.

methods:
  - call_feapi : to call a certai fe service api
  - get_srvcurl: to generate a service url
"""
import requests
import sys
import logging

logger = logging.getLogger(__name__)


REGION_LIST = ["eu-west-0", "na-east-0", "as-south-0"]
SERVICE_LIST = ["iam", "ecs", "evs", "ims"]



def call_feapi(Verb="GET", URI="/", Body=None, Token=None, Service="iam", Region="eu-west-0"):
    """Function for Easy Calling FE APIs. 

    Call the API of the mentioned services, on the Flexible Engine by using the specified URI.

    Args:
      Verb:  the verb of the API Call ( "GET","POST","PATCH","DELETE","PUT"), default value:"GET"
      URI: specify the path of the Call, e.g: /auth/tokens , Default Value: "/"
      Body: a string with the body of the request. default: None
      Service: the service used to send the API to, default: "iam"
      Region: define the FE Region to be used , defailt: "eu-west-0"

    Returns:
      an object, with the same attributes as any returned object of request library.

    Raises:
      TBD

    """
    #First Generating the Service URL
    URL = get_srvcurl(Service, Region)
    ReqURL = URL + URI

    
    #Checking if token is inserted, if not, do not add to Req Headers.
    if Token is None:
        Headers = {'Content-Type': 'application/json'}
    else:
        Headers = {'Content-Type': 'application/json', 'X-Auth-Token': Token}
    logger.info(str("Sending API Call: "+ Verb + " , URL: "+ ReqURL+ " , Body: "+Body))
    try: #raise all exception 

        #Making the request based on the giving verb.
        if Verb == "GET":
            req = requests.get(ReqURL, headers=Headers)
        elif Verb == "POST":
            req = requests.post(ReqURL, data=Body, headers=Headers)
        elif Verb == "PATCH":
            req = requests.patch(ReqURL, data=Body, headers=Headers)
        elif Verb == "DELETE":
            req = requests.delete(ReqURL, Headers)
        elif Verb == "PUT":
            req = requests.put(ReqURL, data=Body, headers=Headers)
        else:
            logger.error(str("Used verb is wrong , Used verb: "+Verb))
            raise TypeError("The Verb used is not supported, Please use on the following:" ,"GET , POST , PATCH , DELETE , PUT" )

        req.raise_for_status() #to raise errors for unsuccessful status codes.


    except Exception as ex:
        logger.error("Failed Request, Error : %s" , ex)
        raise

    return req



def get_srvcurl(service , region):	
    """ generate service URL for any FE service.

    Args:
      service: the service name, e.g: "iam","evs"
      region: region code, e.g: "eu-west-0","as-south-0"

    """   
    if not(region in REGION_LIST):
        raise TypeError(" The region name is wrong, Availble regions:" , REGION_LIST)
    #Confirm correct Service Name:
    if not(service in SERVICE_LIST):
        raise TypeError(" The service id is wrong, Availble Services are:" , SERVICE_LIST)
    else:
        service_url = "https://" + service + "." + region + ".prod-cloud-ocb.orange-business.com"
        return service_url