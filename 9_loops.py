#Equal not loops
i = 3
while i != 0:
    print("Meow")
    i -= 1

#Smaller than loops
i = 0
while i < 3:
    print("Meow")
    i += 1
    
#With loops for & basic print
for i in [0, 1, 2]:
    print("Moooo")

for _ in range(90):
    print("BARK")

print("GUUU\n" * 3, end="")

#With variables & input
while True:
    name = int(input("Meows? "))
    if name < 0:
        continue
    else:
        break

for _ in range(name):
    print("GUUU")
    
#With function
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Mow")
    
main()