import requests
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool


def parse_page(idx):
    url = f"https://www.khakaschiry.ru/news/detail.php?ID={idx}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    content = soup.find_all('div', {'id': 'content'})[0]
    if content.find('div', {'class': 'news-detail'}):
        date = None
        if content.find('span', {'class': 'news-date-time'}):
            date = content.find('span', {'class': 'news-date-time'}).text.strip()
        texts = content.find('div', {'class': 'news-detail'}).text.split('\n')
        to_join_texts = []
        for text in texts:
            text = text.strip()
            if len(text) == 0:
                continue
            if text == date:
                continue
            if text == 'Хабарлар':
                continue
            if text == 'Статья':
                continue
            to_join_texts.append(text)

        article = '\n'.join(to_join_texts)
        with open(f'./parsed_data/khakaschiry/{idx}.txt', 'w', encoding='utf-8') as f:
            f.write(article)


def main():
    save_dir = './parsed_data/khakaschiry'
    os.makedirs(save_dir, exist_ok=True)

    pool = Pool(os.cpu_count())
    pool.map(parse_page, range(0, 12571))


if __name__ == '__main__':
    main()