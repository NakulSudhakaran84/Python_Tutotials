from  selenium import webdriver

driver=webdriver.Firefox(executable_path="G:\\Q Spiders\\Python 3.8.7\\geckodriver-v0.29.0-win32\\geckodriver.exe")
driver.get("http://www.google.com")
print(driver.title())
driver.close()