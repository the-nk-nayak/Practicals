''' Find all numbers which are multiple of 17,
but not the multiple of 5, between 2000 and 2500.'''
num = 17
for i in range(2000,2500):
    if i % num == 0:
        if i % 5:
            print(i) 

                    