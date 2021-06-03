from selenium.webdriver.common.by import By
from selenium import webdriver


class PasteLinkPage:

    def __init__(self, driver):
        self.driver = driver


    PasteLinkPageVerificationText = (By.XPATH, "//h2[contains(text(),'Paste in a URL link or a hexadecimal key')]")
    SubmitButton = (By.XPATH, "//input[@class='_2abd6af1']")
    URLField = (By.XPATH, "//input[@type='text']")
    AlertBox = (By.XPATH, "//div[@class='alertContent']")


    def verifyPasteLinkPageText(self):
        return self.driver.find_element(*PasteLinkPage.PasteLinkPageVerificationText)


    def verifyLinkButton(self):
        return self.driver.find_element(*PasteLinkPage.SubmitButton)


    def verifyURLFieldContent(self):
        return self.driver.find_element(*PasteLinkPage.URLField)


    def getAlertBox(self):
        return self.driver.find_element(*PasteLinkPage.AlertBox)