# 0.7 Script --> Add unexisted website with try method.

from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# Create service for the driver
service = Service(verbose = True)

# Create a webdriver instance (path "C:\TalDrivers\edgedriver_win64")
driver = webdriver.Edge(service = service)

# List of websites to visit
websites = [
    "https://www.walla.co.il",
    "https://www.w3schools.com",
    "https://www.cartoonnetwork.co.uk"]

unExistedWebsite = "https://www.w3schls.com"

# Time delay between websites
t = 5 

while (True):
    # Loop through the list of websites and navigate to each one
    for website in websites:
        driver.get(website) # Open the website in the current browser window
        time.sleep(t)       # Wait for t seconds before navigating to the next website

    try:
        driver.get(unExistedWebsite)
    except:
        print("Heights Logs: Error was occurred. Most likely becuase the website not exist")
    time.sleep(t)

print("Quit from loop!")

# Close the browser window when done
driver.quit()