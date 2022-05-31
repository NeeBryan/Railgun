# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 19:57:27 2021

@author: Bryan
"""

import matplotlib.pyplot as plt
import numpy as np
import vpython as vp
import math as math
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
print(v)
plt.title('projectiles velocity change in railgun')
plt.plot(tt,vv)    
plt.show()

x0=0
y0=2
vy0=v*np.sin(si_r)
vx0=v*np.cos(si_r)
t1=5
dt=0.0001  
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
plt.plot(xx,yy)
plt.show()

shape=int(input('the shape of projectile(1:sphere, 2:square, 3:bullet)'))

if shape == 1:
    plt.title('air resistance(sphere)')
    cd1 = 1.14  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    v=((vx0)**2+(vy0)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*v**2
elif shape == 2:
    plt.title('air resistance(square)')
    cd1 = 1.28  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    v=((vx0)**2+(vy0)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*v**2
else:
    plt.title('air resistance(bullet)')
    cd1 = 0.295  #阻力係數
    Da = 1.225  #空氣密度
    A1 = 0.0004 #角柱底面
    v=((vx0)**2+(vy0)**2)**0.5
    Fa1 = 0.5*Da*cd1*A1*v**2

t=0

xx_ = [0]
yy_ = [2]

xa1=0
ya1=2

while t < 5:
    ax = -Fa1*vx0/(m*abs(v))
    ay = -(Fa1*vy0/(m*abs(v)))-g
    vx0 += ax*dt
    vy0 += ay*dt
    xa1 += vx0*dt
    ya1 += vy0*dt
    xx_.append(xa1)
    yy_.append(ya1)
    t += dt
    
plt.grid()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.plot(xx_, yy_)
plt.show()

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


L=10 # 砲管長 單位:m 
r=5*(10)**(-2) #砲管半徑
D=15*(10)**(-2) #砲管間的距離(電樞的距離) 單位:m
dr=0.001 #一小段電樞 
I=10000000 #電流 單位:ampere
c=4*np.pi*(10)**(-7) #真空中的磁導率
m=1 #子彈的質量 單位:kg

sidesXr1 = [10-0.1*i for i in range(101)]
sidesYr1 = [0.0 for i in range(101)]
sidesZr1 = [0.0 for i in range(101)]

sidesX1 = [0.0 for i in range(16)]
sidesY1 = [0+0.01*i for i in range(16)]
sidesZ1 = [0.0 for i in range(16)]

sidesXr2 = [0+0.1*i for i in range(101)]
sidesYr2 = [0.15 for i in range(101)]
sidesZr2 = [0.0 for i in range(101)]
#----------------------------------------------
sidesX = [10-1*i for i in range(11)]
sidesY = [0.0 for i in range(11)]
sidesZ = [0.0 for i in range(11)]

sidesX += [0.0 for i in range(6)]
sidesY += [0+0.03*i for i in range(6)]
sidesZ += [0.0 for i in range(6)]

sidesX += [0+1*i for i in range(11)]
sidesY += [0.15 for i in range(11)]
sidesZ += [0.0 for i in range(11)]

Sides = [sidesX, sidesY, sidesZ]
#----------------------------------------------
dsi=(2*np.pi)/50
si=[0+dsi*i for i in range(51)]
fig=plt.figure()
ax = fig.gca(projection='3d')

xx1=[]
xx2=[]
xx3=[]
yy1=[]
yy2=[]
yy3=[]
zz1=[]
zz2=[]
zz3=[]

for j in range(10):
    for i in range(51):
        y1 = 0.01*np.cos(si[i])
        z1 = 0.01*np.sin(si[i])
        yy1.append(y1)
        zz1.append(z1)
        x1 = sidesX[j]
        xx1.append(x1)      
    ax.plot3D(xx1, yy1, zz1, color='limegreen')
    xx1.clear()
    yy1.clear()
    zz1.clear()
     
for j in range(18,28):
    for i in range(51):  
        x2 = sidesX[j]  
        y2 = 0.15+0.01*np.cos(si[i])
        z2 = 0.01*np.sin(si[i])
        xx2.append(x2)
        yy2.append(y2)
        zz2.append(z2)
    ax.plot3D(xx2, yy2, zz2, color='limegreen')
    xx2.clear()
    yy2.clear()
    zz2.clear()
    
for j in range(12,16):
    for i in range(51):  
        y3 = sidesY[j]  
        x3 = 0.5*np.cos(si[i])
        z3 = 0.01*np.sin(si[i])
        xx3.append(x3)
        yy3.append(y3)
        zz3.append(z3)
    ax.plot3D(xx3, yy3, zz3, color='blueviolet')
    xx3.clear()
    yy3.clear()
    zz3.clear()   
    


ax = fig.gca(projection='3d')
ax.plot3D(sidesX1, sidesY1, sidesZ1, color='red')
ax.plot3D(sidesXr1, sidesYr1, sidesZr1, color='dodgerblue')
ax.plot3D(sidesXr2, sidesYr2, sidesZr2, color='dodgerblue')
ax.set_zlim(-0.075,0.075)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

'''
L=10 # 砲管長 單位:m 
l=0.15 #電樞長度 單位:m
r=5*(10)**(-2) #砲管半徑
D=15*(10)**(-2) #砲管間的距離(電樞的距離) 單位:m
dr=0.001 #一小段電樞 
I=10000000 #電流 單位:ampere
#c=4*np.pi*(10)**(-7) #真空中的磁導率
c=1
m=1 #子彈的質量 單位:kg
F=0
t=0
dt=0.0001
n=int((D-r)/dr)
tt=[]
L1=0.5
dL1=1
dL2=0.006
#n3=int((2*L1/dL1))+1
n3=16

X, Y, Z = np.meshgrid(np.arange(-15.05, 15.05, 2),
                      np.arange(-15.05, 15.05, 2),
                      np.arange(-15.05, 15.05, 2))

x=np.array([0 for i in range(n3)])
y=np.array([-15.05+dL1*i for i in range(n3)])
z=np.array([-15.05+dL1*i for i in range(n3)])
B=[0,0,0]

u = np.array([[[0 for j in range(n3)] for i in range(n3)] for k in range(n3)]) #磁場x分量
v = np.array([[[0 for j in range(n3)] for i in range(n3)] for k in range(n3)]) #磁場y分量
h = np.array([[[0 for j in range(n3)] for i in range(n3)] for k in range(n3)]) #磁場z分量

u1 = np.array([[[0 for j in range(n3)] for i in range(n3)] for k in range(n3)] ) #磁場x分量
v1 = np.array([[[0 for j in range(n3)] for i in range(n3)] for k in range(n3)] ) #磁場y分量
h1 = np.array([[[0 for j in range(n3)] for i in range(n3)] for k in range(n3)] ) #磁場z分量
#砲管(電流流入)的每一小段位置
sidesXr1 = np.array([10-1*i for i in range(11)])
sidesYr1 = np.array([0.0 for i in range(11)])
sidesZr1 = np.array([0.0 for i in range(11)])
#電樞的每一小段位置
sidesX1 = np.array([0.0 for i in range(7)])
sidesY1 = np.array([0+1.2*i for i in range(7)]) ### 改了
sidesZ1 = np.array([0.0 for i in range(7)])
#砲管(電流流出)的每一小段位置
sidesXr2 = np.array([0+1*i for i in range(11)])
sidesYr2 = np.array([7.2 for i in range(11)]) ### 改了
sidesZr2 = np.array([0.0 for i in range(11)])

vds1 = [-L/10, 0, 0 ] #將砲管(電流流入)切分成100段，每一段的向量
vds2 = [0, 7.2, L/100] #將砲管(電流流出)切分成100段，每一段的向量 ###改了
vds3 = [0, l/100, 0] #將電樞切分成100段，每一段的向量


for i in range(n3):
    for j in range(n3):
        for k in range(n3):   #對導線做積分
            for m in range(11):
                vr1 = [x[k]-sidesXr1[m], y[j]-0, z[i]-0]   #r向量(由下而上積)
                r1 = ((x[k]-sidesXr1[m])**2 + (y[j]-0)**2 + (z[i]-0)**2)**0.5 #座標點到每一段導線的距離
                dB1 = ((c/(4*np.pi))*I*np.cross(vds1,vr1))/(r1**3)   #計算dB
                
                
                vr2 = [z[i]-0, y[j]-7.2, x[k]-sidesXr2[m]]   #r向量(由下而上積)
                r2 = ((x[k]-sidesXr2[m])**2 + (y[j]-7.2)**2 + (z[i]-0)**2)**0.5 #座標點到每一段導線的距離
                dB2 = (c/(4*np.pi))*I*np.cross(vds2,vr2)/r2**3   #計算dB
                
                B[0] += (dB1[0]) #+ dB2[0])   #將各段導線對此時之座標點的磁場dB之x方向相加
                B[1] += (dB1[1]) #+ dB2[1])   #將各段導線對此時之座標點的磁場dB之y方向相加
                B[2] += (dB1[2]) #+ dB2[2])   #將各段導線對此時之座標點的磁場dB之z方向相加
            
            u[i][j][k] = B[0] #將各座標點的x方向磁場匯入代表各座標點的list
            v[i][j][k] = B[1] #將各座標點的y方向磁場匯入代表各座標點的list
            h[i][j][k] = B[2] #將各座標點的z方向磁場匯入代表各座標點的list
            B = [0,0,0]
            

for i in range(n3):
    for j in range(n3):
        for k in range(n3):   #對導線做積分
            for m in range(7): 
                vr3 = [z[i]-0, y[j]-sidesY1[m], x[k]-0]   #r向量(由下而上積)
                r3 = ((x[k]-0)**2 + (y[i]-sidesY1[m])**2 + (z[i]-0)**2)**0.5 #座標點到每一段導線的距離
                dB3 = (c/(4*np.pi))*I*np.cross(vds3,vr3)/r3**3   #計算dB
            
                B[0] += dB3[0]   #將各段導線對此時之座標點的磁場dB之x方向相加
                B[1] += dB3[1]   #將各段導線對此時之座標點的磁場dB之y方向相加
                B[2] += dB3[2]
            
            h[k][j][i] += B[0] #將各座標點的x方向磁場匯入代表各座標點的list
            v[k][j][i] += B[1] #將各座標點的y方向磁場匯入代表各座標點的list
            u[k][j][i] += B[2] #將各座標點的z方向磁場匯入代表各座標點的list
            B = [0,0,0]   # 重置B向量


for j in range(n3):
    for i in range(n3):
        u1[i][j][k]=u[8][i][j]
        v1[i][j][k]=v[8][i][j]
        h1[i][j][k]=h[8][i][j]

fig=plt.figure()
ax = fig.gca(projection='3d')
ax.quiver(X, Y, Z, u1, v1, h1, length=0.5, normalize=True) 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()    
plt.savefig('')
'''