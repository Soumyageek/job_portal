import requests
from bs4 import BeautifulSoup

payload = {
    'session_key':'maneonkar7@gmail.com',
    'session_password':'Chicoo@123'
}

URL = 'https://www.linkedin.com/uas/login-submit'
session = requests.session()
session.post(URL, data=payload)

r = session.get('https://linkedin.com/nhome')
print(r.content)