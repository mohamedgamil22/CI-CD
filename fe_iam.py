"""" a library for all the IAM related APIs.
Can also be used for testing the service when called directly

methods:
  - gen_token(username, password) : generate a token from the IAM
"""
import os
import logging
import feapi_lib


logger = logging.getLogger(__name__)  # pylint: disable=C0103


def main():
    """ main function:
    will trigger All IAM APIs as a test for the service"""

    global logger  # pylint: disable=C0103,W0603
    logging.basicConfig(filename="iam.log", level=logging.INFO)
    logger = logging.getLogger("fe_iam.py")
    try:
        logger.info("Reading Enviromental Varibles: UserName_API , Pass_API")
        user = os.environ['UserName_API']
        passw = os.environ['Pass_API']
    except KeyError:
        print("Please assign the username and password to Enviromental Global Varible")
        print("UserName_API , Pass_API")
        logging.critical("Failed to read UserName_API ,and/or, Pass_API")
        raise
    logger.info("Reading Varibles successeded")

    tok, ex_date = gen_token(user, passw)
    print("Generated Token is:", tok)
    print("Expiration date", ex_date)


def gen_token(username, password):

    # Body of the request
    logger.info("Starting to generate the token")
    body = "{\"auth\":{\"identity\":{\"methods\":[\"password\"],\"password\":{\"user\":{\"name\":\"" + username + \
        "\",\"password\":\"" + password + \
        "\",\"domain\":{\"name\":\"MohamedGamil\"}}}},\"scope\":{\"project\":{\"name\":\"eu-west-0\"}}}}"  # pylint: disable=C0301
    try:
        tokenReq = feapi_lib.call_feapi(
            verb="POST", uri="/v3/auth/tokens", body=body)
        resp_body = tokenReq.json()
        expire_date = resp_body['token']['expires_at']
        mytoken = (tokenReq.headers["X-Subject-Token"])
        logger.info("Generated Token Successfully")
        return mytoken, expire_date
    except:
        print("Issue with request sent")
        logger.error("Failed to Obtain token")
        # print (tokenReq.text)
        raise


if __name__ == "__main__":
    main()
