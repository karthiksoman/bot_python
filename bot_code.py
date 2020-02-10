from selenium import webdriver
import sys
driver = webdriver.Chrome('/usr/local/bin/chromedriver.exe')
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath('//*[@id="email"]').send_keys(sys.argv[1])
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(sys.argv[2])
driver.find_element_by_xpath('//*[@id="u_0_2"]').click()
driver.find_element_by_xpath('//*[@id="facebook"]/body').click()
driver.maximize_window()
# driver.find_element_by_xpath('//*[@id="js_c2"]/div/div/ul/li[9]').click()
# driver.close()
