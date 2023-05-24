from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LogIn import PositiveLoginTest

class UserRolesAcces():

    def __init__(self,driver):
        self.driver = driver




    def userNameFind(self):

        findName = self.driver.find_element(By.XPATH, '//div[@id="q-app"]/div/header/div[1]/div[3]')
        readName = findName.text
        print('You are logged in as: ' + str(readName)+'\n')

    def loginEvent(self):

        time.sleep(1)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, "//div[text()='Login events']").click()
        time.sleep(1)
        sortLoginDate = self.driver.find_element(By.XPATH, "//div[@id='q-app']//th[4]")
        sortLoginDate.click()
        sortLoginDate.click()
        time.sleep(1)
        findLoginDate = self.driver.find_element(By.XPATH, "//div[@id='q-app']//tr[1]/td[4]")
        readLoginDate = findLoginDate.text
        print ('Your login date is: ' + str(readLoginDate))

    def goDasboard(self):

        try:
            self.driver.find_element(By.XPATH,"//div[2]/div[text()='Dashboard']").click()
            time.sleep(1)
            print("You have access to Dashboard")

        except:
            print("Dashboard not found because you don't have access")

    def goAgencies(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Agencies']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Agencies")

        except:
            print("Agencies not found because you don't have access")

    def goHubs(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Hubs']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Hubs")

        except:
            print("Hubs not found because you don't have access")

    def goVenues(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Venues']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Venues")

        except:
            print("Venues not found because you don't have access")

    def goUAV(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='UAV']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to UAV")

        except:
            print("UAV not found because you don't have access")

    def goMission(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Missions']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Missions")

        except:
            print("Missions not found because you don't have access")

    def goClient(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Clients']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Clients")

        except:
            print("Clients not found because you don't have access")

    def goClientevent(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Client Events']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Clients Event")

        except:
            print("Clients Event not found because you don't have access")

    def goAlerts(self):

        try:
            self.driver.find_element(By.XPATH, "//div[text()='Alerts']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Alerts")

        except:
            print("Alerts not found because you don't have access")

    def goDictionaries(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Dictionaries']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Dictionaries")

        except:
            print("Dictionaries not found because you don't have access")

    def goUsers(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Users']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Users")

        except:
            print("Users not found because you don't have access")

    def goLoginEvents(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Login events']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Login events")

        except:
            print("Login events not found because you don't have access")

    def goSystemStatus(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='System Status']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to System Status")

        except:
            print("System Status not found because you don't have access")

    def goBilboStatus(self):

        try:
            self.driver.find_element(By.XPATH,"//div[text()='Bilbo Status']").click()
            time.sleep(1)
            self.driver.back()
            print("You have access to Bilbo Status")

        except:
            print("Bilbo Status not found because you don't have access")



    def runAll(self):

        self.userNameFind()
        # runTest.loginEvent()
        self.goDasboard()
        self.goAgencies()
        self.goHubs()
        self.goVenues()
        self.goUAV()
        self.goMission()
        self.goClient()
        self.goClientevent()
        self.goAlerts()
        self.goDictionaries()
        self.goUsers()
        self.goLoginEvents()
        self.goSystemStatus()
        self.goBilboStatus()








#
# runTest = UserRolesAcces()
# runTest.logIn()
# runTest.userNameFind()
# # runTest.loginEvent()
# runTest.goDasboard()
# runTest.goAgencies()
# runTest.goHubs()
# runTest.goVenues()
# runTest.goUAV()
# runTest.goMission()
# runTest.goClient()
# runTest.goAlerts()
# runTest.goDictionaries()
# runTest.goUsers()
# runTest.goLoginEvents()
# runTest.goSystemStatus()
# runTest.goBilboStatus()
# runTest.logOut()