import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.coca-colacompany.com/")
driver.maximize_window()
driver.implicitly_wait(3)
cookies_popup=driver.find_element(By.XPATH, "//button[contains(@class,'save-preference')]").click()
search_icon= driver.find_element(By.XPATH, "//div[@id='iconContainer']/div/a[@id='searchIcon']").click()
url= driver.current_url
print( "coco search_menu url : "+url)

for i in range (0,9):
    all_content_type = driver.find_element(By.XPATH, "//button[contains(@id,'btn_contentType')]").click()
    content_list = driver.find_elements(By.XPATH, "//ul[contains(@class,'dropdown-menu')]//li//a")
    print(content_list[i].text)
    time.sleep(2)
    content_list[i].click()
    link_list = driver.find_elements(By.XPATH, "//a[contains(@class,'title-anchor')]")
    for element in link_list:
        href_value=element.get_attribute("href")
        print(href_value)
    all_content_type = driver.find_element(By.XPATH, "//button[contains(@id,'btn_contentType')]").click()
    driver.find_element(By.XPATH, "//a[@id='recitemeIcon']").click()
    time.sleep(2)
    list_menu_items=driver.find_elements(By.XPATH,"//li[contains(@class,'cmp-navigation')]")
    for menu_item in list_menu_items:
        action = ActionChains(driver)
        action.move_to_element(menu_item).perform()
        time.sleep(4)