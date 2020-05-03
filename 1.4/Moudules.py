import pyttsx3
import os
import time
import sys
import speech_recognition as SR
import pyaudio
import datetime
# Defintion of Mic

# mic.list_microphone_names()
loglocation = "log.raavlog"


def logfiles(logentry):
    global log
    log = []
    logentry.replace("\n", " ")
    timenow = datetime.datetime.now()
    logfinalvalue = ">>> Command: " + logentry + " at " + str(timenow)
    filelog = open(loglocation, "a")
    filelog.write(logfinalvalue)
    filelog.write("\n")
    filelog.close()


class Helpers:
    # This calss is the memory reading and indexing part
    def __init__(self):
        placeholder = True

    def getx(self, QAtoget, question_memory_value):
        filepathx1 = question_memory_value
        # The try checks to see if the Question Exists
        try:
            open(filepathx1)
        except ValueError:
            open(filepathx1, "w+")
        x = []
        # This opens the Question file to get all of the saved values
        with open(filepathx1) as fp:
            linex1 = fp.readline()
            count = 1
            while linex1:
                x.append(linex1.strip())
                linex1 = fp.readline()
                count += 1
        QAtoget = QAtoget.upper()
        QAtoget = ">>>" + QAtoget
        logfiles("Searching Memory for: " + str(QAtoget))
        if QAtoget in x:
            # This is the indexing part `itemplacement` is the varable that shows what entry the question is on
            itemplacement = x.index(QAtoget)
            logfiles("Found: " + str(QAtoget) +
                     " In Memory at the: " + str(itemplacement) + " slot")
            return itemplacement
        else:
            logfiles("No Memory found for: " + str(QAtoget))
            return False

    def findvalue(self, numlist, answer_memory_value):
        x1 = []
        # This is the file read in part where we see the memory that is stored
        filepathx2 = answer_memory_value
        with open(filepathx2) as fp:
            linex2 = fp.readline()
            count = 1
            while linex2:
                x1.append(linex2.strip())
                linex2 = fp.readline()
                count += 1
        # This is condesing the >>>QUESTION to just QUESTION
        returningvaluecondence = x1[numlist]
        memoryvaluecondeser = returningvaluecondence[3:len(
            returningvaluecondence)]
        return memoryvaluecondeser

    def Output(self, talktext):
        engine = pyttsx3.init()
        engine.say(talktext)
        engine.runAndWait()
        talktext = str(talktext)
        talktext = talktext.lower()
        talktext = talktext + "\n"
        for c in talktext:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.03)

    def onlyMic(self, recognizer_source):
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


def Recognize(self, typeortalk):
    '''if typeortalk == True:
        with mic as source:
            audioData = r.listen(source)
        type(audioData)
        try:
            text = r.recognize_sphinx(audioData)
        except:
            return False
        print(text)
        if text[:4] == "Rave":
            xtemp = len(text)
            textToPass = text[5:xtemp]
            print("Starting with: " + textToPass)
            return textToPass
        else:
            return 0
    if typeortalk == False:
        textToPass = input("Command: ")'''
    placeholder = True


def FollowUp():
    '''with mic as source:
        audioData = r.listen(source)
    type(audioData)
    QuestionText = r.recognize_google(audioData)
    return QuestionText'''
    placeholder = True
