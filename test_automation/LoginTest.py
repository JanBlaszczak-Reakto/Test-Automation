from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTest():

    def __init__(self):
         self.driver = webdriver.Chrome()

    def openService(self):

        servisURL = 'https://vuehost.local:8082/login'

        self.driver.implicitly_wait(5)
        self.driver.get(servisURL)
        self.driver.maximize_window()

    def email(self):

        emailField = self.driver.find_element(By.XPATH, "//div[@id='q-app']//label[1]")
        emailField.send_keys('pilot@reakto.eu')
        time.sleep(1)

    def password(self):

        passwordField = self.driver.find_element(By.XPATH,"//div[@id='q-app']/div/div/main/div[2]/form/label[2]")
        passwordField.send_keys('jasiek2810')
        time.sleep(1)

    def logIn(self):

        confirm = self.driver.find_element(By.XPATH, "//span[text()='Confirm']")
        confirm.click()
        time.sleep(1)

    def logOut(self):

        avatar = self.driver.find_element(By.XPATH, "//i[text()='person']")
        avatar.click()
        logOut = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        logOut.click()

        time.sleep(2)




runTest = LoginTest()
runTest.openService()
runTest.email()
runTest.password()
runTest.logIn()
runTest.logOut()




