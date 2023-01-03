a = int(input("ENter the Number A: "))
b = int(input("ENter the Number B: "))
temp = a
a = b
b = temp
print("Result of using temperoary variable:" ,a)
print("Result of using temperoary variable:" ,b)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
a,b = b,a
print("Result of A after Given equation is " ,a)
print("Result of B after Given equation is " ,b)
print("Both result are same")