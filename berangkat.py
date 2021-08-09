import time
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def click_xpath (str): 
    while 1==1:
        try:
            vo_button = browser.find_element_by_xpath (str)
            break
        except:
            pass

    time.sleep (0.2)
    browser.execute_script("arguments[0].click();", vo_button)

def get_focus_xpath (str):
    v_timeout = time.time() + 20
    vo_result = 0
    while True:
        try:
            vo_result = browser.find_element_by_xpath (str)
            break
        except:
            if time.time() > v_timeout:
                break
    return vo_result

def depart_all():

    click_xpath ('//*[@id="mapAcList"]')
    click_xpath ('//*[@id="flightStatusLanded"]')
    click_xpath ('//*[@id="listDepartAll"]/div/button[1]')

def get_marketing():
    click_xpath ('/html/body/div[7]/div/div[3]/div[5]')
    click_xpath ('//*[@id="popBtn2"]')
    click_xpath ('//*[@id="newCampaign"]')
    # airlines marketing:

    click_xpath ('//*[@id="campaign-1"]/table/tbody/tr[1]')
    time.sleep(1)
    v_options = Select(browser.find_element_by_xpath('//*[@id="dSelector"]'))
    v_options.select_by_value('3')

    time.sleep (2.1)
    click_xpath ('//*[@id="c4Btn"]')

def full_tank():
    # full tank fuel:
    click_xpath('//*[@id="mapMaint"]')
    state_string=WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="remCapacity"]')))
    
    v_capacity = browser.find_element_by_xpath ('//*[@id="remCapacity"]')
    v_purchase = browser.find_element_by_xpath ('//*[@id="amountInput"]')
    v_purchase.clear()

    # only fill tank if value below 6000000
    if(int(v_capacity.text) > 64000000):
        v_purchase.send_keys (str(6000000))
        time.sleep(0.5)


    click_xpath('//*[@id="fuelMain"]/div/div[7]/div/button[2]')

    time.sleep(3)
    # full tank co:
    click_xpath('//*[@id="popBtn2"]')
    time.sleep(0.5)
    v_capacity = browser.find_element_by_xpath ('//*[@id="remCapacity"]')
    v_purchase = browser.find_element_by_xpath ('//*[@id="amountInput"]')
    v_purchase.clear()

    v_purchase.send_keys (v_capacity.text)
    time.sleep(0.5)

    click_xpath('//*[@id="co2Main"]/div/div[8]/div/button[2]')
    
    
    click_xpath ('//*[@id="popup"]/div/div/div[1]/div/span')

    time.sleep(2)

def fill_tanks_and_depart_all():
    while True:
        v_found = 0
        v_timeout = time.time() + 5
        while True:
            try:
                time.sleep(0.2)
                v_departall = browser.find_element_by_xpath ('//*[@id="listDepartAll"]/div/button[2]')
                if v_departall.is_displayed():
                    v_found = 1
                    break
                    
            except:
                pass

            if time.time() > v_timeout:
                break
        
        if v_found == 1:
            full_tank()
            time.sleep(2)
            depart_all()
            time.sleep(2)
        else:
            break

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(os.environ.get("AM4_URL"))
    browser.find_element_by_xpath ('//*[@id="flightStatusInflight"]')

    browser.implicitly_wait(2)

    fill_tanks_and_depart_all()
    