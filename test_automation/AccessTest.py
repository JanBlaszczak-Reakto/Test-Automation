from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LogInProcedure import PositiveLoginTest
from UserRolesAcces import UserRolesAccess
import os
from dotenv import load_dotenv

load_dotenv()


class AccessTest:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = os.getenv('FRONT_URL')
    def openService(self):

        serviceURL = self.URL
        self.driver.get(serviceURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def logInAsAdmin(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('admin@reakto.eu', 'admin')

    def logInAsDev(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('dev@reakto.eu', 'dev')

    def logInAsQA(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('qa@reakto.eu', 'qa')

    def logInAsPilot(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('pilot@reakto.eu', 'pilot')

    def logInPilotCoord(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('coord@reakto.eu', 'coord')

    def logInOperation(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('operator@reakto.eu', 'operator')


    def logInSerwis(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('serwis@reakto.eu', 'serwis')

    def logInSeller(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('seller@reakto.eu', 'seller')

    def logInMarketing(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('marketing@reakto.eu', 'marketing')

    def logInAccount(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('account@reakto.eu', 'account')

    def logInPartner(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('partner@reakto.eu', 'partner')

    def logInClient(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('client@reakto.eu', 'client')

    def logInAgency(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('agency@reakto.eu', 'agency')

    def logInGuest(self):
        test = PositiveLoginTest(self.driver)
        test.executeLoginProcedure('guest@reakto.eu', 'guest')


    def checkUserRoleAccessRestrictions(self):

        access = UserRolesAccess(self.driver)
        access.runAll()

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

runTest = AccessTest() #umiescic w metodzie
runTest.openService()
runTest.logInAsAdmin()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInAsQA()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInAccount()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInAsDev()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInAgency()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInClient()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInGuest()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInMarketing()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInOperation()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInPartner()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInSeller()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInSerwis()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInAsPilot()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()
runTest.logInPilotCoord()
runTest.checkUserRoleAccessRestrictions()
runTest.logOut()


