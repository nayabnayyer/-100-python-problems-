# 21. Check if three angles can form a triangle (sum must be 180°)
def check_triangle():
    try:
        angle_1 = float(input("Enter first angle: "))
        angle_2 = float(input("Enter second angle: "))
        angle_3 = float(input("Enter third angle: "))
        
        Sum_of_angles = angle_1+angle_2+angle_3

        if angle_1>0 and angle_2>0 and angle_3>0:
            if(Sum_of_angles == 180):
                print("These three angles form a triangle.")
            else:
                print("These three angles don't form a triangle.")
        else:
            print("Enter angles greater than 0.")

    except ValueError:
        print("Please enter a valid value. ")
        
check_triangle()

# 22. Determine profit or loss based on cost and selling price.

def checking_profit_loss():
    try:
        sale_price = float(input("Enter the selling price: "))
        cost_price = float(input("Enter the cost price: "))

        if(sale_price>cost_price):
            profit = sale_price-cost_price
            print(f"Profit is: {profit:.2f}")
        elif(cost_price>sale_price):
            loss = cost_price-sale_price
            print(f"Loss is: {loss:.2f}")
        else:
            print("There is no progit no loss.")
    
    except ValueError:
        print("Enter a valid numeric value.")

checking_profit_loss()
 
# 23. Calculate compound interest for given principal, rate, and time

def calculate_compound_interest():
    try:
        principal = float(input("Enter principal amount (P): "))
        rate = float(input("Enter rate in (%): "))
        time = float(input("Enter time (in years): "))

        if principal<=0 and rate<=0 and time<=0:
            print("Enter positive values for principal, rate and time.")
            return
        
        rate_decimal = rate/100    # finds interest rate in poooints to fit the formula better for calculations

        amount = principal * (1 + rate_decimal) ** time
        compound_interest = amount - principal

        print(f"\n--- Results ---")
        print(f"Principal Amount: {principal:.2f}")
        print(f"Rate of Interest: {rate}%")
        print(f"Time Period: {time} years")
        print(f"Total Amount: {amount:.2f}")
        print(f"Compound Interest: {compound_interest:.2f}")
        
    except ValueError:
        print("Please enter valid numeric values only.")

calculate_compound_interest()

# 24. Convert a decimal number to its binary equivalent

def decimal_to_binary():
    n = int(input("Enter a number: "))
    try: 
        if n == 0:
            print("Binary equivalent of 0 is: 0")
            return
        
        binary = ""
        original = n

        while n>0:
            remainder = n%2    # this section takes remainder until quotient becomes 0
            binary = str(remainder)+binary # 
            n = n//2

        print(f"Binary equivalent of {original} is: {binary} ")

    except ValueError:

        print("Enter a valid integer.")
decimal_to_binary()

# 25. Convert a binary string back to a decimal integer.

def binary_to_decimal():
    try:
        binary_string = input("Enter the string in binary: ")
        if not binary_string:
            print("Please enter a binary number.")

        decimal = 0
        power = 0

        for digits in reversed(binary_string):
            if digits not in ('0', '1'):
                print("Invalid input. Please use 0 and 1 only.")

            decimal = int(digits)*(2**power)
            power+=1
        
        print(f"Decimal of {binary_string} is: {decimal}")

    except Exception as e:
        print("An error occured!", e)

binary_to_decimal()

# 26. Generate a random integer between 1 and 100.

import random 

def generate_random_number():
    try:
        random_number = random.randint(1,100)
        print(F"The random number is {random_number} ")

    except Exception as e:
        print("Something went wrong.")

generate_random_number()

# 27. Print a simple right-angled triangle of stars (*).

def triangle_of_stars():
    try:
        rows = input(print("Enter number of rows: "))
        if rows<=0:
            print("Enter a valid digit/number of rows.")

        for i in range(1, rows+1):
            print("* "*i)
    except Exception as e:
        print("Something went wrong.", e)
triangle_of_stars()

# 28. Find the length of a string without using the len() function.

def len_of_string():
    try: 
        string = input("Enter a string: ")
        count = 0
        for char in string:
            count+=1
        print(f"The length of string is {count}")
    except Exception as e:
        print("Something went wrong!", e)
len_of_string()

# 29.  Count the number of vowels in a string

def count_vowels():
    try:
        string = input("Enter a string:" )
        vowels = "aeiouAEIOU"
        count+=1
        for char in string:
            if vowels in string:
                count+=1
        print(f"The vowels in string are {count}")
    except Exception as e:
        print("Something went wrong!", e)
count_vowels()

# 30. Reverse a string provided by the user. (A. through string slicing)

def reverse_string_slicing():
    try:
        text = input("Enter a string: ")
        reversed_text = text[::-1]
        print(f"Reversed: {reversed_text}")
    except Exception as e:
        print("An error occurred:", e)

reverse_string_slicing()

# 30. Reverse a string provided by the user. (B. through using loop)

def reverse_string_loop():
    try:
        text = input("Enter a string: ")
        reversed_text = ""
        
        for char in text:
            reversed_text = char + reversed_text  # Add each char to the FRONT
        
        print(f"Reversed: {reversed_text}")
    except Exception as e:
        print("An error occurred:", e)

reverse_string_loop()


