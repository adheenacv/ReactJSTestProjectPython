def find_one_element(browser, strategy, locator, parent=None, ):
    if parent:
        return parent.find_element(strategy, locator)
    else:
        return browser.find_element(strategy, locator)

def find_all_elements(browser, strategy, locator, parent=None):
    if parent:
        return parent.find_elements(strategy, locator)
    else:
        return browser.find_elements(strategy, locator)