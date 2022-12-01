import turtle
import random

s = turtle.getscreen()
# t = turtle.Turtle()

#Moving the Turtle
# t.right(90)
# t.forward(100)
# t.left(90)
# t.backward(100)

#Moving the Turtle with Coordinates
# t.goto(100,100)
# t.home()

#Drawing a square
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)

#Drawing a rectangle
# t.fd(200)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(200)
# t.rt(90)
# t.fd(100)
# t.rt(90)

#Drawing Preset Figures
# t.circle(60)
# t.dot(20)

#Changing the Screen Color
# turtle.bgcolor('#F08080') #Light Coral

#Changing the Screen Title
turtle.title('The Python Turtle Race')

#Changing the Turtle Size
# t.shapesize(1,5,10)
# t.shapesize(10,5,1)
# t.shapesize(1,10,5)
# t.shapesize(10,1,5)
# t.shapesize(10,10,1)

#Changing the Pen Size
# t.pensize(5)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.pensize(1)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)

#Changing the Turtle and Pen Color
# t.shapesize(3,3,3)
# # t.fillcolor('red')
# # t.pencolor('green')
# t.color('green', 'red')
# t.pensize(10)
# t.forward(200)

#Filling in an Image
# t.begin_fill()
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.lt(120)
# t.fd(100)
# t.end_fill()

#Changing the Turtle Shape
# t.shape('circle')
# t.shape('arrow')
# t.shape('turtle')
# t.shape('classic')

#Changing the Pen Speed
# t.speed(1)
# t.fd(100)
# t.rt(90)
# t.speed(10)
# t.fd(100)

#Customizing in One Line
# t.pen(pencolor='blue', fillcolor='yellow', pensize=1, speed=1)
# t.begin_fill()
# t.circle(100)
# t.end_fill()

#Picking the Pen Up and Down
# t.fd(100)
# t.rt(90)
# t.penup()
# t.fd(100)
# t.rt(90)
# t.pendown()
# t.fd(100)
# t.rt(90)
# t.penup()
# t.fd(100)
# t.pendown()

#Undoing Changes
# t.circle(100)
# t.undo()

#CLearing the Screen
# t.clear()

#Resetting the Environment
# t.reset()

#Leaving a Stamp
# t.stamp()
# t.fd(100)
# t.stamp()
# t.fd(100)
# t.clearstamp(8)

#Cloning Your Turtle
# c = t.clone()
# t.color('magenta')
# c.color('cyan')
# t.circle(100)
# c.circle(50)

#Using Loops and Conditional Statements
# for i in range(4):
#     t.fd(100)
#     t.rt(90)

# n = 10
# while n <= 40:
#     t.circle(n)
#     n += 10

# u = input('Would you like me to draw a shape? Type yes or no: ')
# if u.lower() == 'yes':
#     t.circle(50)
# elif u.lower() == 'no':
#     print('Okay')
# else:
#     print('Invalid Reply')

#Final Project: The Python Turtle Race
#Setting up the Turtles and Homes
player_one = turtle.Turtle()
player_one.color('green')
player_one.shape('turtle')
player_one.penup()

player_two = player_one.clone()
player_two.color('blue')
player_two.penup()


player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

#Creating the Dice
dice = [1,2,3,4,5,6]

#Developing the Game
while True:
    if player_one.pos() >= (300,100):
        print('Player One wins!')
        break
    elif player_two.pos() >= (300,-100):
        print('Player Two wins!')
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the dice")
        dice_outcome =  random.choice(dice)
        print(f'The result of the dice roll is {dice_outcome}.So the number of steps will also be {20*dice_outcome}.')
        player_one.fd(20*dice_outcome)
        player_two_turn = input("Press 'Enter' to roll the dice")
        dice_outcome =  random.choice(dice)
        print(f'The result of the dice roll is {dice_outcome}. So the number of steps will also be {20*dice_outcome}.')
        player_two.fd(20*dice_outcome) 

turtle.done()