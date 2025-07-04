import tkinter as tk
import pyshorteners
import os
import sys

def generate_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        bundle_dir = sys._MEIPASS
        return os.path.join(bundle_dir,relative_path)
    base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)
def shorten():
    try:
        url = longurl_entry.get().strip()
        if not url:
            shorturl_entry.delete(0,tk.END)
            shorturl_entry.insert(0,"Please enter a URL!")
            copy_button.config(state="disabled")
            return
        
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'https://' + url
            
        shortner = pyshorteners.Shortener()
        short_url = shortner.tinyurl.short(url)
        shorturl_entry.delete(0,tk.END)
        shorturl_entry.insert(0,short_url)
        copy_button.config(state="normal")
    except Exception as e:
        shorturl_entry.delete(0,tk.END)
        shorturl_entry.insert(0,f"Error: {str(e)}")
        copy_button.config(state="disabled")

def copy_to_clipboard():
    try:
        short_url = shorturl_entry.get()
        if short_url and not short_url.startswith("Error:") and not short_url.startswith("Please"):
            root.clipboard_clear()
            root.clipboard_append(short_url)
            copy_button.config(text="Copied!", bg="orange")
            root.after(2000, lambda: copy_button.config(text="Copy URL", bg=Button_BG))
    except Exception:
        pass

root = tk.Tk()
root.title("URL SHORTENER")
root.geometry("400x200")

try:
    favicon_path = generate_resource_path('favicon.ico')
    root.iconbitmap(favicon_path)
except Exception:
    pass  

FONT = ("Arial",12)
LABEL_BG = "Blue"
Entry_BG = "White"
Button_BG = "Green"
Button_FG = "White"

container_frame = tk.Frame(root,bg="white")
container_frame.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)

longurl_Label = tk.Label(container_frame,text="Enter Long URL",font=FONT,bg=LABEL_BG)
longurl_entry = tk.Entry(container_frame,font=FONT,width=40,bg=Entry_BG)
shorturl_label = tk.Label(container_frame,text="Output Shortened URL",font=FONT,bg=LABEL_BG)
shorturl_entry = tk.Entry(container_frame,font=FONT,width=40,bg=Entry_BG)

# Create button frame for horizontal layout
button_frame = tk.Frame(container_frame, bg="white")
shorten_button = tk.Button(button_frame,text="Shorten URL",font=FONT,bg=Button_BG,fg=Button_FG,command=shorten)
copy_button = tk.Button(button_frame,text="Copy URL",font=FONT,bg="gray",fg=Button_FG,command=copy_to_clipboard,state="disabled")

longurl_Label.pack(pady=(0,5))
longurl_entry.pack(pady=(0,10))
longurl_entry.bind('<Return>', lambda event: shorten())  # Enter key shortcut
shorturl_label.pack(pady=(0,5))
shorturl_entry.pack(pady=(0,10))
button_frame.pack(pady=10)
shorten_button.pack(side=tk.LEFT, padx=(0,10))
copy_button.pack(side=tk.LEFT)

root.mainloop()
