import math
Yo = int(0.1)
Xo = int(0)
gmoon = -1.62
moment = 1
fuel = 4000
M = 6200
amax = 29.43
Vgas = 3660
alpha = 1
Vox = 0
Voy = 0
Vst = 1701.928
Hst = 50000
orbit = 5617167.6
radius = 1738000
flag = False
t = 0.1
Vstx = Vst*radius/(radius+Hst)
time = 6321.565
print('Ожидание:',time,'сек')
while True:
    fmax = amax*M/Vgas
###============COMMAND BLOCK1============###
    if abs(Vox) < Vstx:
        dmt = fmax*abs(Hst-Yo)/(7*Hst)
        angle = (90/57.29577)*(((Yo+2230)/Hst)**0.3)
        duration = 1
    elif abs(Vox) > Vstx:
        dmt = 0
        duration = 1 # Выходим на нужную скорость по оси X
    if  Yo >= Hst-400 and Voy >= 10:
        dmt = fmax
        duration = 1
        angle = (180/57.29577) # Выравниваем вертикальную скорость
        DAD1 = [round(Xo,2),round(Yo,2),round(Vox,1),round(Voy,1),round(M-2200,2)]
    elif Yo > Hst - 5: # Вышли на орбиту, тормозим вертикальную скорость:
        dmt = 0
        duration = 1
        angle = 0
        DAD2 = [round(Xo,2),round(Yo,2),round(Vox,1),round(Voy,1),round(M-2200,2)]
    if Voy > 1 and Yo > Hst - 1:
        dmt = 2
        angle = (180/57.29577)
        duration = 1
    elif Yo > Hst-1 and Voy <= 0 :
        M = M - 200
        break
    Xst = Vst*(radius/(radius+Yo))*time - 80000*(radius/(radius+Yo))-10920176
    # Подошли к станции, отдали груз, теперь садимся
###=================END=================###
        
    accel = Vgas*dmt/M
    for i in range(0,round(duration)):
        dmt = dmt*(M-dmt)/M
        M = M - dmt*0.1   
        #Все расчёты по оси X
        Fx = (Vgas*dmt)*math.sin(angle)
        ax = Fx/(M+dmt)
        Vox += ax*t*(radius/(radius+Yo))
        x = Xo + Vox*t/(radius/(radius+Yo)) + (ax*t**2)/2
        Xo = x
        #Все расчёты по оси Y
        Fy = (Vgas*dmt)*math.cos(angle) + M*gmoon
        ay = Fy/M
        Voy += ay*t + (Vox**2)*t/(Yo+1737000)
        y = Yo + Voy*t + (ay*t**2)/2
        Yo = y
        #Расчёт ускорения
        ao = math.sqrt(ay**2 + ax**2)
        #Блок скругления планеты:
        if abs(Xo) > 2*orbit:
            Xo = 0
        time +=0.1

    if flag:
        break
print('Скорость станции в проекции на ось X:',round(Vstx,1))
print('Набрана скорость по X, двигатели отключены, по инерции набираем высоту станции')
print('Xo:',DAD1[0],'Yo:',DAD1[1],'Vox:',DAD1[2],'Voy:',DAD1[3],'Fuel:',DAD1[4])
print('Высота набрана, скорость по Y выравнена со скоростью станции (0 м/c +-0.05)')
print('Xo:',DAD2[0],'Yo:',DAD2[1],'Vox:',DAD2[2],'Voy:',DAD2[3],'Fuel:',DAD2[4])
print('Xst:',round(Xst,2),'Yst:',50000,'- координаты станции')
print('Груз отдан')

Xo = -296133

while True:
    fmax = amax*M/Vgas
###============COMMAND BLOCK2============###
    # Посадка
    if Vox > 1:
        dmt = fmax/6
        angle = angle = (-90/57.29577)*(((Yo-1000)/Hst)**0.229)
        duration = 1
    elif Vox < 1 and Voy < -2:
        angle = 0
        dmt = 2.35
        duration = 1
    elif Vox < 1 and Voy > -2:
        dmt = 0
        angle = 0
        duration = 1
    if Yo < 0.5:
        flag = True
        break
###=================END=================###        
    accel = Vgas*dmt/M
    for i in range(0,round(duration)):
        dmt = dmt*(M-dmt)/M
        
        
        #Все расчёты по оси X
        Fx = (Vgas*dmt)*math.sin(angle)
        ax = Fx/(M+dmt)
        Vox += ax*t*(radius/(radius+Yo))
        x = Xo + Vox*t/(radius/(radius+Yo)) + (ax*t**2)/2
        M = M - dmt*0.0583
        Xo = x
        #Все расчёты по оси Y
        Fy = (Vgas*dmt)*math.cos(angle) + M*gmoon
        ay = Fy/M
        Voy += ay*t + (Vox**2)*t/(Yo+1737000)
        y = Yo + Voy*t + (ay*t**2)/2
        Yo = y
        #Расчёт ускорения
        ao = math.sqrt(ay**2 + ax**2)  
        #Блок скругления планеты:
        if abs(Xo) > 2*orbit:
            Xo = 0
        time +=0.1

    if flag:
        break
print('Ожидание 5517.24 сек на орбите, координата после него Xo = - 296133, Yo = 49990.7')
print('Приземление:')
print('Xo:',round(Xo,2),'Yo:',round(Yo,2),'Vx:',round(Vox),'Vy:',round(Voy),'Fuel:',round(M-2000,2))
