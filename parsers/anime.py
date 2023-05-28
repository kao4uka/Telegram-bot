import requests
from bs4 import BeautifulSoup

URL = 'https://rezka.ag/animation/'

HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}



def get_html(url):
    req = requests.get(URL, headers=HEADERS)
    return req



def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item-link')
    anime = []
    for item in items:
        anime.append({
            'link': f'{item.a["href"]}',
            'title': item.find('a').string,
            'info': item.find('div').string
        })
    return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for i in range(1, 2):
            html = get_html(f'{URL}page/{i}/.php')
            current_page = get_data(html.text)
            anime.extend(current_page)
        return anime
    else:
        raise Exception("Error in parser!")