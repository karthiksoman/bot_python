from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver.exe')
driver.get("https://www.facebook.com/")
driver.close()
