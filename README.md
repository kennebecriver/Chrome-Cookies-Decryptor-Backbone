# Chrome-Cookies-Decryptor-Backbone
The Chrome Cookies Decryptor is a Python script designed to decrypt the cookies stored in Google Chrome's local SQLite database.  It has been tested on Windows 11 and Chrome Version 112.

The script uses the PyWin32 library to retrieve the user's encryption key from the Windows Data Protection API, and the pycrypto library to decrypt the cookies using AES-256-GCM encryption. The decrypted cookies are then saved to a text file, which includes the cookie name, host key, and decrypted value.

To compile the script into an executable file, you can use PyInstaller with the command "pyinstaller --onefile script.py". 

This will create a single executable file that can be run on any Windows machine without the need for Python or any additional libraries.
