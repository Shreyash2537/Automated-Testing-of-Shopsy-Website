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
    
    # Wait for the "Women Clothing" dropdown to be present
    women_clothing_dropdown_locator = (By.CSS_SELECTOR, "div.sc-b1fddad4-3:nth-child(1) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(women_clothing_dropdown_locator)
    )
    print("Women Clothing dropdown is present.")
    
    # Click on the "Women Clothing" dropdown
    women_clothing_dropdown = driver.find_element(*women_clothing_dropdown_locator)
    women_clothing_dropdown.click()
    print("Clicked on the Women Clothing dropdown.")
    
    # Wait for the "Saree" section to be clickable
    saree_section_locator = (By.CSS_SELECTOR, "div.sc-347dcad8-4:nth-child(1) > div:nth-child(1) > a:nth-child(2)")
    saree_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(saree_section_locator)
    )
    saree_section.click()
    print("Clicked on the Saree section.")
    
     
    # Wait for the "men Clothing" dropdown to be present
    men_clothing_dropdown_locator = (By.CSS_SELECTOR, "div.sc-b1fddad4-3:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(men_clothing_dropdown_locator)
    )
    print("men Clothing dropdown is present.")
    
    # Click on the "men Clothing" dropdown
    men_clothing_dropdown = driver.find_element(*men_clothing_dropdown_locator)
    men_clothing_dropdown.click()
    print("Clicked on the men Clothing dropdown.")
    
    # Wait for the "jeans" section to be clickable
    jeans_section_locator = (By.CSS_SELECTOR, "div.sc-347dcad8-4:nth-child(7) > div:nth-child(1) > a:nth-child(2)")
    jeans_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(jeans_section_locator)
    )
    jeans_section.click()
    print("Clicked on the jeans section.")
    
    # Switch to the new tab that opens
    driver.switch_to.window(driver.window_handles[-1])
    print("Switched to new tab.")
    
    # Proceed with further actions if needed...

except Exception as e:
    # Print failure message and exception details
    print("Failure in navigating or interacting with elements.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(10)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")