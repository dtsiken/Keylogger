Collection of Keylogger

First is Saves Only Localy in the Text File

Second is Advanced Version. Keystroke that will Sends to Telegram Group using a BOT with set Amount of Time**

**The Text File will be created when executed and the FORMAT will be Like this:**

![image](https://github.com/dtsiken/Keylogger/assets/101923825/8a3fbbad-d49c-46ff-a627-65faa0c88035)

**The Text File will be Created Before Sending to Telegram will be like this:**

![image](https://github.com/dtsiken/Keylogger/assets/101923825/0bef8a42-67c6-4c55-9128-12c2512d5e61)

**This is the Content of the Log inside:**

![image](https://github.com/dtsiken/Keylogger/assets/101923825/deece16b-c1ee-4332-b378-a067843f0336)

**This is the sent Text File to Telegram:**

![image](https://github.com/dtsiken/Keylogger/assets/101923825/e129e57c-534e-4999-a7eb-646bf38e4b6a)


**You can Make a Executable of this Program Follow the Steps Below:**

1. Proceed to this Link:

   https://nuitka.net/doc/download.html

2. Copy this Command and Paste it to the Command Prompt and Hit Enter No Admin Privilege Needed Wait for it to Download(Recommended the Stable Version)

   **Note: You Need an Internet Connection for This Step**

   # Stable version
      python -m pip install -U nuitka

   # Develop version
      python -m pip install -U "https://github.com/Nuitka/Nuitka/archive/develop.zip"

3. Once its Complete Proceed to the Directory of the Python File of the Program that you want to Make a  Executable(If You are Encountering some Errors Run CMD in that Directory as an Admin)

4. Now you are in the Directory
   
   **Type this Command(If you want not Have a CMD Console Showing in the Screen When Running the .exe and Make it Stealthy)**

   python -m nuitka --mingw64 pythonfile.py --standalone --onefile --windows-disable-console

   **Type this Command(If you Want a regular Compiling)**

   python -m nuitka --mingw64 pythonfile.py --standalone --onefile

   **Note: Before you Compile your Program you must Test it (.py) and Running Correctly According to your Specification and The Necessary Libraries must be Installed Properly to Compile it Alongside the Program (.exe) and to prevent the Errors that may Occur.FAILURE TO MEET THIS REQUIREMETS WILL ENCOUNTER ERRORS AND THE .exe WILL NOT WORK CORRECTLY.**

5. Wait for it to Compile and Sometimes when you are First Time Installing the Nuitka There is a Several Prompt and asks you that ends with that "YES/NO"  just type "yes" (it is not case sensitive)

6. There is a Feedback Message in CMD When the Tasks are Done and the .exe file will be located where the directory that you are Working on and Named it the Same as .py File that you Entered Earlier

7. Run it and ENJOY!
   
**Additional Notes: If the .exe has a Error or Something try to Revisit the Source Code(.py) and Test it Again and Recompile it to .exe**

**If the Error still Exists Try This Alternative(Using Pyinstaller)**

1. Proceed to this Link:

   https://pyinstaller.org/en/stable/installation.html

2. Copy this Command and Paste it to the Command Prompt and Hit Enter No Admin Privilege Needed Wait for it to Download

   Note: You Need an Internet Connection for This Step

   pip install pyinstaller

3. Once its Complete Proceed to the Directory of the Python File of the Program that you want to Make a  Executable(If You are Encountering some Errors Run CMD in that Directory as an Admin)

4. Now you are in the Directory

   **Type this Command**

   pyinstaller --onefile your_script.py

5. Wait for it to Compile and Sometimes it takes Long

6. There is a Feedback Message in CMD When the Tasks are Done and the .exe file will be located where the directory that you are Working on and Named it the Same as .py File that you Entered Earlier

7. The Executable must be Created and Ready to Run Enjoy!


