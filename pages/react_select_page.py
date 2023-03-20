from selenium.webdriver.common.by import By

from components.custom.react_multi_select import ReactMultiSelect


class ReactSelectPage:

    __browser = None

    def __init__(self, browser):
        self.__browser = browser

    def basic_multi_select(self):
        select_component = ReactMultiSelect(self.__browser, By.XPATH,
                                            "//h4[text()='Multi']/parent::div/following-sibling::div")
        return select_component

    def multi_select_with_color(self):
        select_component = ReactMultiSelect(self.__browser, By.XPATH,
                                            "//h4[text()='Multi Select']/parent::div/following-sibling::div")
        return select_component

