#import and create turtle
import turtle as trtl
drawer = trtl.Turtle()

#change settings and create head
drawer.penup()
drawer.speed(0)
drawer.goto(0 ,-250)
drawer.pendown()
drawer.circle(300)
drawer.penup()
drawer.goto(0,50)
#creat variables for eyes using inputs
eyes = input("Would you like big eyes or small eyes? Type B for big and S for small")
color = input("Would you like green eyes for blue eyes? Type G for green and B for blue")
#use if statements to create color of eyes
if color == "G":
   drawer.pencolor("green")
   
elif color == "B":
   drawer.pencolor("blue")
#define couner
eyecounter1 = 0
#create eyes
if eyes == "B":
  drawer.goto(125, 175)
  while (eyecounter1 < 2):
    drawer.pensize(50)
    drawer.pendown()
    drawer.circle(1)
    drawer.penup()
    drawer.goto(-125,175)
    eyecounter1 += 1
  drawer.pencolor("black")
  drawer.penup()
  drawer.goto(0,50)
  drawer.pensize(1)
#define counter
eyecounter2 = 0
#create eyes
if eyes == "S":
  drawer.goto(125, 175)
  while (eyecounter2 < 2):
    drawer.pensize(5)
    drawer.pendown()
    drawer.circle(1)
    drawer.penup()
    drawer.goto(-125,175)
    eyecounter2 += 1
  drawer.pencolor("black")
  drawer.penup()
  drawer.goto(0,50)
  drawer.pensize(1)
#ask user for eyebrow choice
eyebrows = input("Would you like big eyebrows or small eyebrows? Type B for big and S for small")
#create eyebrows
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
#ask user for nose choice
nose = input("What size nose would you like? Type B for big and S for small.")
#create nose
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
#ask user for mouth choice
mouth = input("Would you like a smile or no facial expression? Type S for smile and N for no smile")
#create mouth
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
#end program
wn = trtl.Screen()
wn.mainloop()



