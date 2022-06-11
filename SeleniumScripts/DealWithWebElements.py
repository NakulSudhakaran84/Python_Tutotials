from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service

#s=Service("G:\\Q Spiders\\Python 3.8.7\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome(executable_path="G:\\Q Spiders\\Python 3.8.7\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.google.com")
#input=driver.find_element_by_name("q")
input=driver.find_element(By.NAME,"q")
input.send_keys("python")
input.send_keys(Keys.ENTER)

driver.quit()


