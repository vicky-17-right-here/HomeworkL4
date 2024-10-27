# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import time

# chromedriver_path = "./chromedriver"
# service = Service(executable_path=chromedriver_path)
# driver = webdriver.Chrome(service=service)
# driver.get("https://24h.pchome.com.tw/")
# time.sleep(3)

# driver.find_element(By.XPATH,"//input[@type='search']").click()

# while True:
#         keyword = input("請輸入想尋找的商品: ")

#         try:
#             driver.find_element(By.XPATH,"//input[@type='search']").clear()
#             time.sleep(3)
#             driver.find_element(By.XPATH,"//input[@type='search']").send_keys("手機")
#             time.sleep(3)
#             driver.find_element(By.XPATH,"//input[@type='search']").send_keys(Keys.ENTER)
#             time.sleep(3)

#             driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div/section[2]/div/div/section/div/div/div[1]/div/div/ul/li[1]/div/div/div[2]/ul/li[1]/label/div[3]").click()
#             time.sleep(3)
#             driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div/section[2]/div/div/section/div/div/div[1]/div/div/ul/li[1]/div/div/div[2]/ul/li[3]/label/div[2]").click()
#             time.sleep(3)

#             break  

#         except NoSuchElementException:
#             print("找不到相關商品，請重新輸入。")
# driver.quit()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chromedriver_path = "./chromedriver"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://24h.pchome.com.tw/")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@type='search']").click()

while True:
        keyword = input("請輸入想尋找的商品: ")

        try:
            driver.find_element(By.XPATH,"//input[@type='search']").clear()
            time.sleep(3)
            driver.find_element(By.XPATH,"//input[@type='search']").send_keys("手機")
            time.sleep(3)
            driver.find_element(By.XPATH,"//input[@type='search']").send_keys(Keys.ENTER)
            time.sleep(3)

            driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div/section[2]/div/div/section/div/div/div[1]/div/div/ul/li[1]/div/div/div[2]/ul/li[1]/label/div[3]").click()
            time.sleep(3)
            driver.find_element(By.XPATH,"/html/body/div[1]/main/div/div/div/section[2]/div/div/section/div/div/div[1]/div/div/ul/li[1]/div/div/div[2]/ul/li[3]/label/div[2]").click()
            time.sleep(3)

            sort_option =input("請輸入你的過濾條件:1. 推薦排行, 2. 新上架, 3. 價格:")

            if sort_option == "1":
                driver.find_element(By.XPATH,"//span[text()='推薦排行']").click()
            elif sort_option == "2":
                driver.find_element(By.XPATH,"//span[text()='新上架']").click()
            elif sort_option == "3":
                driver.find_element(By.XPATH,"//span[text()='價格']").click()
            
            else:
              print("無法辨識你的選項，請重新輸入。")
              break  

        except NoSuchElementException:
            print("找不到相關商品，請重新輸入。")
driver.quit()        
