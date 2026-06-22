#Handle of Error in ValueError
try:
    x = int(input('What is x? '))
    print(f'x is {x}')
except:
    print('x is not an integer')

#Handle error by loop
while True:
    try:
        x = int(input("What's x? "))
    except:
        print("x is not an integer")
    else:
        break

print(f"X is {x}")