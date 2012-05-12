# tic-tac-toe by zzatkin
import sys,random

board = []
players = []
wins = [[0,1,2],[0,3,6],[0,4,8],[1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]


for i in range(0,9):
	board.append("-")

def check_for_winner():
	for i in range(0,len(wins)):
		if board[wins[i][0]] != "-" and board[wins[i][1]] != "-" and board[wins[i][2]] != "-":
			if board[wins[i][0]] == board[wins[i][1]] and board[wins[i][1]] == board[wins[i][2]] and board[wins[i][2]] == board[wins[i][0]]:
				print_board()
				print board[wins[i][0]] + " has won the game!"
				exit(0)

def is_board_full():
	for i in range(0,9):
		if board[i] == "-":
			return False
	return True

def print_board():
	for i in range(0,9):
		sys.stdout.write(board[i])
		if (i + 1) % 3 == 0:
			sys.stdout.write("\n")

def start():
	print "Player 1: x or o? "
	selection = raw_input("> ")
	if selection == "x" or selection == "X":
		players.append("x")
		players.append("o")
		print "Okay. Player 2 will be o."
	elif selection == "o" or selection == "O":
		players.append("o")
		players.append("x")
		print "Okay. Player 2 will be x."
	else:
		print "Okay, I'll pick for you."
		random_letter = "x" if random.sample([0,1],1) == 0 else "o"
		players.append(random_letter)
		players.append(("o" if random_letter == "x" else "x"))
		print "Player 1 will be " + random_letter + ", and Player 2 will be " + ("o" if random_letter == "x" else "x") + "."
	print """
In this tic-tac-toe game, the board is laid out in such a way that you choose which location you want to place your move. This is how the board is defined to be:
	012
	345
	678
So, if you want to place your letter in the top-right corner, you want to type in the number "2" for your selection.

Have fun, and good luck!
"""
	current_player = 0 if random.sample([0,1],1) == 1 else 0
	while not is_board_full():
		print "Player " + str((current_player + 1)) + "'s (\"" + players[current_player] + "\") turn!"
		print_board()
		valid_input = False
		while not valid_input:
			location = raw_input("Choose a location: ")
			try:
				location = int(location)
			except:
				print "Invalid location. Please try again."
				continue
			if location < 0 or 9 <= location:
				print "Invalid location. Please try again."
				continue
			if board[location] == "x" or board[location] == "o":
				print "That location has already been taken. Please try again."
				continue
			board[location] = players[current_player]
			valid_input = True
		current_player ^= 1
		check_for_winner()

start()
