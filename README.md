# pyAutoUpdate

## A Python library to make sure your Users are up-to-date

## Setup

### The Setup is easy! Here is a step by step guide to Get Started, I know that it looks like much, but it only takes ~5 minutes

1. Download the Repo
2. Install all dependencies
    Here is a list of dependencies and how to install them
    1. Install Python 3.7+ from Python.org or if you are on Linux you can use your Package Manager. 
    2. Install Flask `pip3 install flask` or `pip install flask`
3. Create a Folder for your Server it can be anywhere you like you don't need a Specific Name.
4. Move the "update" and "update_server.py" script in the New Folder.
5. Use the text Editor of your Choice to open the "update_server.py" script and change the "port" variable to any port you want.
Pro-Tip: Do not use the following Ports: 80, 422, 8080, 22, 23 because they are often already used or locked down by the OS.
6. Start the "update_server.py" script with python3.
7. Now __COPY__ all files needed for the user of your Script in the "update" folder and zip them, in a zip called update.zip, make sure you use the "ZIP" algorithm that is standard for Windows.
9. If you want, you can forward the Port so everyone who has your IP or Domain can update their scripts using this server, alternatively you can use Services Like Linode to run the Script.

### You already finished the Setup for the Server-Side

8. Now open the "auto_update.json" file, change the address to your address, and Change the Port to the one Specified.
9. Now you can ship your Programm with the "auto_update. json" and "auto_update.py" file.
10. Now include the following lines in your Python Programm, you should call it as the first function in your Programm.
```python
import auto_update
auto_update.full_update() #If you want you can add start_command=<COMMAND TO START YOUR PROGRAMM> to start your Programm after Updating it.
```
----
Now you can add the Updated version whenever you want in the "update" folder and it will update the User's Programm automatically as long as you change the Version, in the "auto_update_version.txt" file.
### Congrats you just finished the Setup.

---
## DOCS

### The "settings" class -> "auto_update.py" and the "setting" object -> "auto_update.py":
The Settings Class is a Class created when calling the get_update_info function.
It only has a constructor that takes the path of the config file for the Updator. 
The constructor creates a range of settings needed to run the Programm all of them are from the Config File.

The only object made with this class is the "setting" object, that is global, it is called in every function of the "auto_update.py"  script. 
It is __normaly not necessary for you to change any settings on runtime__. 

### The "get_update_info" function -> "auto_update.py":
The "get_update_info" function is called in the "full_update" function. 
It takes one Argument which is the path of the config file that is needed to construct the settings class.
Due to creating the setting object, it is necessary to call it before calling the "install_update" function, it also gets a file that contains the newest
The version that is live, this file is required to exist to run the "install_update" function without any error. 

### The "install_update" function -> "auto_update.py":
The "install_update" function is called in the "full_update" function.
It takes no arguments, but needs the current version provided by calling the "get_update_info" function.
It downloads the .zip file from the Server and unzips it after that it moves every file in it from the new made temp directory to the parent directory. 

### The  "full_update" function -> "auto_update.py":
This function combines all functions in the auto_update.py and runs a command at the end.
The Command can be used to start the Updated Script.

## If there are any questions or isusse don't please ask them in the Issues Tab. Thank you!
