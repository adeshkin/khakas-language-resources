from glob import glob
import pandas as pd


def main():
    data_dir = './parsed_data/khakaschiry'
    paths = sorted(glob(f'{data_dir}/*.txt'))
    texts = []
    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
        texts.append(text)
    df = pd.DataFrame({'text': texts})
    df.to_csv(f'./parsed_data/khakaschiry.csv', index=False)


if __name__ == '__main__':
    main()
