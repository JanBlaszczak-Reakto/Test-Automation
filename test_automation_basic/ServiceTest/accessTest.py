from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from logIn import PositiveLoginTest
from userRolesAccess import UserRolesAccess
import os
from dotenv import load_dotenv
from createNewVenues import CreateNewVenues
from createNewClients import CreateNewClient

load_dotenv()


class AccessTest():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = os.getenv('FRONT_URL')

    def openService(self):
        serviceURL = self.URL
        self.driver.get(serviceURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def logIn(self, login, password):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure(login, password)

    def checkUserRoleAccessRestrictions(self):

        access = UserRolesAccess(self.driver)
        access.checkAccessToAllPages()

    def checkRestrictonsToAddNewVenue(self, venueName):
        newVenues = CreateNewVenues(self.driver)
        newVenues.executeAddNewVenueProcedure(venueName)

    def checkRestrictonsToAddNewClient(self):
        newClient = CreateNewClient(self.driver)
        newClient.executeAddNewClientProcedure()

    def logOut(self):

        try:
            avatar = self.driver.find_element(By.XPATH, "//i[text()='person']")
            avatar.click()
            logOut = self.driver.find_element(By.XPATH, "//a[@href='/login']")
            logOut.click()
            print('Successfully logged out')
            time.sleep(2)
        except:
            print("Can't log out")

    def startTest(self):
        self.openService()
        self.logIn('pilot@reakto.eu', 'pilot')
        self.checkRestrictonsToAddNewClient()
        self.checkRestrictonsToAddNewVenue("New venue")
        self.checkUserRoleAccessRestrictions()
        self.logOut()


runTest = AccessTest()
runTest.startTest()
