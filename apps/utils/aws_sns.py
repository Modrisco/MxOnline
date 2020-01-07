import boto3
import json


def send_sms(mobile, authcode):
    client = boto3.client("sns", "ap-southeast-2")
    context = "Your MxOnline authentication code is " + authcode + " Available in 5 minutes."
    mobile = "+61" + mobile[1:]

    res = client.publish(PhoneNumber=mobile, Message=context)
    # print(res)
    re_json = json.loads(json.dumps(res))
    return re_json
