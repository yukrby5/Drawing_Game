import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("#CDBF1D")
drawing_board.title("Python Turtle")



'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_istance_2 = turtle.Turtle()
turtle_istance_2.left(90)
turtle_istance_2.forward(100)
'''
#square

'''

kare_instance = turtle.Turtle()

for i in range(4):

  kare_instance.forward(50)
  kare_instance.left(90)
  
'''
'''
#star

turtle_instance = turtle.Turtle()
for i in range(25):
    turtle_instance.forward(100)
    turtle_instance.left(200)




turtle.done()
'''

#polygon

turtle_instance = turtle.Turtle() 
num_sides = 8
angle = 360.0/ num_sides
side_length = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()