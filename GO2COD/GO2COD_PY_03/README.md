# Alarm Clock Project

This is a simple Python project that functions as an Alarm Clock. It allows you to set an alarm for a specific time, and when the time is reached, a sound is played to notify you. The project is designed to work across platforms (Linux, macOS, and Windows).

## Features

•	Set an alarm for any specific time (in HH:MM format).
•	Plays an alarm sound when the set time is reached.
•	Cross-platform compatibility for sound playback.

## Requirements

Python Modules:

	•	datetime: To work with date and time.
	•	time: To add delays in program execution.
	•	os: For system-specific sound playback.

## Additional:

	•	A sound file located in the same folder as the script.

## Usage

 1.	Clone this repository to your local machine:

```
git clone https://github.com/codelassey/GO2COD_PY_03.git

cd GO2COD_PY_03

```
 2.	If you do not prefere the alarm sound that comes with this code, place your preferred sound file in the project folder and name it alarm_sound.mp3 (or update the filename in the code).

 
 3.	Run the script:
```
python3 alarmclock.py
```

 4.	Enter the alarm time in HH:MM format when prompted (e.g., 07:30 for 7:30 AM).

 
 5.	The script will notify you and play a sound when the time is reached.

## Platform-Specific Notes

	•	Linux: The script uses xdg-open to play the alarm sound. Ensure that your system can handle media playback using this command.
	•	Windows: The script uses the start command to open the sound file.
	•	macOS: The script uses the open command to play the sound.

For cross-platform usage, ensure the mp3 file can be played using the default media player.

## Example Output
```Set your alarm time (in HH:MM format, e.g., 07:30): 22:15
Alarm is set for 10:15 PM.
Alarm ringing! Time to wake up!
```
## Customization

	•	You can replace mp3 with any other sound file by changing its name in the play_sound() function.
	•	Adjust the time.sleep(10) value to check the time more or less frequently.

## Issues and Contributions

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
