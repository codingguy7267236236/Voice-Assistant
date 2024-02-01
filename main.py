import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from nextcord.ext import commands
import sqlite3
import docx
import wordDoc

#ai name
ai = "laptop"
#discord status variable
discord = False

lim = 5


#responsible for recognising speech
r = sr.Recognizer()

#checking if user says ai's name
def checkname():
    with sr.Microphone() as source:
        #retrieves and processes audio
        audio = r.listen(source)

        #voice data variable
        voice_data = ""

        #try except incase of unkown value being detected
        try:
            voice_data = r.recognize_google(audio)

            if str(voice_data).lower() == ai:
                return voice_data

        #in case the audio doesnt pick anything up
        except sr.UnknownValueError:
            pass

        except sr.RequestError:
            speak("Sorry I am having trouble understanding right now, please try agian!")
        print(voice_data)
        return voice_data

#function for detecting audio
#ask value allows us to ask the user something
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask == False:
            pass
            #speak("How can I help")

        else:
            speak(ask)
        #retrieves and processes audio
        audio = r.listen(source, phrase_time_limit=lim)

        #voice data variable
        voice_data = ""

        #try except incase of unkown value being detected
        try:
            voice_data = r.recognize_google(audio)

        #in case the audio doesnt pick anything up
        except sr.UnknownValueError:
            pass
            #speak("Sorry I couldn't understand that!")

        except sr.RequestError:
            speak("Sorry I am having trouble understanding right now, please try agian later")

        #print(voice_data)
        return voice_data

#speak text to speech
def speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1,1000000000)
    audio_file = f"audio-{r}.mp3"
    path = f"audio/{audio_file}"
    tts.save(path)
    print(audio_string)
    playsound.playsound(f"./{path}")
    os.remove(path)

def getId(name):
    name = name.lower()
    connection = sqlite3.connect("Database.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT Id FROM discord WHERE name='{name}'")
    id = cursor.fetchone()
    if id != None:
        id = id[0]
    return id

#sending messages via discord bot
async def message_func(id,message,bot):
    if id == 763430991946711100 or id == 712327693101695088:
        guild = await bot.fetch_guild(763402952110505984)
        channel = await guild.fetch_channel(763402952659435542)

    elif id == 653620631258005514:
        guild = await bot.fetch_guild(1030528306417774604)
        channel = await guild.fetch_channel(1030528307235672138)
        
    else:
        guild = await bot.fetch_guild(969660464101466162)
        channel = await guild.fetch_channel(969660464642539612)
        
    member = await guild.fetch_member(id)
    print("About to send")
    await channel.send(f"{member.mention} {message}")
    print("Sent")
    
#discord response functions
async def discord_respond(voice_data,bot):
    discord = True
    if ai in str(voice_data).lower():
        if "message" in str(voice_data).lower():
            name = record_audio("Who do you want to message?")
            id = getId(name)
            if id == None:
                speak("Couldn't find user!")
            
            else:
                message = record_audio(f"What do you want to send {name}?")
                await message_func(id,message,bot)

        elif "close discord" in str(voice_data).lower():
            discord = False
            speak("Disconnected from Discord")
            await bot.close()

    return discord

