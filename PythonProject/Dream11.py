from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://dream11.com")
driver.maximize_window()
driver.implicitly_wait(1)
language_menu_btn = driver.find_element(By.XPATH, "//div[@id='select-selected']").click()
language_options = driver.find_elements(By.XPATH, "//div[@id='select-items']/child::div")
count = len(language_options)
print(count)
#menu_btn = driver.find_element(By.XPATH, "//div[@id='select-selected']").click()
#english_lang = driver.find_element(By.XPATH, "//div[@id='select-items']/child::div[@id='english']").click()
faqs_heading = driver.find_element(By.XPATH, "//h3[contains(@class,'universal_heading')]")
driver.execute_script('arguments[0].scrollIntoView();',faqs_heading)
list_of_faqs= driver.find_elements(By.XPATH, "//button[@class='accordion']")
listcount = len(list_of_faqs)
print(listcount)

for i in range(0,listcount):
    list_of_faqs[i].click()
    print(list_of_faqs[i].text)

# //div[@id='select-items']/child::div[@id='hindi']