import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import os


def main():
    articles = []
    for idx in tqdm(range(0, 12571)):
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

            articles.append(article)

    save_dir = './parsed_data'
    os.makedirs(save_dir, exist_ok=True)

    df = pd.DataFrame({'text': articles})
    df.to_csv(f'{save_dir}/khakaschiry.csv', index=False)


if __name__ == '__main__':
    main()