import subprocess
import wolframalpha
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import datetime 
import json
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import pyaudio
import tkinter
from tkinter import *
import shutil
import pyautogui as him2
import time
from ecapture import ecapture as ec
import pytube
from pytube import YouTube
import ctypes
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def speak(text):
	voiceEngine.say(text)
	voiceEngine.runAndWait()

def wish():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Jarvis at your service sir")
    print("Jarvis at your service sir")


def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:", uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)
    
def updateCommandLabel(command):
    showCommand.set(command)

def takeCommand():
    
    global showCommand
    showCommand.set("Listening....")
    wn.update()

    recog = sr.Recognizer()
     
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 0.5
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")
        updateCommandLabel(command)
        wn.update()

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        updateCommandLabel("Unable to Recognize the voice. ")
        wn.update()
        return "None"

    return command

def getWeather(city_name):
    #getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(url)
    x = response.json()

    #If there is no error, getting all the wather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp-=273 
        pressure = y["pressure"]
        humidiy = y["humidity"]
        desc = x["weather"]
        description = desc[0]["description"]
        info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidiy)+"%" +"\n description = " +str(description))
        print(info)
        speak("Here is the weather report at")
        speak(city_name)
        speak(info)
        wn.update()
    else:
        speak(" City Not Found ")
        
def open_calculator():
    """Function to open the Calculator app."""
    try:
        subprocess.Popen('calc.exe')  # Open Calculator app on Windows
    except FileNotFoundError:
        print("Calculator app not found on this system.")
    
def get_current_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    return current_volume

