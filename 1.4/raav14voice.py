# Raav Voice Build 1.1
# 1 MEANS YES 0 MEANS NO
import math
import os
import subprocess
import sys
import time
import urllib
import webbrowser
from tkinter import *

import pyaudio
import pyttsx3
import requests
import speech_recognition as SR
import wikipedia
import wolframalpha
import pathlib
import base64

from Keywords import Keywordcall
from Moudules import Helpers, FollowUp, Recognize, logfiles

# If you want to use the speech recognition moudule or just the type command
TalkToProgram = True
r = SR.Recognizer()
# This is for an audio file
# SR.AudioFile('')
mic = SR.Microphone()
# Change that to true or false
# __________________________USER OPTIONS______________________________________
modelnumber = 1.4
speechrecognizer = "googlecloud"

# __________________________Imports___________________________________________
# import speedtest
# The imports commented out have not been installed on RaavDesk
# Installed on RaavDesk:
# -wolframalpha
# -math {built in}
# -Wikipedia
# -Speech Recognition
# __________________________THE OUTPUT________________________________________

# __________________________Varables__________________________________________
app_id = "LQEGLQ-JVJTQP73QA"
# That is for WolframAlpha
stackurl = "https://stackoverflow.com/search?q="
# for stackoverflow
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# this is for the webbrowser function it would always open in IE
question_memory_value = "Question.raavmemory"
answer_memory_value = "Memory.raavmemory"
log_file_value = "log.raavlog"
# Big list
# Preneeded code
global alreadysaid
alreadysaid = 0
file_path = pathlib.Path(__file__).resolve()
pythonfilelocation = str(file_path.parent)
Memoryx = Helpers()
Keywordx = Keywordcall()
logfiles("---------------STARTED NEW RUN OF PROGRAM----------------")
# __________________________Definitions_______________________________________


def onlyMic(recognizer_source):
    with mic as source:
        audioData = r.listen(source)
    type(audioData)
    logfiles("Audio data " + str(audioData))
    text = r.recognize_google(
        audioData, key=None, language="en-US")
    '''try:
            logfiles("Using " + recognizer_source + " as recoognizer")
            if recognizer_source == "google":
                text = r.recognize_google(
                    audioData, key=None, language="en-US")
            if recognizer_source == "sphinx":
                text = r.recognize_sphinx(audioData)
            if recognizer_source == "googlecloud":
                text = r.recognize_google_cloud(audioData)
            if recognizer_source == "houndify":
                text = r.recognize_houndify(audioData)
            if recognizer_source == "ibm":
                text = r.recognize_ibm(audioData)
            logfiles("Extracted " + text + " from file. ")
        except:
            return False'''
    if text[:4] == "Rave":
        xtemp = len(text)
        textToPass = text[5:xtemp]
        logfiles("Starting with: " + textToPass)
        return textToPass
    else:
        return 0


def internet_check(timeout):
    url = 'https://www.google.com/'
    timeout = 1
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


internetonoff = os.system("ping google.com")
if internetonoff == 1:
    offlinemode = True
    logfiles("connection succesful")
else:
    offlinemode = False
logfiles("offline: " + str(offlinemode))


"""def speedTest():
	s = speedtest.Speedtest()
	s.get_best_server()
	s.download()
	s.upload()
	res = s.results.dict()
	data = res['download']
	data2 = round(data / 1048576)
	return data2
"""


def StackAPI(stackQuestion):
    if offlinemode == True:
        stackQuestion = stackQuestion.replace(" ", "+")
        stackFinalURL = stackurl + stackQuestion
        webbrowser.get(chrome_path).open(stackFinalURL)
        # opens the stackoverflow url
    elif offlinemode == False:
        Memoryx.Output("Stackoverflow is not avalible during offline mode")


def verifyAnswer(questioncheck, checkorfind):
    memtemp = Memoryx.getx(questioncheck, question_memory_value)
    logfiles("Found in memory: " + str(memtemp))
    if memtemp == False:
        logfiles("False was not able to find answer from memory")
        return False
    else:

        if checkorfind == True:
            return True
        else:
            memoryRestoreAnswer = Memoryx.findvalue(
                memtemp, answer_memory_value)
            Memoryx.Output(memoryRestoreAnswer)
            logfiles("True was able to find answer from memory")
            return True


def memoryStorageWrite(addMEM, MEMquestion):
    indexQuestion = verifyAnswer(MEMquestion, True)
    if indexQuestion == True:
        pass
    else:
        if "\n" in addMEM:
            addMEM.replace("\n", " ")
        logfiles("adding " + addMEM + " and " + MEMquestion + " to memory")
        addMEM = addMEM.upper()
        MEMquestion = MEMquestion.upper()
        fileMEM = open(answer_memory_value, "a")
        fileMEM.write(">>>" + addMEM)
        fileMEM.write("\n")
        fileMEM.close()
        fileQST = open(question_memory_value, "a")
        fileQST.write(">>>" + MEMquestion)
        fileQST.write("\n")
        fileQST.close()
        # This makes the program run faster by saving the question and answer so if a previously asked question is stored in memory it can pull it up right away.


def callWolf(wolfQuestion):
    wolfQuestion = str(wolfQuestion)
    wolfQuestion = wolfQuestion.lower()
    # Wolfram Alpha Functions
    client = wolframalpha.Client(app_id)
    # validates the client ID
    result = client.query(wolfQuestion)
    # gets the answer to the question
    wolfAnswer = next(result.results).text
    memoryStorageWrite(wolfAnswer, wolfQuestion)
    # converts the answer to text
    return wolfAnswer
    # returns answer as x = y()


