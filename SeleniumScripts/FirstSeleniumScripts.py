from selenium import webdriver

driver=webdriver.Chrome(executable_path="G:\\Q Spiders\\Python 3.8.7\\chromedriver_win32\\chromedriver.exe")
#print(type(driver))
driver.get("http://www.google.com")
myPageTitle=driver.title
print(myPageTitle)
assert "Google" in myPageTitle

#print(driver.quit)
driver.quit()