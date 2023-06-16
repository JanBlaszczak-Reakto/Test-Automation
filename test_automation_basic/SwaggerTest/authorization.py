import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Autorization():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openSwagger(self):
        swaggerURL = 'https://localhost:5051/swagger/index.html'
        self.driver.get(swaggerURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def openPostInAuth(self):
        self.driver.execute_script("window.scrollBy(0, 1100);")
        self.driver.find_element(By.XPATH, "//div[@id='operations-Auth-post_api_Auth']/div/button/span[1]").click()

    def clickTryItOut(self):
        self.driver.find_element(By.XPATH, "//div[@id='operations-Auth-post_api_Auth']//div[2]/button").click()

    def sendDataToTextArea(self):
        textArea = self.driver.find_element(By.XPATH, "//div[@id='operations-Auth-post_api_Auth']//textarea")
        textArea.click()
        textArea.clear()
        textArea.send_keys('["admin@reakto.eu","admin"]')
        executeInPost = self.driver.find_element(By.XPATH,
                                                 "//div[@id='operations-Auth-post_api_Auth']/div[2]/div/div[2]/button[1]")
        executeInPost.click()

    def findAccesTokenInResponseBody(self):
        self.driver.execute_script("window.scrollBy(0, 1300);")
        responseBody = self.driver.find_element(By.XPATH, "//div[@id='operations-Auth-post_api_Auth']//tbody//span[47]")
        self.accesToken = responseBody.text
        print(self.accesToken)

    def sendAccesTokenToAutorize(self):
        authorize = self.driver.find_element(By.XPATH, "//div[2]/section//button")
        authorize.click()
        time.sleep(10)
    def executeAuthorizationSteps(self):
        self.openPostInAuth()
        self.clickTryItOut()
        self.sendDataToTextArea()
        self.findAccesTokenInResponseBody()
        self.sendAccesTokenToAutorize()