def stackoverflowcall(QuestionAsked):
    if ("SEARCH STACK OVERFLOW" in QuestionAsked) or ("SEARCH STACKOVERFLOW" in QuestionAsked):
        # There are many diffrent combinations that STACKOVERFLOW could be said in
        if ("SEARCH STACK OVERFLOW FOR" in QuestionAsked):
            SendQuestion = QuestionAsked.replace(
                "SEARCH STACK OVERFLOW FOR ", "")
            StackAPI(SendQuestion)
            # ------------------------------------------------------------------------------------
        elif ("SEARCH STACKOVERFLOW FOR" in QuestionAsked):
            SendQuestion = QuestionAsked.replace(
                "SEARCH STACKOVERFLOW FOR", "")
            StackAPI(SendQuestion)
            # ------------------------------------------------------------------------------------
        elif ("SEARCH STACK OVERFLOW ABOUT" in QuestionAsked):
            SendQuestion = QuestionAsked.replace(
                "SEARCH STACK OVERFLOW ABOUT", "")
            StackAPI(SendQuestion)
            # ------------------------------------------------------------------------------------
        elif ("SEARCH STACKOVERFLOW ABOUT" in QuestionAsked):
            SendQuestion = QuestionAsked.replace(
                "SEARCH STACKOVERFLOW ABOUT", "")
            StackAPI(SendQuestion)
            # ------------------------------------------------------------------------------------
        if (len(QuestionAsked) <= 21):
            Memoryx.Output("What would you like to search?")
            QuestionFollowUp = FollowUp()
            StackAPI(QuestionFollowUp)


def wikipediaQ(wikiQuestion):
    wikiQuestion = wikiQuestion.lower()
    wikiQuestion = str(wikiQuestion)
    # Gets the wikipedia input and returns it in 2 sentences
    wikitext = wikipedia.summary(wikiQuestion, sentences=2)
    memoryStorageWrite(wikitext, wikiQuestion)
    # adds the answer to storage
    logfiles("Found " + str(wikitext) + "from wikipedia")
    wikitext = "According to wikipedia, " + wikitext
    return wikitext


# __________________________MAIN-LOOP_________________________________________


def mainline():
    # master.quit()
    logfiles("Starting Mainline")
    if whichbutton == 1:
        miccheck = 0
        while miccheck == 0:
            Memoryx.Output("Starting Microphone")
            returncode = onlyMic(speechrecognizer)
            if returncode == False:
                Memoryx.Output("Im sorry please say that again")
            elif returncode == 0:
                placeholder = True
            else:
                QuestionAsked = returncode
                miccheck = 1
    elif whichbutton == 0 or whichbutton == 3:
        QuestionAsked = 1  # e1.get()
    #e1.delete('0', END)
    # e1.update()
    # this is just to check to make sure that the command isnt just `exit`
    speccheck = Keywordx.specword("exit", QuestionAsked)
    if speccheck == True:
        # master.quit
        # Keywordx.analyze()
        placeholder = True
    tryfail = 0
    QuestionAsked = QuestionAsked.upper()
    logfiles("Testing from memory")
    checkanswerfromverify = verifyAnswer(QuestionAsked, False)
    if checkanswerfromverify == False:
        logfiles("Found from memory: " + str(checkanswerfromverify))
        # This will try to see if the command is answerable by wolframalpha and/or wikipedia
        if offlinemode == False:
            try:
                finalAnswer = callWolf(QuestionAsked)
                Memoryx.Output(finalAnswer)
                tryfail += 1
            except Exception as e:
                logfiles("Error saved as " + e)
                finalAnswer = wikipediaQ(QuestionAsked)
                Memoryx.Output(finalAnswer)
                tryfail += 1
            except Exception as e:
                if tryfail == 0:
                    if checkanswerfromverify == True:
                        pass
                    elif checkanswerfromverify == False:
                        Memoryx.Output("I could not find an answer to that")
        elif offlinemode == True:
            if alreadysaid == 0:
                Memoryx.Output("Continuing in offline mode, everything that has been saved in local files will be avalible but all of the speech integrations and online research is disabled until you reboot me and enbale it.")
                alreadysaid == 1
            elif alreadysaid == 1:
                Memoryx.Output("Cannot Answer Because you are in offline mode")
# --------------------------Code------------------------------------------


global whichbutton
whichbutton = 3
Memoryx.Output("ready")


def setbutton(value):
    if "keysym=Return" in str(value):
        value = 3
        global whichbutton


whichbutton = 1
mainline()


'''
offlinemodeindicator = "Offline Mode: " + str(offlinemode)
master = Tk()
Label(master, text="Command:").grid(row=0)
Label(master, text=offlinemodeindicator).grid(row=1, column=1)
master.geometry("300x60")
imagefilelocation = pythonfilelocation + '/computing.gif'
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Exit', command=master.quit).grid(
    row=0, column=3, sticky=W, pady=4)
Button(master, text='Send', command=lambda *args: setbutton(0)).grid(
    row=0, column=4, sticky=W, pady=4)
master.iconbitmap(pythonfilelocation + '/raav.ico')
master.bind('<Return>', setbutton)
Button(master, text='Voice', command=lambda *args: setbutton(1)).grid(
    row=0, column=5, sticky=W, pady=4)
computinggif = PhotoImage(image=imagefilelocation)
giflabel = Label(image=computinggif)
giflabel.pack()

master.title("Raav " + str(modelnumber))
master.mainloop()
'''
