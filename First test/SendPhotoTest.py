from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SendPhotoTest():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openService(self):

        servisURL = 'https://vuehost.local:8082/hub/7'

        self.driver.implicitly_wait(5)
        self.driver.get(servisURL)
        self.driver.maximize_window()

        time.sleep(3)

    def sendPhoto(self):

        photo1 = self.driver.find_element(By.XPATH, "//span[text()='Send command: Create Photo #1']")
        photo1.click()

        time.sleep(5)

        photo2 = self.driver.find_element(By.XPATH, "//span[text()='Send command: Create Photo #2']")
        photo2.click()
        time.sleep(5)

        photo3 = self.driver.find_element(By.XPATH, "//span[text()='Send command: Create Photo #3']")
        photo3.click()
        time.sleep(5)

        photo4 = self.driver.find_element(By.XPATH, "//span[text()='Send command: Create Photo #4']")
        photo4.click()
        time.sleep(5)

        photo5 = self.driver.find_element(By.XPATH, "//span[text()='Send command: Create Photo #5']")
        photo5.click()
        time.sleep(20)

        self.driver.close()

    def openBilbo(self):

        bilboURL = 'http://10.121.18.10:2000/'
        self.driver.get(bilboURL)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        a = 0

        while a<5:

            self.driver.refresh()
            time.sleep(20)
            a += 1



runTest = SendPhotoTest()
runTest.openService()
runTest.sendPhoto()
runTest.openBilbo()
