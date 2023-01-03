''' Q1. Practice question  5
Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C
50-59, D
0-49, F '''


grade = int(input("Enter your grade: - "))

if grade >= 80:
    print("A")
elif grade >= 79 and grade <=70:
    print("B")
elif grade >= 69 and grade <=60:
    print("C")
elif grade >= 59 and grade <=50:
    print("D")
else:
    print("F")