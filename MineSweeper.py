#Name: Zabih Bilal

#Importing random lib for generating mine field
import random
#Declaration of Global Variables
GRIDSIZE = 0	#Size of grid for user
unr_lst = []	#2D list of Unrevealed Game board

def initMines():
#This function takes zero arguments and returns a grid (2D list)
#Randomly placed mines!
	lst = []	#Declaration of empty list
	#loops to make a 2D list with random mine placement
	for i in range (0,GRIDSIZE):
		lst.append([])
		for j in range (0,GRIDSIZE):
			val = random.randint(1,100) #For Random mine placement
			if val <= 10:
				new_val = "x"
			else:
				new_val = " "
			lst[i].append(new_val)
	#Returning a 2D list of mine_field to main
	return lst

def initBoard():
#This function takes zero arguments and returns a grid 
#Representing the player's game board!
	unre_board = []		#Declaration of empty list
	#loops to make a 2D list with unrevealed Spaces "#"
	for i in range (0,GRIDSIZE):
		unre_board.append([])
		for j in range (0,GRIDSIZE):
			unre_board[i].append("#")
	#Returning a 2D list of Unrevealed gameboard to main
	return unre_board
	
def displayBoard(x):
#This function takes a 2D grid representing the player's game board
#Prints it to the screen with correct orientation
	print(" |",end="")
	
	for i in range (len(x)):
		print (f"{i}",end="")
	print("")
	
	for i in range (len(x)+3):
		print ("-",end="")
	print("")
	
	for i in range (len(x)):
		print (f"{i}|",end="")
		for ele in x[i]:
			print(str(ele),end="")
		print("")

def countHiddenCells(x):
#This function takes a 2D grid of Game board
#Returns the number of cells in the board that are unrevealed "#"
	cnt = 0
	for i in range (len(x)):
		for ele in x[i]:
			if ele == '#':
				cnt += 1	
	return cnt
	
def countMines(x):
#This function takes a 2D grid representing the mine_field
#Returns the number of cells in the grid that contain mines!
	count = 0
	for i in range (len(x)):
		for ele in x[i]:
			if ele == 'x':
				count+=1
	return count

def isMineAt(minefield,ro,co):
#This function takes as arguments, mine_field, Row, Column
#Returns a Boolean Value for while loops 
	if ro < GRIDSIZE and ro>=0 and co < GRIDSIZE and co>=0:
			if minefield[ro][co] == 'x':
				return True
			return False
	else:
		return False
		
def countMinesAround(minefield,ro,co):
#This function takes as arguments, mine_field, Row, Column
#Returns the number of Adjecent mines of user_input
	cnt = 0
	#FOR ALL POSSIBLE TRUE VALUES!!!
	if isMineAt(minefield,ro-1,co-1):
		cnt += 1
	if isMineAt(minefield,ro-1,co):
		cnt += 1
	if isMineAt(minefield,ro-1,co+1):
		cnt += 1
	if isMineAt(minefield,ro,co-1):
		cnt += 1
	if isMineAt(minefield,ro,co+1):
		cnt += 1
	if isMineAt(minefield,ro+1,co-1):
		cnt += 1
	if isMineAt(minefield,ro+1,co):
		cnt += 1
	if isMineAt(minefield,ro+1,co+1):
		cnt += 1
	return cnt

def reveal(minefield,r,c):
#This function takes as arguments, mine_field, Row, Column
#function should reveal the selected cell on the user's gameboard	
	global GRIDSIZE
	global unr_lst
	#If user_inputs are within range return
	if r<0 or r>=GRIDSIZE or c<0 or c>=GRIDSIZE:
		return
	else:
		if unr_lst[r][c] == "#":
			numAdj = countMinesAround(minefield,r,c)
			#If Adjacent mines are 1 or more Update Place with int num 
			if numAdj >=1:
				unr_lst[r][c] = numAdj
			#else Call Function again (Recursion) 
			else:
				unr_lst[r][c] = " "
				reveal(minefield,r+1,c+1)
				reveal(minefield,r+1,c)
				reveal(minefield,r-1,c-1)
				reveal(minefield,r,c+1)
				reveal(minefield,r,c-1)
				reveal(minefield,r+1,c-1)
				reveal(minefield,r-1,c)
				reveal(minefield,r-1,c+1)

