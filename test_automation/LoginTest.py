from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

load_dotenv()
URL=os.getenv('FRONT_URL')

class PositiveLoginTest():

    def __init__(self):
         self.driver = webdriver.Chrome()
         self.userName = None

    def openService(self):


        servisURL = URL
        self.driver.implicitly_wait(5)
        self.driver.get(servisURL)
        self.driver.maximize_window()

    def email(self):

        self.userName = 'pilot@reakto.eu'
        emailField = self.driver.find_element(By.XPATH, "//div[@id='q-app']//label[1]")
        emailField.send_keys(self.userName)
        time.sleep(1)

    def password(self):

        passwordField = self.driver.find_element(By.XPATH,"//div[@id='q-app']/div/div/main/div[2]/form/label[2]")
        passwordField.send_keys('pilot')
        time.sleep(1)

    def logIn(self):

        try:
            logInButton = self.driver.find_element(By.XPATH, "//button")
            logInButton.click()
            time.sleep(1)
            print('User:' + str(self.userName) + ' is Correct')
        except:
            print('User:' + str(self.userName) + ' is not Found')

    def logOut(self):

        avatar = self.driver.find_element(By.XPATH, "//i[text()='person']")
        avatar.click()
        logOut = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        logOut.click()
        time.sleep(2)

    def executeAllMethods(self):

        self.openService()
        self.email()
        self.password()
        self.logIn()




class NegativeLoginTest():

    def __init__(self):
         self.driver = webdriver.Chrome()

    def openService(self):

        servisURL = 'https://vuehost.local:8082/login'
        self.driver.implicitly_wait(5)
        self.driver.get(servisURL)
        self.driver.maximize_window()

    def email(self):

        self.userName= 'random@reakto.eu'
        emailField = self.driver.find_element(By.XPATH, "//div[@id='q-app']//label[1]")
        emailField.send_keys(self.userName)
        time.sleep(1)

    def password(self):

        passwordField = self.driver.find_element(By.XPATH,"//div[@id='q-app']/div/div/main/div[2]/form/label[2]")
        passwordField.send_keys('random')
        time.sleep(1)

    def logIn(self):

        logInButton = self.driver.find_element(By.XPATH, "//button")
        logInButton.click()
        time.sleep(1)

    def findAvatar(self):

        try:
            avatar = self.driver.find_element(By.XPATH, "//i[text()='person']")
            avatar.click()
            print('User:' + str(self.userName) + ' is Correct')

        except:
            print('User: ' + str(self.userName) + ' is not Found')
    def executeAllMethods(self):

        self.openService()
        self.email()
        self.password()
        self.logIn()
        self.findAvatar()
        time.sleep(2)

# runTest = PositiveLoginTest()
# runTest.executeAllMethods()
# runTest.logOut()
# runTest = NegativeLoginTest()
# runTest.executeAllMethods()