# Function to set the volume to a specific level (0.0 to 1.0)
def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def callVoiceAssistant():

    uname=''
    asname=''
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "jarvis" in command:
            wish()
            
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)

        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" +command)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")
       
        elif "who are you" in command:
            speak("I am your virtual assistant.")

        elif "change my name to" in command:
            speak("What would you like me to call you, Sir or Madam ")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)
        
        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam ")
            assname = takeCommand()
            speak("Thank you for naming me!")

        elif "what's your name" in command or "your name" in command:
            asname = "Jarvis"  # Set the assistant's name
            speak(f"My name is {asname}")  # Speak the assistant's name using TTS
        
        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)

        elif "wikipedia" in command:
            speak("What do you want to search on Wikipedia?")
            search_command = takeCommand()
            if search_command:
                try:
                    results = wikipedia.summary(search_command, sentences=2)
                    speak("According to Wikipedia...")
                    speak(results)
                    print(results)
                    wn.update()
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("Can you please specify? I found multiple results.")
                except wikipedia.exceptions.PageError as e:
                    speak("Sorry, I could not find any matching results.")
                    
        elif 'open youtube' in command:
            speak("Here you go, the Youtube is opening\n")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open("google.com")
            
        elif 'open instagram' in command:
            speak("Opening instagram\n")
            webbrowser.open("instagram.com")
            
        elif 'open whatsapp' in command:
            speak("Opening whatsapp\n")
            webbrowser.open("web.whatsapp.com")
            
        elif 'open twitter' in command:
            speak("Opening twitter\n")
            webbrowser.open("twitter.com")

        elif 'play music' in command or " jarvis play song" in command or 'jarvis play music' in command or "play song" in command:
            speak("Enjoy the music!")
            music_dir = r"D:\desktop assistant\music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[0]))

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif "will you be my gf" in command or "will you be my bf" in command:
            speak("I'm not sure about that, may be you should give me some time")

        elif "i love you" in command:
            speak("Thank you! But, It's a pleasure to hear it from you.")

        elif "weather" in command:
            speak(" Please tell your city name ")
            print("City name : ")
            cityName = takeCommand()
            getWeather(cityName)

        elif "what is" in command or "who is" in command:
            
            client = wolframalpha.Client("WHYYAY-PALP4GJP55")
            res = client.query(command)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)

        elif "remember that" in command:
            speak("What should I remember")
            data = takeCommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in command:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))
        
        elif "don't listen" in command or "stop listening" in command:
            speak("For how many seconds do you want to stop listening?")
            timeout_command = takeCommand()

            try:
                timeout_seconds = int(timeout_command)
                speak(f"I will stop listening for {timeout_seconds} seconds.")
                time.sleep(timeout_seconds)
                speak("I'm listening again.")
            except ValueError:
                speak("Sorry, I didn't understand the duration. Please try again.")

        elif "stop assistant" in command:
            speak("Stopping the assistant.")
            break  # Exit the while loop to stop the assistant

        elif "camera" in command or "take a photo" in command:
            ec.capture(0, "Desktop synchronamate camera", "img.jpg")
            
        elif 'shutdown system' in command:
            print("Hold On a Sec! Your system is on its way to shut down.")
            try:
                subprocess.call(['shutdown', '/s', '/f'])
            except Exception as e:
                print("Error occurred:", e)

        elif "restart" in command or "janu restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "sleep mode" in command:
            speak("Putting the computer into sleep mode.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'download video' in command:
            video_url = 'https://www.youtube.com/watch?v=V7LwfY5U5WI'
            youtube = pytube.YouTube(video_url)
            video = youtube.streams.first()
            video.download('C:\\test-')
            print("Viedo Saved")
            speak("Viedo Saved")

        elif 'take screenshot' in command:
            SS = him2.screenshot()
            os.makedirs(r'D:\desktop assistant\screenshots', exist_ok=True)
            SS.save(r'D:\desktop assistant\screenshots\pic1.png')
            print("Screenshot Saved")
            speak("Screenshot Saved")
        
        elif 'calculator' in command:
            print("Opening Calculator...")
            open_calculator()
            print("calculator opened")
            speak("calculator opened")
            
        elif 'add' in command or 'addition' in command:
            speak("Sure, please provide the numbers to add.")
            speak("First number:")
            num1= takeCommand()
            speak("Second number:")
            num2= takeCommand()

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                speak("Sorry, I couldn't understand the numbers.")
                continue
    
            result = num1 + num2
            speak(f"The result of {num1} plus {num2} is {result}")
            print(f"The result of {num1} plus {num2} is {result}")

        elif 'sub' in command or 'subtraction' in command:
            speak("Sure, please provide the numbers to subtract.")
            speak("First number:")
            num1= takeCommand()
            speak("Second number:")
            num2= takeCommand()

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                speak("Sorry, I couldn't understand the numbers.")
                continue
    
            result = num1 - num2
            speak(f"The result of {num1} minus {num2} is {result}")
            print(f"The result of {num1}  minus {num2} is {result}")

        elif 'mul' in command or 'multiplication' in command:
            speak("Sure, please provide the numbers to multiply.")
            speak("First number:")
            num1= takeCommand()
            speak("Second number:")
            num2= takeCommand()

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                speak("Sorry, I couldn't understand the numbers.")
                continue
    
            result = num1 * num2
            speak(f"The result of {num1} into {num2} is {result}")
            print(f"The result of {num1} into {num2} is {result}")
        
        elif 'div' in command or 'division' in command:
            speak("Sure, please provide the numbers to divide.")
            speak("First number:")
            num1= takeCommand()
            speak("Second number:")
            num2= takeCommand()

            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                speak("Sorry, I couldn't understand the numbers.")
                continue
    
            result = num1 / num2
            speak(f"The result of {num1} by {num2} is {result}")
            print(f"The result of {num1} by {num2} is {result}")
            
            
        elif "ms word" in command:
            speak("Opening Microsoft Word")
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])  # Adjust path as needed
            print("ms word is opened")
            speak("ms word is opened")
            
        elif 'powerpoint' in command:
            speak("opening Power Point presentation")
            subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"])  # Adjust path as needed
            print("ms power point is opened")
            speak("ms power point is opened")
            
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
            
        elif 'lock window' in command:
            speak("locking the device")
            print("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif "write a note" in command:
            speak("What should I write, sir?")
            note = takeCommand()
            file = open('note.txt', 'w')
    
            speak("Sir, should I include date and time?")
            snfm = takeCommand()
    
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Corrected format string
                file.write(strTime + " :- " + note)
            else:
                file.write(note)
    
            file.close()  # Close the file after writing
            
        elif "open c drive" in command:
            speak("Opening C drive.")
            try:
                os.system("explorer C:\\")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I encountered an error while trying to open the C drive.")
                
        elif "open d drive" in command:
            speak("Opening D drive.")
            try:
                os.system("explorer D:\\")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I encountered an error while trying to open the D drive.")
                
        elif "open documents" in command:
            speak("Opening Documents folder.")
            try:
                os.system("explorer \"C:\\Users\\91997\\OneDrive\\Documents\"")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I encountered an error while trying to open the Documents folder.")
        
        elif "open downloads" in command:
            speak("Opening Downloads folder.")
            try:
                os.system("explorer \"C:\\Users\\91997\\OneDrive\\Downloads\"")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I encountered an error while trying to open the Downloads folder.")
                
        elif "open pictures" in command:
            speak("Opening Pictures folder.")
            try:
                os.system("explorer \"C:\\Users\\91997\\OneDrive\\Pictures\"")
            except Exception as e:
                print("Error:", e)
                speak("Sorry, I encountered an error while trying to open the Pictures folder.")
                
        elif "volume up" in command:
            current_volume = get_current_volume()
            new_volume = min(current_volume + 0.1, 1.0)  # Increase volume by 10%
            set_volume(new_volume)
            print(f"Volume increased to {new_volume * 100:.0f}%")
        elif "volume down" in command:
            current_volume = get_current_volume()
            new_volume = max(current_volume - 0.1, 0.0)  # Decrease volume by 10%
            set_volume(new_volume)
            print(f"Volume decreased to {new_volume * 100:.0f}%")
        
        
        elif 'exit' in command:
            speak("Exiting Jarvis. Goodbye, sir!")
            wn.quit()
            break
            
                    
        else:
            speak("Sorry, I am not able to understand you")
            

wn = tkinter.Tk()
wn.title("Desktop Synchronize")

# Get the screen resolution of the laptop
screen_width = wn.winfo_screenwidth()
screen_height = wn.winfo_screenheight()

# Calculate the position to center the window
window_width = 700
window_height = 300
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the window geometry to center it on the screen
wn.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Load the background image
bg_image = PhotoImage(file="window.png")

# Create a label with the background image
bg_label = Label(wn, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label for welcome message
Label(wn, text='Welcome....! Meet your Personal Assistant', fg='black', font=('Times New Roman', 20)).place(relx=0.5, rely=0.1, anchor='center')

# Button to start the action
Button(wn, text="Start", bg='pink', font=('Times New Roman', 15), command=callVoiceAssistant).place(relx=0.5, rely=0.4, anchor='center')

# Label to display commands
showCommand = StringVar()
cmdLabel = Label(wn, textvariable=showCommand, fg='black', font=('Courier', 15))
cmdLabel.place(relx=0.5, rely=0.7, anchor='center')

# Run the main event loop
wn.mainloop()