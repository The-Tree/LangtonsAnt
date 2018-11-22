from tkinter import *


def left_mouse(event):
	if paused is True:
		if board[int(event.x/SPOT_LENGTH)][int(event.y/SPOT_LENGTH)] is 0:
			board[int(event.x/SPOT_LENGTH)][int(event.y/SPOT_LENGTH)] = 1
		elif board[int(event.x/SPOT_LENGTH)][int(event.y/SPOT_LENGTH)] is 1:
			board[int(event.x/SPOT_LENGTH)][int(event.y/SPOT_LENGTH)] = 0
		display_board()

	print("left mouse")
	return


def update_all():  # function that is called in tkinter.after()
	if paused is False:
		update_ant()
		update_board()
	elif paused is True:
		update_board()

	window.after(speed, update_all)

	print("update all")
	return


def play_ant():
	global paused
	paused = False

	print("play")
	return


def pause_ant():
	global paused
	paused = True

	print("pause")
	return


def slow_ant():
	global speed
	if speed is 2000:
		speed = 2000
	elif speed is 10:
		speed = 100
	else:
		speed += 100

	print("slow")
	return


def speed_ant():
	global speed
	if speed is 10:
		speed = 10
	elif speed is 100:
		speed = 10
	else:
		speed -= 100

	print("speed")
	return


def next_ant():
	if paused is True:
		update_ant()
		update_board()

	print("next")
	return


def clear_ant():
	global board, step, ant_dir, ant_y, ant_x
	if paused is True:
		step = 0
		ant_dir = ant_dir_start
		ant_y = ant_y_start
		ant_x = ant_x_start
		board = [[0 for y in range(0, BOARD_HEIGHT)] for x in range(0, BOARD_WIDTH)]
		display_board()

	print("clear")
	return


def display_board():
	global board_display
	x1 = 0
	y1 = 0
	x2 = SPOT_LENGTH
	y2 = SPOT_LENGTH

	for x in board:
		for y in x:
			if y is 0:  # empty
				canvas.delete(board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)])
				board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)] = \
					canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="grey")
			elif y is 1:  # filled
				canvas.delete(board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)])
				board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)] = \
					canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="black")

			if int(x1 / SPOT_LENGTH) is ant_x and int(y1 / SPOT_LENGTH) is ant_y:  # x1/20=board position and y1/20=board position
				if ant_dir is 0:
					canvas.delete(board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)])
					board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)] = \
						canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red")
				elif ant_dir is 1:
					canvas.delete(board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)])
					board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)] = \
						canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green")
				elif ant_dir is 2:
					canvas.delete(board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)])
					board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)] = \
						canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue")
				elif ant_dir is 3:
					canvas.delete(board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)])
					board_display[int(x1 / SPOT_LENGTH)][int(y1 / SPOT_LENGTH)] = \
						canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="purple")

			y1 += SPOT_LENGTH
			y2 += SPOT_LENGTH
		y1 = 0
		y2 = SPOT_LENGTH
		x1 += SPOT_LENGTH
		x2 += SPOT_LENGTH

	print("display board")
	return


