from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from tqdm import tqdm
import time


search_input = str('Detector de metais')
msg_send = str('Muito Legal.')

wd = webdriver.Chrome()
wdw = WebDriverWait(wd, 10)  # Expected Conditions


login_url = 'https://accounts.google.com/signin/v2/identifier'
yt_url = f'https://www.youtube.com/results?search_query={search_input}'

href_list = []


def login(wd, login_url):
    wd.get(login_url)
    wd.maximize_window()

    login_locator = (By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')
    wdw.until(expect.presence_of_element_located(login_locator))
    login_box = wd.find_element(*login_locator)  # Vira somente find_element
    login_box.send_keys('email')

    # Nesse caso CSS.SELECTOR não se usa // nem @
    next_locator = (By.CSS_SELECTOR, 'span[class="RveJvd snByac"]')
    wdw.until(expect.presence_of_element_located(next_locator))
    next_bt = wd.find_element(*next_locator)
    next_bt.click()
    time.sleep(2)

    
    key_locator = (By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')
    wdw.until(expect.presence_of_element_located(key_locator))
    key_box = wd.find_element(*key_locator)
    key_box.send_keys('pass')
    
    enter_locator = (By.CSS_SELECTOR, 'span[class="RveJvd snByac"]')
    wdw.until(expect.presence_of_element_located(enter_locator))
    enter = wd.find_element(*enter_locator)
    enter.click()
    time.sleep(5)


def youtube(wd, yt_url, search_input, href_list, msg_send, wdw):
    wd.get(yt_url)
    time.sleep(5)
    wd.execute_script('window.scrollBy(0,3000)', '')
    time.sleep(5)
    hrefs = wd.find_elements_by_xpath(
        '//a[@class="yt-simple-endpoint style-scope ytd-video-renderer"]')
    for href in tqdm(hrefs):
        href_list.append(href.get_attribute('href'))
    for get in tqdm(href_list):
        wd.get(get)
        time.sleep(5)
        like_bt = wd.find_element_by_xpath(
            '//yt-icon[@class="style-scope ytd-toggle-button-renderer"]')
        like_bt.click()
        wd.execute_script('window.scrollBy(0,700)', '')
        time.sleep(15)
        # Expected Conditions
        locator = (By.CSS_SELECTOR, '#contenteditable-root')
        wdw.until(expect.presence_of_element_located(
            locator))  # Expected Conditions
        cmt_box = wd.find_element(*locator)
        cmt_box.click()
        time.sleep(1)
        send_box = wd.find_element_by_xpath(
            '//paper-button[@class="style-scope ytd-button-renderer style-primary size-default]')
        send_box.click()
        time.sleep(5)


login(wd, login_url)
youtube(wd, yt_url, search_input, href_list, msg_send, wdw)
