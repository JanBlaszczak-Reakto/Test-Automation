from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Authorization import Authorization
import os
from dotenv import load_dotenv
import pytest
import unittest
load_dotenv()


class SwaggerTest(unittest.TestCase):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.URL = os.getenv('SWAGGER_URL')

    def openSwagger(self):
        swaggerURL = self.URL
        self.driver.get(swaggerURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def activationOfAuthorization(self):
        authorization = Authorization(self.driver)
        authorization.executeAuthorizationSteps()





# swaggerTest = SwaggerTest()
# swaggerTest.openSwagger()
# swaggerTest.activationOfAuthorization()
