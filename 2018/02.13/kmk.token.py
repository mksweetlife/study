import requests
import base64
import config

def getToken():
    r = requests.post('https://gapi.gabia.com/oauth/token', data = config.api_config)
    j = r.json()
    token = j['access_token']
    return 'www_front:{0}'.format(token)

p = getToken()
#print(p)


def makeHeadersAuth(token):
    fucking_bytes = bytes(token, 'utf-8')
    token_encoded = base64.b64encode(fucking_bytes)
    Rjwu_bytes = token_encoded.decode('utf-8')

    return Rjwu_bytes

def hanbang():
    return makeHeadersAuth(getToken())


