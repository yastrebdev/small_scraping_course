import requests
import fake_useragent
from bs4 import BeautifulSoup


user = fake_useragent.UserAgent().random

header = {'user-agent': user}


link = 'https://browser-info.ru/'
response = requests.get(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id = 'tool_padding')

# check js
check_js = block.find('div', id='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

# check flash
check_flash = block.find('div', id='flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

#check user-agent
check_user = block.find('div', id='user_agent').text

print(result_js)
print(result_flash)
print(check_user)