from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
service = Service(executable_path="/Users/shreyashkumarbhargav/Downloads/chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service)


try:
    # Navigate to Shopsy homepage
    driver.get("https://www.shopsy.in/")
    print("Navigated to Shopsy homepage.")
    
    # Close any popups if present
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='close-popup']"))
        )
        close_button.click()
        print("Closed popup.")
    except Exception as e:
        print("No popup to close or it took too long.")
    
    # Wait for the search input field to be present
    search_input_locator = (By.CSS_SELECTOR, ".sc-5591d660-3")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_input_locator)
    )
    print("Search input field is present.")
    
    # Find the search input field and perform a search
    input_element = driver.find_element(*search_input_locator)
    input_element.clear()
    input_element.send_keys("bags" + Keys.ENTER)
    print("Performed search for 'bags'.")
    
    # Wait for search results to be loaded
    search_result_locator = (By.CSS_SELECTOR, "div.bjxoUG:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(search_result_locator)
    )
    print("Search results are loaded.")
    
    # Click on the first product image in the search results
    product_image = driver.find_element(*search_result_locator)
    product_image.click()
    print("Clicked on the first product image link.")
    
    # Switch to the new tab that opens
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to new tab.")
    
    # Wait for the 'Add to Cart' button to be clickable
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-17hd0rf > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"))
    )
    add_to_cart_button.click()
    print("Clicked on 'Add to Cart' button.")
    
    # Print a message indicating successful add to cart
    print("Product added to cart successfully!")

    # Navigate to the cart page
    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sc-3a37045b-6 > svg:nth-child(1)"))
    )
    cart_button.click()
    print("Navigated to cart page.")
    
    # Wait for the 'Remove' button to be clickable
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-1oszu61 > div:nth-child(2) > div:nth-child(1)"))
    )
    remove_button.click()
    print("Clicked on 'Remove' button.")
    
    # Wait for the 'Are you sure?' confirmation button to be clickable
    confirm_remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".r-1pz39u2 > div:nth-child(2) > div:nth-child(1)"))
    )
    confirm_remove_button.click()
    print("Confirmed removal of product.")
    
    # Print a message indicating successful removal from cart
    print("Product removed from cart successfully!")

    homepage= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"#__next > main > div.sc-3a37045b-0.fsBMbO > div > div.sc-3a37045b-2.hSpCsx > a > div > svg"))
    )
    homepage.click()
    print("Navigated to Home Page successfully")
    footwear= WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,"#__next > main > div.sc-f940efef-1.lckLMq > div > div.css-175oi2r.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-agouwx.r-2eszeu > div > div.sc-cd4a929f-0.dPmaxo > div > div.css-175oi2r > div > div > div > div > div:nth-child(4) > a > div > img"))
    )
    footwear.click()
    print("clicked on footwear section successfully")

    footwear_page_element_locator = (By.CSS_SELECTOR, "#__next > main > div.sc-f940efef-1.lckLMq > div > div.css-175oi2r.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-agouwx.r-2eszeu > div > div.sc-cd4a929f-0.dPmaxo > div > div.css-175oi2r > div > div > div > div > div:nth-child(4) > a > div") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(footwear_page_element_locator)
    )
    print("Footwear page loaded successfully.")
                                      

except Exception as e:
    # Print failure message and exception details
    print("Failure in adding or removing product from cart.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(10)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")