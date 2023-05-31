import time

from selenium import webdriver

import unittest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ESPN(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        driver=webdriver.Chrome("C:\\Driver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.espncricinfo.com")
        driver.maximize_window()


    def test_OutPlyerNmae(self):
        KeySeriessexction=driver.find_element(By.XPATH,"//span[text()='World Cup Super League']")
        Ac=ActionChains(driver)
        Ac.move_to_element(KeySeriessexction).perform()
        IPL2023=driver.find_element(By.XPATH,"//span[text()='IPL 2023']/parent::a")
        IPL2023.click()
        time.sleep(20)
        yesbutton=driver.find_element(By.ID,"wzrk-confirm")
        yesbutton.click()
        time.sleep(10)
        Result=driver.find_element(By.XPATH,"//span[text()='Results']")
        Ac=ActionChains(driver)
        Ac.move_to_element(Result).click().perform()
        Lastmatchwin=driver.find_element(By.XPATH,"//div[@class='ds-block']//a")
        Lastmatchwin.click()
        time.sleep(13)
        #IPLMenu=IPL1.find_element(By.XPATH,"//span[text() = 'Indian Premier League 2023']/../ i")
        #IPLMenu.click()
        # ipl2021=IPL1.find_element(By.XPATH,"//li[@title='Indian Premier League 2023']")
        # Ac1=ActionChains(IPL1)
        # Ac1.move_to_element(ipl2021).click().perform()
        lastIpl=driver.find_element(By.XPATH,"//div[@class='ds-w-[288px] card scorecard']")
        lastIpl.click()
        ScoreCard=driver.find_element(By.XPATH,"//span[text()='Scorecard']")
        ScoreCard.click()
        print(driver.current_url)
        time.sleep(20)
        # Ining = IPL1.find_elements(By.XPATH, "//span[@class='ds-text-tight-xs']")
        # for i in range(2):
        #     print(Ining[i].text)
        #     print("-------------------------------------------")
        #     OutPlyList= IPL1.find_elements(By.XPATH,"//td[@class='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center']/a")
        #     for player in OutPlyList:
        #         print(player.get_attribute("title"))
        OutPlyList = driver.find_elements(By.XPATH,"//td[@class='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center']/a")
        for player in OutPlyList:
            print(player.get_attribute("title"))

    def tearDown(self) -> None:
        driver.quit()


if __name__=="__main__":
    unittest.main()