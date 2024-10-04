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
    
    # Wait for the login button to be clickable and click it
    login_button_locator = (By.CSS_SELECTOR, "#__next > main > div.sc-3a37045b-0.fsBMbO > div > div.sc-3a37045b-3.jbUmWD > div:nth-child(1) > div > div > div.sc-c711f4f6-2.jKBKKx")  
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(login_button_locator)
    )
    login_button.click()
    print("Clicked on login button.")
    
    # If the login is within an iframe, switch to it
    try:
        iframe_locator = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div/iframe")  
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(iframe_locator)
        )
        print("Switched to login iframe.")
    except Exception as e:
        print("No iframe for login detected, proceeding without iframe switch.")
    
    # Wait for the phone number input field to be present
    phone_input_locator = (By.CSS_SELECTOR, "#slot_4 > div > div.sc-4a2e88f0-3.cCsvqZ > input")  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(phone_input_locator)
    )
    print("Phone number input field is present.")
    
    # Find the phone number input field and enter the phone number
    phone_input = driver.find_element(*phone_input_locator)
    phone_input.clear()
    phone_input.send_keys("7654895394")  # Replace with the actual phone number for testing
    print("Entered phone number.")
    
    # Click the 'Next' or 'Submit' button
    next_button_locator = (By.CSS_SELECTOR, "#slot_6 > div > button")  # Replace with the actual selector
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(next_button_locator)
    )
    next_button.click()
    print("Clicked on 'continue' button.")
    
    # Wait for the OTP input field to be present
    otp_input_locator1 = (By.CSS_SELECTOR, "#slot_2 > div > div.sc-4a2e88f0-13.MFoNf > div > input:nth-child(1)")  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(otp_input_locator1)
    )
    
    
    # Enter the OTP
    otp_input = driver.find_element(*otp_input_locator1)
    otp_input.clear()
    otp_input.send_keys("2")  # Replace with the actual OTP for testing
    
    otp_input_locator2 = (By.CSS_SELECTOR, "#slot_2 > div > div.sc-4a2e88f0-13.MFoNf > div > input:nth-child(2)")  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(otp_input_locator2)
    )
    
    
    # Enter the OTP
    otp_input = driver.find_element(*otp_input_locator2)
    otp_input.clear()
    otp_input.send_keys("1")  # Replace with the actual OTP for testing
    
    otp_input_locator3 = (By.CSS_SELECTOR, "#slot_2 > div > div.sc-4a2e88f0-13.MFoNf > div > input:nth-child(3)")  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(otp_input_locator3)
    )
    
    
    # Enter the OTP
    otp_input = driver.find_element(*otp_input_locator3)
    otp_input.clear()
    otp_input.send_keys("4")  # Replace with the actual OTP for testing
    
    otp_input_locator4 = (By.CSS_SELECTOR, "#slot_2 > div > div.sc-4a2e88f0-13.MFoNf > div > input:nth-child(4)")  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(otp_input_locator4)
    )
  
    
    # Enter the OTP
    otp_input = driver.find_element(*otp_input_locator4)
    otp_input.clear()
    otp_input.send_keys("5")  # Replace with the actual OTP for testing
   
    otp_input_locator5 = (By.CSS_SELECTOR, "#slot_2 > div > div.sc-4a2e88f0-13.MFoNf > div > input:nth-child(5)") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(otp_input_locator5)
    )
   
    
    # Enter the OTP
    otp_input = driver.find_element(*otp_input_locator5)
    otp_input.clear()
    otp_input.send_keys("1")  # Replace with the actual OTP for testing
    
    otp_input_locator6 = (By.CSS_SELECTOR, "#slot_2 > div > div.sc-4a2e88f0-13.MFoNf > div > input:nth-child(6)")  
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(otp_input_locator6)
    )
   
    
    # Enter the OTP
    otp_input = driver.find_element(*otp_input_locator6)
    otp_input.clear()
    otp_input.send_keys("3")  
    print("Entered OTP.")
    
    # Click the 'Verify' button
    verify_button_locator = (By.CSS_SELECTOR, "#slot_3 > div > button") 
    verify_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(verify_button_locator)
    )
    verify_button.click()
    print("Clicked on 'Verify' button.")
    
    # Wait for the login to complete (e.g., check for the presence of a logout button or user profile)
    user_profile_locator = (By.CSS_SELECTOR, "#__next > main > div.sc-3a37045b-0.fsBMbO > div > div.sc-3a37045b-3.jbUmWD > div:nth-child(1) > div > div > div.sc-c711f4f6-2.jKBKKx")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(user_profile_locator)
    )
    print("Login successful.")

except Exception as e:
    # Print failure message and exception details
    print("Failure during login process.")
    print(f"Error: {e}")

finally:
    # Wait for a few seconds to observe the result
    time.sleep(20)
    
    # Close the browser
    driver.quit()
    print("Browser closed.")