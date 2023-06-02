from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from LogIn import PositiveLoginTest


class CreateNewVenues:

    def __init__(self, driver):
        self.driver = driver

    def addNewVenue(self):

        try:
            self.driver.find_element(By.XPATH, "//div[text()='CRM']").click()
            self.driver.find_element(By.XPATH, "//div[text()='venues']").click()
            self.driver.find_element(By.XPATH, "//span[text()='add new venue']").click()  # click add new venue
            self.driver.find_element(By.XPATH, "//*[@id='q-app']/div/div[2]/main/div/div[1]/label").send_keys(
                'Aaa')  # change name
            time.sleep(2)
            self.driver.find_element(By.XPATH,
                                     "//div[@id='q-app']/div/div[2]/main/div/div[1]/div[3]/button[2]/span[2]").click()  # save
            time.sleep(2)
            self.driver.find_element(By.XPATH,
                                     "//div[@id='q-app']/div/div[2]/main/div/div[1]/div[3]/button[3]").click()  # cancel
            time.sleep(1)
            self.driver.back()
            print("You can  add new venue")


        except:
            self.driver.back()
            print("You can't  add new venue")