#ai responding
def respond(voice_data):
    if ai in str(voice_data):
        #webbrowser path to display web pages
        path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        #path = None

        
        if "what is your name" in str(voice_data).lower():
            speak(f"My name is: {ai}")

        elif "what time is" in str(voice_data).lower():
            print(ctime())
            speak(ctime())
                

            if found == False:
                speak("I don't know that one")

        elif "what day is it" in str(voice_data).lower():
            pass


        elif "search" in str(voice_data).lower():
            #capturing user audio input for search term
            search = record_audio("What do you want to search?")
            #creating url to search on google
            url = "https://google.com/search?q=" + search
            #loading the web page
            webbrowser.get(path).open(url)
            speak("Here is what I found for " + search)

        elif "youtube" in str(voice_data).lower():
            #capturing user audio input for search term
            search = record_audio("What do you want to search on youtube?")
            #creating url to search on google
            url = "https://youtube.com/results?search_query=" + search
            #loading the web page
            webbrowser.get(path).open(url)
            speak("Here is what I found for " + search)

        elif "exit" in str(voice_data).lower() or "goodbye" in str(voice_data).lower() or "good bye" in str(voice_data).lower():
            speak("Goodbye!")
            exit()

        elif "haaland" in str(voice_data).lower():
            url = "https://www.youtube.com/watch?v=kzTi73HQoPI"
            #loading the web page
            webbrowser.get(path).open(url)

        elif "open" in str(voice_data).lower():
            if "geography project" in str(voice_data).lower():
                url = "URL TO GEOGRAPHY PROJECT"
                webbrowser.get(path).open(url)

            elif "computer science project" in str(voice_data).lower():
                url = "URL TO COMPUTER SCIENCE PROJECT"
                webbrowser.get(path).open(url)

            elif "onenote" in str(voice_data).lower():
                url = "URL TO ONENOTE"
                webbrowser.get(path).open(url)
                
            elif "arcgis" in str(voice_data).lower():
                url = "https://www.arcgis.com/home/webmap/viewer.html"
                webbrowser.get(path).open(url)

            #opens all the geography related resources 
            elif "geography stuff" in str(voice_data).lower():
                url = "https://www.arcgis.com/home/webmap/viewer.html"
                webbrowser.get(path).open(url)
                url = ""
                webbrowser.get(path).open(url)

            elif "word document" in str(voice_data).lower():
                name = record_audio("What is the filename?")
                if name == None:
                    speak("Couldn't find file")

                else:
                    mes = wordDoc.open(name)
                    speak(mes)

            elif "discord" in str(voice_data).lower():
                url = "https://discord.com/channels/@me"
                webbrowser.get(path).open(url)

        #closing tabs
        elif "close chrome" in str(voice_data).lower():
            #closing chrome
            os.system("taskkill /im chrome.exe /f")
            speak("Chrome closed")
        
        #create function
        elif "create" in str(voice_data).lower():
            if "word" in str(voice_data).lower():
                doc = docx.Document()
                name = record_audio("What filename do you want to give the file?")
                if name == None:
                    name = "temp"
                path = f"./documents/word/{name}.docx"
                doc.save(path)
                speak(f"Document {name} saved")

        elif "edit" in str(voice_data).lower():
            if "word document" in str(voice_data).lower():
                path = "./documents/word/test 1.docx"
                doc = docx.Document(path)
                file = wordDoc.wordDoc(doc,path)
                editing = True
                speak("Editing word document mode activated")
                while editing == True:
                    voice_data = record_audio()
                    mes = wordDoc.check(voice_data,ai,file)
                    if mes != None:
                        speak(mes)
                        
                    if mes == "Editing mode deactivated":
                        editing = False
                    
        #starts the voice assistant discord bot
        elif "connect to discord" in str(voice_data).lower():
            bot = commands.Bot(command_prefix="!")

            @bot.event
            async def on_ready():
                discord = True
                speak("Connected to Discord")

                while discord:
                    #check = checkname()
                    #print(check)
                    #if ai in check.lower():
                    voice_data = record_audio()
                    await discord_respond(voice_data,bot)

            bot.run("DISCORD BOT TOKEN")

        #Funny rickroll meme
        else:
            url = "https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif"
            webbrowser.get().open(url)
            playsound.playsound(f"rickroll.mp3")
        
    print(voice_data)
    #waiting = False


#code block starts the voice assistant and listens for voice input
time.sleep(1)
speak(f"Say hello {ai} to begin")
waiting = False
while 1:
    #check = checkname()
    #if ai in check.lower():
    voice_data = record_audio()
    respond(voice_data)
