import os

import pandas as pd
import re





def main():
    # khak_symbols = ['ӧ', 'ң', 'і', 'ҷ', 'ғ', 'ӱ']
    # print(khak_symbols)
    # print([x.upper() for x in khak_symbols])
    # pd.set_option('display.max_colwidth', None)

    data_dir = './parsed_data'
    save_dir = './data'
    os.makedirs(save_dir, exist_ok=True)
    for name in ['khakaschiry', 'vk_ah_tashyl', 'vk_khakas_chiry', 'vk_khakas_radio', 'vk_ust_chul']:
        path = f'{data_dir}/{name}.csv'
        df = pd.read_csv(path)
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        df['text'] = df['text'].apply(lambda x: x.strip())

        map_symbols = {'#ХакасРадио': '',
                       r'http\S+': '',
                       'ў': 'ӱ',
                       'ÿ': 'ӱ',
                       'ұ': 'ӱ',
                       'ө': 'ӧ',
                       'ö': 'ӧ',
                       'Ö': 'Ӧ',
                       'Ө': 'Ӧ',
                       'ӊ': 'ң',
                       'Ӌ': 'Ҷ',
                       'ӌ': 'ҷ',
                       'I': 'І',
                       'i': 'і',
                       'Ӏ': 'І',
                       'ỉ': 'і',
                       'İ': 'І',
                       'І': 'І',
                       'ë': 'ё',
                       'Ё': 'Ё',
                       '\xa0': '',
                       '\xad': '',
                       '\u200d': '',
                       '\ufeff': '',
                       r"(\W)\1{2,}": r"\1",  # repeated 3 or more times
                       r'Автор :\s*.*': ' ',
                       'сом орыны': ' '
                       }

        for symbol1, symbol2 in map_symbols.items():
            df['text'] = df['text'].apply(lambda x: re.sub(symbol1, symbol2, x))

        df['not_text'] = df['text'].apply(lambda x: not bool(re.search(r'\w', x)))
        df.drop(df[df['not_text']].index, inplace=True)
        df.drop('not_text', axis=1, inplace=True)

        df['len'] = df['text'].apply(lambda x: len(x))
        df.drop(df[df['len'] < 5].index, inplace=True)
        df.drop('len', axis=1, inplace=True)

        df.drop_duplicates(inplace=True)
        df.dropna(inplace=True)

        # symbols = sorted(set(' '.join(df['text'])))
        # step = 15
        # for start in range(0, len(symbols), step):
        #     print(symbols[start:start+step])
        #     print()

        # df['a'] = df['text'].apply(lambda x: not bool(re.search("[ӧңіҷғӱ]", x.lower())))
        # df[df['a']]

        # df.sample(3, random_state=97)

        df.to_csv(f'./{save_dir}/{name}.csv', index=False)


if __name__ == '__main__':
    main()
