# 31. Find the largest element in a list

def largest_element():
    numbers = list(map( int, input("Enter numbers: ").split()))

    if not numbers:
        print("List is empty")
        return 
    
    largest = numbers[0]
    for num in numbers:
        if num>largest:
            largest = num
    
    print(f"Largest number is {largest}")

largest_element()

# 32. Find the smallest element in a list 

def smallest_element():
    numbers = list(map( int, input("Enter numbers: ").split()))

    if not numbers:
        print("List is empty")
        return 
    
    smallest = numbers[0]
    for num in numbers:
        if num<smallest:
            smallest = num
    
    print(f"Smallest number is {smallest}")

smallest_element()

# 33. Find the sum of all elements in a list
def find_sum():
    numbers = list(map( int, input("Enter numbers: ").split()))

    total = 0
    for num in numbers:
        total+=num
    print(f"Total sum of all the numbers in list is: {total}")
find_sum()

# 34. Find the average of all elements in a list
def find_sum():
    numbers = list(map( int, input("Enter numbers: ").split()))

    total = 0
    for num in numbers:
        total+=num
    average = total/len(numbers)

    print(f"Average of all the numbers in list is: {average}")
find_sum()

# 35. Check if a list is empty

def is_empty():
    user_input = input("Enter numbers separated by spaces (or press Enter for empty): ")
    
    if user_input.strip() == "":
        numbers = []
    else:
        numbers = list(map(int, user_input.split()))
    
    if not numbers:
        print("The list is EMPTY ✅")
    else:
        print(f"The list has {len(numbers)} element(s): {numbers}")

is_empty()

# 36. Count how many times an element appears in a list

def count_occurrences():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter the number to count: "))
    
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    
    print(f"{target} appears {count} time(s)")

count_occurrences()

# 37. Remove duplicates from a list

def remove_duplicates():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    
    print(f"Original: {numbers}")
    print(f"Without duplicates: {unique}")

remove_duplicates()

# 38. Reverse a list (without using reverse())

def reverse_list():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    # Using slicing (easiest)
    reversed_slicing = numbers[::-1]
    
    # Using loop (manual way)
    reversed_loop = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_loop.append(numbers[i])
    
    print(f"Original: {numbers}")
    print(f"Reversed (slicing): {reversed_slicing}")
    print(f"Reversed (loop): {reversed_loop}")

reverse_list()

# 39. Check if two lists are identical

def are_identical():
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))
    
    if len(list1) != len(list2):
        print("Lists are NOT identical (different lengths)")
        return
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print("Lists are NOT identical (elements differ)")
            return
    
    print("Lists are IDENTICAL ✅")

are_identical()

# 40. Find common elements between two lists

def find_common():
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))
    
    common = []
    for num in list1:
        if num in list2 and num not in common:
            common.append(num)
    
    print(f"Common elements: {common}")

find_common()
    

