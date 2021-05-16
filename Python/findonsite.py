import requests
from bs4 import BeautifulSoup

def format_text():
    with open('Python/file.txt', 'r', encoding='utf-8') as f:
        lst = f.readlines()
        for i in lst:
            if '<a class="cardVideo__cardImgTop cardImgTop cardImgTop_22x12"' in i:
                pass
            else:
                lst[lst.index(i)] = ''
        passer = False
        while passer != True:
            try:
                lst.remove('')
            except:
                passer = True
        print(lst[0:50])

if False:
    f =  open('Python/file.txt', 'w', encoding='utf-8')
    for ind in range(1,100):
        url = f'https://www.karusel-tv.ru/video?page={ind}'
        try:
            product_url = requests.get(url)
            soup = BeautifulSoup(product_url.text, 'lxml')
            page = soup.find_all('a')

            for i in page:
                f.write(str(i))
        except ConnectionError:
            f.close()
            break
format_text()