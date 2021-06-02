
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

''' 
from TestData.HomePageData import HomePageData
'''
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_HomePage_PasteLink(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        # Manual test step 1 - checking home page displays
        log.info("HOME PAGE CHECK - Checking for expected body header text.")
        homePageVerificationText = homepage.verifyHomePageText().text
        try:
            assert("Test drive multi-writer Dat!" in homePageVerificationText)
            log.info("HOME PAGE CHECK - Pass")
        except AssertionError:
            log.error("HOME PAGE CHECK - Expected home page text not found!")

        # Manual test step 2 - clicking on Have a Link? button
        log.info("HAVE A LINK? BUTTON - About to click.")
        homepage.verifyLinkButton().click()
        self.driver.refresh()