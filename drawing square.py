import turtle
def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle brad - Draws a square
    brad = turtle.Turtle()
    brad.fillcolor("#33cc8c")
    brad.shape("square")
    brad.speed(0)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    brad.forward(150)
    brad.right(90)
    brad.forward(150)
    for j in range(1,5):
        brad.right(90)
        brad.forward(300)
        
    #create turtle angie - draws circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    #create turtle zack - draws triangle
    #zack = turtle.Turtle()
    #zack.shape("circle")
    #zack.color("green")
    #zack.right(45)
    #zack.forward(200)
    #zack.right(135)
    #zack.forward(300)
    #zack.right(135)
    #zack.forward(200)
    
    
    window.exitonclick()

draw_art()
