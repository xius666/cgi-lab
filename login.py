#!/usr/bin/env python3

from templates import login_page,after_login_incorrect, secret_page
from secret import username, password
import os
import json
from http.cookies import SimpleCookie
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
http_cookie=os.environ['HTTP_COOKIE']
cookie = SimpleCookie(http_cookie)
c_username = None
c_password = None
#print('Content-Type: application/json')
#print(json.dumps(dict(os.environ), indent = 4))
if cookie.get("Username"):
    c_username = cookie.get("Username").value
if cookie.get("Password"):
    c_password = cookie.get("Password").value

if c_username == username and c_password == password:#the cookie is indeed legit
    print(secret_page(username, password))
else:#if no cookie presented or the cookie is invalie
    input_username= form.getvalue("username")
    input_password= form.getvalue("password")
    if input_username==None and input_password == None:
        print(login_page()) #no user input provided
    elif (input_username == username and input_password == password):
        
        print (f"Set-Cookie:Username = {username};")#set cookies
        print (f"Set-Cookie:Password = {password};")
        print('Content-Type: text/html')
        print()
        print(f"<!doctype html><html><body><li>logged in successfully</li></body></html>")
        #Q4
        #print(f"<html><body><p> <b>username</b>: {input_username}</p> <p> <b>password</b>: {input_password}</p></body></html>")
    else:# input the wrong credential
        print(after_login_incorrect())



