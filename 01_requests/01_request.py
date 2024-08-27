import requests

# link = 'https://icanhazip.com/'
link = 'https://browser-info.ru/'
response = requests.get(link).text # get content from page

with open('1.html', 'w', encoding='utf-8') as file:
    file.write(response)

# print(dir(requests.get(link)))