'''
Progam: lottery.py
Author: Amit
Date: 9/20/19

Program will randomly generate five random numbers between 1-70, and one random
megaball number between 1-25.  Results will be displayed in fields'''


from breezypythongui import EasyFrame
import random

class Lottery(EasyFrame):
	''' Displays the result of a six randomly generated lotto numbers'''

	def __init__(self):
		''' Sets up the windo and the widgets'''
		EasyFrame.__init__(self, "Lucky Lottery Drawing", height = 250, width = 325, background = 'red')

		''' Crates the labels and integer fields'''
		self.title = self.addLabel(text = "Your Numbers are... ", row = 0, column = 1, columnspan = 3, sticky = "NSEW", background = 'red')
		self.first = self.addIntegerField(value = "", row = 1, column = 0)
		self.second = self.addIntegerField(value = "", row = 1, column = 1)
		self.third = self.addIntegerField(value = "", row = 1, column = 2)
		self.fourth = self.addIntegerField(value = "", row = 1, column = 3)
		self.fifth = self.addIntegerField(value = "", row = 1, column = 4)
		self.label = self.addLabel(text = "MegaBall Number: ", row = 2, column = 0, columnspan = 5, sticky = "NSEW", background = 'red')
		self.sixth = self.addIntegerField(value = "", row = 3, column =2)

		''' Creates button, and adds styling to text'''
		self.button = self.addButton(text = "Let's Play!", row = 4, column = 1, columnspan = 3, command = self.play)
		self.button["background"] = 'blue'
		self.button["foreground"] = 'white'
		self.title["font"] = 'Arial+Bold'
		self.label["font"] = 'Verdana+Bold'

	# Event handling method
	def play(self):

		lotto = []
		mega = []
		for x in range(0, 5):
			number = random.randint(1, 70)
			if number not in lotto:
				lotto.append(number)
			else:
				number = random.randint(1, 70)
				lotto.append(number)

		for x in range(0, 1):
			number2 = random.randint(1, 25)
			mega.append(number2)

		self.first.setValue(lotto[0])
		self.second.setValue(lotto[1])
		self.third.setValue(lotto[2])
		self.fourth.setValue(lotto[3])
		self.fifth.setValue(lotto[4])
		self.sixth.setValue(mega)

def main():
	Lottery().mainloop()

main()