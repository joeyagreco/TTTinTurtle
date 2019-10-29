# 2019 Joey Greco
# 
# Tic-Tac-Toe using Turtle

import turtle

class Board():
	
	def __init__(self):
	
		# CONSTANTS:
		# length/height of 1 box in the board
		self.UNIT = 50
		# length of diagonal of 1 box in the board
		self.DIAGONAL_UNIT = 70
		# degrees to face up
		self.UP = 90
		# degrees to face left
		self.LEFT = 180
		# degrees to face down
		self.DOWN = 270
		# degrees to face right
		self.RIGHT = 360
		# degrees to face down and right
		self.DOWN_RIGHT = 315
		# degrees to face down and left
		self.DOWN_LEFT = 225
		# degrees to face up and right
		self.UP_RIGHT = 45
		# degrees to face up and left
		self.UP_LEFT = 135
		# font for updateBoardText()
		self.FONT = ("Arial", 22, "normal")
		# font alignment for updateBoardText()
		self.ALIGN = "center"
		
		# create turtle and screen
		self.t = turtle.Turtle()
		self.t.screen.setup(500, 500)
		self.t.hideturtle()
		self.t.penup()
		self.t.hideturtle()
		self.t.speed(0)
		self.t.color("black")
		self.t.pensize(5)
		self.t.shape("circle")
		
		# now draw the empty board
		# this x and y will draw board in center of screen
		self.t.setx(-25)
		self.t.sety(75)
		self.t.setheading(self.DOWN)
		self.t.pendown()
		self.t.forward(self.UNIT * 3)
		self.t.backward(self.UNIT)
		self.t.setheading(self.LEFT)
		self.t.forward(self.UNIT)
		self.t.backward(self.UNIT * 3)
		self.t.forward(self.UNIT)
		self.t.setheading(self.DOWN)
		self.t.forward(self.UNIT)
		self.t.setheading(self.UP)
		self.t.forward(self.UNIT * 3)
		self.t.backward(self.UNIT)
		self.t.setheading(self.RIGHT)
		self.t.forward(self.UNIT)
		self.t.backward(self.UNIT * 3)
		self.t.penup()
		
		
		# instance variables for core game 
		
		# array to hold the board
		# this will hold "X", "O", or "None" if the index is empty
		# by default, every index is empty
		self.arrBoard = [None] * 9
		
		# this will keep track of how many moves have been completed
		# it is used to determine if the game has tied
		# it is used in changeTurn()
		self.turnsCompleted = 0
		
		# this keeps track of whose turn it is
		# x will always go first
		# it is used in changeTurn()
		self.xTurn = True
		
		# this is set to True if the game ends in a tie
		# it is referenced by the updateBoardText() function
		self.tie = False
		
		# this is set to True when the drawVictoryLine() method is called
		# it is referenced by the updateBoardText() function
		self.VLDrawn = False
		
		
		
		
		
	def setIndexCoordinates(self, index):
			
		# this sets the coordinates of this turtle
		# for the given index of a square on the board
		# index will be 1-9
		# this function will put the turtle in the top left corner of the given index
		
		if(index == 1):
			self.t.setx(-75.00)
			self.t.sety(75.00)
		elif(index == 2):
			self.t.setx(-25.00)
			self.t.sety(75.00)
		elif(index == 3):
			self.t.setx(25.00)
			self.t.sety(75.00)
		elif(index == 4):
			self.t.setx(-75.00)
			self.t.sety(25.00)
		elif(index == 5):
			self.t.setx(-25.00)
			self.t.sety(25.00)
		elif(index == 6):
			self.t.setx(25.00)
			self.t.sety(25.00)
		elif(index == 7):
			self.t.setx(-75.00)
			self.t.sety(-25.00)
		elif(index == 8):
			self.t.setx(-25.00)
			self.t.sety(-25.00)
		elif(index == 9):
			self.t.setx(25.00)
			self.t.sety(-25.00)
		else:
			print(index)
			raise ValueError("Value must be 1-9")
		
		
	def drawX(self, index):
	
		# this method will draw an x in the given square
		# square will be given as index 1-9
		
		# set coordinates
		self.setIndexCoordinates(index)
		
		# now draw X
		self.t.penup()
		self.t.color("red")
		self.t.setheading(self.DOWN_RIGHT)
		self.t.forward(10)
		self.t.pendown()
		self.t.forward(self.UNIT)
		self.t.penup()
		self.t.backward(self.UNIT + 10)
		self.t.setheading(self.RIGHT)
		self.t.forward(self.UNIT)
		self.t.setheading(self.DOWN_LEFT)
		self.t.forward(10)
		self.t.pendown()
		self.t.forward(self.UNIT)
		self.t.penup()
	

	def drawO(self, index):
	
		# this method will draw an O in the given square
		# square will be given as index 1-9
		
		# set coordinates
		self.setIndexCoordinates(index)
		
		# now draw O
		self.t.penup()
		self.t.color("blue")
		self.t.setheading(self.RIGHT)
		self.t.forward(self.UNIT/2)
		self.t.setheading(self.DOWN)
		self.t.forward(10)
		self.t.setheading(self.LEFT)
		self.t.pendown()
		self.t.circle(15)
		self.t.penup()

	
	def drawVictoryLine(self, startIndex, endIndex):
	
		# victory line will be drawn from startIndex to endIndex at the end of the game
		# these indices will be 1-9
		
		# slow drawing speed for effect
		self.t.speed(1)
		
		# draw victory line in gold
		self.t.color("gold")
		
		# make line thicker than x lines
		self.t.pensize(8)
		
		# set coordinates of starting index
		self.setIndexCoordinates(startIndex)
		
		# lift pen up
		self.t.penup()
		
		# check for where to draw line and draw it
		if(startIndex == 1 and endIndex == 9):
			# top left to bottom right
			self.t.setheading(self.DOWN_RIGHT)
			self.t.pendown()
			self.t.forward(self.DIAGONAL_UNIT * 3)
		elif(startIndex == 7 and endIndex == 3):
			# bottom left to top right
			self.t.setheading(self.DOWN)
			self.t.forward(self.UNIT)
			self.t.setheading(self.UP_RIGHT)
			self.t.pendown()
			self.t.forward(self.DIAGONAL_UNIT * 3)
		elif((startIndex == 1 and endIndex == 7) or (startIndex == 2 and endIndex == 8) or (startIndex == 3 and endIndex == 9)):
			# any top square to its bottom square
			self.t.setheading(self.RIGHT)
			self.t.forward(self.UNIT/2)
			self.t.setheading(self.DOWN)
			self.t.pendown()
			self.t.forward(self.UNIT * 3)
		elif((startIndex == 1 and endIndex == 3) or (startIndex == 4 and endIndex == 6) or (startIndex == 7 and endIndex == 9)):
			# any left square to its far right square
			self.t.setheading(self.DOWN)
			self.t.forward(self.UNIT/2)
			self.t.setheading(self.RIGHT)
			self.t.pendown()
			self.t.forward(self.UNIT * 3)
		elif(startIndex == endIndex):
			# this will draw when there is a tie
			
			# speed up drawing and change color to orange
			self.t.color("orange")
			self.t.speed(0)
			self.t.setheading(self.DOWN_RIGHT)
			
			# draw first line
			self.t.pendown()
			self.t.forward(self.DIAGONAL_UNIT * 3)
			self.t.penup()
			
			# reset coordinates for second line
			self.setIndexCoordinates(1)
			self.t.setheading(self.DOWN)
			self.t.forward(self.UNIT * 3)
			
			# draw second line
			self.t.pendown()
			self.t.setheading(self.UP_RIGHT)
			self.t.pendown()
			self.t.forward(self.DIAGONAL_UNIT * 3)
		else:
			print(startIndex + " ," + endIndex)
			raise ValueError("Not valid values for indices")
			
		# lift pen and make drawing speed fast again	
		self.t.penup()
		self.t.speed(0)
		
		# set variable to let object know this function has been called
		self.VLDrawn = True
		
	
	def updateBoard(self, index, isX):
		
		# this function draws an X or O on the given index
		# isX is a boolean letting us know if we are drawing an X or an O
		
		# first, check if X or O
		# then draw on the board
		# and add to array
		if(isX):
			self.drawX(index)
			self.arrBoard[index - 1] = 'X'
		else:
			self.drawO(index)
			self.arrBoard[index - 1] = 'O'
	

	def updateBoardText(self):
		
		# this updates the text underneath the board 
		# throughout the game
		
		# first, clear any text there already
		self.eraseBoardText()
		
		print(self.t.pos())
		
		# check first if the game is over
		# if it is, we must display the outcome in the bottom text
		if(self.VLDrawn):
			
			# reset coordinates since calling gameOver() moves them
			self.setIndexCoordinates(8)
			self.t.setx(self.t.position()[0] + 25)
			self.t.sety(self.t.position()[1] - self.UNIT * 2)
			
			# check if the game ended in a tie
			if(self.tie):
				# write text for tie
				self.t.color("orange")
				self.t.pendown()
				self.t.write("Tie!", False, align = self.ALIGN, font = self.FONT)
				self.t.penup()
			elif(not self.xTurn):
				# write text for X win
				self.t.color("red")
				self.t.pendown()
				self.t.write("X Wins!", False, align = self.ALIGN, font = self.FONT)
				self.t.penup()
			else:
				# write text for O win
				self.t.color("blue")
				self.t.pendown()
				self.t.write("O Wins!", False, align = self.ALIGN, font = self.FONT)
				self.t.penup()
			# return so we dont display the turn text below
			return
		
		# set to correct starting coordinates to write text
		self.setIndexCoordinates(8)
		self.t.setx(self.t.position()[0] + 25)
		self.t.sety(self.t.position()[1] - self.UNIT * 2)
		
		# this gets updated before every turn		
		# check whos turn it is
		if(self.xTurn):
			# write text for X turn
			self.t.color("red")
			self.t.pendown()
			self.t.write("X Turn", False, align = self.ALIGN, font = self.FONT)
			self.t.penup()
		else:
			# write text for O turn
			self.t.color("blue")
			self.t.pendown()
			self.t.write("O Turn", False, align = self.ALIGN, font = self.FONT)
			self.t.penup()
		


	def eraseBoardText(self):
		
		# this is a helper function for updateBoardText()
		# it erases any text by drawing an opaque rectangle over it
			
		# set to correct starting coordinates to draw rectangle
		self.setIndexCoordinates(7)
		self.t.sety(self.t.position()[1] - self.UNIT * 2)
		
		# now, draw opaque rectangle
		self.t.color("white")
		self.t.begin_fill()
		self.t.setheading(self.RIGHT)
		self.t.pendown()
		self.t.forward(self.UNIT * 3)
		self.t.setheading(self.UP)
		self.t.forward(40)
		self.t.setheading(self.LEFT)
		self.t.forward(self.UNIT * 3)
		self.t.setheading(self.DOWN)
		self.t.forward(40)
		self.t.end_fill()	
		self.t.penup()
		
	def changeTurn(self):
		
		# this function changes the turn to X if it is O's turn
		# and O if it is X's turn
		# it also keeps track of how many turns have been completed
		
		# increment turn count and change turn
		self.turnsCompleted += 1
		self.xTurn = (not self.xTurn)
		
		
	def reachedMaxTurns(self):
		
		# this function keeps track of how many turns have been completed
		# and returns false once 8 turns have been completed
		# if the change of turn CAN be completed, this returns True
		
		# check turn count
		if(self.turnsCompleted >= 9):
			# then no more turns can be started, the game is over
			return True
		return False	
	

	def getMove(self):
		
		# this function gets an index from the player
		# and returns it
		
		# loop until player gives a valid move
		while True:
			# get move from player
			move = int(input("\nWhere would you like to go? (1-9): "))
			# check if the move is valid and in range
			if(move >= 1 and move <= 9 and self.arrBoard[move-1] == None):
				# return the move from the player
				# this will be 1-9
				return move
			else:
				print("\nInvalid Placement.")
			
			
	def gameOver(self):
		
		# this function check if the game is over
		# it returns True if it is
		
		# first check for a winner
		if(self.arrBoard[0] == self.arrBoard[1] and self.arrBoard[1] == self.arrBoard[2] and self.arrBoard[0] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(1,3)
			return True
		elif(self.arrBoard[3] == self.arrBoard[4] and self.arrBoard[4] == self.arrBoard[5] and self.arrBoard[3] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(4,6)
			return True
		elif(self.arrBoard[6] == self.arrBoard[7] and self.arrBoard[7] == self.arrBoard[8] and self.arrBoard[6] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(7,9)
			return True
		elif(self.arrBoard[0] == self.arrBoard[3] and self.arrBoard[3] == self.arrBoard[6] and self.arrBoard[0] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(1,7)
			return True
		elif(self.arrBoard[1] == self.arrBoard[4] and self.arrBoard[4] == self.arrBoard[7] and self.arrBoard[1] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(2, 8)
			return True
		elif(self.arrBoard[2] == self.arrBoard[5] and self.arrBoard[5] == self.arrBoard[8] and self.arrBoard[2] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(3,9)
			return True
		elif(self.arrBoard[0] == self.arrBoard[4] and self.arrBoard[4] == self.arrBoard[8] and self.arrBoard[0] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(1,9)
			return True
		elif(self.arrBoard[2] == self.arrBoard[4] and self.arrBoard[4] == self.arrBoard[6] and self.arrBoard[2] != None):
			# erase text before victory line is drawn
			self.eraseBoardText()
			self.drawVictoryLine(7,3)
			return True
		# now check	for tie
		elif(self.reachedMaxTurns()):
			print("\nTie!")
			# update tie reference variable
			self.tie = True
			# erase text before tie lines are drawn
			self.eraseBoardText()
			self.drawVictoryLine(1,1)
			return True;
		else:
			return False
		
	
	def play(self):
		
		# this function runs the game
		# this will loop until gameOver() returns True
		while True:
			# call function to display text under board
			self.updateBoardText()
			
			# check whose turn it is and draws X or O in index accordingly
			if(self.xTurn):
				self.updateBoard(self.getMove(), self.xTurn)
			else:
				self.updateBoard(self.getMove(), self.xTurn)
			
			# now change whose turn it is
			self.changeTurn()
			
			# now check if a game-ending condition has been met
			print(self.turnsCompleted)
			if(self.gameOver()):
				# call function again to show outcome on board
				self.updateBoardText()
				print("Game Over")
				turtle.done()
				break
			
# create and play the game			
b = Board()	
b.play()




	
