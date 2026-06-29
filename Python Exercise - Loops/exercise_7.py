numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    #Break kills item loop so 50 is not included when > 500 is break
    if i > 500:
        break
    #Skip the number depends on condition
    elif i > 150:
        continue
    #Print the number divisible by 5 using modular = 0
    elif i % 5 == 0:
        print(i)
        