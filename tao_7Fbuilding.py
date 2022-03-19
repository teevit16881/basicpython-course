import turtle
tao = turtle.Pen()#use tao as a pen
tao.shape('turtle')#change arrow to turtle icon

def building(floor = 7):
    '''this function is for drawing a n_floor building'''
    for i in range(floor):
        for j in range(2):
            tao.fd(170)
            tao.lt(90)
            tao.fd(50)
            tao.lt(90)
            j+=1
        tao.penup()
        tao.fd(10)
        tao.lt(90)
        tao.fd(10)
        tao.pendown()
        for k in range(4):
            tao.fd(30)
            tao.rt(90)
            tao.fd(30)
            tao.rt(90)
            tao.fd(30)
            tao.rt(90)
            tao.fd(30)
            tao.penup()
            tao.bk(40)
            tao.rt(90)
            tao.pendown()
            k+=1
        tao.penup()
        tao.fd(40)
        tao.rt(90)
        tao.bk(170)
        tao.pendown()
        i+=1

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(-85,-300)
building()
tao.penup()
tao.fd(230)
tao.lt(90)
tao.fd(70)
tao.pendown()
tao.circle(30)
