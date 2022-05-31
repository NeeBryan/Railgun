# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 22:21:32 2021

@author: -
"""

import matplotlib.pyplot as plt
import numpy as np
import math
#import vpython as vp

#==============================================================================



L=10 # 砲管長 單位:m 
r=5*(10)**(-2) #砲管半徑
D=15*(10)**(-2) #砲管間的距離(電樞的距離) 單位:m
dr=0.001 #一小段電樞 
I = float(input('輸入磁軌砲的電流(需大於10000A)')) #電流 單位:ampere
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
plt.xlabel('time (s)')
plt.ylabel('velocity (m/s)')  
plt.title('projectiles velocity change in railgun')
plt.plot(tt,vv) 
plt.show()


#Shape Effect On Drag(conductor)-------------------------------------------

x0=0
y0=2
vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)
t1=5
dt=0.1  
n2=int(t1/dt)

xx=[]
yy=[]

#plt.title('Shape effect on drag(conductor)')
t=0
tt=[]
xx_1 = []
yy_1 = []
vx01=vx0
vy01=vy0

xx_2 = []
yy_2 = []
vx02=vx0
vy02=vy0

xx_3 = []
yy_3 = []
vx03=vx0
vy03=vy0

JJ_c1 = []
JJ_c2 = []
JJ_c3 = []
J_c1 = 0
J_c2 = 0
J_c3 = 0



t=0
xa1=0
ya1=2
while ya1 > 0:
    #plt.title('air resistance(sphere)')
    cd1 = 0.5  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #球體與流體接觸面積
    
    v=((vx01)**2+(vy01)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*(v**2)
    
    ax = -Fa1*vx01/(m*abs(v))      #x方向加速度
    ay = -(Fa1*vy01/(m*abs(v)))-g  #y方向加速度
    vx01 += ax*dt   #x方向速度
    vy01 += ay*dt   #y方向速度
    xa1 += vx01*dt  #x方向位移
    ya1 += vy01*dt  #y方向位移
    #J_c1 += Fa1*dt
    J_c1 = m*(vx01**2+vy01**2)**0.5
    xx_1.append(xa1)
    yy_1.append(ya1)
    JJ_c1.append(J_c1)
    t += dt
    
    


t=0
xa1=0
ya1=2
while ya1 > 0:
    #plt.title('air resistance(square)')
    cd1 = 1.28  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #平面與流體接觸面積
    
    v=((vx02)**2+(vy02)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*(v**2)
    
    ax = -Fa1*vx02/(m*abs(v))
    ay = -(Fa1*vy02/(m*abs(v)))-g
    vx02 += ax*dt
    vy02 += ay*dt
    xa1 += vx02*dt
    ya1 += vy02*dt
    #J_c2 += Fa1*dt
    J_c2 = m*(vx02**2+vy02**2)**0.5
    xx_2.append(xa1)
    yy_2.append(ya1)
    JJ_c2.append(J_c2)
    t += dt
    


t=0
xa1=0
ya1=2
while ya1 > 0:
    #plt.title('air resistance(bullet)')
    cd1 = 0.295  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #彈頭與流體接觸面積
    
    v=((vx03)**2+(vy03)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*(v**2)
    
    ax = -Fa1*vx03/(m*abs(v))
    ay = -(Fa1*vy03/(m*abs(v)))-g
    vx03 += ax*dt
    vy03 += ay*dt
    xa1 += vx03*dt
    ya1 += vy03*dt
    #J_c3 += Fa1*dt
    J_c3 = m*(vx03**2+vy03**2)**0.5
    xx_3.append(xa1)
    yy_3.append(ya1)
    JJ_c3.append(J_c3)
    t += dt
    tt.append(t)
    


#Shape Effect On Drag(non-conductor)-------------------------------------------

x0=0
y0=2
vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)
t1=5
dt=0.1  
n2=int(t1/dt)
xx=[]
yy=[]

m1 = 0.5 #電樞質量    
vx0_n=2*m1*vx0/(m+m1)
vy0_n=2*m1*vy0/(m+m1)

print('v(non-conductor)',(vx0_n**2+vy0_n**2)**0.5,  '(m/s)')



#plt.title('Shape effect on drag(non-conductor)')

t=0
tt=[]
xx_ = []
yy_ = []

xx_1n = []
yy_1n = []
vx01_n=vx0_n
vy01_n=vy0_n

xx_2n = []
yy_2n = []
vx02_n=vx0_n
vy02_n=vy0_n

xx_3n = []
yy_3n = []
vx03_n=vx0_n
vy03_n=vy0_n

JJ_n1 = []
JJ_n2 = []
JJ_n3 = []
J_n1 = 0
J_n2 = 0
J_n3 = 0


t=0
xa1=0
ya1=2
while ya1 > 0:
    #plt.title('air resistance(sphere)')
    cd1 = 0.5  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #球體與流體接觸面積
    
    v_=((vx01_n)**2+(vy01_n)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*(v_**2)
    
    ax = -Fa1*vx01_n/(m*abs(v_))      #x方向加速度
    ay = -(Fa1*vy01_n/(m*abs(v_)))-g  #y方向加速度
    vx01_n += ax*dt   #x方向速度
    vy01_n += ay*dt   #y方向速度
    xa1 += vx01_n*dt  #x方向位移
    ya1 += vy01_n*dt  #y方向位移
    #J_n1 += Fa1*dt
    J_n1 = m*(vx01_n**2+vy01_n**2)**0.5
    JJ_n1.append(J_n1)
    xx_1n.append(xa1)
    yy_1n.append(ya1)
    t += dt
    
    


t=0
xa1=0
ya1=2
while ya1 > 0:
    #plt.title('air resistance(square)')
    cd1 = 1.28  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #平面與流體接觸面積
    
    v_=((vx02_n)**2+(vy02_n)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*(v_**2)
    
    ax = -Fa1*vx02_n/(m*abs(v_))
    ay = -(Fa1*vy02_n/(m*abs(v_)))-g
    vx02_n += ax*dt
    vy02_n += ay*dt
    xa1 += vx02_n*dt
    ya1 += vy02_n*dt
    #J_n2 += Fa1*dt
    J_n2 = m*(vx02_n**2+vy02_n**2)**0.5
    JJ_n2.append(J_n2)
    xx_2n.append(xa1)
    yy_2n.append(ya1)
    t += dt
    


t=0
xa1=0
ya1=2
while ya1 > 0:
    #plt.title('air resistance(bullet)')
    cd1 = 0.295  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #彈頭與流體接觸面積
    
    v_=((vx03_n)**2+(vy03_n)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*(v_**2)
    
    ax = -Fa1*vx03_n/(m*abs(v_))
    ay = -(Fa1*vy03_n/(m*abs(v_)))-g
    vx03_n += ax*dt
    vy03_n += ay*dt
    xa1 += vx03_n*dt
    ya1 += vy03_n*dt
    #J_n3 += Fa1*dt
    J_n3 = m*(vx03_n**2+vy03_n**2)**0.5
    JJ_n3.append(J_n3)
    xx_3n.append(xa1)
    yy_3n.append(ya1)
    t += dt
    tt.append(t)
    
    
    

#plt.title('position,acceleration versus time')
ax1 = plt.subplot()
#plt.xlabel('time(s)')


#ax1.tick_params(axis='y',labelcolor='red')

ax2 = ax1.twinx()
#ax2.tick_params(axis='y',labelcolor='blue') 
    
plt.title('trajectory vs impulse(conductor)')     
plt.grid()
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.plot(xx_1, yy_1,label='sphere(trajectory)')
ax1.plot(xx_2, yy_2,label='square(trajectory)')
ax1.plot(xx_3, yy_3,label='bullet(trajectory)')
ax1.legend(loc=4)
#plt.show()

#plt.grid()
#plt.xlabel('x')
ax2.set_ylabel('impulse(N/s)')
#ax2.title('impulse(conductor)')
ax2.plot(xx_1, JJ_c1,label='sphere(impulse)',linestyle='--')
ax2.plot(xx_2, JJ_c2,label='square(impulse)',linestyle='--')
ax2.plot(xx_3, JJ_c3,label='bullet(impulse)',linestyle='--')
ax2.legend(loc=3)
plt.show()

ax1 = plt.subplot()
#plt.xlabel('time(s)')


#ax1.tick_params(axis='y',labelcolor='red')

ax2 = ax1.twinx()
    
plt.title('trajectory vs impulse(non-conductor)')   
plt.grid()
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.plot(xx_1n, yy_1n,label='sphere(trajectory)')
ax1.plot(xx_2n, yy_2n,label='square(trajectory)')
ax1.plot(xx_3n, yy_3n,label='bullet(trajectory)')
#ax1.tick_params(axis='y',labelcolor='red')
ax1.legend(loc=4)
#plt.show()

#plt.grid()
#ax2.xlabel('x')
ax2.set_ylabel('impulse(N/s)')
#ax2.title('impulse(non-conductor)')
ax2.plot(xx_1n, JJ_n1,label='sphere(impulse)',linestyle='--')
ax2.plot(xx_2n, JJ_n2,label='square(impulse)',linestyle='--')
ax2.plot(xx_3n, JJ_n3,label='bullet(impulse)',linestyle='--')
ax2.legend(loc=3)
plt.show()

#compare-----------------------------------------------------------------------

plt.grid()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('conductor vs non-conductor(bullet)')
plt.plot(xx_3, yy_3,label='conductor')
plt.plot(xx_3n, yy_3n,label='non-conductor')
plt.legend(loc=4)
plt.show()

#==============================================================================
#impulse=======================================================================




#compare-----------------------------------------------------------------------
plt.grid()
plt.xlabel('x')
plt.ylabel('J(N/s)')
plt.title('impulse,conductor vs non-conductor(bullet)')
plt.plot(xx_3, JJ_c3,label='conductor')
plt.plot(xx_3n, JJ_n3,label='non-conductor')
plt.legend(loc=4)
plt.show()