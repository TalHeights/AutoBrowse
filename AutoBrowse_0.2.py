# 0.2 Script --> Adding loop for navigating between websites.

import webbrowser
import time

# List of websites to open
websites = ["https://www.facebook.com", "https://www.ebay.com", "https://www.instagram.com"]

# Loop through the list of websites and open them
for website in websites:
    webbrowser.open(website)
    time.sleep(5)  # Wait for 10 seconds before opening the next website