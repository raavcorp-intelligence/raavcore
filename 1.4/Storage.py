import pyttsx3
import os
import time
import sys


class Memory:
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
		
		QAtoget = ">>>" + QAtoget
		if QAtoget in x:
			#This is the indexing part `itemplacement` is the varable that shows what entry the question is on
			itemplacement = x.index(QAtoget)
			return itemplacement
		else:
			return False
	def findvalue(self, numlist, answer_memory_value):
		x1 = []
		#This is the file read in part where we see the memory that is stored
		filepathx2 = answer_memory_value
		with open(filepathx2) as fp:
			linex2 = fp.readline()
			count = 1
			while linex2:
				x1.append(linex2.strip())
				linex2 = fp.readline()
				count += 1
		#This is condesing the >>>QUESTION to just QUESTION
		numlist = numlist - 1
		returningvaluecondence = x1[numlist]
		memoryvaluecondeser = returningvaluecondence[3:len(returningvaluecondence)]
		return memoryvaluecondeser

	def Output(self, talktext):
		engine = pyttsx3.init()
		engine.say(talktext)
		engine.runAndWait()
		talktext = talktext + "\n"
		for c in talktext:
			sys.stdout.write(c)
			sys.stdout.flush()
			time.sleep(0.08)