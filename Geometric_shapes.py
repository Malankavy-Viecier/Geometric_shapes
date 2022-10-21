import turtle

turtle.reset()
for n in range(1, 5):
    turtle.forward(70)
    turtle.right(90)
#Square

turtle.up()
turtle.goto(90, 100)
turtle.down()
for n in range(1, 7):
    turtle.forward(70)
    turtle.right(60)
#Hexagon

turtle.up()
turtle.goto(-100, -60)
turtle.down()
for n in range(1, 4):
    turtle.forward(90)
    turtle.right(120)
#Triangle

turtle.up()
turtle.goto(-150, 145)
turtle.down()
for n in range(1, 13):
    turtle.forward(50)
    turtle.right(30)
#Dodecagon

turtle.up()
turtle.goto(80, -80)
turtle.down()
for n in range(1, 21):
    turtle.forward(30)
    turtle.right(18)
#Icosagon

