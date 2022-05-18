from tkinter import *

class Maker:
	@classmethod
	def create_board(cls, board=None):
		if board is None:
			board = [['' for i in range(1, 10)] for i in range(1, 10)]

		cls.root = Tk()
		cls.root.title('Sudoku Puzzle Creator')
		cls.root.geometry('305x320')

		cls.board = board

		cls.e = {}

		label0_0 = Label(cls.root, bg = 'BLACK')
		label0_0.grid(row=0,column=0,padx=(2,0))
		if type(board[0][0]) == int:
			cls.e[(0,0)] = Label(label0_0, text = f'{board[0][0]}', width = 3)
		else:
			cls.e[(0,0)] = Entry(label0_0, width = 4)
		cls.e[(0,0)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[0][1]) == int:
			cls.e[(0,1)] = Label(label0_0, text = f'{board[0][1]}', width = 3)
		else:
			cls.e[(0,1)] = Entry(label0_0, width = 4)
		cls.e[(0,1)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[0][2]) == int:
			cls.e[(0,2)] = Label(label0_0, text = f'{board[0][2]}', width = 3)
		else:
			cls.e[(0,2)] = Entry(label0_0, width = 4)
		cls.e[(0,2)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[1][0]) == int:
			cls.e[(1,0)] = Label(label0_0, text = f'{board[1][0]}', width = 3)
		else:
			cls.e[(1,0)] = Entry(label0_0, width = 4)
		cls.e[(1,0)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[1][1]) == int:
			cls.e[(1,1)] = Label(label0_0, text = f'{board[1][1]}', width = 3)
		else:
			cls.e[(1,1)] = Entry(label0_0, width = 4)
		cls.e[(1,1)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[1][2]) == int:
			cls.e[(1,2)] = Label(label0_0, text = f'{board[1][2]}', width = 3)
		else:
			cls.e[(1,2)] = Entry(label0_0, width = 4)
		cls.e[(1,2)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[2][0]) == int:
			cls.e[(2,0)] = Label(label0_0, text = f'{board[2][0]}', width = 3)
		else:
			cls.e[(2,0)] = Entry(label0_0, width = 4)
		cls.e[(2,0)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[2][1]) == int:
			cls.e[(2,1)] = Label(label0_0, text = f'{board[2][1]}', width = 3)
		else:
			cls.e[(2,1)] = Entry(label0_0, width = 4)
		cls.e[(2,1)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[2][2]) == int:
			cls.e[(2,2)] = Label(label0_0, text = f'{board[2][2]}', width = 3)
		else:
			cls.e[(2,2)] = Entry(label0_0, width = 4)
		cls.e[(2,2)].grid(row=2,column=2,pady=2,padx=2)

		label0_1 = Label(cls.root, bg = 'BLACK')
		label0_1.grid(row=0,column=1)
		if type(board[0][3]) == int:
			cls.e[(0,3)] = Label(label0_1, text = f'{board[0][3]}', width = 3)
		else:
			cls.e[(0,3)] = Entry(label0_1, width = 4)
		cls.e[(0,3)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[0][4]) == int:
			cls.e[(0,4)] = Label(label0_1, text = f'{board[0][4]}', width = 3)
		else:
			cls.e[(0,4)] = Entry(label0_1, width = 4)
		cls.e[(0,4)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[0][5]) == int:
			cls.e[(0,5)] = Label(label0_1, text = f'{board[0][5]}', width = 3)
		else:
			cls.e[(0,5)] = Entry(label0_1, width = 4)
		cls.e[(0,5)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[1][3]) == int:
			cls.e[(1,3)] = Label(label0_1, text = f'{board[1][3]}', width = 3)
		else:
			cls.e[(1,3)] = Entry(label0_1, width = 4)
		cls.e[(1,3)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[1][4]) == int:
			cls.e[(1,4)] = Label(label0_1, text = f'{board[1][4]}', width = 3)
		else:
			cls.e[(1,4)] = Entry(label0_1, width = 4)
		cls.e[(1,4)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[1][5]) == int:
			cls.e[(1,5)] = Label(label0_1, text = f'{board[1][5]}', width = 3)
		else:
			cls.e[(1,5)] = Entry(label0_1, width = 4)
		cls.e[(1,5)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[2][3]) == int:
			cls.e[(2,3)] = Label(label0_1, text = f'{board[2][3]}', width = 3)
		else:
			cls.e[(2,3)] = Entry(label0_1, width = 4)
		cls.e[(2,3)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[2][4]) == int:
			cls.e[(2,4)] = Label(label0_1, text = f'{board[2][4]}', width = 3)
		else:
			cls.e[(2,4)] = Entry(label0_1, width = 4)
		cls.e[(2,4)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[2][5]) == int:
			cls.e[(2,5)] = Label(label0_1, text = f'{board[2][5]}', width = 3)
		else:
			cls.e[(2,5)] = Entry(label0_1, width = 4)
		cls.e[(2,5)].grid(row=2,column=2,pady=2,padx=2)

		label0_2 = Label(cls.root, bg = 'BLACK')
		label0_2.grid(row=0,column=2)
		if type(board[0][6]) == int:
			cls.e[(0,6)] = Label(label0_2, text = f'{board[0][6]}', width = 3)
		else:
			cls.e[(0,6)] = Entry(label0_2, width = 4)
		cls.e[(0,6)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[0][7]) == int:
			cls.e[(0,7)] = Label(label0_2, text = f'{board[0][7]}', width = 3)
		else:
			cls.e[(0,7)] = Entry(label0_2, width = 4)
		cls.e[(0,7)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[0][8]) == int:
			cls.e[(0,8)] = Label(label0_2, text = f'{board[0][8]}', width = 3)
		else:
			cls.e[(0,8)] = Entry(label0_2, width = 4)
		cls.e[(0,8)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[1][6]) == int:
			cls.e[(1,6)] = Label(label0_2, text = f'{board[1][6]}', width = 3)
		else:
			cls.e[(1,6)] = Entry(label0_2, width = 4)
		cls.e[(1,6)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[1][7]) == int:
			cls.e[(1,7)] = Label(label0_2, text = f'{board[1][7]}', width = 3)
		else:
			cls.e[(1,7)] = Entry(label0_2, width = 4)
		cls.e[(1,7)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[1][8]) == int:
			cls.e[(1,8)] = Label(label0_2, text = f'{board[1][8]}', width = 3)
		else:
			cls.e[(1,8)] = Entry(label0_2, width = 4)
		cls.e[(1,8)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[2][6]) == int:
			cls.e[(2,6)] = Label(label0_2, text = f'{board[2][6]}', width = 3)
		else:
			cls.e[(2,6)] = Entry(label0_2, width = 4)
		cls.e[(2,6)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[2][7]) == int:
			cls.e[(2,7)] = Label(label0_2, text = f'{board[2][7]}', width = 3)
		else:
			cls.e[(2,7)] = Entry(label0_2, width = 4)
		cls.e[(2,7)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[2][8]) == int:
			cls.e[(2,8)] = Label(label0_2, text = f'{board[2][8]}', width = 3)
		else:
			cls.e[(2,8)] = Entry(label0_2, width = 4)
		cls.e[(2,8)].grid(row=2,column=2,pady=2,padx=2)

		label1_0 = Label(cls.root, bg = 'BLACK')
		label1_0.grid(row=1,column=0,padx=(2,0))
		if type(board[3][0]) == int:
			cls.e[(3,0)] = Label(label1_0, text = f'{board[3][0]}', width = 3)
		else:
			cls.e[(3,0)] = Entry(label1_0, width = 4)
		cls.e[(3,0)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[3][1]) == int:
			cls.e[(3,1)] = Label(label1_0, text = f'{board[3][1]}', width = 3)
		else:
			cls.e[(3,1)] = Entry(label1_0, width = 4)
		cls.e[(3,1)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[3][2]) == int:
			cls.e[(3,2)] = Label(label1_0, text = f'{board[3][2]}', width = 3)
		else:
			cls.e[(3,2)] = Entry(label1_0, width = 4)
		cls.e[(3,2)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[4][0]) == int:
			cls.e[(4,0)] = Label(label1_0, text = f'{board[4][0]}', width = 3)
		else:
			cls.e[(4,0)] = Entry(label1_0, width = 4)
		cls.e[(4,0)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[4][1]) == int:
			cls.e[(4,1)] = Label(label1_0, text = f'{board[4][1]}', width = 3)
		else:
			cls.e[(4,1)] = Entry(label1_0, width = 4)
		cls.e[(4,1)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[4][2]) == int:
			cls.e[(4,2)] = Label(label1_0, text = f'{board[4][2]}', width = 3)
		else:
			cls.e[(4,2)] = Entry(label1_0, width = 4)
		cls.e[(4,2)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[5][0]) == int:
			cls.e[(5,0)] = Label(label1_0, text = f'{board[5][0]}', width = 3)
		else:
			cls.e[(5,0)] = Entry(label1_0, width = 4)
		cls.e[(5,0)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[5][1]) == int:
			cls.e[(5,1)] = Label(label1_0, text = f'{board[5][1]}', width = 3)
		else:
			cls.e[(5,1)] = Entry(label1_0, width = 4)
		cls.e[(5,1)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[5][2]) == int:
			cls.e[(5,2)] = Label(label1_0, text = f'{board[5][2]}', width = 3)
		else:
			cls.e[(5,2)] = Entry(label1_0, width = 4)
		cls.e[(5,2)].grid(row=2,column=2,pady=2,padx=2)

		label1_1 = Label(cls.root, bg = 'BLACK')
		label1_1.grid(row=1,column=1)
		if type(board[3][3]) == int:
			cls.e[(3,3)] = Label(label1_1, text = f'{board[3][3]}', width = 3)
		else:
			cls.e[(3,3)] = Entry(label1_1, width = 4)
		cls.e[(3,3)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[3][4]) == int:
			cls.e[(3,4)] = Label(label1_1, text = f'{board[3][4]}', width = 3)
		else:
			cls.e[(3,4)] = Entry(label1_1, width = 4)
		cls.e[(3,4)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[3][5]) == int:
			cls.e[(3,5)] = Label(label1_1, text = f'{board[3][5]}', width = 3)
		else:
			cls.e[(3,5)] = Entry(label1_1, width = 4)
		cls.e[(3,5)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[4][3]) == int:
			cls.e[(4,3)] = Label(label1_1, text = f'{board[4][3]}', width = 3)
		else:
			cls.e[(4,3)] = Entry(label1_1, width = 4)
		cls.e[(4,3)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[4][4]) == int:
			cls.e[(4,4)] = Label(label1_1, text = f'{board[4][4]}', width = 3)
		else:
			cls.e[(4,4)] = Entry(label1_1, width = 4)
		cls.e[(4,4)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[4][5]) == int:
			cls.e[(4,5)] = Label(label1_1, text = f'{board[4][5]}', width = 3)
		else:
			cls.e[(4,5)] = Entry(label1_1, width = 4)
		cls.e[(4,5)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[5][3]) == int:
			cls.e[(5,3)] = Label(label1_1, text = f'{board[5][3]}', width = 3)
		else:
			cls.e[(5,3)] = Entry(label1_1, width = 4)
		cls.e[(5,3)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[5][4]) == int:
			cls.e[(5,4)] = Label(label1_1, text = f'{board[5][4]}', width = 3)
		else:
			cls.e[(5,4)] = Entry(label1_1, width = 4)
		cls.e[(5,4)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[5][5]) == int:
			cls.e[(5,5)] = Label(label1_1, text = f'{board[5][5]}', width = 3)
		else:
			cls.e[(5,5)] = Entry(label1_1, width = 4)
		cls.e[(5,5)].grid(row=2,column=2,pady=2,padx=2)

		label1_2 = Label(cls.root, bg = 'BLACK')
		label1_2.grid(row=1,column=2)
		if type(board[3][6]) == int:
			cls.e[(3,6)] = Label(label1_2, text = f'{board[3][6]}', width = 3)
		else:
			cls.e[(3,6)] = Entry(label1_2, width = 4)
		cls.e[(3,6)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[3][7]) == int:
			cls.e[(3,7)] = Label(label1_2, text = f'{board[3][7]}', width = 3)
		else:
			cls.e[(3,7)] = Entry(label1_2, width = 4)
		cls.e[(3,7)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[3][8]) == int:
			cls.e[(3,8)] = Label(label1_2, text = f'{board[3][8]}', width = 3)
		else:
			cls.e[(3,8)] = Entry(label1_2, width = 4)
		cls.e[(3,8)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[4][6]) == int:
			cls.e[(4,6)] = Label(label1_2, text = f'{board[4][6]}', width = 3)
		else:
			cls.e[(4,6)] = Entry(label1_2, width = 4)
		cls.e[(4,6)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[4][7]) == int:
			cls.e[(4,7)] = Label(label1_2, text = f'{board[4][7]}', width = 3)
		else:
			cls.e[(4,7)] = Entry(label1_2, width = 4)
		cls.e[(4,7)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[4][8]) == int:
			cls.e[(4,8)] = Label(label1_2, text = f'{board[4][8]}', width = 3)
		else:
			cls.e[(4,8)] = Entry(label1_2, width = 4)
		cls.e[(4,8)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[5][6]) == int:
			cls.e[(5,6)] = Label(label1_2, text = f'{board[5][6]}', width = 3)
		else:
			cls.e[(5,6)] = Entry(label1_2, width = 4)
		cls.e[(5,6)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[5][7]) == int:
			cls.e[(5,7)] = Label(label1_2, text = f'{board[5][7]}', width = 3)
		else:
			cls.e[(5,7)] = Entry(label1_2, width = 4)
		cls.e[(5,7)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[5][8]) == int:
			cls.e[(5,8)] = Label(label1_2, text = f'{board[5][8]}', width = 3)
		else:
			cls.e[(5,8)] = Entry(label1_2, width = 4)
		cls.e[(5,8)].grid(row=2,column=2,pady=2,padx=2)

		label2_0 = Label(cls.root, bg = 'BLACK')
		label2_0.grid(row=2,column=0,padx=(2,0))
		if type(board[6][0]) == int:
			cls.e[(6,0)] = Label(label2_0, text = f'{board[6][0]}', width = 3)
		else:
			cls.e[(6,0)] = Entry(label2_0, width = 4)
		cls.e[(6,0)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[6][1]) == int:
			cls.e[(6,1)] = Label(label2_0, text = f'{board[6][1]}', width = 3)
		else:
			cls.e[(6,1)] = Entry(label2_0, width = 4)
		cls.e[(6,1)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[6][2]) == int:
			cls.e[(6,2)] = Label(label2_0, text = f'{board[6][2]}', width = 3)
		else:
			cls.e[(6,2)] = Entry(label2_0, width = 4)
		cls.e[(6,2)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[7][0]) == int:
			cls.e[(7,0)] = Label(label2_0, text = f'{board[7][0]}', width = 3)
		else:
			cls.e[(7,0)] = Entry(label2_0, width = 4)
		cls.e[(7,0)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[7][1]) == int:
			cls.e[(7,1)] = Label(label2_0, text = f'{board[7][1]}', width = 3)
		else:
			cls.e[(7,1)] = Entry(label2_0, width = 4)
		cls.e[(7,1)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[7][2]) == int:
			cls.e[(7,2)] = Label(label2_0, text = f'{board[7][2]}', width = 3)
		else:
			cls.e[(7,2)] = Entry(label2_0, width = 4)
		cls.e[(7,2)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[8][0]) == int:
			cls.e[(8,0)] = Label(label2_0, text = f'{board[8][0]}', width = 3)
		else:
			cls.e[(8,0)] = Entry(label2_0, width = 4)
		cls.e[(8,0)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[8][1]) == int:
			cls.e[(8,1)] = Label(label2_0, text = f'{board[8][1]}', width = 3)
		else:
			cls.e[(8,1)] = Entry(label2_0, width = 4)
		cls.e[(8,1)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[8][2]) == int:
			cls.e[(8,2)] = Label(label2_0, text = f'{board[8][2]}', width = 3)
		else:
			cls.e[(8,2)] = Entry(label2_0, width = 4)
		cls.e[(8,2)].grid(row=2,column=2,pady=2,padx=2)

		label2_1 = Label(cls.root, bg = 'BLACK')
		label2_1.grid(row=2,column=1)
		if type(board[6][3]) == int:
			cls.e[(6,3)] = Label(label2_1, text = f'{board[6][3]}', width = 3)
		else:
			cls.e[(6,3)] = Entry(label2_1, width = 4)
		cls.e[(6,3)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[6][4]) == int:
			cls.e[(6,4)] = Label(label2_1, text = f'{board[6][4]}', width = 3)
		else:
			cls.e[(6,4)] = Entry(label2_1, width = 4)
		cls.e[(6,4)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[6][5]) == int:
			cls.e[(6,5)] = Label(label2_1, text = f'{board[6][5]}', width = 3)
		else:
			cls.e[(6,5)] = Entry(label2_1, width = 4)
		cls.e[(6,5)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[7][3]) == int:
			cls.e[(7,3)] = Label(label2_1, text = f'{board[7][3]}', width = 3)
		else:
			cls.e[(7,3)] = Entry(label2_1, width = 4)
		cls.e[(7,3)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[7][4]) == int:
			cls.e[(7,4)] = Label(label2_1, text = f'{board[7][4]}', width = 3)
		else:
			cls.e[(7,4)] = Entry(label2_1, width = 4)
		cls.e[(7,4)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[7][5]) == int:
			cls.e[(7,5)] = Label(label2_1, text = f'{board[7][5]}', width = 3)
		else:
			cls.e[(7,5)] = Entry(label2_1, width = 4)
		cls.e[(7,5)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[8][3]) == int:
			cls.e[(8,3)] = Label(label2_1, text = f'{board[8][3]}', width = 3)
		else:
			cls.e[(8,3)] = Entry(label2_1, width = 4)
		cls.e[(8,3)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[8][4]) == int:
			cls.e[(8,4)] = Label(label2_1, text = f'{board[8][4]}', width = 3)
		else:
			cls.e[(8,4)] = Entry(label2_1, width = 4)
		cls.e[(8,4)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[8][5]) == int:
			cls.e[(8,5)] = Label(label2_1, text = f'{board[8][5]}', width = 3)
		else:
			cls.e[(8,5)] = Entry(label2_1, width = 4)
		cls.e[(8,5)].grid(row=2,column=2,pady=2,padx=2)

		label2_2 = Label(cls.root, bg = 'BLACK')
		label2_2.grid(row=2,column=2)
		if type(board[6][6]) == int:
			cls.e[(6,6)] = Label(label2_2, text = f'{board[6][6]}', width = 3)
		else:
			cls.e[(6,6)] = Entry(label2_2, width = 4)
		cls.e[(6,6)].grid(row=0,column=0,pady=2,padx=2)
		if type(board[6][7]) == int:
			cls.e[(6,7)] = Label(label2_2, text = f'{board[6][7]}', width = 3)
		else:
			cls.e[(6,7)] = Entry(label2_2, width = 4)
		cls.e[(6,7)].grid(row=0,column=1,pady=2,padx=2)
		if type(board[6][8]) == int:
			cls.e[(6,8)] = Label(label2_2, text = f'{board[6][8]}', width = 3)
		else:
			cls.e[(6,8)] = Entry(label2_2, width = 4)
		cls.e[(6,8)].grid(row=0,column=2,pady=2,padx=2)
		if type(board[7][6]) == int:
			cls.e[(7,6)] = Label(label2_2, text = f'{board[7][6]}', width = 3)
		else:
			cls.e[(7,6)] = Entry(label2_2, width = 4)
		cls.e[(7,6)].grid(row=1,column=0,pady=2,padx=2)
		if type(board[7][7]) == int:
			cls.e[(7,7)] = Label(label2_2, text = f'{board[7][7]}', width = 3)
		else:
			cls.e[(7,7)] = Entry(label2_2, width = 4)
		cls.e[(7,7)].grid(row=1,column=1,pady=2,padx=2)
		if type(board[7][8]) == int:
			cls.e[(7,8)] = Label(label2_2, text = f'{board[7][8]}', width = 3)
		else:
			cls.e[(7,8)] = Entry(label2_2, width = 4)
		cls.e[(7,8)].grid(row=1,column=2,pady=2,padx=2)
		if type(board[8][6]) == int:
			cls.e[(8,6)] = Label(label2_2, text = f'{board[8][6]}', width = 3)
		else:
			cls.e[(8,6)] = Entry(label2_2, width = 4)
		cls.e[(8,6)].grid(row=2,column=0,pady=2,padx=2)
		if type(board[8][7]) == int:
			cls.e[(8,7)] = Label(label2_2, text = f'{board[8][7]}', width = 3)
		else:
			cls.e[(8,7)] = Entry(label2_2, width = 4)
		cls.e[(8,7)].grid(row=2,column=1,pady=2,padx=2)
		if type(board[8][8]) == int:
			cls.e[(8,8)] = Label(label2_2, text = f'{board[8][8]}', width = 3)
		else:
			cls.e[(8, 8)] = Entry(label2_2, width=4)
		cls.e[(8, 8)].grid(row=2, column=2, pady=2, padx=2)

		confirm_button = Button(cls.root, text='Confirm', command = cls.confirm)
		confirm_button.grid(row=3,column=0,columnspan=2,pady=4)

		difficulty_label = Label(cls.root,text='Set Difficulty')
		difficulty_label.grid(row=4,column=0,columnspan=2,pady=4)

		difficulty_scale = Scale(cls.root,from_=1,to=40,orient=HORIZONTAL)
		difficulty_scale.grid(row=4, column=1,columnspan=2,pady=4)

		confirm_button = Button(cls.root, text='Generate Sudoku', command=lambda: cls.generate_sudoku(difficulty_scale.get()))
		confirm_button.grid(row=3, column=1,columnspan=2,pady=4)

		cls.root.mainloop()

		return cls.board

	@classmethod
	def confirm(cls):
		# print(cls.e[(0,0)].get())
		for i in range(0, 9):
			for k in range(0, 9):
				try:
					if type(cls.board[i][k]) is int: # if there is already an int in the position don't change it
						pass
					elif cls.board[i][k] != None or cls.board[i][k] != '':
						cls.board[i][k] = int(cls.e[(i, k)].get())
				except:
					cls.board[i][k] = None

		cls.root.destroy()

	@classmethod
	def generate_sudoku(cls, difficulty):
		base = 3
		side = base * base

		# pattern for a baseline valid solution
		def pattern(r, c): return (base * (r % base) + r // base + c) % side

		# randomize rows, columns and numbers (of valid base pattern)
		from random import sample
		def shuffle(s): return sample(s, len(s))

		rBase = range(base)
		rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
		cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
		nums = shuffle(range(1, base * base + 1))

		# produce board using randomized baseline pattern
		board = [[nums[pattern(r, c)] for c in cols] for r in rows]

		squares = side * side
		empties = squares * 3 // 4 - (51 - difficulty)
		for p in sample(range(squares), empties):
			board[p // side][p % side] = None

		cls.root.destroy()
		cls.create_board(board)