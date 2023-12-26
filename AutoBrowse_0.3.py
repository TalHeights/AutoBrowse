# 0.3 Script --> Work with Selenium.
# Opening different sites in managed window.

from selenium import webdriver
import time

# Create a webdriver instance (path "C:\TalDrivers\edgedriver_win64")
driver = webdriver.Edge()

# List of websites to visit
websites = [
    "https://www.facebook.com",
    "https://www.ebay.com",
    "https://www.instagram.com",
    "https://www.primevideo.com",
    "https://www.w3schools.com",
    "https://www.youtube.com",
    "https://www.reddit.com",
    "https://www.twitter.com",
    "https://www.netflix.com",
    "https://www.linkedin.com",
    "https://www.amazon.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.google.com",
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
    "https://www.ikea.com"]

# Time delay between websites
t = 5 

while (True):
    # Loop through the list of websites and navigate to each one
    for website in websites:
        driver.get(website)  # Open the website in the current browser window
        time.sleep(t)       # Wait for t seconds before navigating to the next website

# Close the browser window when done
driver.quit()