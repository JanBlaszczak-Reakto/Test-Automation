from selenium.webdriver.common.by import By
from selenium import webdriver
import time


class CreateNewVenues:

    def __init__(self, driver):
        self.driver = driver

    def goToCRM(self):

        try:
            self.driver.find_element(By.XPATH, "//div[text()='CRM']").click()
            return True

        except:
            print("you don't have access to CRM")
            return False

    def goToVenues(self):

        try:
            self.driver.find_element(By.XPATH, "//div[text()='venues']").click()
            return True
        except:
            print("You don't have access to Venue")
            return False

    def clickAddNewVenue(self):

        try:
            self.driver.find_element(By.XPATH, "//span[text()='add new venue']").click()
            print("You can add New Venue")
            return True
        except:
            print("You can't add New Venue")
            return False

    def addVenueName(self, venueName):
        newNameField = self.driver.find_element(By.XPATH, "//label")
        newNameField.send_keys(venueName)

    def clickSave(self):
        saveButton = self.driver.find_element(By.XPATH, "//button[2]")
        saveButton.click()
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//div[text()='VEN-?']")
            print("You can't save new Venue because this name is already taken!")
        except:
            print("You can save new Venue")

    def clickCancel(self):
        self.driver.find_element(By.XPATH, "//button[3]").click()
        self.driver.back()

    def executeAddNewVenueProcedure(self, venueName):
        if not self.goToCRM(): return
        if not self.goToVenues(): return
        if not self.clickAddNewVenue(): return
        self.addVenueName(venueName)
        self.clickSave()
        self.clickCancel()
