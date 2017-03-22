import numpy as np 

def game_on(grid):
	if min(np.sum(grid,axis=0))==-3 or min(np.sum(grid,axis=1))==-3 or np.trace(grid)==-3 or np.trace(grid[::-1])==-3:
		print('Player 2 wins')
		return False
	if max(np.sum(grid,axis=0))==3 or max(np.sum(grid,axis=1))==3 or np.trace(grid)==3 or np.trace(grid[::-1])==3:
		print('Player 1 wins')
		return False
	if np.any(grid == 0) == False:
		print('It\'s a draw!')
		return False
	return True


grid = np.zeros((3,3)) #initial grid. 0 in unfilled grids.
icounter = 1
who = 1

while game_on(grid):
	who = icounter%2
	print('Player ' + str(2-who) +', your move: ')
	while True: 
		try:
			r,c = map(int,input().strip())
			break
		except:
			print('Wrong input. Try again!')

	while grid[r-1,c-1]!= 0:
		print('Cheater! Enter in an empty place: ')
		r,c = map(int,input().strip())

	grid[r-1,c-1] = (-1)**(who+1)
	print(grid)
	icounter+=1