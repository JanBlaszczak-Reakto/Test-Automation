from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginTest import PositiveLoginTest,NegativeLoginTest

class UserRoles():

    def logIn(self):
        self.logTest=PositiveLoginTest()
        self.logTest.executeAllMethods()


    def userNameFind(self):

        findName = self.logTest.driver.find_element(By.XPATH, '//div[@id="q-app"]/div/header/div[1]/div[3]')
        readName = findName.text
        print('You are logged in as: ' + str(readName))

    def loginEvent(self):

        time.sleep(5)
        self.logTest.driver.refresh()
        goLoginEvent = self.logTest.driver.find_element(By.XPATH, "//div[text()='Login events']").click()
        time.sleep(5)
        sortLoginDate = self.logTest.driver.find_element(By.XPATH, "//div[@id='q-app']//th[4]")
        sortLoginDate.click()
        sortLoginDate.click()
        time.sleep(1)
        findLoginDate = self.logTest.driver.find_element(By.XPATH, "//div[@id='q-app']//tr[1]/td[4]")
        readLoginDate = findLoginDate.text
        print ('Your login date is:' +  str(readLoginDate))

    def logOut(self):

        avatar = self.logTest.driver.find_element(By.XPATH, "//i[text()='person']")
        avatar.click()
        logOut = self.logTest.driver.find_element(By.XPATH, "//a[@href='/login']")
        logOut.click()

        time.sleep(2)








runTest = UserRoles()
runTest.logIn()
runTest.userNameFind()
runTest.loginEvent()