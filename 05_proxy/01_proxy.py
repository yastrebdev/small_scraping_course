import requests
import multiprocessing

def handler(proxy):
    link = 'http://icanhazip.com/'
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }

    try:
        response = requests.get(link, proxies=proxies, timeout=2).text
        print(f'IP: {response.strip()}')
    except requests.exceptions.RequestException:
        print('Proxy not valid')


if __name__ == "__main__":
    with open('ip.txt') as file:
        proxy_base = file.read().splitlines()
        print(proxy_base)

    with multiprocessing.Pool() as process:
        process.map(handler, proxy_base)