def update_board():
	global board_display

	if ant_dir is 0:
		canvas.delete(board_display[ant_x][ant_y])
		board_display[ant_x][ant_y] = \
			canvas.create_rectangle(ant_x*SPOT_LENGTH, ant_y*SPOT_LENGTH,
									(ant_x+1)*SPOT_LENGTH, (ant_y+1)*SPOT_LENGTH,
									outline="black", fill="red")

		prev_y = (ant_y - 1) % BOARD_HEIGHT
		prev_x = ant_x
	elif ant_dir is 1:
		canvas.delete(board_display[ant_x][ant_y])
		board_display[ant_x][ant_y] = \
			canvas.create_rectangle(ant_x*SPOT_LENGTH, ant_y*SPOT_LENGTH,
									(ant_x+1)*SPOT_LENGTH, (ant_y+1)*SPOT_LENGTH,
									outline="black", fill="green")

		prev_y = ant_y
		prev_x = (ant_x - 1) % BOARD_WIDTH
	elif ant_dir is 2:
		canvas.delete(board_display[ant_x][ant_y])
		board_display[ant_x][ant_y] = \
			canvas.create_rectangle(ant_x*SPOT_LENGTH, ant_y*SPOT_LENGTH,
									(ant_x+1)*SPOT_LENGTH, (ant_y+1)*SPOT_LENGTH,
									outline="black", fill="blue")

		prev_y = (ant_y + 1) % BOARD_HEIGHT
		prev_x = ant_x
	elif ant_dir is 3:
		canvas.delete(board_display[ant_x][ant_y])
		board_display[ant_x][ant_y] = \
			canvas.create_rectangle(ant_x*SPOT_LENGTH, ant_y*SPOT_LENGTH,
									(ant_x+1)*SPOT_LENGTH, (ant_y+1)*SPOT_LENGTH,
									outline="black", fill="purple")

		prev_y = ant_y
		prev_x = (ant_x + 1) % BOARD_WIDTH

	if board[prev_x][prev_y] is 0:  # empty
		canvas.delete(board_display[prev_x][prev_y])
		board_display[prev_x][prev_y] = \
			canvas.create_rectangle(prev_x*SPOT_LENGTH, prev_y*SPOT_LENGTH,
									(prev_x+1)*SPOT_LENGTH, (prev_y+1)*SPOT_LENGTH,
									outline="black", fill="grey")
	elif board[prev_x][prev_y] is 1:  # filled
		canvas.delete(board_display[prev_x][prev_y])
		board_display[prev_x][prev_y] = \
			canvas.create_rectangle(prev_x*SPOT_LENGTH, prev_y*SPOT_LENGTH,
									(prev_x+1)*SPOT_LENGTH, (prev_y+1)*SPOT_LENGTH,
									outline="black", fill="black")

	print("update board")
	return


def update_ant():
	global ant_x, ant_y, ant_dir, step

	if board[ant_x][ant_y] is 0:
		board[ant_x][ant_y] = 1
		ant_dir = (ant_dir + 1) % 4
	elif board[ant_x][ant_y] is 1:
		board[ant_x][ant_y] = 0
		ant_dir = (ant_dir - 1) % 4

	if ant_dir is 0:  # up
		ant_y = (ant_y + 1) % BOARD_HEIGHT
	elif ant_dir is 1:  # right
		ant_x = (ant_x + 1) % BOARD_WIDTH
	elif ant_dir is 2:  # down
		ant_y = (ant_y - 1) % BOARD_HEIGHT
	elif ant_dir is 3:  # left
		ant_x = (ant_x - 1) % BOARD_WIDTH

	step += 1

	print("update ant")
	return


ant_x_start = 40
ant_y_start = 30
ant_dir_start = 0

ant_x = ant_x_start
ant_y = ant_y_start
ant_dir = ant_dir_start # 0=up 1=right 2=down 3=left

BOARD_WIDTH = 80
BOARD_HEIGHT = 60

SPOT_LENGTH = 10

board = [[0 for y in range(0, BOARD_HEIGHT)] for x in range(0, BOARD_WIDTH)]

window = Tk()

canvas = Canvas(window, width=BOARD_WIDTH*SPOT_LENGTH, height=BOARD_HEIGHT*SPOT_LENGTH, bg="white")
canvas.pack(side=TOP)

board_display = [[canvas.create_rectangle(0, 0, 0, 0) for y in range(0, BOARD_HEIGHT)] for x in range(0, BOARD_WIDTH)]

paused = True
speed = 100  # frames to wait to call after

step = 0  # which generation it is

play_b = Button(window, text="Play", command=play_ant)
play_b.pack(side=LEFT)
pause_b = Button(window, text="Pause", command=pause_ant)
pause_b.pack(side=LEFT)
slow_b = Button(window, text="Slow Down", command=slow_ant)
slow_b.pack(side=LEFT)
speed_b = Button(window, text="Speed Up", command=speed_ant)
speed_b.pack(side=LEFT)
next_b = Button(window, text="Next", command=next_ant)
next_b.pack(side=LEFT)
clear_b = Button(window, text="Clear", command=clear_ant)
clear_b.pack(side=LEFT)

display_board()

canvas.bind("<Button-1>", left_mouse)
window.after(0, update_all())
mainloop()

print("PROGRAM ENDED ON STEP: " + str(step))

print("")
print("fin~~~")
