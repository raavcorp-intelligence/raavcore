# Raav Voice Build 1.1
# 1 MEANS YES 0 MEANS NO
from tkinter import *
import wolframalpha
import os
from Moudules import Memory
from Keywords import Keywords
import wikipedia
import speech_recognition as SR
import math
import webbrowser
import subprocess
import pyaudio
import pyttsx3
import sys
import time
import urllib
import requests
# If you want to use the speech recognition moudule or just the type command
TalkToProgram = False

# Change that to true or false
# __________________________USER OPTIONS______________________________________


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
# Big list
# Preneeded code

Memoryx = Memory()
Keywordx = Keywords()

# __________________________Definitions_______________________________________


def internet_check(timeout):
    url = 'http://www.google.com/'
    timeout = 5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False


internetonoff = internet_check(1)
if internetonoff == False:
    offlinemode = True
else:
    offlinemode = False


def keyWords(string):  # This will always be learning and storing
    Memoryx.Output("Booting Keywords")


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
    if memtemp == False:
        return False
    else:

        if checkorfind == True:
            return True
        else:
            memoryRestoreAnswer = Memoryx.findvalue(
                memtemp, answer_memory_value)
            Memoryx.Output(memoryRestoreAnswer)
            return True


def memoryStorageWrite(addMEM, MEMquestion):
    indexQuestion = verifyAnswer(MEMquestion, True)
    if indexQuestion == True:
        pass
    else:
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


def FollowUp():
    with mic as source:
        audioData = r.listen(source)
    type(audioData)
    QuestionText = r.recognize_google(audioData)
    return QuestionText


def wikipediaQ(wikiQuestion):
    wikiQuestion = wikiQuestion.lower()
    # Gets the wikipedia input and returns it in 2 sentences
    wikitext = wikipedia.summary(wikiQuestion, sentences=2)
    memoryStorageWrite(wikitext, wikiQuestion)
    # adds the answer to storage
    wikitext = "According to wikipedia, " + wikitext
    return wikitext


# __________________________MAIN-LOOP_________________________________________


def mainline():
    QuestionAsked = e1.get()
    # this is just to check to make sure that the command isnt just `exit`
    if QuestionAsked == "exit":
        sys.exit()
    tryfail = 0
    QuestionAsked = QuestionAsked.upper()
    checkanswerfromverify = verifyAnswer(QuestionAsked, False)
    # This will try to see if the command is answerable by wolframalpha and/or wikipedia
    try:
        finalAnswer = callWolf(QuestionAsked)
        Memoryx.Output(finalAnswer)
        tryfail += 1
    except:
        finalAnswer = wikipediaQ(QuestionAsked)
        Memoryx.Output(finalAnswer)
        tryfail += 1
    if tryfail == 0:
        if checkanswerfromverify == True:
            pass
        elif checkanswerfromverify == False:
            Memoryx.Output("I could not find an answer to that")

    # Too Repeat dont delete this

# --------------------------Code------------------------------------------


internetonoff = internet_check(1)
if internetonoff == False:
    offlinemode = True
else:
    offlinemode = False

Memoryx.Output("ready")


master = Tk()
Label(master, text="Command:").grid(row=0)
master.geometry("400x200")
e1 = Entry(master)
e1.grid(row=0, column=1)
Button(master, text='Exit', command=master.quit).grid(
    row=3, column=0, sticky=W, pady=4)
Button(master, text='Send', command=mainline).grid(
    row=3, column=1, sticky=W, pady=4)
# Button(master, text='Voice', command=Recognize).grid(
#   row=3, column=2, sticky=W, pady=4)

mainloop()
