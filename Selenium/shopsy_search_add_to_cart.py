from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome options and WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the website
driver.get("https://www.shopsy.in")
time.sleep(5)

# Search for a product
search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")
search_box.send_keys("mobile")
search_box.send_keys(Keys.ENTER)
time.sleep(5)

# Click on the first product
first_product = driver.find_element(By.XPATH, "//body/div[@id='__next']/main[@class='sc-f940efef-0 kqLgIr']/div[@class='sc-f940efef-1 lckLMq']/div[@class='css-175oi2r']/div[@class='css-175oi2r r-150rngu r-eqz5dr r-16y2uox r-1wbh5a2 r-11yh6sk r-1rnoaur r-agouwx r-2eszeu']/div[@class='css-175oi2r']/div[@class='sc-d0e4397a-0 cahpRU']/div[@class='sc-d0e4397a-1 gTgRpp']/div[@id='slot_10000']/div[@class='sc-46489703-0 etuTng']/div[@class='sc-46489703-1 drgEeC']/div[@class='sc-46489703-0 ceUfrI']/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
first_product.click()
time.sleep(5)

# Print product details
product_name = driver.find_element(By.XPATH, "//span[normalize-space()='Apple Iphone 15 (Starlight, 512 GB) (6 GB RAM)']")
print("Product Name:", product_name.text)
product_price = driver.find_element(By.XPATH, "//div[@class='css-146c3p1 r-cqee49 r-1vgyyaa r-1x35g6 r-1rsjblm']")
print("Product Price:", product_price.text)

# Add the product to the cart
add_to_cart_button = driver.find_element(By.XPATH, "//body/div[@id='__next']/main[@class='sc-f940efef-0 kqLgIr']/div[@class='sc-f940efef-1 lckLMq']/div[@class='css-175oi2r']/div[@class='css-175oi2r r-150rngu r-eqz5dr r-16y2uox r-1wbh5a2 r-11yh6sk r-1rnoaur r-agouwx r-2eszeu']/div[@class='css-175oi2r']/div[@class='sc-d0e4397a-0 cahpRU']/div[@class='sc-d0e4397a-1 hiKPTd']/div[@id='slot_10000']/div[@class='sc-46489703-0 gKCArY']/div[@class='sc-46489703-1 gRlMtv']/div[@class='sc-46489703-0 ceUfrI']/div[@class='sc-46489703-1 bjxoUG']/div[@class='css-175oi2r r-13awgt0 r-eqz5dr']/div/div[@class='css-175oi2r r-13awgt0 r-eqz5dr r-1w6e6rj r-1777fci r-13qz1uu']/div[@class='css-175oi2r r-13awgt0 r-18u37iz r-1w6e6rj r-1777fci r-13qz1uu r-17hd0rf']/div[1]/div[1]/div[1]/div[1]/div[1]")
add_to_cart_button.click()
time.sleep(5)

# View the cart
view_cart_button = driver.find_element(By.XPATH, "//div[contains(text(),'Cart')]")
view_cart_button.click()
time.sleep(5)

# Close the browser
driver.quit()
