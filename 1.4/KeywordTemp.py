# This is a tempoary file for the keyword funtion
name = "raav"
age = "not aging"
job = "none"
color = "I do not have a color"
cando = "I can help you with tasks"

keypartword = "what can you do"

keysplitword = keypartword.split(" ")
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