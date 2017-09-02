import json as j
from homeautomationcli.utils import *
from homeautomationcli.encryption import *
import sys


# User Login
def login(useremail, userpass):
    aes = EpsumCryptAES()
    Authorization = aes.encrypt('{"message":"hello"}', userpass)
    header = {'USER': useremail, 'Authorization': Authorization}
    Getrequest('/user/login', header)


# User Registration
def user_regd():
    aes = EpsumCryptAES()
    print("Email ID :")
    email = sys.stdin.readline()
    email = email[:-1]

    print("Your Name :")
    name = sys.stdin.readline()
    name = name[:-1]

    print("Date Of Birth :")
    dob = sys.stdin.readline()
    dob = dob[:-1]

    print("Mobile :")
    phone = sys.stdin.readline()
    phone = phone[:-1]

    print("Nationality :")
    nationality = sys.stdin.readline()
    nationality = nationality[:-1]

    print("Gender :")
    gender = sys.stdin.readline()
    gender = gender[:-1]

    print("Password :")
    password = sys.stdin.readline()
    password = password[:-1]

    key = j.loads(regd_key(showOutput=False))["secret"]
    key = str(base64.b64decode(key), encoding="utf-8")
    body = j.dumps(
        {"name": name, "dob": dob, "phone": phone, "nationality": nationality, "password": password, "gender": gender})

    body = aes.encrypt(body, key)
    header = {'User': email}
    Putrequest('/user', header, body)


# View user profile
def profile(useremail, userpass):
    aes = EpsumCryptAES()
    Authorization = aes.encrypt('{"message":"hello"}', userpass)
    header = {'USER': useremail, 'Authorization': Authorization}
    Getrequest('/user', header)


# User Profile Edit
def profile_edit(useremail, userpass):
    aes = EpsumCryptAES()
    print("Address :")
    address = sys.stdin.readline()
    address = address[:-1]

    print("Phone :")
    phone = sys.stdin.readline()
    phone = phone[:-1]

    print("Social")
    social = sys.stdin.readline()
    social = social[:-1]
    social = j.loads(social)

    print("ID Proof")
    idproof = sys.stdin.readline()
    idproof = idproof[:-1]
    idproof = j.loads(idproof)

    body = j.dumps({"address": address, "phone": phone, "social": social, "idproof": idproof})
    body = aes.encrypt(body, userpass)
    header = {'USER': useremail}
    Postrequest('/user', header, body)


# Get User Setting
def user_setting(useremail, userpass):
    aes = EpsumCryptAES()
    Authorization = aes.encrypt('{}', userpass)
    header = {"USER": useremail, "Authorization": Authorization}
    Getrequest('/user/settings', header)


# Update User Setting
def user_setting_update(useremail, userpass):
    aes = EpsumCryptAES()
    print("Home")
    home = sys.stdin.readline()
    home = home[:-1]
    home = j.loads(home)

    print("Rooms")
    rooms = sys.stdin.readline()
    rooms = rooms[:-1]
    rooms = j.loads(rooms)

    body = j.dumps({"homes": home, "rooms": rooms})
    body = aes.encrypt(body, userpass)
    header = {"USER": useremail}
    Postrequest('/user/settings', header, body)


# Control modules
def control_module(useremail, userpass):
    aes = EpsumCryptAES()
    print("Thing ID :")
    thingid = sys.stdin.readline()
    thingid = thingid[:-1]

    print("Congiguration (json[])")
    config = sys.stdin.readline()
    config = config[:-1]
    config = j.loads(config)

    body = j.dumps({"thingid": thingid, "config": config})
    body = aes.encrypt(body, userpass)
    header = {"USER": useremail}
    Postrequest('/thing', header, body)


# Module Info
def module_info(useremail, userpass):
    aes = EpsumCryptAES()
    print("Thing ID :")
    thingid = sys.stdin.readline()
    thingid = thingid[:-1]
    Authorization = j.dumps({"message": "hello", "thingid": thingid})
    header = {"USER": useremail, "Authorization": Authorization}
    Getrequest('/thing', header)


