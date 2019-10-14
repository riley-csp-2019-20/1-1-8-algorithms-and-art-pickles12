import turtle as trtl
drawer = trtl.Turtle()

drawer.penup()
drawer.speed(0)
drawer.goto(0 ,-250)
drawer.pendown()
drawer.circle(300)
drawer.penup()
drawer.goto(0,50)
eyes = input("Would you like big eyes or small eyes? Type B for big and S for small")
color = input("Would you like green eyes for blue eyes? Type G for green and B for blue")

if color == "G":
    drawer.pencolor("green")
elif color == "B":
    drawer.pencolor("blue")
if eyes == "B":
    drawer.goto(125, 175)
    drawer.pensize(50)
    drawer.pendown()
    drawer.circle(1)
    drawer.penup()
    drawer.goto(-125,175)
    drawer.pendown()
    drawer.circle(1)
    drawer.pencolor("black")
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)


elif eyes == "S":
    drawer.goto(125, 175)
    drawer.pensize(5)
    drawer.pendown()
    drawer.circle(1)
    drawer.penup()
    drawer.goto(-125,175)
    drawer.pendown()
    drawer.circle(1)
    drawer.pencolor("black")
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)

eyebrows = input("Would you like big eyebrows or small eyebrows? Type B for big and S for small")

if eyebrows == "B":
    drawer.goto(50, 225)
    drawer.pensize(30)
    drawer.setheading(0)
    drawer.pendown()
    drawer.forward(125)
    drawer.penup()
    drawer.goto(-50,225)
    drawer.setheading(180)
    drawer.pendown()
    drawer.forward(125)
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)

elif eyebrows == "S":
    drawer.goto(50, 225)
    drawer.pensize(5)
    drawer.setheading(0)
    drawer.pendown()
    drawer.forward(125)
    drawer.penup()
    drawer.goto(-50,225)
    drawer.setheading(180)
    drawer.pendown()
    drawer.forward(125)
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)

nose = input("What size nose would you like? Type B for big and S for small.")

if nose == "B":
    drawer.setheading(180)
    drawer.pendown()
    drawer.pensize(10)
    drawer.forward(100)
    drawer.right(125)
    drawer.forward(150)
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)

elif nose == "S":
    drawer.setheading(180)
    drawer.pendown()
    drawer.pensize(5)
    drawer.forward(50)
    drawer.right(125)
    drawer.forward(75)
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)

mouth = input("Would you like a smile or no facial expression? Type S for smile and N for no smile")

if mouth == "S":
    drawer.goto(-100, -75)
    drawer.setheading(270)
    drawer.pendown()
    drawer.circle(100, 180)
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)

if mouth == "N":
    drawer.goto(100, -75)
    drawer.setheading(180)
    drawer.pendown()
    drawer.forward(200)
    drawer.penup()
    drawer.goto(0,50)
    drawer.pensize(1)
  
wn = trtl.Screen()
wn.mainloop()
