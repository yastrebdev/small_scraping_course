import requests
import fake_useragent
from bs4 import BeautifulSoup

image_number = 0
storage_number = 1
link = 'https://zastavok.net'

for storage in range(1):
    headers = {'User-Agent': fake_useragent.UserAgent().random}
    response = requests.get(f'{link}/{storage_number}', headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
    block = soup.find('div', class_='block-photo')
    all_image = block.find_all('div', class_='short_full')

    for image in all_image:
        image_link = image.find('a').get('href')
        download_storage = requests.get(f'{link}/{image_link}').text
        download_soup = BeautifulSoup(download_storage, 'lxml')
        block = download_soup.find('div', class_ = 'image_data').find('div', class_='block_down')
        result_link = block.find('a').get('href')

        image_bytes = requests.get(f'{link}/{result_link}').content

        with open(f'image/i-{image_number}.jpg', 'wb') as file:
            file.write(image_bytes)

        image_number += 1
        print('Your download image')

    storage_number += 1