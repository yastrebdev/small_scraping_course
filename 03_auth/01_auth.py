import requests
import fake_useragent
from bs4 import BeautifulSoup

session = requests.Session()

link = 'https://com-forum.ru/forum/index.php?action=login'
user = fake_useragent.UserAgent().random
header = {
    'user-agent': user
}

data = {
    'username': 'ChestolubovSMM@yandex.ru',
    'password': 'EtEJ!E5E'
}

response = session.post(link, data=data, headers=header)
profile_info = 'https://www.woman.ru/user/403467445/'
profile_response = session.get(profile_info, headers=header).text

soup = BeautifulSoup(profile_response, 'lxml')
user = soup.find('a', {'class': 'user-info__name'}).text

cookie_dict = [
    {'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value}
    for key in session.cookies
]

session2 = requests.Session()

for cookies in cookie_dict:
    session2.cookies.set(**cookies)

resp = session2.get(profile_info, headers=header)


print(user)