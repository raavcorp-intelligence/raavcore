# This is the Keyword program this is where all of the AI magic happens
# It goes thru the keywords trying to find if one matches the current criteria then it will assign it to a command
import random

# This is a list of attributes that will be described by keywords.
name = "raav"
age = "not aging"
job = "none"
color = "i do not have a color"
cando = "I can help you with tasks"
wordexit = ["EXIT", "EXIT PROGRAM", "EXIT NOW", "SHUT DOWN"]
wordhow = ["HOW ARE YOU", "WHATS UP", "WHAT'S UP", "WASSUP"]
replyhow = ["im doing fine", "im well thank you", "im good",
            "im as good as a virus taking over a computer", "i have no emotions"]

randomnumber = random.randint(1, 20)


class Keywordcall:
    def __init__(self):
        placeholder = True
        # So this is kinda like a analization program
        # It will break up each word and it will analize it
        # We need a condition that will dod something whether it is a who, what, where, why, and how keywords.

    def analyze(self, keypartword):
        keysplitword = keypartword.split(" ")
        print(keysplitword)
        print(keysplitword)
        print(keysplitword[1])
        if "is" in keysplitword:
            typeofquestion = "Boolean"
            if "is" == keysplitword[0]:
                if "the" == keysplitword[1]:
                    firstquestion = keysplitword[2]
        if "what" in keysplitword:
            typeofquestion = "string"
            if "what" == keysplitword[0]:
                if "can" == keysplitword[1]:
                    if "you" == keysplitword[2]:
                        if "do" == keysplitword[3]:
                            print(cando)

        # if "name" in keypartword:

    def specword(self, word, question):
        if word == "exit":
            if question.upper() in wordexit:
                return True
            else:
                return False
        if word == "what":
            if question.upper() in wordhow:
                return replyhow[randomnumber]
            else:
                return False
