import os
import time
import requests
from selenium import webdriver

# Define the URL to scrape
WEB_URL = "URL WILL GO HERE "

# Initialize a Firefox webdriver
driver = webdriver.Firefox()

# Open the webpage
driver.get(WEB_URL)

# Wait for 5 seconds to let the page load
time.sleep(5)

# Execute JavaScript to get src attributes of specific elements
elements = driver.execute_script("""
    var elements = document.getElementsByClassName("wETe9b jFVN1");
    var srcList = [];
    for (let element of elements) {
        srcList.push(element.src);
    }
    return srcList; 
""")

# Close the webdriver
driver.quit()

# Create directory to save downloaded images if it doesn't exist
if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')

# Download each image
for index, image_url in enumerate(elements):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            # Save the image to disk
            with open(f"downloaded_images/image_{index}.jpg", 'wb') as f:
                f.write(response.content)
            print(f"Image {index} downloaded successfully.")
        else:
            print(f"Failed to download image {index}: HTTP status code {response.status_code}")
    except Exception as e:
        print(f"Error downloading image {index}: {str(e)}")

print("All images downloaded.")
