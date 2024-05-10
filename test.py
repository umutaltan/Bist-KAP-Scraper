from selenium import webdriver
from selenium.webdriver.common.by import By
# Chrome WebDriver'ı başlat
"""driver = webdriver.Firefox()

# Web sitesini ziyaret et
driver.get("https://www.kap.org.tr/tr/")

# Dinamik içeriğin yüklenmesini bekle
driver.implicitly_wait(3)

# Belirli bir sınıfa sahip olan elementi bulun
elements = driver.find_elements(By.XPATH,'/html/body/div[7]/div/div[6]/disclosure-list/div/div/div/div[1]/disclosure-list-item[1]/div/div/div/div/div[7]')

# Elementin özelliklerini yazdır
for element in elements:
    element_href = element.get_attribute(name='href')

son_kap_id = element_href.split("/")[-1]
print(son_kap_id)
# Tarayıcıyı kapat
driver.quit()"""


def get_latest_KAP_link(url,xpath,attribute):
    driver = webdriver.Firefox() #driber objesini oluştur
    driver.get(url) # web sitesini aç
    driver.implicitly_wait(3) #üç saniye bekle
    elements = driver.find_elements(By.XPATH,xpath) #xpath'e göre id elementini al

    for element in elements: #elementin href etiketini alarak linkini bul
        element_href = element.get_attribute(name=attribute)

    son_kap_id = element_href.split("/")[-1] #KAP'ın linkinin sonunu al
    driver.quit() #tarayıcıyı kapat
    return son_kap_id


url ="https://www.kap.org.tr/tr/"
xpath="/html/body/div[7]/div/div[6]/disclosure-list/div/div/div/div[1]/disclosure-list-item[1]/div/div/div/div/div[7]"
attribute="href"

print(get_latest_KAP_link("https://www.kap.org.tr/tr/","/html/body/div[7]/div/div[6]/disclosure-list/div/div/div/div[1]/disclosure-list-item[1]/div/div/div/div/div[7]","href"))