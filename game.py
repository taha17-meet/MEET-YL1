from meet import *
ball1 = {"radius": 10 ,"x" :-20, "y" :5 , "dy" :-0.50 , "dx" : -0.111 }
cells = []
circle1 = create_cell(ball1)
cells.append(circle1)
ball2 = {"radius": 25 ,"x" :-50, "y" :30, "dy" :0.50 , "dx" : 0.111 }
circle1 = create_cell(ball2)
cells.append(circle1)
ball3 = {"radius": 40 ,"x" :80, "y" :60, "dy" :0.50 , "dx" : 0.111 }
circle1 = create_cell(ball3)
cells.append(circle1)
ball4 = {"radius":55 ,"x" :140, "y" :90, "dy" :-0.50 , "dx" : -0.111 }
circle1 = create_cell(ball4)
cells.append(circle1)
ball5 = {"radius": 70 ,"x" :180, "y" :120, "dy" :0.50 , "dx" : 0.111 }
circle1 = create_cell(ball5)
cells.append(circle1)
ball6 = {"radius": 85 ,"x" :-230, "y" :150, "dy" :-0.50 , "dx" : -0.111 }
circle1 = create_cell(ball6)
cells.append(circle1)
ball7 = {"radius": 100 ,"x" :270, "y" :180, "dy" :0.50 , "dx" : 0.111 }
circle1 = create_cell(ball7)
cells.append(circle1)
ball8 = {"radius": 115 ,"x" :-230, "y" :222, "dy" :-0.50 , "dx" : -0.111 }
circle1 = create_cell(ball8)
cells.append(circle1)

while (True):
	move_cells(cells)
