import os
import feapi_lib
import logging


logger = logging.getLogger(__name__)

def main():
    global logger
    logging.basicConfig(filename = "iam.log",level = logging.INFO)
    logger = logging.getLogger("fe_iam.py")
    try:
        logger.info("Reading Enviromental Varibles: UserName_API , Pass_API")
        USER = os.environ['UserName_API']
        PASSW = os.environ['Pass_API']
    except KeyError:
        print ("Please assign the username and password to Enviromental Global Varible")
        print ("UserName_API , Pass_API")
        logging.critical("Failed to read UserName_API ,and/or, Pass_API")
        raise
    logger.info("Reading Varibles successeded")

    tok,ex_date = gen_token(USER,PASSW)
    print("Generated Token is:",tok)
    print("Expiration date",ex_date)



def gen_token(username,password):


    ''' Body of the request'''
    logger.info("Starting to generate the token")
    BODY= "{\"auth\":{\"identity\":{\"methods\":[\"password\"],\"password\":{\"user\":{\"name\":\""+username+"\",\"password\":\""+password+"\",\"domain\":{\"name\":\"MohamedGamil\"}}}},\"scope\":{\"project\":{\"name\":\"eu-west-0\"}}}}"
    try:
        tokenReq = feapi_lib.call_feapi(Verb="POST", URI="/v3/auth/tokens", Body=BODY)
        RESP_BODY = tokenReq.json()
        expire_date = RESP_BODY['token']['expires_at']
        MYTOKEN = (tokenReq.headers["X-Subject-Token"])
        logger.info("Generated Token Successfully")
        return MYTOKEN,expire_date
    except:
        print("Issue with request sent")
        logger.error("Failed to Obtain token")
        # print (tokenReq.text)
        raise




if __name__  == "__main__":
    main()