from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import numpy as np
import time


driver = webdriver.Chrome()
driver.implicitly_wait(1)

td_ = []
tr_ = []

my_url = "http://loterias.caixa.gov.br/wps/portal/loterias/landing/loteca"

def navigate(my_url):
    driver.get(my_url)
    
    for i in range(826):
        
        inp =  driver.find_elements_by_id("buscaConcurso")
        inp[0].clear()
        inp[0].send_keys(('00' + str(i + 1))[-3:])
        inp[0].send_keys(u'\ue007')      
        
        titles_element = driver.find_elements_by_xpath("//div/h2/span")
        tables_element = driver.find_elements_by_xpath("//*[contains(@class,'table-d loteca hidden-mobile')]")
        
        time.sleep(5)        

        for row in tables_element:
            tr = row.find_elements_by_tag_name("tr")
            for td in tr:
                tx = td.find_elements_by_tag_name("td") 
                g = [x.text for x in tx]
                if g != []:
                    g.insert(0,titles_element[3].text)
                    td_.append(g)
                  
                
        np.save('arquivo',td_)

if __name__ == "__main__":
    navigate(my_url)

