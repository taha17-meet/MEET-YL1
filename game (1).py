import meet 
cells =[]

x = 0
while x <10:
	a = {"radius":13 , "x":meet.get_random_x() , "y":meet.get_random_y() , "dx": 0.11 , "dy": 1 , "color": "black"}
	c= meet.create_cell(a)
	cells.append(c)
	x+=1


a = {"radius":13 , "x":0 , "y":0 , "dx": 0, "dy": 0 , "color": "black"}
user= meet.create_cell(a)
cells.append(user)
while True : 
	meet.move_cells(cells)
	for cell in cells:
		x=cell.xcor()
		y=cell.ycor()
		h= meet.get_screen_height()
		w = meet.get_screen_width()
		if (x>w or x<-w):
			cell.set_dx(-cell.get_dx())
		if (y>h or y<-h):
			cell.set_dy(-cell.get_dy())
	dx,dy = meet.get_user_direction(user)
	user.set_dx(dx)
	user.set_dy(dy)