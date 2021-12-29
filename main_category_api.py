from bs4 import BeautifulSoup
import requests,os

main_page= BeautifulSoup(requests.get('https://wallpapercave.com/categories').text,'html.parser')

all_categories = [f"{item.get('href').split('/')[-1]}" for item in main_page.find('ul',{'id':'catsinbox'}).find_all('a')]

# for variable in all_category_links:
#     print(variable)