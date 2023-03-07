ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"

# afkBot
Python Script that will move your mouse occasionally in order to prevent computer from sleeping

If you do not have python installed on your machine:

WINDOWS MACHINES
----------------
1. If you do not have a package manager installed, download chocolatey by opening your Command Prompt and pasting this command in:

@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

2. Install Python by typing this command into your command prompt: 
 
choco install python

3. Install pyautogui by typing this command into your command prompt: 
 
choco install pyautogui


MACOS

1. If you do not have a package manager installed, download HomeBrew by opening your terminal and pasting this command in:

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2. Install python by typing this command into your command prompt:

brew install python

3. Install pyautogui by pasting this command into your command prompt:

brew install pyautogui
