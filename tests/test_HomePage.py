
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
        log.info("HOME PAGE CHECK - Checking for expected body header text.")
        '''  Expected result: Dat Shopping List web app's home page should display
        so checking main body header text is present
        '''
        homePageVerificationText = homepage.verifyHomePageText().text

        try:
            assert("Test drive multi-writer Dat!" in homePageVerificationText)
            log.info("HOME PAGE CHECK - Pass")
        except AssertionError:
            log.error("HOME PAGE CHECK - Expected home page text not found!")
        self.driver.refresh()