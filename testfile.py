from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Navigate to the HTML file
driver.get("file:///C:/Users/ArabelZ/Desktop/labexamprog4/aldunar_labexam.html")

try:
    # Wait for the Home section link to be clickable and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#home']"))).click()

    # Verify if the Home section is active
    assert driver.find_element(By.CSS_SELECTOR, "header nav a[href='#home']").get_attribute("class") == "active", "Home section is not active"

    # Wait for the About section link to be clickable and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#aboutme']"))).click()

    # Verify if the About section is active
    assert driver.find_element(By.CSS_SELECTOR, "header nav a[href='#aboutme']").get_attribute("class") == "active", "About section is not active"

    # Wait for the Contact section link to be clickable and click it
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#contact']"))).click()

    # Verify if the Contact section is active
    assert driver.find_element(By.CSS_SELECTOR, "header nav a[href='#contact']").get_attribute("class") == "active", "Contact section is not active"

    print("Navigation bar functionality is working correctly!")

except Exception as e:
    print("Test failed:", e)

finally:
    # This is a delay before closing the browser window
    input("Press Enter to close the browser window...")
    # Close the browser
    driver.quit()
