from math import *
import math
from package import module_slide1, module_slide1_2
from math import sqrt
import math as m

radius = 5 
area =  math.pi * math.pow(radius,2)
print("Pi=",math.pi)
print("Diện tích hình tròn: ",area)

name="Lộc"
greeting= module_slide1.greet(name)
print(greeting)

result= module_slide1_2.add(4,1)
print(result)

number=25
square_root= sqrt(number)
print("Can bac hai cua ",number," la: ",square_root)

print("Pi=",pi)
print("sin cua 30 la: ",sin(30))
degre=m.degrees(sin(30))
print("degre=",degre)
print("sinh cua 1 la: ",sinh(1))

x = 10
y = 20
gcd=m.gcd(x,y)
lcm=m.lcm(x,y)
print("Ước chung lớn nhất của ",x,"và",y,"=",gcd)
print("Bội chung nhỏ nhất của ",x,"và",y,"=",lcm)