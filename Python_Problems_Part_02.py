# 11. Sum of first n natural numbers 

n = int(input("Enter a natural number n: "))

if n < 0:
    print("Please enter a positive number")
else:
    SUM = n*(n+1)//2
    print(f"The sum of first {n} natural numbers is {SUM}.")

# 12. Count the number of digits in a given integer.

number = int(input("Enter a number:"))
count = len(str(number))
print(f"The number of digits in {number} is {count}.")
if ( count % 2 == 0 ):
    print("The integer count is even!")
else:
    print("The integer count is odd!")

# 13. Reverse the digits of a user-provided number.

number = int(input("Enter a number:"))
reverse = str(number)[::-1]
print(f"The reverse of {number} is {reverse}.")

# 14. Checking if given number or string is palindrome or not 

def is_palindrome(text):
    # Turn it into a string just in case it's a number
    text = str(text).lower() 
    reversed_text = text[::-1]
    
    # Return the result of the comparison (True or False)
    return text == reversed_text

# Use input() without int() so it can accept words AND numbers
user_input = input("Enter a string or number: ")

if is_palindrome(user_input):
    print(f"Yes, '{user_input}' is a palindrome.")
else:
    print(f"No, '{user_input}' is not a palindrome.")

# 15. Check if a 3-digit number is an Armstrong number (e.g., \(153 = 1^3 + 5^3 + 3^3\)

def is_armstrong(num):
    str_num = str(num)
    power = len(str_num)

    total_sum = 0

    for digits in str_num:
        total_sum+=int(digits)**power

user_num = int(input("Enter a number: "))

if is_armstrong(user_num):
    print(f"{user_num} is an armstrong number.")
else:
    print(f"{user_num} is not an armstrong number.")

# 16. Checking if a number is prime 
def is_prime(num):
    if num<2:
        return False
    
    for i in range(2,num):
        if n%i==0:
            return False
        return True
    
n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number!")
else:
    print(f"{n} is not a prime number!")

# 17. a. First 10 fibonacci numbers
a = 0
b = 1
print("First 10 fibonacci numbers:\n ")
for i in range(10):
    print(a, end= " ")
    next_num = a+b
    a=b
    b = next_num

# 17. b. Displaying fibonacci numbers through user input
n = int(input("how many fibonacci numbers? "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    a,b = b, a+b

# 18. Print all factors of a number 

def find_factors(n):
    print(f"Factors of {n} are:")
    for i in range(1,n+1):
        if n%i==0:
            print(i, end = " ")
num = int(input("Enter a number: "))
find_factors(num)

# 19. Determine if a given character is a vowel or consonant

def is_vowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

def is_consonant(chat):
    return char.isalpha() and not is_vowel(char)

char = input("Enter a character: ")
if is_vowel(char):
    print(f"{char} is a vowel!")
elif is_consonant(char):
    print(f"{char} is a consonant!")
else:
    print(f"{char} is not a letter at all.")

# 20. Print ASCII value of any character

def get_ascii(char):
    '''Return ASCII value of character'''
    if len(char)!=1:
        return "Please enter exactly one character."
    return ord(char)

char = input("Enter a character: ")
result = get_ascii(char)
if isinstance(result, int):
    print(f"ASCII value of {char} is {result}")
else:
    print(result)
