# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 22:43:01 2021

@author: Bryan
"""

import matplotlib.pyplot as plt
import numpy as np
#from vpython import *
import math as math
'''
shape=int(input('the shape of projectile(1:sphere, 2:square, 3:bullet)'))
'''
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
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(tt,vv)    
plt.show()

x0=0
y0=2
vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)
t1=5
dt=0.1  
n2=int(t1/dt)
xx=[]
yy=[]


for i in range(n2):
    x = x0+(v*np.cos(si_r))*dt
    xx.append(x)
    x0 = x
    vy = vy0-g*dt
    y = y0+vy*dt
    yy.append(y)
    y0 = y
    vy0 = vy

     
plt.grid()    
plt.title('projectiles trajectory within 5s')  
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xx,yy)
plt.show()

t=0
tt=[]
xx_ = []
yy_ = []

xx_1 = []
yy_1 = []
vx01=vx0
vy01=vy0

xx_2 = []
yy_2 = []
vx02=vx0
vy02=vy0

xa1=0
ya1=2

t=0
while t < 5:
    #plt.title('air resistance(sphere)')
    cd1 = 0.5  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    
    v=((vx0)**2+(vy0)**2)**0.5
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


t=0
xa1=0
ya1=2 

while t < 5:
    #plt.title('air resistance(square)')
    cd1 = 1.28  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    
    v=((vx01)**2+(vy01)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*v**2
    
    ax = -Fa1*vx01/(m*abs(v))
    ay = -(Fa1*vy01/(m*abs(v)))-g
    vx01 += ax*dt
    vy01 += ay*dt
    xa1 += vx01*dt
    ya1 += vy01*dt
    xx_1.append(xa1)
    yy_1.append(ya1)
    t += dt


t=0
xa1=0
ya1=2
while t < 5:
    #plt.title('air resistance(bullet)')
    cd1 = 0.295  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    
    v=((vx02)**2+(vy02)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*v**2
    
    ax = -Fa1*vx02/(m*abs(v))
    ay = -(Fa1*vy02/(m*abs(v)))-g
    vx02 += ax*dt
    vy02 += ay*dt
    xa1 += vx02*dt
    ya1 += vy02*dt
    xx_2.append(xa1)
    yy_2.append(ya1)
    t += dt
    tt.append(t)
  
    
    
plt.grid()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xx_, yy_,label='sphere')
plt.plot(xx_1, yy_1,label='square')
plt.plot(xx_2, yy_2,label='bullet')
plt.legend()
plt.show()

'''
#========================compare
plt.grid()
plt.title('air resistance(Prism) vs no air resistance')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xx,yy, label='no resistance')
plt.plot(xx_, yy_, label='with resistance')
plt.legend()
plt.show()
'''
#===================================================