from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class Ipl(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver.implicitly_wait(10)
        driver.get("https://www.iplt20.com/matches/schedule/men")
        driver.maximize_window()

    def test_Ipl(self):
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='cookie__accept cookie__accept_btn']").click()
        wait = WebDriverWait(driver,20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='https://www.iplt20.com/matches'])[2]")))
        driver.find_element(By.XPATH, "(//a[@href='https://www.iplt20.com/matches'])[2]").click()
        time.sleep(15)
        wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='ng-binding']")))
        stadiums_list=driver.find_elements(By.XPATH, "//p[@class='ng-binding']")
        wait.until(EC.presence_of_element_located((By.XPATH, "//li[@ng-repeat='list in fixLiveList']//div[@class='vn-matchDate ng-binding']")))
        dates = driver.find_elements(By.XPATH, "//li[@ng-repeat='list in fixLiveList']//div[@class='vn-matchDate ng-binding']")
        print("Stadium Name With Location :")
        for stadium in stadiums_list:
            print(" :" " "+stadium.text)

        print("All Matches Dates:")
        for date in dates:
            print("Date:"" "+date.text)

    def test_matches_results(self):
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='cookie__accept cookie__accept_btn']").click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='https://www.iplt20.com/matches'])[2]")))
        driver.find_element(By.XPATH, "(//a[@href='https://www.iplt20.com/matches'])[2]").click()
        time.sleep(15)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='RESULTS']")))
        driver.find_element(By.XPATH, "//a[text()='RESULTS']").click()
        all_results = driver.find_elements(By.XPATH, "//div[@class='vn-ticketTitle ng-binding ng-scope']")
        print("All Matches Result:")
        for result in all_results:
            print(result.text)

    def tearDown(self) -> None:
        driver.quit()
