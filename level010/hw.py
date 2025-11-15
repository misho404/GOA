# შედარებითი ოპერატორები: <,>,==,<=,>=,!=


print(10<20)
print(9<11)
print(999<1000)
print(404<505)
print(777<999)

print(10>9)
print(99>98)
print(404>303)
print(69>67)
print(54>14)

print(10==10)
print(7==7)
print(11==11)
print(33==33)
print(45==45)

print(0<=1)
print(4<=5)
print(6<=67)
print(4<=4)
print(9<=10)

print(9>=8)
print(8>=7)
print(7>=6)
print(6>=5)
print(5>=4)

print(67!=69)
print(9!=11)
print(6!=7)
print(9!=0)
print(5!=6)
#logical operator ესესნი არის or , and ისინი მარცხნიდან მარჯვნივ იკითხება თავიდან or-ი იგნორდება მანამდე იკითხება and-ი და შემდეგ იკითხება or-ი

print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False and False)

num=(input("enter one number: "))
num2=(bool(num==15))
print(num2)

nam=(input("enter your name: "))
nam001=("misho")
nam77=(nam001==nam)
print(nam77)

age=(input("enter your age: "))
must=(age==18)
print(must)