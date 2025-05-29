import random

empty = " "
wall = "█"

height = 61
width = 237

def move_cur(cursor, direction):
	if direction == "left":
		return [cursor[0]-2, cursor[1]]
	if direction == "right":
		return [cursor[0]+2, cursor[1]]
	if direction == "up":
		return [cursor[0], cursor[1]-2]
	if direction == "down":
		return [cursor[0], cursor[1]+2]
	
	raise Error("Not a valid direction")

def is_valid_cur(cursor):
	return cursor[0] >= 0 and cursor[0] < height and cursor[1] >= 0 and cursor[1] < width

def set_matrix_at(mat, cursor, value):
	mat[cursor[0]][cursor[1]] = value

def get_matrix_at(mat, cursor):
	return mat[cursor[0]][cursor[1]]

maze = []
for y in range(height):
	maze.append([])
	for x in range(width):
		maze[-1].append(wall)

cursor = (1, 1)
pos_stack = []
while True:
	directions = ["left", "right", "down", "up"]
	random.shuffle(directions)
	
	did_move = False
#	print(pos_stack)
	for dir in directions:
#		print(dir)
		new_cur = move_cur(cursor, dir)
		if is_valid_cur(new_cur) and get_matrix_at(maze, new_cur) == wall:
			middle_cur = [(cursor[0] + new_cur[0]) // 2, (cursor[1] + new_cur[1]) // 2]
			
			set_matrix_at(maze, new_cur, empty)
			set_matrix_at(maze, middle_cur, empty)
			
			pos_stack.append((cursor[0], cursor[1]))
			cursor = (new_cur[0], new_cur[1])
			did_move = True
			break
	
	if not did_move:
		if len(pos_stack) == 0:
			break
		
		cursor = [pos_stack[-1][0], pos_stack[-1][1]]
		del pos_stack[-1]

for row in maze:
	for cell in row:
		print(cell, end="")
	
	print("")