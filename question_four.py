# 4(i)
#a) 
""" 
OOP is a class defined function containing attributes.
It is important in providing more flexibility and organization in programs.
"""

#b) 
""" 
Class is the container for the attributes.
It is different from objects because it is the root of an instance while the object is an attribute. 
"""

# 4(ii)

sentence = ("What is a class in a class?")
words = sentence.split()
print(words)


for word in words:
    word_count = words.count(word)
print(f"{word}:{word_count}")

# 4(iii)

def sum():
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    sum = a+b

    print(f"The sum of a and b is {sum}")

sum()

# 4(iv)

class Car():
    def __init__(self:Car):
        self.brand = brand
        self.name = name
        self.color = color

    
    car('Benz', 'M10', 'Pink')
    print(car)

Car()

# 4(v)
class Car():
    def __init__(self:Car):
        self.brand = brand
        self.name = name
        self.color = color
        self.message = start_engine

    car = ('Benz', 'M10', 'Pink', 'Started')
    print(car)

Car()