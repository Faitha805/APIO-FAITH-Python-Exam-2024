# 1.(i)

def circle_area():
    raduis = int(input("Enter the raduis of the circle: "))

    area = 3.14 * (raduis**2)

    print(f"The area of the circle with raduis of {raduis} is: {area} ")

circle_area()

# 1.(ii)

integers = [4, 7, 2, 9, 12, 15]
odd_sum = 0

for odd_numbers in integers:
    if odd_numbers % 2 != 0:
         odd_sum += odd_numbers 
         print(f"The sum of th odd numbers in the list of integers is: {odd_sum}")


# 1.(iii)

def number_operation():
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))

    sum = number_one + number_two
    print(f"The sum of the two numbers is: {sum}")

    difference = number_one - number_two
    print(f"The difference of the two numbers is: {difference}")

    product = number_one * number_two
    print(f"The product of the two numbers is: {product}")

    quotient = number_one / number_two
    print(f"The quotient of the two numbers is: {quotient}")

number_operation()

# 1.(v)

# Dictionary
student_info = {'name':'Alice', 'age': 20, 'grade':'A'}

#Updating the value of 'age' to 26
student_info['age'] = 26

# Adding a new key-pair value
update_info = {'city':'Kampala'}
student_info.update(update_info)
print(student_info)
