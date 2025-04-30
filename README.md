# Weatherbot.py

## Purpose
The purpose of this script is to automate a discord message daily telling me the Weather in my local region of Toronto. Discord is commonly used messaging service and I have built a habit of checking my messages and thus, automatically receive a message using Windows Task Scheduler with the current temperature.

## How does it work?
The script is set on Windows Task Scheduler but can be replicated for MacOS using Launchd or Cron job for Linux systems. Set the script to run at an update time, this can be on device login, at a specific time interval, etc. 
Once the script runs in a selected channel or configured to be a personal message, the weather API will be called and collect the regional weather and messaged in the form of Celsius. 
