import requests

def login(LOGIN, PASSWORD):
    url = 'https://api.tisaude.com/api/login'
    payload = {
        'login': LOGIN,
        'senha': PASSWORD
    }

    r = requests.post(url, json=payload)

    # print("@login.py r.json(): " + str(r.json()))  # DEBUG
    
    return r.json().get('access_token')
