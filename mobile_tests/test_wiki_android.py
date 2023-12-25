
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be



def test_onboarding_screen_and_search():
    with allure.step('Verify content page 1'):
        results = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))
        results.should(have.exact_text("The Free Encyclopedia\n…in over 300 languages"))

    with allure.step('Open next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify content page 2'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))

    with allure.step('Open next page'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify content page 3'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))

    with allure.step('Press Continue button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Verify content page 4'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Send anonymous data'))

    with allure.step('Accept User Agreemen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/acceptButton')).click()

    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selenium')

    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Selenium'))

