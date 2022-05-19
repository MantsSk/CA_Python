from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest


driver = ''
iframe = ''

@pytest.mark.skip(reason="This is setup function")
def test_setup():
    s=Service("/Users/mantasskara/Downloads/chromedriver")
    global driver
    global iframe
    driver = webdriver.Chrome(service=s)
    driver.get("https://frontend.nopcommerce.com/")

    iframe = driver.find_element(By.XPATH, "/html/body/main/div/iframe")
    driver.switch_to.frame(iframe)

@pytest.mark.parametrize("input, expected_name", [
    ("Nike", "Nike Floral Roshe Customized Running Shoes"),
    ("Computer", "Build your own computer"),
    ("MacBook", "Apple MacBook Pro 13-inch"),
    ("Shoe", "Nike Floral Roshe Customized Running Shoes")
    ])
def test_basic_product_search(input, expected_name):
    test_setup()

    # driver.get("https://frontend.nopcommerce.com/")
    searchInput = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
    searchInput.send_keys(input)

    button = driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button')
    button.click()

    product = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/h2/a')

    # time.sleep(10)
    assert product.text == expected_name

@pytest.mark.parametrize("input, expected_name, select_input", [
    ("Nike", "Nike Floral Roshe Customized Running Shoes", "10"),
    ("Computer", "Build your own computer", "2"),
    ("MacBook", "Apple MacBook Pro 13-inch", "3"),
    ("Shoe", "adidas Consortium Campus 80s Running Shoes", "10")
    ])
def test_basic_product_search_with_advanced_found(input, expected_name, select_input): # for testing if products can be found with different categories
    test_setup()

    # driver.get("https://frontend.nopcommerce.com/")
    searchInput = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
    searchInput.send_keys(input)

    button = driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button')
    button.click()

    advancedSearchButton = driver.find_element(By.XPATH, '//*[@id="advs"]')
    advancedSearchButton.click()

    select = Select(driver.find_element(By.XPATH, '//*[@id="cid"]'))
    select.select_by_value(select_input)
    # driver.implicitly_wait(15)
    searchButton = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[1]/form/div[2]/button')
    searchButton.click()

    product = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/h2/a')

    assert product.text == expected_name

@pytest.mark.parametrize("input, expected_name, select_input", [
    ("Nike", "No products were found that matched your criteria.", "14"),
    ("Computer", "No products were found that matched your criteria.", "12"),
    ("MacBook", "No products were found that matched your criteria.", "13"),
    ("Shoe", "No products were found that matched your criteria.", "14")
    ])
def test_basic_product_search_with_advanced_not_found(input, expected_name, select_input): # for testing if products are not shown when not appropriate category is selected
    test_setup()

    # driver.get("https://frontend.nopcommerce.com/")
    searchInput = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
    searchInput.send_keys(input)

    button = driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button')
    button.click()

    advancedSearchButton = driver.find_element(By.XPATH, '//*[@id="advs"]')
    advancedSearchButton.click()

    select = Select(driver.find_element(By.XPATH, '//*[@id="cid"]'))
    select.select_by_value(select_input)
    # driver.implicitly_wait(15)
    searchButton = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[1]/form/div[2]/button')
    searchButton.click()

    no_products_message = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div')

    assert no_products_message.text == expected_name

@pytest.mark.parametrize("input, expected_name", [
    ("Nike", "Nike Floral Roshe Customized Running Shoes"),
    ("Computer", "Build your own computer"),
    ("MacBook", "Apple MacBook Pro 13-inch"),
    ("Shoe", "Nike Floral Roshe Customized Running Shoes")
    ])
def test_open_product_simple(input, expected_name): # open product after simple search, check if product exists, compare text
    test_setup()

    # driver.get("https://frontend.nopcommerce.com/")
    searchInput = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
    searchInput.send_keys(input)

    button = driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button')
    button.click()

    product = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/h2/a')
    product.click()

    product_page_name = driver.find_element(By.XPATH, '//*[@id="product-details-form"]/div[2]/div[1]/div[2]/div[1]/h1')
    # time.sleep(10)
    assert product_page_name.text == expected_name

@pytest.mark.parametrize("input, expected_name, select_input", [
    ("Nike", "Nike Floral Roshe Customized Running Shoes", "10"),
    ("Computer", "Build your own computer", "2"),
    ("MacBook", "Apple MacBook Pro 13-inch", "3"),
    ("Shoe", "adidas Consortium Campus 80s Running Shoes", "10")
    ])
def test_open_product_simple_advanced_search(input, expected_name, select_input): # open product after advanced search, check if product exists, compare text
    test_setup()

    # driver.get("https://frontend.nopcommerce.com/")
    searchInput = driver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
    searchInput.send_keys(input)

    button = driver.find_element(By.XPATH, '//*[@id="small-search-box-form"]/button')
    button.click()

    advancedSearchButton = driver.find_element(By.XPATH, '//*[@id="advs"]')
    advancedSearchButton.click()

    select = Select(driver.find_element(By.XPATH, '//*[@id="cid"]'))
    select.select_by_value(select_input)
    # driver.implicitly_wait(15)
    searchButton = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[1]/form/div[2]/button')
    searchButton.click()

    product = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/h2/a')
    product.click()

    product_page_name = driver.find_element(By.XPATH, '//*[@id="product-details-form"]/div[2]/div[1]/div[2]/div[1]/h1')
    assert product_page_name.text == expected_name
