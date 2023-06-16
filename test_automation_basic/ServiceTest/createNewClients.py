from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class CreateNewClient:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def goToCRM(self):

        try:
            self.driver.find_element(By.XPATH, "//div[text()='CRM']").click()
            print("You have access to CRM")
            return True
        except:
            print("You don't have access to CRM")
            return False

    def goToClients(self):

        try:
            self.driver.find_element(By.XPATH, "//div[text()='clients']").click()
            print("You don't have access to Clients")
            return True
        except:
            print("You don't have access to Clients")
            return False

    def clickAddNewClient(self):

        try:
            buttonAddNewClient = self.driver.find_element(By.XPATH, "//span[text()='add new client']")
            buttonAddNewClient.click()
            print("You can add new Client")
            return True
        except:
            self.driver.back()
            print("You can't add new Client")
            return False

    def addClientName(self):
        addName = self.driver.find_element(By.XPATH, "//div[2]/div//label")
        addName.send_keys('Rezerwy Państwowe')

    def addClientEmaliAdress(self):
        addEmailAdress = self.driver.find_element(By.XPATH, "//div[3]//label")
        addEmailAdress.send_keys('rezerwy.panstwowe@gmail.com')

    def addClientVatID(self):
        addVatID = self.driver.find_element(By.XPATH, "//div[4]//label")
        addVatID.send_keys('7643891245')

    def addClientPhoneNumber(self):
        addPhoneNumber = self.driver.find_element(By.XPATH, "//div[5]//label")
        addPhoneNumber.send_keys('+48 731 465 896')

    def clickSharingMarketingData(self):
        sharingMarketingData = self.driver.find_element(By.XPATH, "//div[6]//div[2]/div/div")
        self.actions.double_click(sharingMarketingData).perform()  # Double click

    def clickSharingMarketingRecords(self):
        sharingMarketingRecords = self.driver.find_element(By.XPATH, "//div[7]//div[2]/div/div")
        self.actions.double_click(sharingMarketingRecords).perform()  # Double click

    def expandVenuesList(self):  # Rozwinięcie listy obiektów.
        Venueslist = self.driver.find_element(By.XPATH, "//div[8]//label")
        Venueslist.click()

    def selectOneVenue(self):
        self.driver.find_element(By.XPATH, "// span[text() = 'VEN-1 Centrum handlowe']").click()

    def saveNewClient(self):
        clickSaveButton = self.driver.find_element(By.XPATH, "//span[text()='save']")
        clickSaveButton.click()

    def goToClientsList(self):
        clickCancelButton = self.driver.find_element(By.XPATH, "//span[text()='cancel']")
        clickCancelButton.click()

    def executeAddNewClientProcedure(self):

        if not self.goToCRM(): return
        if not self.goToClients(): return
        if not self.clickAddNewClient(): return
        self.addClientName()
        self.addClientEmaliAdress()
        self.addClientVatID()
        self.addClientPhoneNumber()
        self.clickSharingMarketingData()
        self.clickSharingMarketingRecords()
        self.expandVenuesList()
        self.selectOneVenue()
        self.saveNewClient()
        self.goToClientsList()
