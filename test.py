from selenium import webdriver
from selenium.webdriver.common.by import By
# Chrome WebDriver'ı başlat
driver = webdriver.Firefox()

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
driver.quit()
