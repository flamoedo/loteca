from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import numpy as np
import time

import pandas as pd

chrome_options = Options()  
# chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.implicitly_wait(1)

td_ = []

url = "http://bra.worldfootball.net/tabela_e_jogos/" #bra-serie-a-2018-spieltag/1/

def navigate(init_url):

    my_url = init_url

    for liga in ('bra-serie-b-','bra-serie-a-'):

        for ano in range(2011,2019, 1):

            for rodada in range(1,39, 1):

                my_url = init_url + liga + str(ano) + '-spieltag/' + str(rodada) + '/'

                driver.get(my_url)

                tables_element = driver.find_elements_by_xpath("//*[contains(@class,'standard_tabelle')]")

                row = tables_element[0]
                tr = row.find_elements_by_tag_name("tr")

                for td in tr:
                    tx = td.find_elements_by_tag_name("td") 
                    g = [x.text for x in tx]
                    if g != []:
                        td_.append(g)

                # np.save('arquivo2',td_)
                # np.savetxt('test.out', td_, delimiter=',')

                df = pd.DataFrame(td_,columns=['Data','Hora','Home','S','Away','Res','',''])

                df.to_csv('arquivo3.csv')

if __name__ == "__main__":
    navigate(url)

