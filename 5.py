"""
Задача.
Получить список всех велосипедов на странице, их название, код, описание и цену,
записать результат в csv.
"""
import csv
import requests
from bs4 import BeautifulSoup

url = 'http://sportunit.ru/velosipedy?limit=100'
# url - адрес сайта для парсинга;

response = requests.get(url)
# получаем текст html по ссылке;

html = response.text
# записываем текст в html;

multi_class  = 'product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12'.split(' ')
# содержит в себе мультиклассы - набор из нескольких классов и превращаем в массив;

soup = BeautifulSoup(html, 'html.parser')
# делаем суп из html, используя для парсинга библиотеку html.parser;

products = soup.find_all('div', {'class':'col-xs-12'})
# находим всё по тэгу <div> и любым из мультиклассов multi_class;

all_products = []
# массив для хранения всех результатов по продуктам;
for product in products:
    if product.attrs['class'] == multi_class:
    # находим product, у которых в атрибутах (attrs) именно мультикласс;
        image = product.find('img')['src']
        # получаем ссылку на изображение;
        name = product.find('div', {'class':'product-name'}).text
        # получаем имя продукта;
        product_description = product.find('div', {'class':'product-description'}).text
        # получаем описание продукта;
        product_model = product.find('div', {'class':'product-model'}).text
        # получаем номер модели продукта;
        price = product.find('p', {'class':'price'}).text.strip().replace('р.','')
        # получаем цену продукта;
        all_products.append([name, product_description, product_model, price, image])
        # записываем это всё в список, каждый эл-нт которого это список с данными
        # по одному продукту;
        
names = ['Наиманование','Описание','Артикль','Цена','Изображение']

with open('data.csv', 'r', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(names)
    
    for product in all_products:
        writer.writerow(product)
        
"""
Результа.
Хз, не записывается в csv =(
Но данные собирает.
"""
