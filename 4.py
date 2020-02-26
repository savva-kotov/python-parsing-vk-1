"""
Задача.
Найти среднее количество голов команды за матч.
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.worldfootball.net/teams/leicester-city/2013/3/'
# url - адрес сайта для парсинга;

response = requests.get(url)
# получаем текст html по ссылке;

html = response.text
# записываем текст в html;

soup = BeautifulSoup(html, 'html.parser')
# делаем суп из html, используя для парсинга библиотеку html.parser;

table = soup.find('table', {'class': 'standard_tabelle'})
# находим тэги <table> с классом standard_tabelle;

lines = table.find_all('tr')
# в table  записываем все тэги <tr>...</tr>;

res = []
# переменная с результатом;
for line in lines:
    elements = line.find_all('td')
    # во всех тэгах <tr> находим тэги <td>;
    if len(elements) == 8:
    # и если их длина равна 8;
        res.append(int(elements[6].text.strip().split(':')[0]))
        # то берем текст из 6-го элемента, там где хранятся результаты матча;
        # strip() - возвращает копию строки, в которой все символы были 
        # удалены с начала и конца строки (символом по умолчанию является пробел);
        # split(':') - разделяем эл-ты по двоеточию и делаем списко, берем 
        # первый эл-нт и добавляем в список res для среднего;
print(sum(res) / len(res))

"""
Результа.
1.5660377358490567
"""
