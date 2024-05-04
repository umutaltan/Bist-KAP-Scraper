import requests
from bs4 import BeautifulSoup

def get_request(url):
    response = requests.get(url)
    return response

def get_news(hisse_kodu,kap_tarihi,url):
    new_url = ""
    kaplar = []
    for i in range(1281426,1281326,-1):
        new_url = url + str(i)
        
        soup = BeautifulSoup(get_request(new_url).text, 'html.parser')

        if soup.find('div', class_='type-medium bi-dim-gray').text == hisse_kodu:
            kaplar.append([soup.find('div', class_='type-medium bi-dim-gray').text,
                           soup.find('div', class_='type-medium bi-sky-black').text])
    return kaplar

# Veri çekeceğiniz web sitesinin URL'si 1281426
url = 'https://www.kap.org.tr/tr/Bildirim/'

hisse_kodu=input()

print(get_news(hisse_kodu,2,url))

