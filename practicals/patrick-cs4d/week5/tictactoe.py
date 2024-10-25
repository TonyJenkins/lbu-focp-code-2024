#!/usr/bin/env python3
def checkForWin(game_board) :
	if (game_board[0] == game_board[1]) and (game_board[1] == game_board[2]) and (game_board[0]!='_'): return True
	if (game_board[3] == game_board[4]) and (game_board[4] == game_board[5]) and (game_board[5]!='_'): return True
	if (game_board[6] == game_board[7] == game_board[8]) and game_board[8]!='_': return True
	if (game_board[0] == game_board[4] == game_board[8]) and game_board[0]!='_': return True
	if (game_board[2] == game_board[4] == game_board[6]) and game_board[6]!='_': return True
	return False

if __name__ == '__main__':
	player1 = input('Player 1 Name ')
	player2 = input('Player 2 Name ')

	game_board=['_']*9
	print(game_board[0] + '|'+ game_board[1] + '|' + game_board[2])
	print(game_board[3] + '|'+ game_board[4] + '|' + game_board[5])
	print(game_board[6] + '|'+ game_board[7] + '|' + game_board[8])
	turns = 0

	while True:
		pos = input(f'{player1 if turns%2==0 else player2 } enter any position you want from 0-8: \n')
		pos = int (pos)

		if game_board[pos] != '_': continue

		if(turns%2==0): game_board[pos]='X'
		else: game_board[pos]='O'

		print(game_board[0] + '|'+ game_board[1] + '|' + game_board[2])
		print(game_board[3] + '|'+ game_board[4] + '|' + game_board[5])
		print(game_board[6] + '|'+ game_board[7] + '|' + game_board[8])

		if checkForWin(game_board): break

		turns = turns + 1


	if (turns%2==0): print(f'{player1} wins!')
	else: print (f'{player2} wins!')



