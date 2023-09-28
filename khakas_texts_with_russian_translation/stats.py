import pandas as pd


def main():
    data_dir = './data'
    mode = 'test'
    path = f'{data_dir}/{mode}.csv'
    print(path)

    df = pd.read_csv(path)

    k_sents = df['kjh'].values.tolist()
    r_sents = df['ru'].values.tolist()

    assert len(k_sents) == len(r_sents)
    num_sents = len(k_sents)

    num_k_words = 0
    for k_sent in k_sents:
        num_k_words += len(k_sent.split())

    num_r_words = 0
    for r_sent in r_sents:
        num_r_words += len(r_sent.split())

    print('# sentences:', num_sents)
    print('# kjh words:', num_k_words)
    print('# ru words:', num_r_words)


if __name__ == '__main__':
    main()
