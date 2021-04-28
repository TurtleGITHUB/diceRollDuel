"""
Program: layoutdemo.py
Author: Robert 4/19/2021

*** Note: the file breezypythongui.py MUST be in the same directoty as this file for the application to work and MUST IMPORT pyttsx3.
"""

from breezypythongui import EasyFrame
from tkinter import *
import random
import pyttsx3




class DiceRoll(EasyFrame):
	"""Displays labels in quadrants of the frame."""

	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, title = "Dice Roll", width = 600, height = 400, background = "lightyellow")
		# 
		self.addLabel(text = "It's time to Duel!", row = 0,column = 2, font = "Arial", background = "lightgreen", sticky = "N")
		self.player1 = self.addLabel(text = "Player's Dice Roll", row = 2, column = 0, columnspan = 2, font = "Arial", background = "lightblue", sticky = "W")
		self.computer1 = self.addLabel(text = "Computer's Dice Roll", row = 2, column = 3, columnspan = 2, font = "Arial", background = "pink", sticky = "E")
		self.button = self.addButton(text = "Duel!", row = 3, column = 2, command = self.playGame)

		self.playerRoll = self.addIntegerField(value = 0, row = 3, column = 0, sticky = "S")
		self.computerRoll = self.addIntegerField(value = 0, row = 3, column = 3, sticky = "S")
		self.resultArea = self.addLabel(text = "", row = 4, column = 2, font = "Arial", background = "lightyellow")
	


	def playGame(self):
		"""Handles game event"""
		# input calculation
		playerRoll = random.randint(1, 20)
		computerRoll = random.randint(1, 20)
		result = ""
		

		if playerRoll > computerRoll:
			result = "Player Wins!"
			
			engine = pyttsx3.init()
			
			text = "You must be cheating!"
			engine.say(text)
			
			engine.runAndWait(2)

		elif playerRoll == computerRoll:
			result = "Its a Tie, play again!"
			
			engine = pyttsx3.init()
			
			text = "We Better play again"
			engine.say(text)
			
			engine.runAndWait()

		else: 
			playerRoll < computerRoll
			result = "Computer Wins!"

			engine = pyttsx3.init()
			
			text = "I won won won won"
			engine.say(text)
			
			engine.runAndWait()





		#output Phase
		self.playerRoll.setNumber(playerRoll)
		self.computerRoll.setNumber(computerRoll)
		self.resultArea["text"] = result





		



		





# Definition of the main() function for program entry
def main():
	"""Instantiates  and pops up the window."""
	DiceRoll().mainloop()

# Global call to the main() function
main()
		
