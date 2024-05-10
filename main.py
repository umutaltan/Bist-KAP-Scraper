import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

#siteye istek atılır.
def get_request(url):
    response = requests.get(url)
    return response

#haberler, hisse kodları ve tarihler döndürülür.
def get_news(hisse_kodu,id,url):
    new_url = ""
    kaplar = []
    
    for i in range(id,id-20,-1):
        new_url = url + str(i)
        
        soup = BeautifulSoup(get_request(new_url).text, 'html.parser')

        if soup.find('div', class_='type-medium bi-dim-gray').text == hisse_kodu:
            kaplar.append([soup.find('div', class_='type-medium bi-dim-gray').text,
                           soup.find('div', class_='type-medium bi-sky-black').text,
                           soup.find('td', class_='taxonomy-context-value-summernote multi-language-content content-tr').text])
    return kaplar

def get_latest_KAP_link(url,xpath,attribute):
    driver = webdriver.Firefox() #driver objesini oluştur
    driver.get(url) # web sitesini aç
    driver.implicitly_wait(3) #üç saniye bekle
    elements = driver.find_elements(By.XPATH,xpath) #xpath'e göre id elementini al

    for element in elements: #elementin href etiketini alarak linkini bul
        element_href = element.get_attribute(name=attribute)

    son_kap_id = element_href.split("/")[-1] #KAP'ın linkinin sonunu al
    driver.quit() #tarayıcıyı kapat
    return int(son_kap_id)

url="https://www.kap.org.tr/tr/"
xpath="/html/body/div[7]/div/div[6]/disclosure-list/div/div/div/div[1]/disclosure-list-item[1]/div/div/div/div/div[7]"
attr="href"


id=get_latest_KAP_link(url,xpath,attr)
hisse_kodu=input("HISSE KODU: ")
kap_news = get_news(hisse_kodu,id,url+'Bildirim/')
for kap in kap_news:
    for kap_detay in kap:
        print(kap_detay)
    print("\n")
#taxonomy-context-value-summernote multi-language-content content-tr
