# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 22:26:58 2021

@author: Bryan
"""

import matplotlib.pyplot as plt
import numpy as np
from vpython import *
import math as math

shape=int(input('the shape of projectile(1:sphere, 2:square, 3:bullet)'))

#-----test-------
L=10 # 砲管長 單位:m 
r=5*(10)**(-2) #砲管半徑
D=15*(10)**(-2) #砲管間的距離(電樞的距離) 單位:m
dr=0.001 #一小段電樞 
I = float(input('輸入磁軌砲的電流')) #電流 單位:ampere
c=4*np.pi*(10)**(-7) #真空中的磁導率
m=1 #子彈的質量 單位:kg
F=0
t=0
dt=0.0001
n=int((D-2*r)/dr)
tt=[]
 
si = input('輸入磁軌砲的發射仰角(角度)')
si_r = math.radians((float(si)))
 
for i in range(n):
    dB = c*I/(2*np.pi*r)
    F += dr*I*dB
    r += dr


a=F/m
v0=0
g=9.8
vv=[]
n1=int(((2*L/(a-g*np.sin(si_r)))**0.5)/dt)

for i in range(n1):
    v = v0+(a-g*np.sin(si_r))*dt
    tt.append(t)
    vv.append(v)
    t += dt
    v0 = v
print('v(conductor) ',v, '(m/s)')
plt.grid()
plt.title('projectiles velocity change in railgun')
plt.plot(tt,vv)    
plt.show()


if shape == 1:
    #plt.title('air resistance(sphere)')
    cd1 = 0.5  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    
    scene = canvas(y=100,width=100,height=100)  
    wall=box(pos=vector(0,0,0),size=vector(1000,3,0.5))
    ball1=sphere(pos=vector(-500,0,0),radius=8,color=color.red, make_trail=True,label='conductor no resistance')
    ballorigin1=sphere(pos=vector(-500,0,0),radius=8)
    ball2=sphere(pos=vector(-500,0,0),radius=8,color=color.blue, make_trail=True,label='conductor resistance')
    ballorigin2=sphere(pos=vector(-500,0,0),radius=8)
    
    #scene2 = canvas(y=100,width=100,height=100)  
    #wall=box(pos=vector(0,0,0),size=vector(1000,3,0.5))   
    ball3=sphere(pos=vector(-500,0,0),radius=8,color=color.green, make_trail=True)
    ballorigin3=sphere(pos=vector(-500,0,0),radius=8)
    ball4=sphere(pos=vector(-500,0,0),radius=8,color=color.orange, make_trail=True)
    ballorigin4=sphere(pos=vector(-500,0,0),radius=8)
    L1=label(pos=vector(-500,-50,0),color=color.red, text='conductor no resistance')
    L2=label(pos=vector(-500,-100,0),color=color.blue, text='conductor with resistance')
    L3=label(pos=vector(-500,-150,0),color=color.green, text='non-conductor no resistance')
    L4=label(pos=vector(-500,-200,0),color=color.orange, text='non-conductor with resistance')
    
elif shape == 2:
    #plt.title('air resistance(square)')
    cd1 = 1.28  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面

    scene = canvas(y=100,width=100,height=100)
    wall=box(pos=vector(0,0,0),size=vector(1000,3,0.5))
    square1=box(pos=vector(-500,0,0),size=vector(10,10,10),color=color.red, make_trail=True)
    squareorigin1=box(pos=vector(-500,0,0),size=vector(10,10,10))
    square2=box(pos=vector(-500,0,0),size=vector(10,10,10),color=color.blue, make_trail=True)
    squareorigin2=box(pos=vector(-500,0,0),size=vector(10,10,10))
    
    #scene2 = canvas(y=100,width=100,height=100)
    #wall=box(pos=vector(0,0,0),size=vector(1000,3,0.5))
    square3=box(pos=vector(-500,0,0),size=vector(10,10,10),color=color.green, make_trail=True)
    squareorigin3=box(pos=vector(-500,0,0),size=vector(10,10,10))
    square4=box(pos=vector(-500,0,0),size=vector(10,10,10),color=color.orange, make_trail=True)
    squareorigin4=box(pos=vector(-500,0,0),size=vector(10,10,10))
    L1=label(pos=vector(-500,-50,0),color=color.red, text='conductor no resistance')
    L2=label(pos=vector(-500,-100,0),color=color.blue, text='conductor with resistance')
    L3=label(pos=vector(-500,-150,0),color=color.green, text='non-conductor no resistance')
    L4=label(pos=vector(-500,-200,0),color=color.orange, text='non-conductor with resistance')
      
else:
    #plt.title('air resistance(bullet)')
    cd1 = 0.295  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面

    #scene = canvas(y=100,width=100,height=100)
    #wall=box(pos=vector(0,0,0),size=vector(1000,3,0.5))
    cone1=cone(pos=vector(-500,0,0),radius=5,length=10,color=color.red, make_trail=True)
    coneorigin1=cone(pos=vector(-500,0,0),radius=5,length=10)
    cone2=cone(pos=vector(-500,0,0),radius=5,length=10,color=color.blue, make_trail=True)
    coneorigin2=cone(pos=vector(-500,0,0),radius=5,length=10)
    
    #scene2 = canvas(y=100,width=100,height=100)
    #wall=box(pos=vector(0,0,0),size=vector(1000,3,0.5))
    cone3=cone(pos=vector(-500,0,0),radius=5,length=10,color=color.green, make_trail=True)
    coneorigin3=cone(pos=vector(-500,0,0),radius=5,length=10)
    cone4=cone(pos=vector(-500,0,0),radius=5,length=10,color=color.orange, make_trail=True)
    coneorigin4=cone(pos=vector(-500,0,0),radius=5,length=10)
    L1=label(pos=vector(-500,-50,0),color=color.red, text='conductor no resistance')
    L2=label(pos=vector(-500,-100,0),color=color.blue, text='conductor with resistance')
    L3=label(pos=vector(-500,-150,0),color=color.green, text='non-conductor no resistance')
    L4=label(pos=vector(-500,-200,0),color=color.orange, text='non-conductor with resistance')  
  
x0=0
y0=2
vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)
t1=5
dt=0.05  
n2=int(t1/dt)
xx=[]
yy=[]

while y0 > 0:
    x = x0+(v*np.cos(si_r))*dt
    xx.append(x)
    x0 = x
    vy = vy0-g*dt
    y = y0+vy*dt
    yy.append(y)
    y0 = y
    vy0 = vy
    
    if shape == 1:
        ball1.pos.x = x-500
        ball1.pos.y = y
        rate(30)
    elif shape == 2:
        square1.pos.x = x-500
        square1.pos.y = y
        rate(30)
    else:
        cone1.pos.x = x-500
        cone1.pos.y = y
        rate(30)
        
'''    
plt.grid()    
plt.title('projectiles trajectory within 5s (conductor)')  
plt.plot(xx,yy)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()

plt.grid()    
plt.title('projectiles trajectory within 5s (non-conductor)')  
plt.plot(xxn,yyn)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
'''
#===============================================================

t=0
vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)

xx_ = []
yy_ = []

xa1=0
ya1=2

dt=0.5
while ya1 > 0:
    
    Fa1 = 0.5*Da*cd1*A1*v**2
    
    ax = -Fa1*vx0/(m*abs(v))
    ay = -(Fa1*vy0/(m*abs(v)))-g
    vx0 += ax*dt
    vy0 += ay*dt
    xa1 += vx0*dt
    ya1 += vy0*dt
    xx_.append(xa1)
    yy_.append(ya1)
    t += dt
    
    if shape == 1:
        ball2.pos.x = xa1-500
        ball2.pos.y = ya1
        rate(30)
    elif shape == 2:
        square2.pos.x = xa1-500
        square2.pos.y = ya1
        rate(30)
    else:
        cone2.pos.x = xa1-500
        cone2.pos.y = ya1
        rate(30)
    

#===================================================

x0=0
y0=2

vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)

m1=0.5
vx0=2*m1*vx0/(m+m1)
vy0=2*m1*vy0/(m+m1)
t1=5
dt=0.1
n2=int(t1/dt)
xxn=[]
yyn=[]

while y0 > 0:
    x = x0+vx0*dt
    xxn.append(x)
    x0 = x
    vy = vy0-g*dt
    y = y0+vy*dt
    yyn.append(y)
    y0 = y
    vy0 = vy
    t+=dt
    if shape == 1:
        ball3.pos.x = x-500
        ball3.pos.y = y
        rate(30)
    elif shape == 2:
        square3.pos.x = x-500
        square3.pos.y = y
        rate(30)
    else:
        cone3.pos.x = x-500
        cone3.pos.y = y
        rate(30)

t=0

xx_n = []
yy_n = []

xa1=0
ya1=2

vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)

m1=0.5
vx0=2*m1*vx0/(m+m1)
vy0=2*m1*vy0/(m+m1)

print('v(non-conductor)',(vx0**2+vy0**2)**0.5,  '(m/s)')

dt=0.1
while ya1 > 0:
    
    Fa1 = 0.5*Da*cd1*A1*v**2
    
    ax = -Fa1*vx0/(m*abs(v))
    ay = -(Fa1*vy0/(m*abs(v)))-g
    vx0 += ax*dt
    vy0 += ay*dt
    xa1 += vx0*dt
    ya1 += vy0*dt
    xx_n.append(xa1)
    yy_n.append(ya1)
    t += dt
    
    if shape == 1:
        ball4.pos.x = xa1-500
        ball4.pos.y = ya1
        rate(30)
    elif shape == 2:
        square4.pos.x = xa1-500
        square4.pos.y = ya1
        rate(30)
    else:
        cone4.pos.x = xa1-500
        cone4.pos.y = ya1
        rate(30)


#========================compare
plt.grid()
plt.title('air resistance vs no air resistance(bullet)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xx,yy,'b', label='conductor(no resistance)')
plt.plot(xx_, yy_,'b--', label='conductor(with resistance)')
plt.plot(xxn,yyn,'r', label='non-conductor(no resistance)')
plt.plot(xx_n, yy_n,'r--', label='non-conductor(with resistance)')
plt.legend()
plt.show()
'''
plt.grid()
plt.title('air resistance(Prism) vs no air resistance')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xxn,yyn, label='no resistance(non-conductor)')
plt.plot(xx_n, yy_n, label='with resistance(non-conductor)')
plt.legend()
plt.show()
'''