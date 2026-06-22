#Define the format and exponential of n and p
def number():
    n = float(input("How much? "))
    p = float(input("How much? "))
    return n**p

nume = number()
a = f"Human errors is inevitable and now they counting from 1 to {nume:,}"

print(a)