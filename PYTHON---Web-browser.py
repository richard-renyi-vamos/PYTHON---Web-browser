import tkinter as tk
from tkinterweb import HtmlFrame

def open_url():
    url = entry.get()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    frame.load_url(url)

# Create the main window
root = tk.Tk()
root.title("Simple Web Browser with GUI")

# Create a label
label = tk.Label(root, text="Enter URL:")
label.pack()

# Create an entry widget
entry = tk.Entry(root, width=50)
entry.pack()

# Create a button
button = tk.Button(root, text="Open URL", command=open_url)
button.pack()

# Create an HTML Frame
frame = HtmlFrame(root, horizontal_scrollbar="auto")
frame.pack(fill="both", expand=True)

# Start the GUI event loop
root.mainloop()
