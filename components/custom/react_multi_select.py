from selenium.webdriver.common.by import By

from util import finder


class ReactMultiSelect:
    __browser = None
    __element = None
    __parent = None

    def __init__(self, browser, strategy, locator, parent=None):
        self.__browser = browser
        self.__element = finder.find_one_element(browser, strategy, locator, parent)
        self.__parent = parent

        if self.__element:
            self.__browser.execute_script("arguments[0].scrollIntoView();", self.__element)

    def get_element(self):
        return self.__element

    def get_parent(self):
        return self.__parent

    def click_on_clear_all_items(self):
        clear_all = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                            "div[class$='-indicatorContainer']:nth-child(1)", self.__element)
        clear_all.click()

    def is_placeholder_displayed(self):
        placeholder = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                              "[id$='-placeholder']", self.__element)
        return placeholder.is_displayed()

    def select_single_item(self, item):
        dropdown_button = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                                  "span[class$='indicatorSeparator'] ~ div", self.__element)
        dropdown_button.click()

        dropdown_list_container = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                                          "[id$='-listbox']", self.__element)

        list_item = finder.find_one_element(self.__browser, By.XPATH,
                                            ".//div[contains(@id,'-option-')][text()='" + item + "']",
                                            dropdown_list_container)
        list_item.click()

        dropdown_button.click()

    def select_multiple_items(self, items):
        dropdown_button = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                                  "span[class$='indicatorSeparator'] ~ div", self.__element)
        dropdown_button.click()

        dropdown_list_container = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                                          "div[id$='-listbox']", self.__element)

        for item in items:
            list_item = finder.find_one_element(self.__browser, By.XPATH,
                                                ".//div[contains(@id,'-option-')][text()='" + item + "']",
                                                dropdown_list_container)
            list_item.click()

        dropdown_button.click()

    def get_selected_items(self):
        selected_items = []

        selected_list_items = finder.find_all_elements(self.__browser, By.CSS_SELECTOR,
                                                       "div[class$='-multiValue']", self.__element)

        for selected_item in selected_list_items:
            selected_items.append(selected_item.text)

        return selected_items

    def click_on_clear_item(self, item):
        item_to_be_removed = finder.find_one_element(self.__browser, By.CSS_SELECTOR,
                                                     "div[aria-label='Remove " + item + "']", self.__element)
        item_to_be_removed.click()

    def get_color_of_selected_item(self, item):
        item = finder.find_one_element(self.__browser, By.XPATH,
                                       ".//div[contains(class, 'select__multi-value__label')][text()=' " + item + "']",
                                       self.__element)
        return item.get_attribute('color')
