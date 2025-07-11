import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait



# Suppress unnecessary logging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # TensorFlow suppress
chrome_log_options = ['--log-level=3', '--disable-logging', '--silent', '--disable-dev-shm-usage']  # Chrome options

# Paths
chrome_executable_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chromedriver_path = r"C:\chromedriver\chromedriver.exe"  # Update this path to where your chromedriver is located

# List of Chrome profiles
chrome_profiles_with_remarks = {



    "Profile 13": "A4",
    "Profile 14": "A5",
    "Profile 15": "A6",
    "Profile 16": "A7",
    "Profile 17": "A8",
    "Profile 18": "A9",
    "Profile 19": "A10",
    "Profile 20": "A11",
    "Profile 3": "5DD",
    "Profile 2": "788",
    "Profile 4": "Test",
    "Profile 22": "TWT",

}


# Telegram bot details
bot_token = '8022081464:AAHUd2tXUx7zrJNZwALea8pjl8MjfZXMmss'
chat_id = '-1002463691776'

def send_telegram_message(chat_id, message):
    """Send a message to a Telegram chat."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"Message sent: {message}")
        else:
            print(f"Failed to send message: {message}")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

def automate_for_profile(profile_name):

    profile_remark = chrome_profiles_with_remarks.get(profile_name, profile_name)  # Default to profile_name if no remark
    
        # Dictionary to track task completion
    task_status = {
        "Mine Game": "Incomplete",  
        "Plinko Game": "Incomplete", 
        "Wheel Game": "Incomplete",
        
    }

    # Set up Chrome options
    options = Options()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.binary_location = chrome_executable_path
    options.add_argument(f"--user-data-dir=C:\\Users\\x815\\AppData\\Local\\Google\\Chrome\\User Data")  # Update this path as needed
    options.add_argument(f"--profile-directory={profile_name}")  # Use the current profile

    # Set up the Service with the path to chromedriver.exe
    service = Service(executable_path=chromedriver_path)

    complete_emoji = "✅"
    incomplete_emoji = "❌"

    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")  # Navigate to the target URL
        driver.maximize_window()

        # Wait for the password input field to be clickable
        time.sleep(3)  # Adjust sleep time as necessary
        password_input = driver.find_element(By.ID, "password")  # Find the password input field
        password_input.click()  # Click on the password input field
        password_input.clear()  # Clear the input field if necessary
        password_input.send_keys("11112222")  # Enter the password

        # Submit the form
        password_input.send_keys(Keys.RETURN)

        time.sleep(2)
        
        

        # Task 1: Miner Game
        try:
        
            # Change The Network
            driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
            
            time.sleep(3)
            
            # Step 1: Click the network picker button
            network_picker_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="network-display"]'))
            )
            network_picker_button.click()
            print("Network picker button clicked successfully.")
                
            # Step 2: Wait for the network options popup to appear
            time.sleep(5)  # Give some time for the popup to fully load
            
            try:
                sepolia_option = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//p[text()='Sonic Testnet']"))
                )
                
                driver.execute_script("arguments[0].click();", sepolia_option)
                print(f"Sonic Testnet click successfully.")
                
            except Exception as e:
                print(f"Error clicking Sonic Testnet")
            

            time.sleep(5)  # Give some time for the popup to fully load

            driver.get("https://arcade.soniclabs.com/game/mines")
            time.sleep(15)
            
            try:
                # Confirm the transaction
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-testid, 'page-container-footer-next')]"))
                )
                confirm_button.click()
                time.sleep(15)
                print("Metamask Clicked")
            except Exception as e:
                print("Metamask Not Visible")
            
            # Click a random button
            try:
            
                try:
                    # Check if the "Get" button is clickable
                    get_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'wr-bg-green-500') and contains(., 'Get')]"))
                    )
                    # Click the "Get" button and wait for 10 seconds
                    get_button.click()
                    print("Clicked 'Get' button successfully.")
                    time.sleep(10)

                except Exception as e:
                    print("Get button not found or not clickable, proceeding to random button selection:", str(e))


                # Repeat the process for 10 times
                for _ in range(10):
                    try:
                        # Step 1: Click a random button
                        time.sleep(5)
                        buttons = driver.find_elements(By.CSS_SELECTOR, "div.wr-mb-0.wr-aspect-square button")
                        if buttons:
                            random_button = random.choice(buttons)
                            driver.execute_script("arguments[0].click();", random_button)
                            print("Random button clicked successfully.")
                        else:
                            print("No buttons found with specified class.")
                        time.sleep(20)  # Wait for 20 seconds after clicking the button
                        
                        # Step 2: Attempt to locate and click the "Get" button
                        try:
                            # Switch to new window
                            driver.switch_to.window(driver.window_handles[1])
                            # Confirm the transaction
                            confirm_button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-testid, 'page-container-footer-next')]"))
                            )
                            confirm_button.click()
                            print("Metamask Clicked")
                        except Exception as e:
                            print("Metamask Not Visible")
                        
                        time.sleep(20)  # Wait for 20 seconds after clicking the button
                        # Step 2: Attempt to locate and click the "Get" button
                        try:
                            get_button = WebDriverWait(driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'wr-bg-green-500') and contains(., 'Get')]"))
                            )
                            get_button.click()
                            print("Clicked 'Get' button successfully.")
                        except Exception as e:
                            print("Error clicking 'Get' button:", str(e))
                        
                        time.sleep(20)  # Wait for another 20 seconds after clicking "Get" button

                    except Exception as e:
                        print(f"Error in iteration: {str(e)}")


            except Exception as e:
                print(f"Error during interaction: {str(e)}")
                task_status["Mine Game"] = "Incomplete"
                
                """
                # Open a new tab and navigate to the extension URL
                driver.execute_script("window.open('');")  # Open a new tab
                driver.switch_to.window(driver.window_handles[1])  # Switch to the new tab
                driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html")
                time.sleep(3)  # Wait for the page to load

                # Locate and click the confirm button in the extension
                confirm_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn--rounded.btn-primary.page-container__footer-button"))
                )
                time.sleep(5)  # Short wait before clicking
                confirm_button.click()
                print("Confirm button clicked in extension page.")
                # Close the current tab and switch back to the previous tab
                driver.close()  # Closes the current tab
                driver.switch_to.window(driver.window_handles[0])  # Switches back to the first tab
                print("Switched back to the previous tab.")
                """

            

        except Exception as e:
            task_status["Ithaca Testnet"] = "Incomplete"
            print(f"Error occurred: ")
            time.sleep(3)


        
        
        

    except Exception as e:
        print(f"An error occurred on profile {profile_remark}")

    finally:
    
        result_message = f"{profile_remark}:\n"
        
        for task, status in task_status.items():
            result_message += f"{task} {complete_emoji if status == 'Complete' else incomplete_emoji}\n"
    
        send_telegram_message(chat_id, result_message)
        # Wait to see the result and then close the browser
        time.sleep(2)
        driver.quit()

# Loop through each profile and perform automation
for profile, remark in chrome_profiles_with_remarks.items():
    print(f"Starting automation for {remark}...")
    automate_for_profile(profile)
    print(f"Completed automation for {remark}.\n")
