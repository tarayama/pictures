#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

#APIエンドポイント
endpoint = 'http://127.0.0.1/api/v1'

#アカウントの新規登録
def register_your_account(username, password):
    registration_url = "{}/rest-auth/registration/".format(endpoint)

    headers = {
        'Content-Type': 'application/json',
            }
    body = {
        "username": username,
        #"email": "", #null is ok. however, you can use this field
        "password1": password,
        "password2": password
    }
    response = requests.post(registration_url, headers=headers, data=json.dumps(body).encode())
    print(response)
    values = json.loads(response.text)
    try:
        print("Your API Key: ",values['key'])
    except:
        print(values)
    return YOUR_API_KEY

#ログイン
def login_your_account(username, password):
    login_url = "{}/rest-auth/login/".format(endpoint)
    headers = {
        'Content-Type': 'application/json',
            }
    body = {
        "username": username,
        #"email": "", #null is ok
        "password": password,
    }
    response = requests.post(login_url, headers=headers, data=json.dumps(body).encode())
    print(response)
    values = json.loads(response.text)
    try:
        YOUR_API_KEY = values['key']
        print("Your API Key: ",YOUR_API_KEY)
        return YOUR_API_KEY
    except:
        print(values)
        return values   

#ログアウト
def logout_your_account(): #公式ドキュメントによると形骸的なものできちんと機能していないそうです。
    logout_url = "{}/rest-auth/logout/".format(endpoint)
    response = requests.post(logout_url)
    values = json.loads(response.text)
    return values

#user_idの取得
def Check_your_user_id(API_KEY):
    userid_url = "{}/GET/userinfo".format(endpoint)
    api_token = 'Token {}'.format(API_KEY)
    headers = {
        'Authorization': api_token
            }
    response = requests.get(userid_url, headers=headers)
    values = json.loads(response.text)
    try:
        user_id = values[0]['id']
        #print("user_id : ",user_id)
        return user_id
    except:
        #print(values)
        return values
    
#カテゴリーリストの取得
def get_CategotyList(API_KEY):
    api_token = 'Token {}'.format(API_KEY)
    message_url = '{}/GET/Category'.format(endpoint)
    headers = {
        'Authorization': api_token,
        'Content-Type': 'application/json',
            }
    response = requests.get(message_url, headers=headers)
    #print(response)
    values = json.loads(response.text)
    #print(values)
    return values

#食品登録
def post_food(API_KEY, user_id, name, memo, category, limit):
    api_token = 'Token {}'.format(API_KEY)
    message_url = '{}/POST/Food'.format(endpoint)
    headers = {
        'Authorization': api_token,
        'Content-Type': 'application/json',
            }

    body = {
        "user": user_id, #your userid. Don't enter without your userid.
        "name": name,
        "memo": memo,
        "category": categoryid, #categoryidはget_CategoryListで取得したidをstrで入力してください
        "limit": limit, #"YYYY-MM-DD"
        "solution": "0"
    }

    response = requests.post(message_url, headers=headers, data=json.dumps(body).encode())
    #print(response)
    values = json.loads(response.text)
    #print(values)
    return values

#登録食品一覧取得
def get_food(API_KEY):
    api_token = 'Token {}'.format(API_KEY)
    message_url = '{}/GET/Food'.format(endpoint)
    headers = {
        'Authorization': api_token,
        'Content-Type': 'application/json',
            }
    response = requests.get(message_url, headers=headers)
    #print(response)
    values = json.loads(response.text)
    #print(values)
    return values



#近隣5件のフードバンク取得
def get_near_foodbank(postal_code):
    url = "http://127.0.0.1:8000/postal_code/{}".format(postal_code) #174-0053 is Toyo University Sports center's postal code.
    headers={"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    print(response)
    print(response.text)
    values = json.loads(response.text)
    print(values)
    return values

#画像からの賞味期限取得
from pyzbar.pyzbar import decode
from PIL import Image

# 画像ファイルの指定
image = "YOURBARCODE.jpg"
data = decode(Image.open(image))
jancode = data[0][0].decode('utf-8', 'ignore')
print(jancode)

#JANコードからの商品名取得
def get_Foodname_by_jancode(jancode):
    url = "http://127.0.0.1:8000/jancode/{}".format(jancode)
    headers={"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    print(response)
    #print(response.text)
    values = json.loads(response.text)
    print(values)
    return values
    

