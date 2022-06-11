from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.implicitly_wait(10)

searchTab=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("samsung phones")
selectedPhone=driver.find_element(By.XPATH,"//div[@data-keyword='samsung phones under 30000']").click()
search=driver.find_element(By.XPATH,"//div[@class='nav-search-submit nav-sprite']").click()
checkbox=driver.find_element(By.XPATH,"//li[@aria-label='Samsung']/span//div/label/i[@class='a-icon a-icon-checkbox']").click()

phones=driver.find_elements(By.XPATH,"//div//a/span[@class='a-size-medium a-color-base a-text-normal']")
prices=driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")

myPhones=[]
myPrices=[]

for phone in phones:
   # print("Phone names :",phone.text)
    myPhones.append(phone.text)

print("*"*50)

for price in prices:
   # print("Price : ",price.text)
    myPrices.append(price.text)


finallist=zip(myPhones,myPrices)

#for data in list(finallist):
 #   print(data)

wb=Workbook()
wb["Sheet"].title="Samsung Phones"
sh=wb.active

sh.append(['Model','Price'])

for i in list(finallist):
    sh.append(i)

wb.save("C:\\Users\\Nakul Sudhakaran\\Desktop\\SamsungPhonePriceList.xlsx")



driver.quit()