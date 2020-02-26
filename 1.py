"""
Задача.
Спарсить и вывести список самых больших звезд из статьи по адресу:
http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html
и сохранить в .txt файл.
"""
import requests
from bs4 import BeautifulSoup

url = "http://light-science.ru/kosmos/vselennaya/top-10-samyh-bolshih-zvezd-vo-vselennoj.html"
# url - адрес сайта для парсинга;

myheader = {'user-agent': 'Mozilla Firefox/51.0.1'}
# myheader - юзер-агент, нужно включить чтобы requests возвращал 200(успех), 
# вместо 403(доступ запрещен);

response = requests.get(url, headers=myheader)
# получаем текст html по ссылке, используя юзер-агент, без этого агента сайт
# будет считать наш запрос ботом;

#print(response.text)
# вывод html текста;

#print(response.headers)
# вывод html заголовков;

html = response.text
# записываем текст в html;

soup = BeautifulSoup(html, 'html.parser')
# делаем суп(?) из html, используя для парсинга библиотеку html.parser;

container = soup.find('div', {'class':'td-post-content'})
# ограничиваем поиск до записей, содержащих класс td-post-content;

elements = container.find_all('p')
# в elements записываем все тэги <p>...</p>;

result = 'Топ самых больших звезд: \n'
# создаем заголовок для итогового списка;

for element in elements:
    if element.find('strong'):
        # если внутри тэга <p> находим тэг <strong>;
        result += element.find('strong').text + '\n'
        # то выводим содержимое тэга <strong>;

with open('result.txt', 'w', encoding='utf-8') as f:
    # открываем файл result.txt (в таком виде должен быть в той же папке что
    # и py-файл, иначе нужно указывать весь путь к файлу txt;
    # 'w' - открываем для записи (write);
    # encoding='utf-8' - кодируем в utf-8;
    # as f - присваиваем элиас f;
    f.write(result)
    # записываем туда строку с результатом;

"""
Результа.
Топ самых больших звезд:
1. VY Большого Пса
2. VV Цефея A
3. Мю Цефея
4. V838 Единорога
5. WHO G64
6. V354 Цефея
7. KY Лебедя
8. KW Стрельца
9. RW Цефея
10. Бетельгейзе
"""
