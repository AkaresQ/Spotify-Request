import requests , json
Sess = requests.Session()
pw = "username"
un = "password"
headers = {"content-type": "application/x-www-form-urlencoded"}
Src = Sess.get(f"https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fint%2Faccount%2Foverview%2F",headers=headers)
ctoken = Src.cookies['csrf_token']
rapi = 'https://accounts.spotify.com/api/login'
payload = {'remember': 'true', 'username': un, 'password': pw, 'csrf_token': ctoken}
bon = dict(_bon="MHwwfC0xNjcwODIzMDAzfC03MDE3NDU2NjEyNnwxfDF8MXwx")
sendreq = Sess.post(rapi,headers=headers,json=payload,cookies=bon)

if 'errorInvalidCredentials' in sendreq.text:
    print("Invalid Account")
else:
    print("Valid Account")
