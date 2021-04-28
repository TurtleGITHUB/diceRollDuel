"""
Program: diceRoll.py
Author: Robert 4/19/2021

*** Note: the file breezypythongui.py MUST be in the same directoty as this file for the application to work and MUST IMPORT pyttsx3.
"""

from breezypythongui import EasyFrame
import random
import pyttsx3



class DiceRoll(EasyFrame):
	"""Displays labels in quadrants of the frame."""

	def __init__(self):
		"""Sets up the window and the label."""
		EasyFrame.__init__(self, title = "Dice Roll", width = 600, height = 400, background = "lightgreen")
		
		# 
		self.addLabel(text = "It's time to Duel!", row = 0, column = 2, columnspan = 1, background = "yellow", sticky = "NSEW").config(font = ("Arial Black", 12))

		self.player1 = self.addLabel(text = "Player's Dice Roll", row = 1, column = 0, columnspan = 1, background = "lightblue", sticky = "W").config(font = ("Arial Black", 10))
		
		self.computer1 = self.addLabel(text = "Computer's Dice Roll", row = 1, column = 3, columnspan = 1, background = "pink", sticky = "E").config(font = ("Arial Black", 10))
		
		self.button = self.addButton(text = "DUEL", row = 2, column = 2, command = self.playGame).config(font = ("Arial Black", 20))

		self.playerRoll = self.addIntegerField(value = 0, row = 2, column = 0, sticky = "N")
		
		self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 3, sticky = "N")
		
		self.resultArea = self.addLabel(text = "", row = 3, column = 2, background = "lightgreen", sticky = "S")
		self.resultArea.config(font = ("Arial Black", 12))


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
			
			engine.runAndWait()

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
		
