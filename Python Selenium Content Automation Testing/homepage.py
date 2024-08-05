from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from docx import Document
import time

def main():
    # Specify the path to the downloaded chromedriver.exe
    chromedriver_path = r"C:\Users\User1\chromedriver-win64\chromedriver.exe"

    # Use ChromeOptions to set the executable path
    options = ChromeOptions()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Use ChromeService to set the executable path for ChromeDriver
    service = ChromeService(executable_path=chromedriver_path)

    # Use the specified ChromeDriver service and options
    driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the website
    driver.get('https://emploin.in/')

    # Add a delay to keep the Chrome window open for 10 seconds
    time.sleep(10)

    # Close the Chrome window
    driver.quit()

if __name__ == "__main__":
    main()
