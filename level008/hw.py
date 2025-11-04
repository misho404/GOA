#type ფუნქცია ცნობს ყველანაირ data type-ს მაგალითად
a=type(True)
print(a) 
#data convertion ეს არის ველიუს ტაიპის მნიშვნელობის შეცვლა მაგალითად: 
x="55"
type(x)
y=int(x)
print (5+y)
#data convert-ი შეიძლება გაკეთდეს ბევრ სხვადასხვანაირ data type-ზე მაგ:
m=3.5
type(m)
n=(m+4.5)
print(n)
#ახლა მაგალითები:
#1
i="10"
o=int(i)
print(i)
#2
x="55"
y=int(x)
print(y)
#3
p="7"
l=int(p)
print(l)
#1
a1=20
a2=str(a1)
print(a2)
#2
a3=3.5
a4=str(a3)
print(a4)
#3
a5=100
a6=str(a5)
print(a6)
#1
s1=4
s2=float(s1)
print(s2)
#2
s3=57
s4=float(s3)
print(s4)
#3
s5=7809
s6=float(s5)
print(s6)


n1=(input("number: "))

name=(input("yor name: "))
n4=(n1)
print(name * n4)



n2=(input("number: "))
n3=(input("number: "))
n5=(input("number: "))
nn=(n2+n3+n5)
yy=str(nn)