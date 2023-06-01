from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SourceDemo(unittest.TestCase):

    def setUp(self) -> None:
        global driver
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()

    def test_SourceDemo(self):
        time.sleep(10)
        wait=WebDriverWait(driver,15)
        list=['standard_user','locked_out_user','problem_user','performance_glitch_user']
        count=len(list)
        print(count)
        for i in range(0,count):
            if "locked_out_user" == list[i]:
                continue

            driver.find_element(By.ID, "user-name").send_keys(list[i])
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.NAME, "login-button").click()
            wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
            driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']/a").click()
            driver.find_element(By.ID, "checkout").click()
            driver.find_element(By.ID, "continue").click()
            time.sleep(10)
            error = driver.find_element(By.XPATH, "//div[contains(@class,'error-message')]/h3")
            error_msg = error.text
            self.assertTrue(error_msg == "Error: First Name is required")
            time.sleep(5)
            first_name = driver.find_element(By.ID, "first-name")
            first_name.send_keys("Santoshi")
            wait.until(EC.presence_of_element_located((By.ID, "last-name")))
            driver.find_element(By.ID, "last-name").send_keys("Londhe")
            driver.find_element(By.ID, "postal-code").send_keys("413503")
            wait.until(EC.element_to_be_clickable((By.ID, "continue")))
            driver.find_element(By.ID, "continue").click()
            driver.find_element(By.ID, "finish").click()
            thankyou_msg = driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']").text
            self.assertTrue(thankyou_msg == "Thank you for your order!")
            wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
            driver.find_element(By.XPATH, "//a[text()='Logout']").click()
            time.sleep(10)

    def tearDown(self) -> None:
        driver.quit()


if __name__ == "__main__":
    unittest.main()
