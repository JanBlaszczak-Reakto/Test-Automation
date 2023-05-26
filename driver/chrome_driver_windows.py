from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service
import time

class RunChromeTest():

    def test(self):
        chrome_service = Service(executable_path="C:\\Users\\Dell\\Documents\\GitHub\\Test-Automation\\driver\\chromedriver.exe")
        #Instantiate Browser
        driver = webdriver.Chrome(service=chrome_service)
        #Open the provided URL
        driver.get("http://localhost:2060/")
        time.sleep(10)
untest = RunChromeTest()
untest.test()