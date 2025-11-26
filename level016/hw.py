

user_password= "m1m2m3"
input_password=input("enter password: ")

tryy=3

while input_password!=user_password and tryy>0:
    print(tryy)
    print("password is incorrect")
    tryy=tryy-1
    input_password=input("enter password ")

#while tryy>=0:


print("password is correct")

