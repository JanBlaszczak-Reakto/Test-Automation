from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from LoginTest import PositiveLoginTest
from UserRolesAcces import UserRolesAcces

class Test():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openService(self):

        servisURL = 'https://vuehost.local:8082/login'
        self.driver.implicitly_wait(5)
        self.driver.get(servisURL)
        self.driver.maximize_window()

    def logInAdmin(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('administrator@reakto.eu','administrator')

    def logInDev(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('dev@reakto.eu','dev')

    def logInQA(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('qa@reakto.eu','qa')

    def logInPilot(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('pilot@reakto.eu','pilot')

    def logInOperation(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('operator@reakto.eu','operator')


    def logInSerwis(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('serwis@reakto.eu','serwis')

    def logInSeller(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('seller@reakto.eu','seller')

    def logInMarketing(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('marketing@reakto.eu','marketing')

    def logInAccount(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('account@reakto.eu','account')

    def logInPartner(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('partner@reakto.eu','partner')

    def logInClient(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('client@reakto.eu','client')

    def logInAgency(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('agency@reakto.eu','agency')

    def logInGuest(self):
        test = PositiveLoginTest(self.driver)
        test.executeAllMethods('guest@reakto.eu','guest')


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
runTest.openService()
runTest.logInAdmin()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInQA()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInAccount()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInDev()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInAgency()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInClient()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInGuest()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInMarketing()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInOperation()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInPartner()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInSeller()
runTest.userRolesAcces()
runTest.logOut()
runTest.logInSerwis()
runTest.userRolesAcces()
runTest.logOut()