# Module Registration
def module_regd(useremail, userpass):
    aes = EpsumCryptAES()

    print("Thing Id :")
    thingid = sys.stdin.readline()
    thingid = thingid[:-1]

    print("Thing Name :")
    thingname = sys.stdin.readline()
    thingname = thingname[:-1]

    header = {"USER": useremail}
    body = j.dumps({"thingid": thingid, "thingname": thingname})
    body = aes.encrypt(body, userpass)
    Putrequest('/thing/register', header, body)


# Module Configure
def module_config(useremail, userpass):
    aes = EpsumCryptAES()
    print("Thing Name :")
    thingname = sys.stdin.readline()
    thingname = thingname[:-1]
    body = j.dumps({"thingname": thingname})
    body = aes.encrypt(body, userpass)
    header = {"USER": useremail}
    Postrequest('/thing/config', header, body)


# Forgot Password Step-1
def forgot_1(useremail, userpass):
    aes = EpsumCryptAES()
    print("Token")
    token = sys.stdin.readline()
    token = token[:-1]
    body = j.dumps({"token": token})
    body = aes.encrypt(body, userpass)
    header = {"USER": useremail}
    Postrequest('/user/forgot1', header, body)


# Forgot Password Step-2
def forgot_2(useremail, userpass):
    aes = EpsumCryptAES()
    print("Token")
    token = sys.stdin.readline()
    token = token[:-1]

    print("New Password")
    newpassword = sys.stdin.readline()
    newpassword = newpassword[:-1]

    body = j.dumps({"newpassword": newpassword, "token": token})
    body = aes.encrypt(body)
    header = {"USER": useremail}
    Postrequest('/user/forgot2', header, body)


# Update User Password
def password_update(useremail, userpass):
    aes = EpsumCryptAES()
    print("Password")
    password = sys.stdin.readline()
    password = password[:-1]
    body = j.dumps({"password": password})
    body = aes.encrypt(body)
    header = {"USER": useremail}
    Postrequest('/user/update', header, body)


# Show History
def history(useremail, userpass):
    aes = EpsumCryptAES()
    Authorization = j.dumps({"message": "hello"})
    Authorization = aes.encrypt(Authorization, userpass)
    header = {"USER": useremail}
    Getrequest('/user/activity', header)


# Get Key For Registration
def regd_key(showOutput=True):
    return Getrequest('/getkey', '', showOutput)


# Admin actions

# Add a thing definition
def thingreg_from_base_model():
    print('Enter admin email : ')
    email = sys.stdin.readline()[:-1]
    print('Password : ')
    password = sys.stdin.readline()[:-1]
    print("New Thing ID : ")
    thingid = sys.stdin.readline()[:-1]
    print("Thing name: ")
    thingname = sys.stdin.readline()[:-1]
    print("Base Model: ")
    basemodel = sys.stdin.readline()[:-1]
    header = {"USER": email}
    body = j.dumps({"thingid": thingid, "thingname": thingname, 'basemodel': basemodel})
    aes = EpsumCryptAES()
    body = aes.encrypt(body, password)
    Postrequest('/thing/register', header, body)


def thingDefinition():
    print('Enter admin email : ')
    email = sys.stdin.readline()[:-1]
    print('Password : ')
    password = sys.stdin.readline()[:-1]
    print("Model name : ")
    modelname = sys.stdin.readline()[:-1]
    print("Thing Type: ")
    thingtype = sys.stdin.readline()[:-1]
    print("Schema: ")
    schema = sys.stdin.readline()[:-1]
    header = {"USER": email}
    body = j.dumps({"modelname": modelname, "thingtype": thingtype, 'schema': j.loads(schema)})
    aes = EpsumCryptAES()
    body = aes.encrypt(body, password)
    Putrequest('/thing/define', header, body)


def adminActions():
    print("1- Add a Thing defination")
    print("2- Register a thing with a unique id")
    print("3- Back")
    choice = sys.stdin.readline()
    choice = int(choice[:-1])
    if choice == 1:
        thingDefinition()
    elif choice == 2:
        thingreg_from_base_model()
    elif choice == 3:
        from .commandline import entry
        entry()
    else:
        print("Invalid Choice.. Try again")
        adminActions()