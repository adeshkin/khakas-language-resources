import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


def main():
    data_dir = './data'
    path = f'{data_dir}/vk_ust_chul.csv'
    print(path)
    df = pd.read_csv(path)
    num_sents = 0
    num_words = 0
    texts = df['text'].values.tolist()
    num_texts = len(texts)

    for text in texts:
        num_sents += len(sent_tokenize(text))
        num_words += len(text.split())

    print('# texts:', num_texts)
    print('# sentences:', num_sents)
    print('# words:', num_words)


if __name__ == '__main__':
    main()
