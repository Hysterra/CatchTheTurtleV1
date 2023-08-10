import turtle
from random import randint
import time


#variables
apsis = 0
ordinat = 0
style = ('Arial', 30, 'normal')

score = 0
FONT = ('Arial', 30, 'normal')

second = 30
#funcs

def addScore(a,b):
    global score

    score = score + 1
    relocateTurtle()

def relocateTurtle():

    apsis = randint(-100, 100)
    ordinat = randint(-100, 100)
    target.hideturtle()
    target.goto(x=apsis, y=ordinat)
    target.showturtle()

'''
def pointer():
    points.clear()
    points.write(f"Points: {score}", font=style)
'''
def timeFUNC():
    global second
    second = second - 1
    time.sleep(1)
#screen codes
board = turtle.Screen()
board.title("Catch The Turtle 1.0")
board.bgcolor("light blue")

#score table
points = turtle.Turtle()
points.color("Black")
points.penup()
points.goto(-200, 250)
points.hideturtle()

#Turtle codes
target = turtle.Turtle()
target.penup()
target.shape(name="turtle")


#timer
count = turtle.Turtle()
count.penup()
count.goto(-100, 200)
count.hideturtle()






def playGame():
    global second

    while second >= 0:

        #skor kısmı
        target.onclick(addScore)
        points.clear()
        points.write(f"Points: {score}", font=style)

        '''        
        #turtle'ımızın rastgele hareket kısmı
        
        apsis = randint(-100,100)
        ordinat = randint(-100,100)
        target.hideturtle()
        target.goto(x=apsis, y=ordinat)
        target.showturtle()
        '''



        #zaman sayacı kısmı
        count.clear()
        count.write(f"Tıme: {second}", font=style)

        timeFUNC()



playGame()


#### COUNTDOWN ile score sayacı aynı anda yenileniyor. turtle'a basınca skor artmalı ve yeni turtle oluşmalı
#bu sırada sayaç otomatik olarak devam etmeli ve oyun sayaca bağlı olmalı

# bastığımda turtle yeniden oluşmalı

turtle.mainloop()