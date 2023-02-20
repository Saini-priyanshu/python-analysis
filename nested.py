from turtle import*

speed('fastest')
pencolor('blue')
for i in range(8):
    pensize(6)
    fd(100)
    for i in range(8):
        pensize(3)
        fd(50)
        fillcolor('red')
        begin_fill()
        for i in range(8):
            pensize(1)
            fd(25)
            dot(10)
            rt(45)
        end_fill()
        lt(45)
    rt(45)    

hideturtle()
mainloop()