def largest(list):
    max = list[0]
    for l in list:
        if l > max:
            max = l
    return max

list = [50,80,90,100,99,150]
print("Largest element is: ", largest(list))