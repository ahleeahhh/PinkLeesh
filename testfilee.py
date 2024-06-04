import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPinkLeeshWebsite(unittest.TestCase):

    def setUp(self):
        # Start the WebDriver and open the webpage
        self.driver = webdriver.Chrome()
        self.driver.get("file:///D:/AHLEEAHHH/PROG4PROJECT/Portfolio/aldunar_labexam(1).html")
        self.driver.maximize_window()

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

    def test_functionality(self):
        # Test the navigation functionality
        self._test_navigation()

        # Test the portfolio carousel functionality
        self._test_portfolio_carousel()

    def test_responsiveness(self):
        # Test responsiveness by resizing the window and checking element visibility
        self.driver.set_window_size(768, 1024)  # Example mobile resolution
        self._test_navigation()  # Test navigation on mobile resolution

        self.driver.set_window_size(1440, 900)  # Example desktop resolution
        self._test_navigation()  # Test navigation on desktop resolution

    def test_performance(self):
        # Test page load performance by measuring the time taken to load the page
        start_time = time.time()
        self.driver.refresh()
        end_time = time.time()
        load_time = end_time - start_time
        self.assertLess(load_time, 5, "Page load time exceeds 5 seconds")

    def _test_navigation(self):
        # Wait for the header to load
        header = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header"))
        )

        # Find the navigation toggle button
        nav_toggle = self.driver.find_element(By.ID, "nav-toggle")

        # Check if the navigation menu is already visible
        nav_menu = self.driver.find_element(By.ID, "nav-menu")
        if not nav_menu.is_displayed():
            # Click on the navigation toggle button to open the menu
            nav_toggle.click()

            # Wait for the navigation menu to be visible
            nav_menu = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "nav-menu"))
            )

        # Find the "About" link and click on it
        about_link = nav_menu.find_element(By.XPATH, "//a[@href='#ABOUTME']")
        about_link.click()

        # Wait for the "About Me" section to be visible
        about_section = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "ABOUTME"))
        )

        # Find and print the text in the "About Me" section
        about_text = about_section.find_element(By.TAG_NAME, "p").text
        self.assertIsNotNone(about_text, "About Me section text is missing")

    def _test_portfolio_carousel(self):
        # Scroll to the portfolio carousel
        portfolio_carousel = self.driver.find_element(By.ID, "portfolioCarousel")
        self.driver.execute_script("arguments[0].scrollIntoView();", portfolio_carousel)

        # Wait for the next slide to become active
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".carousel-item.active"))
        )


if __name__ == "__main__":
    unittest.main()

