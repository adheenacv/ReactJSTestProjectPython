import pytest
from selenium import webdriver

from pages.react_select_page import ReactSelectPage

@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://react-select.com/home')

    yield browser

    browser.close()

def test_pre_selected_list_in_basic_multi_select(browser):
    expected_list = ['Purple', 'Red']
    react_page = ReactSelectPage(browser)
    actual_list = react_page.basic_multi_select().get_selected_items()
    assert actual_list == expected_list


def test_clear_all_list_in_basic_multi_select(browser):
    react_page = ReactSelectPage(browser)
    react_page.basic_multi_select().click_on_clear_all_items()
    actual_status = react_page.basic_multi_select().is_placeholder_displayed()

    assert actual_status is True


def test_select_multiple_items_in_basic_multi_select(browser):
    react_page = ReactSelectPage(browser)
    react_page.basic_multi_select().click_on_clear_all_items()

    items = ['Red', 'Purple', 'Orange', 'Yellow']
    react_page.basic_multi_select().select_multiple_items(items)
    actual_list = react_page.basic_multi_select().get_selected_items()
    assert actual_list == items

def test_clear_single_item_in_basic_multi_select(browser):
    initial_list = ['Purple', 'Red']
    item_to_be_removed = 'Purple'
    initial_list.remove(item_to_be_removed)

    react_page = ReactSelectPage(browser)
    react_page.basic_multi_select().click_on_clear_item(item_to_be_removed)
    actual_list = react_page.basic_multi_select().get_selected_items()

    assert actual_list == initial_list

def test_pre_selected_list_in_multi_select_with_color(browser):
    expected_list = ['Ocean', 'Blue']
    react_page = ReactSelectPage(browser)
    actual_list = react_page.multi_select_with_color().get_selected_items()
    assert actual_list == expected_list


def test_clear_all_list_in_multi_select_with_color(browser):
    react_page = ReactSelectPage(browser)
    react_page.multi_select_with_color().click_on_clear_all_items()
    actual_status = react_page.multi_select_with_color().is_placeholder_displayed()

    assert actual_status is True


def test_select_multiple_items_in_multi_select_with_color(browser):
    react_page = ReactSelectPage(browser)
    react_page.multi_select_with_color().click_on_clear_all_items()

    items = ['Red', 'Purple', 'Orange', 'Yellow']
    react_page.multi_select_with_color().select_multiple_items(items)
    actual_list = react_page.multi_select_with_color().get_selected_items()
    assert actual_list == items


def test_clear_single_item_in_multi_select_with_color(browser):
    initial_list = ['Ocean', 'Blue']
    item_to_be_removed = 'Blue'
    initial_list.remove(item_to_be_removed)

    react_page = ReactSelectPage(browser)
    react_page.multi_select_with_color().click_on_clear_item(item_to_be_removed)
    actual_list = react_page.multi_select_with_color().get_selected_items()

    assert actual_list == initial_list

