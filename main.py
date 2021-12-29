from bs4 import BeautifulSoup
import requests
import os
from main_category_api import all_categories

if os.path.isdir('Download') == False:
    os.makedirs('Download')
folder_path = f"{os.getcwd()}\\Download"


for category in all_categories:
    page = BeautifulSoup(requests.get(
        f'https://wallpapercave.com/categories/{category}').text, 'html.parser')
    links = [f"https://wallpapercave.com{item.get('href')}" for item in page.find_all(
        'div', class_="albumphoto")]

    # os.mkdir(f'{folder_path}\\{category}')
    for page_link in links:
        page_2nd = BeautifulSoup(requests.get(page_link).text, 'html.parser')

        download_links = [
            f"https://wallpapercave.com{item.get('href')}" for item in page_2nd.find_all('a', class_="download")]

        # for i in download_links:
        #     print(f"{i.split('/')[-1]}")
        # for making derectorys
        os.makedirs(f'{folder_path}\\{category}\\{page_link.split("/")[-1]}')
        for link in download_links:
            image = requests.get(link)  # for getting link of specific image
            # for download imgae files to specific location
            with open(f'{folder_path}\\{category}\\{page_link.split("/")[-1]}\\{link.split("/")[-1]}.jpg', 'wb') as i:
                i.write(image.content)
