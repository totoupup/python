from turtle import *
pensize(5)
speed(0)
##color('#F4A460')#橘黄
##color('#FFE4E1')#肉粉
#github

##【背景圆】
color('#B088FF')#浅紫
pu()
goto(0,-200)
pd()
begin_fill()
circle(200)
end_fill()


##定义画弧函数
def arc(initial_degree,range_num,step,rotate_degree):
    seth(initial_degree)
    for n in range(range_num):   
        fd(step)
        rt(rotate_degree)#    


##【图层1——面部轮廓】
#(81.13,15.94)
#(104.15,111.82)
color('#F4A460')#橘黄
#左耳
pu()
goto(-83.13,-10.94)
pd()
begin_fill()
arc(120,145,1,1/4)
goto(-30,50)
end_fill()

#右耳
pu()
goto(83.13,-10.94)#(88.13,10.94)
pd()
begin_fill()
arc(60,145,1,-1/4)
goto(30,50)
end_fill()

#腮
#右腮帮
pu()
goto(83.13,-10.94)#0
pd()
begin_fill()

#pencolor("green")
arc(-35,135,1,9/11)#1
print(pos())

#下巴
#pencolor("yellow")
arc(-145,70,1,3/10)#右半下颌2
print(pos())

#pencolor("red")
arc(-175,40,1,1/5)#下巴连接线3
print(pos())

#pencolor("pink")
arc(168,70,1,3/10)#左半下颌4
print(pos())

#左腮帮
#pencolor("grey")
arc(146,135,1,9/11)#5
print(pos())

#两耳连接
pu()
goto(-30,50)
arc(15,80,1,1/2)

end_fill()


##【图层2——耳部轮廓】
color('#FFC0CB')
#左耳
pu()
goto(-40,50)
pd()
begin_fill()

arc(-164,55,1,-7/8)

arc(120,100,1,1/3)#有疑问

goto(-40,50)

end_fill()

#右耳
print("耳朵打点")
pu()
goto(40,50)
pd()
begin_fill()

arc(-16,55,1,7/8)#(81.13,15.94)
print(pos())

arc(60,100,1,-1/3)#(104.15,111.82)
print(pos())

goto(40,50)

end_fill()

   
##图层3——眼部轮廓
pu()
goto(-80,0)

##图层4——鼻子轮廓
pu()
goto(10,54)
pd()
goto(-10,54)
color("white")
begin_fill()
arc(-90,150,1,1/9)
arc(-110,65,1,-1)
#setx(-xcor())
begin_fill()
goto(-xcor(),ycor())
goto(10,54)
goto(-10,54)
end_fill()
pu()
goto(10,54)
pd()
arc(-90,150,1,-1/9)
arc(-70,65,1,1)



end_fill()

hideturtle()
