import turtle
import time

t= turtle.Turtle()

def curve():
    t.pen(pencolor="white",pensize=3, speed=7)
    for i in range(200):
        t.rt(1)
        t.fd(1)



def love_sign():
    t.pen(pencolor="white", fillcolor="hot pink", pensize=3 , speed=7)
    t.shape("turtle")
    t.shapesize(1,1,1)
    t.begin_fill()
    t.lt(50)
    t.fd(113)
    curve()
    t.fd(112)
    t.end_fill()
    t.hideturtle()



#window decoration

window= turtle.Screen()
window.bgcolor('black')
window.screensize(800,700)
window.setup(width=1.0, height=1.0 ,startx=None, starty=None)




t.penup()
t.goto(-80,300)
time.sleep(1)
t.pendown()
t.shapesize(1,2,1)



# Letter I

t.pen(pencolor="white", fillcolor="dark violet", pensize=3 , speed=9)


t.begin_fill()


t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)


# height of I

t.fd(140)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(160)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(140)
t.left(90)
t.rt(90)
t.fd(25)


t.end_fill()


#End of I




t.penup()
t.goto(-550,-20)
t.pendown()


#Draw 'LOVE'


t.pen(pencolor="white", fillcolor="dark violet", pensize=3 , speed=9)
t.begin_fill()



t.rt(90)
t.fd(25)
t.rt(90)
t.fd(165)
t.lt(90)
t.fd(115)
t.rt(90)
t.fd(25)
t.rt(90)
t.fd(140)
t.rt(90)
t.fd(190)
t.rt(90)

t.end_fill()


#end of 'L'


t.penup()
t.fd(140)


# gap b/w L AND O

t.fd(70)

# letter: 'O'

t.pen(pencolor="white", fillcolor="cyan", pensize=3 , speed=9)


t.begin_fill()


t.rt(90)
t.fd(190)
t.lt(90)
t.pendown()
t.circle(60)
t.lt(90)
t.penup()
t.fd(20)
t.rt(90)
t.pendown()
t.circle(40)
t.rt(90)
t.penup()
t.fd(20)
t.lt(90)



t.end_fill()


# end of 'O'



# gapb/w o and v

t.fd(100)
t.pendown()


# letter v

t.pen(pencolor="white", fillcolor="dark violet", pensize=3 , speed=9)


t.begin_fill()

t.lt(100)
t.fd(120)
t.rt(100)
t.fd(20)
t.rt(80)
t.fd(100)
t.lt(80)
t.fd(20)
t.lt(80)
t.fd(100)
t.rt(80)
t.fd(20)
t.rt(100)
t.fd(120)
t.rt(80)
t.fd(50)
t.lt(180)


t.end_fill()


# end of V

t.penup()



# gap b/w v and e

t.fd(100)
t.pendown()


# letter E

t.pen(pencolor="white", fillcolor="dark violet", pensize=3 , speed=9)

t.begin_fill()
t.lt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(60)
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(60)
t.rt(90)
t.fd(20)
t.rt(90)
t.fd(80)

t.end_fill()

# end of e

t.penup()
t.rt(180)

#gap b/w e and y

t.fd(200)
t.pendown()


# letter Y

t.pen(pencolor="white", fillcolor="dark violet", pensize=3 , speed=3)

t.begin_fill()


t.lt(90)
t.fd(50)
t.lt(30)
t.fd(80)
t.rt(120)
t.fd(20)
t.rt(60)
t.fd(60)
t.lt(180)
t.rt(60)
t.fd(60)
t.rt(60)
t.fd(20)
t.rt(120)
t.fd(80)
t.lt(30)
t.fd(50)
t.rt(90)
t.fd(20)
t.rt(180)

t.end_fill()


# end of Y

t.pendown()
t.fd(120)
t.pendown()