''' Practice  question  4 
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive '''


age = int(input("Enter Your age: - "))

if age>=18:
    print("You are old enough to learn to drive")
else:
    print(f"You need to be 18 and you are {18-age} old")