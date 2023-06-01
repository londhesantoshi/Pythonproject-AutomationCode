from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class Espn(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.espncricinfo.com/")
        driver.implicitly_wait(10)
        driver.maximize_window()

    def test_Espn(self):
        wait=WebDriverWait(driver,30)
        key_series_section = driver.find_element(By.XPATH,"//span[text()='World Cup Super League']")
        act = ActionChains(driver)
        act.move_to_element(key_series_section).perform()
        driver.find_element(By.XPATH, "//span[text()='IPL 2023']/parent::a").click()
        time.sleep(20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='Sign me Up!']")))
        driver.find_element(By.XPATH, "//button[@class='Sign me Up!']").click()
        driver.find_element(By.XPATH, "//span[text()='Indian Premier League 2023']").click()
        time.sleep(15)
        driver.find_element(By.XPATH, "//a[@href='/series/ipl-2021-1249214']").click()
        driver.find_element(By.XPATH, "//div[@class='ds-py-3 ds-px-4']/a[contains(@href,'bangalore-vs-kolkata')]").click()
        time.sleep(10)
        print("--------------------------")
        print(" Url Of Result:")
        print(driver.current_url)
        print("--------------------------")
        print("Got Out Players of Royal & Knight Riders Team:")
        got_out_players_list=driver.find_elements(By.XPATH, "//td[@class='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center']")
        for out_player in got_out_players_list:
            print(out_player.text)

   def tearDown(self) -> None:
       driver.close()
