from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    HomePageVerificationText = (By.XPATH, "//h4[contains(text(),'Test drive multi-writer Dat!')]")
    LinkButton = (By.XPATH, "//button[contains(text(),'Have a Link? Paste it Here')]")


    def verifyHomePageText(self):
        return self.driver.find_element(*HomePage.HomePageVerificationText)


    def verifyLinkButton(self):
        return self.driver.find_element(*HomePage.LinkButton)

