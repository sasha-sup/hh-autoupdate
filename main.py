import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if 'HH_USER' in os.environ and 'HH_PASSWORD' in os.environ:
    username=os.environ['HH_USER']
    password=os.environ['HH_PASSWORD']
else:
    sys.exit("Credentials are not defined.")

capabilities = {
    "browserName": "chrome",
    "browserVersion": "103.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

def setup_driver():
    web = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)
    return(web)

def get_page():
    delay=10
    wait=time.sleep(5)
    page=setup_driver()
    page.get('https://hh.ru/account/login?backurl=%2F&hhtmFrom=main')
    WebDriverWait(page, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/form/div[4]/button[2]')))
    page.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/form/div[4]/button[2]').click()
    page.find_element(by=By.XPATH, value='//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[1]/fieldset/input').send_keys(username)
    page.find_element(by=By.XPATH, value='//*[@id="HH-React-Root"]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[2]/fieldset/input').send_keys(password)
    page.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/form/div[4]/div/button[1]').click()
    WebDriverWait(page, delay).until(EC.presence_of_all_elements_located((By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div/div/div[1]/a')))
    wait
    page.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[2]/div[1]/div/div/div/div[1]/a').click()
    wait
    page.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[3]/div[1]/div/div/div[1]/div[3]/div[4]/div/div[6]/div/div/div/div[1]/span/button').click()
    page.quit()

def main():
    get_page()

if '__main__' == __name__:
    main()    