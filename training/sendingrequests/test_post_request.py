# doc -- https://requests.readthedocs.io/en/master/user/quickstart/#make-a-request
#
#
#
# Python task:
# 	Create a POST request with the following url, payload, and header:
# 		https://httpbin.org/post
# 		{ "name":"John", "age":30, "car":None }
# 		Content-Type: application/x-www-form-urlencoded
#
# 	The request should assert to verify you receive a 200 status back, and "args" is {}. There should be two asserts for this.
#
# Bonus: Create the request in one function and have it call another function to send the POST request.
#
# QA:
# Create 10 different test cases to test this post request.
import json

import requests


def test_post_request():
    payload = json.dumps({ "name":"John", "age":30, "car":None })
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post('https://httpbin.org/post', data=payload, headers=headers)
    json_data_response = json.loads(response.content)
    print(response.status_code)
    print(json_data_response)
    assert response.status_code == 200
    assert json_data_response["args"] == {}

####################BONUS####################

def send_post_request(url, payload, header):
    response = requests.post(url, json=payload, headers=header)
    return response.status_code, response.content

def test_posting_request():
    url = 'https://httpbin.org/post'
    payload = json.dumps({"name": "John", "age": 30, "car": None})
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    expected_status, json_obj = send_post_request(url, payload,headers)
    print(json_obj)
    assert expected_status == 200
    assert json.loads(json_obj)["args"] == {}


# QA:
# Create 10 different test cases to test this post request.
#
# 1- Happy Path
# 2- Empty payload
# 3- No Payload
# 4- incorrect url
# 5- no headers
# 6- incorrect url
# 7- incorect request (send a get request)
# 8- incorrect datatypes in payload
# 9- insecure url
# 10- missing payload
