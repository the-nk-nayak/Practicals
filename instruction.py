string = "I am Nishi Kant Nayak"
print(string)
li = list(string.split(" "))
print(li)
li1 = sorted(li)
print(li1)
def Reverse(list1) :
    return [element for element in reversed(list1)]
print(Reverse (li1))