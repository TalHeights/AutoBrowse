# 0.6 Script --> Add sites with different suffixes.
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# Create service for the driver
service = Service(verbose = True)

# Create a webdriver instance (path "C:\TalDrivers\edgedriver_win64")
driver = webdriver.Edge(service = service)

# List of websites to visit
websites = [
    "https://www.google.co.il",
    "https://www.walla.co.il",
    "http://www.moomoo.co.il",
    "https://www.ynet.co.il",
    "https://www.leumit.co.il",
    "https://www.gov.il",
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.ebay.com",
    "https://www.instagram.com",
    "https://www.primevideo.com",
    "https://www.w3schools.com",
    "https://www.reddit.com",
    "https://www.twitter.com",
    "https://www.netflix.com",
    "https://www.linkedin.com",
    "https://www.amazon.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.wikipedia.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.nationalgeographic.com",
    "https://www.quora.com",
    "https://www.pinterest.com",
    "https://www.tumblr.com",
    "https://www.yahoo.com",
    "https://www.dropbox.com",
    "https://www.spotify.com",
    "https://www.walmart.com",
    "https://www.target.com",
    "https://www.bestbuy.com",
    "https://www.ikea.com",
    "https://www.google.co.uk",
    "https://www.cartoonnetwork.co.uk",
    "https://www.usa.gov"]

# Time delay between websites
t = 5 

while (True):
    # Loop through the list of websites and navigate to each one
    for website in websites:
        driver.get(website) # Open the website in the current browser window
        time.sleep(t)       # Wait for t seconds before navigating to the next website

# Close the browser window when done
driver.quit()