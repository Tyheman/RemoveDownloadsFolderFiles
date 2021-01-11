# RemoveDownloadsFolderFiles
This script allows windows users to remove all files in their downloads folder after a specified amount of time. This works great for individuals who want to keep that folder clean and empty of old installers and files.

The executable was designed for a Windows machine with the default setting being set to 7 days.

If you choose to download the .exe file follow these steps

1.) Locate the file in your downloads folder

2.) Locate your machines startup folder
- The default path is C:\Users\"YOUR USERNAME"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
- In the "YOUR USERNAME" section type in the user who is logged in. This can be found by tpying in "whoami" into the command prompt

3.) Once you have located the folder place the executable file into that folder

Note: This will run once every time the machine starts up, this will check to see if your files are older than 7 days old and remove them if they are older.
