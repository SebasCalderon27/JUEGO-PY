import turtle
import time
import random

posponer = 0.1

#MARCADOR
score = 0
high_score = 0

#CONFIGURACION DE VENTANA
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#CABEZA
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100) 

segmentos= []

#TEXTO
texto=turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("SCORE:0            HIGH SCORE: 0", align = "center", font = ("Courier", 24, "normal"))

#FUNCIONES
def arriba():
    cabeza.direction != "down"
    cabeza.direction = "up"
def abajo():
    cabeza.direction != "up"
    cabeza.direction = "down"
def izquierda():
    cabeza.direction != "right"
    cabeza.direction = "left"
def derecha():
    cabeza.direction != "left"
    cabeza.direction = "right" 

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#TECLADO
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
       
while True:
    wn.update()
    
    #COLISIONES BORDES
    if cabeza.xcor() > 280 or cabeza.xcor( ) < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        #ESCONDER SEGMENTOS
        for segmento in segmentos:
            segmento.goto (2000,2000)

        #LIMPIAR LISTA SEGMENTOS
        segmentos.clear()
        
        #RESET MARCADOR
        score = 0
        texto.clear()
        texto.write("SCORE:{}             HIGH SCORE:{}".format(score, high_score),
                align = "center", font = ("Courier", 24, "normal"))
        
    #COLISION CON COMIDA
    if cabeza.distance(comida) < 20:
        #MOVER LA COMIDA
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto (x,y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        #AUMENTAR MARCADOR
        score += 10
        
        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write("SCORE:{}             HIGH SCORE:{}".format(score, high_score),
                align = "center", font = ("Courier", 24, "normal"))
        
    #MOVER CUERPO DE SERPIENTE
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()
    
     #COLISIONES CON CUERPO
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #ESCONDER SEGMENTO
            for segmento in segmentos:
                segmento.goto(1000,1000)
            
            #BORRAR PARTES DE SERPIENTE
            segmentos.clear()
            
            #RESET MARCADOR
            score = 0
            texto.clear()
            texto.write("SCORE:{}             HIGH SCORE:{}".format(score, high_score),
                align = "center", font = ("Courier", 24, "normal"))
            
    time.sleep(posponer)  