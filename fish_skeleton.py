from turtle import *
pensize(5)
pencolor('black')
speed(10)
#github

##鱼头
#鱼头轮廓:右开口抛物线公式x=(y**2)/2px
for y1 in list(range(0,54)):
    pd()
    goto((y1**2)/40,y1)
pu()
home()
for y2 in list(range(0,54)):
    #x=(y**2)/2px
    pd()
    goto((y2**2)/40,-y2)    
#鱼眼
pu()
goto(30,-6)
pd()
circle(6)

##鱼身
pu()
goto(50,0)
pd()
goto(300,0)
#鱼刺
for i in list(range(7)):
    x=75+35*i
    y=54-i**2
    pu()
    goto(x,y)
    pd()
    seth(-120)
    goto(x-25,0)
    lt(60)
    goto(x,-y)


##鱼尾
pu()
goto(300,0)
pd()
goto(360,50)
goto(330,0)
goto(360,-50)
goto(300,0)


hideturtle()
