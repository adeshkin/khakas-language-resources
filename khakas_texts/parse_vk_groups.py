import os
import vk_api
import pandas as pd
from tqdm import tqdm


def main():
    def auth_handler():
        key = input("Enter authentication code: ")
        remember_device = True
        return key, remember_device

    login = input("Enter your login: ")
    password = input("Enter your password: ")

    vk_session = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler, app_id=2685278)
    vk_session.auth()

    tools = vk_api.VkTools(vk_session)

    khakas_vk_groups = {'vk_khakas_radio': ('183612544', 'https://vk.com/club183612544'),
                        'vk_khakas_chiry': ('98093412', 'https://vk.com/khakas_chiry'),
                        'vk_ah_tashyl': ('31631018', 'https://vk.com/club31631018'),
                        'vk_ust_chul': ('16506982', 'https://vk.com/club16506982')}

    save_dir = './parsed_data'
    os.makedirs(save_dir, exist_ok=True)

    for group in khakas_vk_groups:
        group_id = khakas_vk_groups[group][0]
        wall = tools.get_all('wall.get', 20, {'owner_id': f'-{group_id}'})

        posts = wall['items']
        texts = []
        for post in tqdm(posts, desc=group, total=len(posts)):
            if 'text' in post:
                texts.append(post['text'])

        df = pd.DataFrame({'text': texts})
        df.to_csv(f'{save_dir}/{group}.csv', index=False)


if __name__ == '__main__':
    main()
