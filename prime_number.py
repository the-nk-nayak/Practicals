num = int(input("Enter the Number to be checked :- "))
a = 2
while (a<num):
    if num % a == 0:
        print(f"The number, {num} is not a prime number")
        break
    a = a+1

if num == a:
    print(f"The Number is prime")