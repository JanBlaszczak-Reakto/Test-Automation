from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginTest import PositiveLoginTest,NegativeLoginTest

class UserRolesAcces():

    def logIn(self):
        self.test=PositiveLoginTest()
        self.test.executeAllMethods()


    def userNameFind(self):

        findName = self.test.driver.find_element(By.XPATH, '//div[@id="q-app"]/div/header/div[1]/div[3]')
        readName = findName.text
        print('You are logged in as: ' + str(readName))

    def loginEvent(self):

        time.sleep(1)
        self.test.driver.refresh()
        goLoginEvent = self.test.driver.find_element(By.XPATH, "//div[text()='Login events']").click()
        time.sleep(1)
        sortLoginDate = self.test.driver.find_element(By.XPATH, "//div[@id='q-app']//th[4]")
        sortLoginDate.click()
        sortLoginDate.click()
        time.sleep(1)
        findLoginDate = self.test.driver.find_element(By.XPATH, "//div[@id='q-app']//tr[1]/td[4]")
        readLoginDate = findLoginDate.text
        print ('Your login date is: ' + str(readLoginDate))

    def goDasboard(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Dashboard']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Dashboard")

        except:
            print("Dashboard not found because you don't have access")

    def goAgencies(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Agencies']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Agencies")

        except:
            print("Agencies not found because you don't have access")

    def goHubs(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Hubs']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Hubs")

        except:
            print("Hubs not found because you don't have access")

    def goVenues(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Venues']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Venues")

        except:
            print("Venues not found because you don't have access")

    def goUAV(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='UAV']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to UAV")

        except:
            print("UAV not found because you don't have access")

    def goMission(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Missions']").click()
            time.sleep(2)
            self.test.driver.back()
            print("You have access to Missions")

        except:
            print("Missions not found because you don't have access")

    def goClient(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Clients']").click()
            time.sleep(2)
            self.test.driver.back()
            print("You have access to Clients")

        except:
            print("Clients not found because you don't have access")

    def goDictionaries(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Dictionaries']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Dictionaries")

        except:
            print("Dictionaries not found because you don't have access")

    def goUsers(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Users']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Users")

        except:
            print("Users not found because you don't have access")

    def goLoginEvents(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Login events']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Login events")

        except:
            print("Login events not found because you don't have access")

    def goSystemStatus(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='System Status']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to System Status")

        except:
            print("System Status not found because you don't have access")

    def goBilboStatus(self):

        try:
            self.test.driver.find_element(By.XPATH,"//div[text()='Bilbo Status']").click()
            time.sleep(1)
            self.test.driver.back()
            print("You have access to Bilbo Status")

        except:
            print("Bilbo Status not found because you don't have access")

    def logOut(self):

        try:
            avatar = self.test.driver.find_element(By.XPATH, "//i[text()='person']")
            avatar.click()
            logOut = self.test.driver.find_element(By.XPATH, "//a[@href='/login']")
            logOut.click()
            print('Successfully logged out')
            time.sleep(2)
        except:
            print("Can't log out")








runTest = UserRolesAcces()
runTest.logIn()
runTest.userNameFind()
runTest.loginEvent()
runTest.goDasboard()
runTest.goAgencies()
runTest.goHubs()
runTest.goVenues()
runTest.goUAV()
runTest.goMission()
runTest.goClient()
runTest.goDictionaries()
runTest.goUsers()
runTest.goLoginEvents()
runTest.goSystemStatus()
runTest.goBilboStatus()
runTest.logOut()