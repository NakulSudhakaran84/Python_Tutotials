from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="G:\\Q Spiders\\Python 3.8.7\\chromedriver_win32\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

driver.maximize_window()

print(driver.title)
driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "button").click()

driver.find_element(By.XPATH, "//a[@id='menu_admin_viewAdminModule']").click()
driver.find_element(By.XPATH, "//a[@id='welcome']").click()
time.sleep(3)
# Logout=driver.find_element((By.XPATH,"//a[@href='/index.php/auth/logout']")).click()

driver.quit()
