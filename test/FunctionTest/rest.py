from flask import jsonify, request, session, Flask
from werkzeug.security import check_password_hash

from userDAL import *

USER_DATA = {
    "username": "manish",
    "password":"pathak"
}

def Authenticate():
    if not request.is_json:
        return "Missing JSON in request"

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return "Missing username parameter"
    if not password:
        return "Missing password parameter"

    # password1=hashlib.md5(password.encode())
    userResult=userAuthenticateDAL(username,password)
    # if username != USER_DATA.get("username") and password != USER_DATA.get("password"):
    #     return "Bad username or password"
    return userResult
