#Iteration with list
people = ["Griffin", "Sony", "David"]

for people in people:
    print(people)
    
people = ["Griffin", "Sony", "David"]

for i in range(len(people)):
    print(i + 1, people[i], sep = '. ')

#Dictionary iteration
people = {
    'Griffin' : 'America',
    'Sony' : 'America',
    'Angel' : 'America',
    'Natasha' : 'Russia'
}

for i in people:
    print(i, people[i], sep = ', ')

#List of dictionaries
people = [
    {'name' : 'Griffin', 'locale' : 'America', 'pet' : 'Alligator'},
    {'name' : 'Emma', 'locale' : 'England', 'pet' : 'Dog'},
    {'name' : 'Volvo', 'locale' : 'Germany', 'pet' : 'Dog'},
    {'name' : 'Henrick', 'locale' : 'Germany', 'pet' : 'Cat'},
    {'name' : 'Zabesk', 'locale' : 'Sweden', 'pet' : 'Cat'},
    {'name' : 'Arinoa', 'locale' : 'Spain', 'pet' : 'Dog'},
]

for person in people:
    print(person['name'], person['locale'], person['pet'], sep=', ')

#Nested List
def main():
    block_number(10)

def block_number(size):
    for i in range(size):
        print("#" * size)

main()

def main():
    x = int(input("How much is block? "))
    block(x)

def block(size):
    for i in range(size):
        print_block(size)

def print_block(n):
    print("-" * n)
    
main()