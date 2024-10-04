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
    # Navigate to Firstcry homepage
    driver.get("https://www.shopsy.in/")
    mobile_number="7654895394"
    print("Navigated to shopsy homepage.")
    
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
    print("Performed search for 'bags.")
    
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
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#slot_10000 > div > div.sc-46489703-1.gRlMtv > div > div:nth-child(2) > div > div > div > div > div:nth-child(1) > div > div > div > div > div"))
    )
    add_to_cart_button.click()
    print("Clicked on 'Add to Cart' button.")
    
    # Print a message indicating successful add to cart
    print("Product added to cart successfully!")
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#slot_9001000 > div > div > div > div:nth-child(6) > div > div:nth-child(2) > div"))
    )
    remove_button.click()
    print("Clicked on 'Remove' button.")
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(9) > div > div.css-175oi2r > div > div > div > div > div > div > div.css-175oi2r.r-1pz39u2.r-18u37iz > div:nth-child(2) > div > div"))
        )
        close_button.click()
    except Exception as e:
        print("No popup to close or it took too long.")
    print("Product removed from cart successfully!")

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#slot_1 > div > div > div.css-175oi2r.r-1awozwy.r-1rl26hh.r-cdmcib.r-1ugchlj.r-1777fci.r-1v1z2uz.r-3ew84i > div > div"))
    )
    login_button.click()
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to new tab.")
    
    print("Login button clicked successfully")
    try:
        mobile_number_field = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[1]/div/div[1]/div/div/div/div[3]/input")
        mobile_number_field.send_keys("7654895394")

    # Submit the mobile number form
        mobile_number_field.send_keys(Keys.RETURN)
        print("Mobile number entered")
    except Exception as e:
        print("No field found to enter number")
    
    
    # Confirm removal if necessary
   #
    
    # Print a message indicating successful removal from cart
    
    
except Exception as e:
    # Print failure message and exception details
    print("Failure in adding and removing product to cart.")
    print(f"Error: {e}")


finally:
    # Wait for a few seconds to observe the result
    time.sleep(20)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")
    
