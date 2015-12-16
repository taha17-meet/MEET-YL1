import meet
from meet import *
import random 
num_cells=0
colors = ["purple", "blue" , "green", "pink"]
cells = []
balls1={"radius": 20 , "x" : random.randint(0,100),"y":random.randint(0,100) , "dx": .3, "dy" : .2 , "color" : random. choice (colors)}
circle1 = create_cell(balls1)
cells.append(circle1)

while num_cells <30:
	balls = {'radius' :random.randint(20,60),'x':random.randint(-200,100),'y':random.randint(-200,100) ,'dx': random.random() , 'dy':random.random () , 'color' : random.choice(colors)}
	num_cells+=1
	circle = create_cell(balls)
	cells.append(circle)
	

user_cell={'radius':random.randint(20,60) ,'x':random.randint(-200,100),'y':random.randint(-200,100) ,'dx': random.randint(-10, 10) , 'dy':random.randint (-10,10) , 'color' : random.choice(colors)}
t=create_cell(user_cell)
cells.append(t)


def borders(cells):
	for cell in cells:
		width=get_screen_width()
		height=get_screen_height()
		x=cell.xcor()
		y=cell.ycor()
		if x > width :
			cell.set_dx(-cell.get_dx())
		if x < -width:
			cell.set_dx(-cell.get_dx())
		if y > height :
			cell.set_dy(-cell.get_dy())
		if y < -height:
			cell.set_dy(-cell.get_dy())

	

	

 

while(True):
	x,y = meet.get_user_direction(circle1)
	circle.set_dx(y)
	circle1.set_dy(x)
	borders(cells)
	move_cells(cells)
	dx,dy = get_user_direction(t)
	t.set_dx(dx)
	t.set_dy(dy)
	for cell2 in cells :
		x1=t.xcor()
		x2=cell2.xcor()
		y1=t.ycor()
		y2=cell2.ycor()
		radius1 = t.get_radius()
		radius2 = cell2.get_radius()
		z=y1-y2
		w=x1-x2	
		if ((w**2+z**2)**0.5) < (radius1+radius2):
			if (radius1>radius2):

				cell2.goto (meet.get_random_x() , (meet.get_random_y()))
				t.set_radius(radius1+ 0.008*radius2)

			






meet.mainloop()
