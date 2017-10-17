import requests

baseurl = "http://epsumthings.herokuapp.com/api"
#baseurl = "http://localhost:8008/api"


# Get Request Function
def Getrequest(endpoint, header, showOutput=True):
    url = baseurl + endpoint
    response = requests.get(url=url, headers=header)
    if showOutput:
        print("Output:")
        print(response.json())
    return response.text


# Post Request Function
def Postrequest(endpoint, header, body):
    url = baseurl + endpoint
    response = requests.post(url=url, headers=header, data=body)
    print("Output:")
    print(response.json())


# Put Request Function
def Putrequest(endpoint, header, body):
    url = baseurl + endpoint
    response = requests.put(url=url, headers=header, data=body)
    print("Output:")
    print(response.json())
