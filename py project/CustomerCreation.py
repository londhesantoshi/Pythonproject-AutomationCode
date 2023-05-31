import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time
import unittest

class CustomerCreation(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://org91296e38.crm8.dynamics.com/main.aspx")
        driver.maximize_window()

    def test_Create_a_lead(self):
        wait = WebDriverWait(driver,10)
        wait.until(Ec.presence_of_element_located((By.XPATH, "//input[@name='loginfmt']")))
        driver.find_element(By.XPATH, "//input[@name='loginfmt']").send_keys("pcubeworkforce@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='Next']").click()
        time.sleep(10)
        password=driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys("Salesforce")
        driver.find_element(By.XPATH, "//input[@value='Sign in']").click()
        driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
        time.sleep(10)
        iframe=wait.until(Ec.element_to_be_clickable((By.XPATH,"//iframe[@id='AppLandingPage']")))
        driver.switch_to.frame(iframe)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//div[@title='Dynamics 365 — custom']")))
        driver.find_element(By.XPATH, "//div[@title='Dynamics 365 — custom']").click()
        time.sleep(20)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//div[@title='Leads']")))
        driver.find_element(By.XPATH, "//div[@title='Leads']").click()
        time.sleep(20)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='New']")))
        driver.find_element(By.XPATH, "//button[@aria-label='New']").click()
        topic_list=['Test','Practice','Services']
        N=8
        topic =''.join(random.choices(string.ascii_letters,k=N))
        time.sleep(10)
        driver.find_element(By.XPATH, "//input[@aria-label='Topic']").send_keys(topic)
        driver.find_element(By.XPATH, "//input[@aria-label='First Name']").send_keys("Santoshi")
        driver.find_element(By.XPATH, "//input[@aria-label='Last Name']").send_keys("Jagdale")
        driver.find_element(By.XPATH, "//input[@aria-label='Company']").send_keys("Dynamic System")
        time.sleep(10)
        driver.find_element(By.XPATH, "//button[@aria-label='Save & Close']").click()
        time.sleep(5)

    def test_Convert_Lead_into_opportunity(self):
        wait = WebDriverWait(driver, 10)
        wait.until(Ec.presence_of_element_located((By.XPATH, "//input[@name='loginfmt']")))
        driver.find_element(By.XPATH, "//input[@name='loginfmt']").send_keys("pcubeworkforce@gmail.com")
        driver.find_element(By.XPATH, "//input[@type='submit' and @value='Next']").click()
        time.sleep(10)
        password = driver.find_element(By.XPATH, "//input[@id='i0118']").send_keys("Salesforce")
        driver.find_element(By.XPATH, "//input[@value='Sign in']").click()
        driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
        time.sleep(10)
        iframe = wait.until(Ec.element_to_be_clickable((By.XPATH, "//iframe[@id='AppLandingPage']")))
        driver.switch_to.frame(iframe)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//div[@title='Dynamics 365 — custom']")))
        driver.find_element(By.XPATH, "//div[@title='Dynamics 365 — custom']").click()
        time.sleep(20)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//div[@title='Leads']")))
        driver.find_element(By.XPATH, "//div[@title='Leads']").click()
        time.sleep(20)
        wait.until(Ec.presence_of_element_located((By.XPATH,"//input[@aria-label='Lead Filter by keyword']")))
        driver.find_element(By.XPATH,"//input[@aria-label='Lead Filter by keyword']").send_keys("---Santoshi")
        time.sleep(10)
        driver.find_element(By.XPATH, "//button[@aria-label='Start search']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[contains(@href,'https://org91296e38.crm8.dynamics')]").click()
        time.sleep(10)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//button[@aria-label='Qualify']")))
        driver.find_element(By.XPATH, "//button[@aria-label='Qualify']").click()
        time.sleep(20)
        wait.until(Ec.element_to_be_clickable((By.XPATH, "//a[text()='---Santoshi ---Jagdale']")))
        driver.find_element(By.XPATH, "//a[text()='---Santoshi ---Jagdale']").click()
        driver.find_element(By.XPATH, "//button[@aria-label='Continue']")
        time.sleep(10)
        driver.find_element(By.XPATH, "//button[@aria-label='Save More Commands. Save (CTRL+S)']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[@class='symbolFont ChevronDown-symbol pa-jf pa-cd pa-cw pa-ce ']").click()
        time.sleep(5)

    def tearDown(self) -> None:
        driver.close()

