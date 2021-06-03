
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time

''' 
from TestData.HomePageData import HomePageData
'''
from pageObjects.HomePage import HomePage
from pageObjects.PasteLinkPage import PasteLinkPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    @pytest.mark.functional
    def test_HomePage_PasteLink(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        pastelinkpage = PasteLinkPage(self.driver)

        #  Manual test step 1 - checking home page displays
        log.info("HOME PAGE CHECK - Checking for expected body header text.")
        homePageVerificationText = homepage.verifyHomePageText().text
        try:
            assert("Test drive multi-writer Dat!" in homePageVerificationText)
            log.info("HOME PAGE CHECK - Pass")
        except AssertionError:
            log.error("HOME PAGE CHECK - Expected home page text not found!")

        #  Manual test step 2 - clicking on Have a Link? button. Expect 'Paste in a URL ." page to display
        log.info("HOME PAGE CHECK / HAVE A LINK? BUTTON - About to click.")
        homepage.verifyLinkButton().click()
        log.info("PASTE LINK PAGE CHECK - Expect page to render.")
        linkPageVerificationText = pastelinkpage.verifyPasteLinkPageText().text
        try:
            assert ("Paste in a URL link" in linkPageVerificationText)
            log.info("PASTE LINK PAGE CHECK - Pass")
        except AssertionError:
            log.error("PASTE LINK PAGE CHECK - Expected paste link URL page text not found.")

        #  Manual test step 3 - checking URL field default is blank
        log.info("PASTE LINK PAGE CHECK / URL Field Default - Expect to be blank")
        linkPageURLFieldDefaultValue = pastelinkpage.verifyURLFieldContent().text
        try:
            assert linkPageURLFieldDefaultValue == ''
            log.info("PASTE LINK PAGE CHECK / URL Field Default - Pass")
        except AssertionError:
            log.error("PASTE LINK PAGE CHECK / URL Field Default - Not null")

        #  Manual test step 4 - type in bad URL and expect warning popup
        log.info("PASTE LINK PAGE CHECK / Bad URL - Entering")
        badString = "www.bbc.co.uk"
        pastelinkpage.verifyURLFieldContent().send_keys(badString)
        pastelinkpage.verifyLinkButton().click()
        alertBoxText = pastelinkpage.getAlertBox().text
        try:
            assert("URL or key must contain a 64 character hex value" in alertBoxText)
            log.info("PASTE LINK PAGE CHECK / Bad URL - Pass, expected warning popup displayed")
        except AssertionError:
            log.error("PASTE LINK PAGE CHECK / Bad URL - No warning popup displayed")

        #  Manual test step 5 - click on popup to close it
        pastelinkpage.getAlertBox().click()
        try:
            assert (pastelinkpage.verifyURLFieldContent().get_property("value") == badString)
            log.info("PASTE LINK PAGE CHECK / Bad URL - Pass, persisted after closing warning popup as expected")
        except AssertionError:
            log.error("PASTE LINK PAGE CHECK / Bad URL - Not persisted after closing warning pop")

        #  Manual test step 6 - delete bad URL and submit a null value
        pastelinkpage.verifyURLFieldContent().clear()
        pastelinkpage.verifyLinkButton().click()
        time.sleep(2)
        # Expect no popup warning displayed when null URL entered
        alertBoxVisible = pastelinkpage.getAlertBox().is_displayed()
        try:
            assert(alertBoxVisible == False)
            log.info("PASTE LINK PAGE CHECK / Null URL - Pass")
        except AssertionError:
            log.error("PASTE LINK PAGE CHECK / Null URL - Warning popup still displayed")

        self.driver.refresh()