from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import unittest
import time


class Bjp(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.bjp.org/")
        driver.maximize_window()

    def test_Bjp(self):
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"State Websites")))
        driver.find_element(By.LINK_TEXT,"State Websites").click()
        select_state = driver.find_element(By.XPATH, "//select[@class='form-select']")
        select_state.click()
        option_list= driver.find_elements(By.XPATH, "//select[@class='form-select']/option")
        for option in option_list:
            if "D" in option.text:
                s = Select(select_state)
                s.select_by_visible_text(option.text)
                state_details= driver.find_elements(By.XPATH, "//h6[text()='State Office Details']")
                for state in state_details:
                    if option.text==state.text:
                        print(state.text)
                    else:
                        continue


    def tearDown(self) -> None:
        driver.quit()

# unittest.main(verbosity=2)