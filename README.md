

### Monolingual khakas data:
- located - **khakas_texts/data**

```python
import pandas as pd

name = 'khakaschiry'
path = f'khakas_texts/data/{name}.csv'
df = pd.read_csv(path)
texts = df['text'].values.tolist()

print(texts[0])
```

|      name       |            source            | # texts | # sentences | # words | comment                                                                                             | 
|:---------------:|:----------------------------:|:-------:|:-----------:|---------|-----------------------------------------------------------------------------------------------------|
|   khakaschiry   |  https://www.khakaschiry.ru  |  12013  |   271183    | 2914305 | the texts are articles about something, perfect texts in the Khakas language                        |
|  vk_ah_tashyl   | https://vk.com/club31631018  |   828   |    4884     | 45917   | the texts are different posts from the vk group, about 10-20 percent of the texts may be in Russian |
| vk_khakas_chiry | https://vk.com/khakas_chiry  |  2045   |    36793    | 401597  | the texts are different posts from the vk group, about 10-20 percent of the texts may be in Russian |
| vk_khakas_radio | https://vk.com/club183612544 |  5138   |    36532    | 348552  | the texts are different posts from the vk group, about 10-20 percent of the texts may be in Russian |
|   vk_ust_chul   | https://vk.com/club16506982  |  1267   |    6217     | 50187   | the texts are different posts from the vk group, about 10-20 percent of the texts may be in Russian |



### Parallel corpus:
- located - **khakas_texts_with_russian_translation/data**
- _kjh_ - khakas
- _ru_ - russian
- source - https://khakas.altaica.ru/texts

```python
import pandas as pd

mode = 'train'
path = f'khakas_texts_with_russian_translation/data/{mode}.csv'
df = pd.read_csv(path)
pairs = df[['kjh', 'ru']].values.tolist()
print(pairs[0])
```

|                 | # sentences | 
|:---------------:|:-----------:|
|      train      |    79836    |
|       val       |    1000     |
|      test       |    1000     | 


|             | train  | val   | test  | 
|:-----------:|--------|-------|:-----:|
| # kjh words | 589470 | 11734 | 11554 |
| # ru words  | 642068 | 12893 | 12528 |


