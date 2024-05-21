import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create ChromeOptions and add any necessary arguments
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')  # Optional: Add any other Chrome options you need

# Create a Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the external link
driver.get('https://maps.app.goo.gl/UH3PyPhFdoA7xNbe7')

# Wait for the page to load (you may need to adjust the wait time)
time.sleep(5)  # Increased wait time to ensure the page loads properly

# Find and click the first element (e.g., a button)
element = driver.find_element(By.CSS_SELECTOR, '.g88MCb')  # Replace with the correct CSS selector
element.click()

# Wait for the interaction to take effect (if needed)
time.sleep(5)

# Find and click the second element (e.g., a button)
element2 = driver.find_element(By.CSS_SELECTOR, '.zaxyGe')  # Replace with the correct CSS selector
element2.click()

# Wait for the interaction to take effect (if needed)
time.sleep(5)

# Get the page source after the interaction
page_source = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract information from the page (e.g., find and print text from a specific element)
target_element = soup.find('div', class_='yA7sBe')  # Replace with the correct HTML tag and class name
if target_element:
    print(target_element.text)

# Close the WebDriver
driver.quit()
