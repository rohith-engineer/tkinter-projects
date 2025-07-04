🔧 Project Description
A simple GUI-based tool using Python's Tkinter that takes a long URL and converts it into a shortened URL using the pyshorteners library with the TinyURL API.

📦 Pre-requisites / Technologies Used
Tool/Library	Purpose
tkinter	GUI library for Python to create desktop applications
pyshorteners	Python library to generate short URLs (TinyURL, etc.)
os + sys	Used to make the app work with both source and .exe
iconbitmap()	Sets a custom icon (used when packaging as executable)

📌 Core Features
Takes a long URL as input.

Generates a shortened version using TinyURL via pyshorteners.

Displays the shortened URL in a textbox.

GUI built for ease of use—clear labels, input/output boxes, and a single action button.

Packaged using pyinstaller for Windows (.exe) deployment.