import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Function to start the browser and open a URL
def start_browser():
    url = entry_url.get()
    headless = headless_var.get()

    # Chrome options
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")  # Run browser in headless mode (without UI)

    # Start the browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)

# Create the main window
root = tk.Tk()
root.title("Python Browser with Settings")

# URL label and entry
label_url = tk.Label(root, text="Enter URL:")
label_url.pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Headless option checkbox
headless_var = tk.BooleanVar()
check_headless = tk.Checkbutton(root, text="Run Headless", variable=headless_var)
check_headless.pack(pady=5)

# Start browser button
button_start = tk.Button(root, text="Start Browser", command=start_browser)
button_start.pack(pady=10)

# Run the tkinter main loop
root.mainloop()
