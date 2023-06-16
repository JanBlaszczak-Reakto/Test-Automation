from selenium.webdriver.common.by import By
import time


class UserRolesAccess:

    def __init__(self, driver):
        self.driver = driver

    def grabLastSuccessfullLoginTime(self):
        time.sleep(1)
        self.driver.refresh()
        self.driver.find_element(By.XPATH, "//div[text()='Login events']").click()
        time.sleep(1)
        sortLoginDate = self.driver.find_element(By.XPATH, "//div[@id='q-app']//th[4]")
        sortLoginDate.click()
        sortLoginDate.click()
        time.sleep(1)
        findLoginDate = self.driver.find_element(By.XPATH, "//div[@id='q-app']//tr[1]/td[4]")
        readLoginDate = findLoginDate.text
        print('Your login date is: ' + str(readLoginDate))

