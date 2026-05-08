# 1. Printing Hello World
print("Hello World!")

# 2. sum of 2 numbers

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print(sum)

# 3. Swapping values 

value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))
value1, value2 = value2, value1
print(f"value1 is {value1}.")
print(f"value2 is {value2}.")

# 4. Even or Odd

number = int(input("Enter a number: "))
if number%2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 5. Maximum of 2 numbers

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
if number_1 > number_2:
    maximum = number_1
else:
    maximum = number_2
print(f"The maximum of 2 numbers is {maximum}.")

# 6. Celcius to Farenhite
temperature_in_celcius = int(input("Enter temperature: "))
temperature_in_farenhite = (temperature_in_celcius*9/5)+32
print(f"The temperature in farenhite is {temperature_in_farenhite}.")

# 7. Leap Year
year = int(input("Enter a year: "))
if year%4 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

# 8. Factorial of a number
number = int(input("Enter a number: "))
factorial = 1
if (number < 0):
    print("Factorial of negative numbers doesn't exist.")
elif (number == 0):
    print("Factorial of 0 is 1")
else:
    for i in range(1, number+1):
        factorial=factorial*i
    print(f"Factorial of {number} is {factorial}.")

# 9. Calculator in python 
print( """Choose the operation:" \n
"       1. Addition" \n
"       2. Subtraction" \n
"       3. Multiplication" \n
"       4. Division" \n
"       5. Exponent\n""")

operation = int(input("Enter operation you want to perform: "))

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if operation == 1:
    print("Sum is = ", num1 + num2)

elif operation == 2:
    print("Difference is = ", num1 - num2)

elif operation == 3:
    print("Multiplication is =", num1*num2)

elif operation == 4:
    print("Division is =", num1/num2)

elif operation == 5:
    print("Exponent is =", num1**num2)

else:
    print("Invalid Choice.")

# 10. Multiplcation Table

num = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")



