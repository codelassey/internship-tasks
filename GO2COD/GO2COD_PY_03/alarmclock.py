#Importing the required modules
# I'm using datetime to get the current time and time to pause the program
import datetime
import time
import os  # This is used to play a sound when the alarm goes off
import platform #To detect the operating system of the user

# Function to play a sound when the alarm is reached
# I'll use the built-in 'os' module to play a sound file
def play_sound():
    print("Alarm ringing! Time to wake up!")
    # Assuming a sound file named 'alarm_sound.mp3' is in the same folder
    # Replace 'alarm_sound.mp3' with the path to your sound file
    sound_file = "yhaw_hero_too_young.mp3"
    # Check the operating system of the user
    system_name = platform.system()
    if system_name == "Windows":
         os.system(f"start {sound_file}")
    elif system_name == "Linux":
         os.system(f"xdg-open {sound_file}")
    elif system_name == "Darwin": #MacOS
         os.system(f"open {sound_file}")
    else:
         print("Can't play sound due to unsupported operating system")

# Asking the user for the alarm time
# I want the user to input the time in HH:MM format
alarm_time = input("Set your alarm time (in HH:MM format, e.g., 07:30): ")

# I need to ensure the input is in the correct format
try:
    # I'll convert the input into a datetime object
    alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
    alarm_datetime = datetime.datetime.combine(datetime.date.today(), datetime.time(alarm_hour, alarm_minute))
    print(f"Alarm is set for {alarm_datetime.strftime('%I:%M %p')}.")
except ValueError:
    print("Invalid time format! Please enter the time in HH:MM format.")
    exit()  # Exiting the program if the input is invalid

# This is the main loop that checks the current time
while True:
    # Getting the current time
    current_time = datetime.datetime.now()

    # Comparing the current time with the alarm time
    if current_time >= alarm_datetime:
        # If the current time is the alarm time or later, I trigger the alarm
        play_sound()
        break  # Breaking out of the loop after the alarm is triggered

    # To avoid checking the time constantly, I'll add a small delay
    time.sleep(10)  # I'll check every 10 seconds to save resources

# After the alarm has been triggered, I can add a nice message to end the program
print("Alarm ended. Have a great day!")
