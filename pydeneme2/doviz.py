from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd


url='https://www.tcmb.gov.tr/kurlar/today.xml'
path='./chromedriver.exe'
service=Service(executable_path=path)

driver=webdriver.Chrome(service=service)

driver.get(url)
wait   = WebDriverWait(driver, 10)
table  = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"table.kurlarTablo")))

prices=driver.find_elements(by='xpath', value='//table[contains(@class,"kurlarTablo")]')

cells=[]


for price in prices:
    cells.append([c.text.strip() for c in price.find_elements(By.TAG_NAME, "td")])
    
    

driver.quit()
df_cells=pd.DataFrame({'title': cells}).to_csv('doviz.csv', index=False)
