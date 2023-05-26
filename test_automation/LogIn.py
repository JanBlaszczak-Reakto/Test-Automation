from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()


class PositiveLoginTest:

    def __init__(self, driver):
        self.driver = driver
        self.userName = None
        self.URL=os.getenv('FRONT_URL')


    def openService(self):


        servisURL = self.URL
        self.driver.implicitly_wait(5)
        self.driver.get(servisURL)
        self.driver.maximize_window()

    def fillUserNameField(self, userName):

        self.userName = userName
        emailField = self.driver.find_element(By.XPATH, "//div[@id='q-app']//label[1]")
        emailField.send_keys(self.userName)
        time.sleep(1)

    def fillPasswordField(self, password):

        passwordField = self.driver.find_element(By.XPATH,"//div[@id='q-app']/div/div/main/div[2]/form/label[2]")
        passwordField.send_keys(password)
        time.sleep(1)

    def logIn(self):

        try:
            logInButton = self.driver.find_element(By.XPATH, "//button")
            logInButton.click()
            time.sleep(1)
            print('\nUser:' + str(self.userName) + ' is Correct\n')
        except:
            print('\nUser:' + str(self.userName) + ' is not Found\n')

    def logOut(self):

        avatar = self.driver.find_element(By.XPATH, "//i[text()='person']")
        avatar.click()
        logOut = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        logOut.click()
        time.sleep(2)

    def executeLoginProcedure(self, userName, password):

        # self.openService()
        self.fillUserNameField(userName)
        self.fillPasswordField(password)
        self.logIn()
        # self.logOut()




# class NegativeLoginTest():
#
#     def __init__(self):
#          self.driver = webdriver.Chrome()
#
#
#
#     def email(self):
#
#         self.userName= 'random@reakto.eu'
#         emailField = self.driver.find_element(By.XPATH, "//div[@id='q-app']//label[1]")
#         emailField.send_keys(self.userName)
#         time.sleep(1)
#
#     def password(self):
#
#         passwordField = self.driver.find_element(By.XPATH,"//div[@id='q-app']/div/div/main/div[2]/form/label[2]")
#         passwordField.send_keys('random')
#         time.sleep(1)
#
#     def logIn(self):
#
#         logInButton = self.driver.find_element(By.XPATH, "//button")
#         logInButton.click()
#         time.sleep(1)
#
#     def findAvatar(self):
#
#         try:
#             avatar = self.driver.find_element(By.XPATH, "//i[text()='person']")
#             avatar.click()
#             print('User:' + str(self.userName) + ' is Correct')
#
#         except:
#             print('User: ' + str(self.userName) + ' is not Found')
#     def executeAllMethods(self):
#
#
#         self.email()
#         self.password()
#         self.logIn()
#         self.findAvatar()
#         time.sleep(2)

# runTest = PositiveLoginTest()
# runTest.executeAllMethods()

# runTest = NegativeLoginTest()
# runTest.executeAllMethods()




