from selenium import webdriver
import sys
import time
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})
driver = webdriver.Chrome(chrome_options=option,executable_path='/usr/local/bin/chromedriver.exe')
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath('//*[@id="email"]').send_keys(sys.argv[1])
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(sys.argv[2])
driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()
driver.find_element_by_xpath('//*[@id="js_ot"]/div/div/ul/li[9]/a/span/span').click()