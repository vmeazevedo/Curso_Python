import time
import turtle
from turtle import Turtle, Screen

t = turtle.Turtle()
turtle.title('Presente para o meu amor!')

screen = turtle.Screen()
screen.bgcolor("black")
# screen.bgpic('C:\\Python\\mjm.gif')

#Desenha o coração
t.color("white")
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(180)
t.circle(-90,200)
# left(120)
t.setheading(60)
t.circle(-90,200)
t.forward(180)
t.end_fill()
t.hideturtle()

#Texto principal
t.up()
t.goto(0,180)
t.down()
t.write('FELIZ ANIVERSÁRIO MEU AMOR!',False,'center', font=('Arial Narrow',18,'bold'))
time.sleep(3)

#Frases
t.up()
t.goto(0,-30)
t.down()
t.write('Oi meu amor, nessa data de hoje eu quero lhe lembrar da pessoa maravilhosa ',False,'center', font=('Arial Narrow',18,'bold'))
time.sleep(3)

t.up()
t.goto(0,-60)
t.down()
t.write('que você é para mim e o quão importante é em minha vida!',False,'center', font=('Arial Narrow',18,'bold'))
time.sleep(3)

t.up()
t.goto(0,-90)
t.down()
t.write('Desejo toda feliciadade do mundo para você meu bem! Um feliz aniversário!',False,'center', font=('Arial Narrow',18,'bold'))
time.sleep(3)

t.up()
t.goto(0,120)
t.down()
t.write('EU TE AMO!',False,'center', font=('Arial Narrow',40,'bold'))
time.sleep(3)

turtle.mainloop()