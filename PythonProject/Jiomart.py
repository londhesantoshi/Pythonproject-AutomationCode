from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.jiomart.com/")
driver.maximize_window()
driver.implicitly_wait(2)
menu=driver.find_element(By.XPATH, "//button[@id='btn_ham_menu']").click()
sel_by_cat=driver.find_element(By.XPATH, "(//a[@class='d-flex'])[2]").click()
furniture_cat=driver.find_element(By.XPATH, "(//div[@class='jm-list-content jm-list-gap']//div[2])[11]").click()
work_study_cat = driver.find_element(By.XPATH, "//div[contains(text(),'Work')]").click()
chairs = driver.find_element(By.XPATH, " //div[@id='sub-category-13452']/a[1]").click()
sort_by= driver.find_element(By.XPATH, "//button[@class='jm-btn secondary small jm-fc-black']").click()
high_to_low=driver.find_element(By.XPATH, "//div[contains(@class,'dropdown-menu')]/descendant::li[2]").click()
chair_list=driver.find_elements(By.XPATH, "//div[contains(@class,'primary-grey-80')]")
print(chair_list[2].text)
print(chair_list[16].text)
print(len(chair_list))

for i in range(0,17):
    print(chair_list[i].text)



# chair_list= driver.find_elements(By.XPATH, "//div[@class='plp-card-details-tag']/following-sibling::div[contains(@class,'name')]")
# chair_list=[el1,el2,...el17]
# print(chair_list[3].text)
# print(chair_list[16].text)
#for bucket in tank:

# for chair in chair_list:
#     print(chair.text)

# for i in range(0,17):
#     print(chair_list[i].text)












