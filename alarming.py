'''Alarm app to remind you something'''
import random
import webbrowser
from datetime import datetime
from playsound import playsound

tones = ['alarm1', 'alarm2', 'alarm3', 'alarm4', 'alarm5']
time = input(
    'What time you want to set the alarm?\
    Enter in the format HH:MM:SS AM(or PM): ')
hour = time[0:2]
minute = time[3:5]
seconds = time[6:8]
period = time[9:11].upper()
print(
    f'Alarm set at {hour}:{minute}:{seconds} {period} successfully! \
    Enjoy your time.')
tracker = str(input(
    'Do you have a work tracker sheet to update?(yes/no) \
    (supports google sheets as of now)'))
if tracker.upper() == 'YES':
    path = str(input('Please paste the google sheet path:'))
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if period == current_period:
        if hour == current_hour:
            if minute == current_minute:
                if seconds == current_seconds:
                    print(
                        f'Its {hour}:{minute}:{seconds} {period}. '
                        f'Alarming!!')
                    random_tone = random.choice(tones) + '.mp3'
                    playsound(random_tone, block=False)
                    if tracker.upper() == 'YES':
                        print('Here you go!! update the sheet')
                        webbrowser.open(url=path)
                    break

