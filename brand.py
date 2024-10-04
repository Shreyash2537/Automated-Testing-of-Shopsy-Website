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
    
    # Click on the brand dropdown
    brand_dropdown_locator = (By.CSS_SELECTOR, "html body div#__next main.sc-f940efef-0.kqLgIr div.sc-f940efef-1.lckLMq div.css-175oi2r div.css-175oi2r.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-agouwx.r-2eszeu div.css-175oi2r div.sc-d0e4397a-0.cahpRU div.sc-d0e4397a-1.gTgRpp div#slot_10000.css-175oi2r.r-f8sm7e.r-3w0k23.r-13qz1uu div.sc-46489703-0.etuTng div.sc-46489703-1.cnDhii div.sc-46489703-0.ceUfrI div.sc-46489703-1.bjxoUG div.sc-46489703-0.ceUfrI div.sc-46489703-1.bjxoUG div.css-175oi2r.r-13awgt0.r-eqz5dr div.css-175oi2r.r-1fdo3w0 div div.css-175oi2r.r-1awozwy.r-1loqt21.r-18u37iz.r-1wtj0ep.r-13qz1uu")  # Replace with actual selector
    brand_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(brand_dropdown_locator)
    )
    brand_dropdown.click()
    print("Clicked on the brand dropdown.")
    
    # Check the checkbox for a specific brand
    brand_checkbox_locator = (By.CSS_SELECTOR, "div.css-175oi2r:nth-child(7) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")  # Replace with actual selector
    brand_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(brand_checkbox_locator)
    )
    brand_checkbox.click()
    print("Checked the checkbox for the selected brand.")
    
    # Wait for the filtered results to be loaded
    filtered_result_locator = (By.CSS_SELECTOR, "div.css-175oi2r:nth-child(7) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")  # Replace with actual selector
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(filtered_result_locator)
    )
    print("Filtered products based on selected brand are loaded.")

    # Print a message indicating successful filtering
    print("Products filtered by brand successfully!")

    # Proceed with further actions if needed...

except Exception as e:
    # Print failure message and exception details
    print("Failure in searching, filtering, or interacting with products.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(10)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")