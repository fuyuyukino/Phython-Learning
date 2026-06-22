#Basic print
print("Hello World!")
print("I am", 18 , "years old")



#Variable
x = 1
y = 2
print(x+y)

name = "David"
print(name)

#Global Variable
x = "Books"

def hobby():
    print("I want " + x)
    
hobby()

def lecture():
    global x
    x = "Mechanical Statistic"
    
lecture()

print("Now, I will have lecture about " + x)
    


#Data Type (Not completed though)
r = {"Hello" : "John"}
s = {3, 4, 5}
t = 1j
u = ['Apple', 'Banana', 'Orange']
v = ('Apple', 'Banana', 'Orange')
w = True
x = 2
y = 1.5
z = "Hello"

print(type(r))
print(type(s))
print(type(t))
print(type(u))
print(type(v))
print(type(w))
print(type(x))
print(type(y))
print(type(z))

#Convert (Complex number cannot be converted)
x = 10
y = 2.5
z = 1+0j

print(int(y))
print(float(x))
print(complex(x))



#String Array (Print character inside string)
a = "Hello, World!"
print(a[1])

#Looping String
for x in "Banana":
    print(x)

#String Length (Give the length of characters inside string)
a = "Hello, World!"
print(len(a))

#Check String
txt = "Art is wonderfull"
print("Art" in txt)

txt = "I love Arch"
if "Arch" in txt:
    print("Yes")

#Slice String (Slice words from n start to n finish (Last character is not included))
b = "Hello, World!"
print(b[2:5])       #Slice from front

b = "Hello, World!"
print(b[-5:-2])     #Slice from back

b = "Hello, World!"
print(b[ :5])       #Slice start to n

b = "Hello, World!"
print(b[2: ])       #Slice n to end

#Case
a = "Hello, World!"
print(a.upper())                #Uppercase

a = "Hello, World!"
print(a.lower())                #Lowercase

a = "Hello, World!"
print(a.strip())                #Remove whitespace

a = "Hello, World!"
print(a.replace("H", "J"))      #Replace character

a = "Hello, World!"
print(a.split(","))             #Split the character

a = input("What's your name?") 
print(a.title().capitalize())   #Capitalize the Front character of each words