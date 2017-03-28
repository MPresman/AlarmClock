'''
'''
import time
import datetime
import re
import pygame


def setAlarm():
    print("Hello, what time would you like the alarm to sound? Please input in this format\ne.g. 7:45pm\n")
    time = input("Time: ")

    splitTime = re.compile(r'(\d+?)(:)(\d+?)(pm|am)') #split up time inputted for manipulation
    timeRe = splitTime.search(time)

    hour = int(timeRe.group(1))
    minutes = int(timeRe.group(3))
    dayOfTime = timeRe.group(4).lower() #set pm or am to lowercase for ease

    #errorChecking for proper time format
    if hour > 12 or hour < 1:
        print("Please input your time properly, in 12 hour time")
        setAlarm()

    if minutes > 59 or minutes <  0:
        print("Please input your time properly")
        setAlarm()


    #if time of day is pm, then reassign all values from 1pm - 11:59pm as 13, 14, 15, etc 24 hour.
    if dayOfTime == "pm" and hour != 12:
        convertedHour = hour + 12

    else:
        convertedHour = hour

    if dayOfTime == "am" and hour == 12:
        convertedHour = 24

    finalTime = str(convertedHour) + ":" + str(minutes)
    print(finalTime)
    return finalTime



def clockCheck():
    #get the hour and time from setAlarm
    splitTime = re.compile(r'(\d+?)(:)(\d+)')
    timeRe = splitTime.search(setAlarm())
    alarmHour = int(timeRe.group(1))
    alarmMinute = int(timeRe.group(3))

    #get the live time
    now = datetime.datetime.now()
    currentHour = now.hour
    currentMinute = now.minute
    currentSecond = now.second


    while True:
        if currentHour != alarmHour:
            time.sleep(60-currentSecond) #if this isn't done, the alarm could be off by a couple seconds. Line's up things
            time.sleep((60*60) - (60*(currentMinute-1))) #this sleeps the program until the next hour is hit and reruns a check
            now = datetime.datetime.now()
            currentHour = now.hour
        elif currentMinute != alarmMinute:
            time.sleep(60-currentSecond) #sleep until the next minute and rerun the check
            now = datetime.datetime.now()
            currentMinute = now.minute
            currentSecond = now.second
        else:
            break
    alarmSound()


def alarmSound():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/michaelpresman/PycharmProjects/AlarmClock/sound.wav")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    clockCheck()

main()