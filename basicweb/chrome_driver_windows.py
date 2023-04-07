from selenium import  webdriver
from selenium.webdriver.chrome.service import Service as Service

class RunChromeTest():

    def test(self):
        chrome_service = Service(executable_path="C:\\Users\\dell\\workspace_python\\SeleniumWDTutorial\\drivers\\chromedriver.exe")
        #Instantiate Browser
        driver = webdriver.Chrome(service=chrome_service)
        #Open the provided URL
        driver.get("https://www.letskodeit.com")

untest = RunChromeTest()
untest.test()