from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginTest import PositiveLoginTest,NegativeLoginTest
from UserRolesAcces import UserRolesAcces

class Test():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def logIn(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods()

    def userRolesAcces(self):

        acces = UserRolesAcces(self.driver)
        acces.runAll()

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

runTest = Test()
runTest.logIn()
runTest.userRolesAcces()
runTest.logOut()


