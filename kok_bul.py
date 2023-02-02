#ax2+bx+c= 0 denkleminin koklerini bulan program

import math

def kokbul():
    delta = pow(b,2)-4*a*c
    kok1 = (-b + math.sqrt(delta))/2*a
    kok2 = (-b - math.sqrt(delta))/2*a
    if delta < 0:
        print("Denklemin kökü yoktur.")
    else:
        if kok1 == kok2:
            print("Kökler birbirine eşittir.Kökler: ",kok1)
        else:
            print("Kökler birbirine eşit değildir.")
            print("Denklemin kökleri: ",kok1,kok2)
        
a = int(input("x^2 katsayısını giriniz: "))
b = int(input("x katsayısını giriniz: "))
c = int(input("1 katsayısını giriniz: "))
kokbul()