def main():
	global GRIDSIZE
	global unr_lst
	''' Declaration of variables for While loops'''
	loop = True
	x = True
	z = True
	k = True
	#Initializing variables for ints as counters
	ncnt = 0
	numofmines = 0
	
	#User_input for GridSize
	GRIDSIZE = int(input("Enter a GridSize: "))
	#Generate Mine_Field
	mine_field = initMines()
	#Generate Unrevealed Field 
	'''Game Board'''
	unr_lst = initBoard()
	'''Numer of Mines for comparison for wining msg'''
	numofmines = countMines(mine_field)
	
	#Loop for Inputs Till Player Loses or Wins !!!
	while loop == True:
		#Display GameBoard after every move
		displayBoard(unr_lst)
		unr_spaces = countHiddenCells(unr_lst)
		mines_left = countMines(mine_field)
		
		#Taking input from user in list for row and colum
		#user_input[0] = ROW ---------- user_input[1] = COL
		user_input = input("Select a cell (row,col) > ").split(",")
		
		'''Check if input is Valid'''
		while k == True:
		#Conditions for inValid Inputs
			if user_input[0]<'0' or user_input[1]<'0':
				print("Invalid Input")
				user_input = input("Select a cell (row,col) > ").split(",")
					
			elif user_input[0]>=str(GRIDSIZE) or user_input[1]>=str(GRIDSIZE) :
				print("Invalid Input")
				user_input = input("Select a cell (row,col) > ").split(",")
			
			elif len(user_input)==1 or len(user_input)==0 :
				print("Invalid Input")
				user_input = input("Select a cell (row,col) > ").split(",")
			else:
				break
				
		#Convert each str to int in list
		for x in user_input:
			x = int(x)
		
		#Check for adj mines to compare and replace values in game Board
		Adjmines = countMinesAround(mine_field,int(user_input[0]),int(user_input[1]))
		#If Bool true mine present end game else conti
		Boole = isMineAt(mine_field,int(user_input[0]),int(user_input[1]))
		if Boole == True:
			loop = False
			#'''GAMEEE OVERRRR'''
			# Reveals all mines of user hits one with Losing MSG!!
			for i in range (len(mine_field)):
				for j in range (len(mine_field)):
					if mine_field[i][j] != ' ':
						unr_lst[i][j]=mine_field[i][j]
			#Display Latest Game Board with all mines Revealed
			displayBoard(unr_lst)
			print("\nGame Lost with GRIDSIZE "+str(GRIDSIZE))
			print("GAME OVER!!!")	
		#'''Continue Game'''
		else:
			#if not a mine and Adj_mine more than 0 replace lst place with int
			if mine_field[int(user_input[0])][int(user_input[1])] != 'x' and Adjmines > 0:
				unr_lst[int(user_input[0])][int(user_input[1])]=Adjmines
			#else call recursive fn with while
			else:
				#True till user_input revealed space
				while z == True:	
					if unr_lst[int(user_input[0])][int(user_input[1])] != ' ':
						#Call the reveal function to check all adj cells and reveal them with 
						#spaces or ints
						reveal(mine_field,int(user_input[0]),int(user_input[1]))
						break
					#if Invalid input Keep looping z true
					else:
						print ("Place already Revealed!!!")
						user_input = list(input("Select a cell (row,col) > "))
						user_input.remove(',')
						'''Check if input is Valid'''
						while k == True:
						#Conditions for inValid Inputs
							if user_input[0]<'0' or user_input[1]<'0':
								print("Invalid Input")
								user_input = input("Select a cell (row,col) > ").split(",")
									
							elif user_input[0]>=str(GRIDSIZE) or user_input[1]>=str(GRIDSIZE) :
								print("Invalid Input")
								user_input = input("Select a cell (row,col) > ").split(",")
							
							elif len(user_input)==1 or len(user_input)==0 :
								print("Invalid Input")
								user_input = input("Select a cell (row,col) > ").split(",")

							else:
								break
						for i in range (len(user_input)):
							int(user_input[i])
						z=True
			#loop for checking unrevealed places "#" left on game board
			#increment counter			
			for i in range (len(unr_lst)):
				for j in range (len(unr_lst[i])):
					if unr_lst[i][j] == '#':
						ncnt+=1
			if ncnt == numofmines:		#if counter equal numofmines
				displayBoard(unr_lst)	#Player Wins!...... Display Latest Board
				print("You Win!!!")		#Wining Msg
				break					#End Game 'Break loop'	
			#else counter 0 and continue loop
			ncnt = 0
			loop = True

main()