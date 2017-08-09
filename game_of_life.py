row = 3
col = 4
seeds = [[0,0], [1,2], [2,2], [1,3]]
rds = 10

def game_of_life(row, col, seeds, rds):
  grid = [[0 for i in range(col)] for j in range(row)]

  for seed in seeds:
	  if seed[0] <= len(grid) and seed[1] <= len(grid[0]):
		  grid[seed[0]][seed[1]] = 1

  for rd in range(rds):
	  print "Round : " + str(rd + 1)
	  print grid
	  temp_grid = [[0 for i in range(col)] for j in range(row)]

	  for i in range(row):
		  for j in range(col):
			  current_value = grid[i][j]
			  total = sum_of_neighbours(grid, i, j)
			  if total < 2:
				  temp_grid[i][j] = 0
			  elif current_value == 1 and total <= 3:
				  temp_grid[i][j] = grid[i][j]
			  elif current_value == 1 and total > 3:
				  temp_grid[i][j] = 0
			  elif current_value == 0 and total == 3:
				  temp_grid[i][j] = 1

	  grid = temp_grid


def sum_of_neighbours(grid, row, col):
  total = 0

  if row == 0 or row == len(grid):
	  i_range = 2
  else:
	  i_range = 3

  for i in range(i_range):
	  for j in range(3):

		  mod = ((col + j - 1 + len(grid[i])) % len(grid[i]))
		  if [row, col] != [i, mod]:
			  total += grid[i][mod]
  return total

game_of_life(row, col, seeds, rds)
