import pandas as pd
import re
import os


def main():
    data_dir = './prepared_data'
    mode = 'train'

    with open(f'{data_dir}/{mode}.kjh', 'r', encoding='utf-8') as f:
        k_sents = [x.strip() for x in f.readlines()]

    with open(f'{data_dir}/{mode}.ru', 'r', encoding='utf-8') as f:
        r_sents = [x.strip() for x in f.readlines()]

    assert len(k_sents) == len(r_sents)

    df = pd.DataFrame({'kjh': k_sents, 'ru': r_sents})
    df['kjh'] = df['kjh'].apply(lambda x: re.sub('ӌ', 'ҷ', x))

    # symbols = sorted(set(' '.join(df['kjh'])))
    # step = 15
    # for start in range(0, len(symbols), step):
    #     print(symbols[start:start+step])
    #     print()

    save_dir = './data'
    os.makedirs(save_dir, exist_ok=True)

    df.to_csv(f'./{save_dir}/{mode}.csv', index=False)


if __name__ == '__main__':
    main()
