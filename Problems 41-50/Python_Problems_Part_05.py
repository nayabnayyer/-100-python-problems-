# 41: Finding second largest number in List
def second_largest():
    nums = list(map(int, input("Enter numbers: ").split()))
    
    if len(nums) < 2:
        print("Need at least 2 numbers")
        return
    
    largest = second = float("-inf")

    for num in nums:
        if num > largest: # if this number is larger than current largest
            second = largest  # then the old biggest number becomes second largest number
            largest = num  # and new number becomes largest 
        elif num> second and num!= largest: # now if a number is greater than second one and NOT equal to largest
            second = num  # then this number becomes second largest 
    
    if second == float('-inf'):
        print("No second largest found")
    else:
        print(f"Second largest: {second}")

second_largest()

# 42. Merging 2 lists 

def merge_sorted_lists():
    list1 = list(map(int, input("Enter first sorted list: ").split()))
    list2 = list(map(int, input("Enter second sorted list: ").split()))
    
    list1.sort()
    list2.sort()
    
    print(f"Sorted list1: {list1}")
    print(f"Sorted list2: {list2}")

    i = j = 0  # starting index of both lists is 0
    merged = []
    
    while i<len(list1) and j<len(list2):
        if list1[i]<list2[j]:
            merged.append(list1[i])
            i+ = 1
        else:
            merged.append(list1[j])
            j+ = 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    print(f"Merged: {merged}")

merge_sorted_lists()

# 43. Matrix Addition

def matrix_addition():
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    
    print("Matrix A:") 
    A = [list(map(int, input().split())) for _ in range(rows)]
    
    print("Matrix B:") 
    B = [list(map(int, input().split())) for _ in range(rows)]
    
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    
    print("Result:") 
    for row in result:
        print(row)

matrix_addition()

# 44. Transpose of a Matrix

def transpose_matrix():
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))
    
    print(f"Enter {rows} rows of {cols} numbers each:")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Transpose using nested list comprehension
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    print("\nTransposed matrix:")
    for row in transposed:
        print(row)

transpose_matrix()

# 45. Flatten a Nested List

def flatten_list():
    print("Enter your nested list one inner list at a time.")
    print("Example: For [[1,2], [3,4]], enter '1 2' then '3 4'")
    print("Type 'done' when finished.\n")
    
    nested = []
    while True:
        user_input = input("Enter inner list numbers:")
        if user_input.lower() == 'done':
            break
        # Convert the input string into a list of integers
        inner_list = list(map(float, user_input.split()))
        nested.append(inner_list)
    
    # Flatten the nested list
    flat = []
    flat = sorted([item for sublist in nested for item in sublist])
    
    print(f"\nNested list: {nested}")
    print(f"Flattened: {flat}")

flatten_list()

# 46. GCD (Euclidean Algorithm)

def find_gcd():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    original_a, original_b = a, b
    
    while b:
        a, b = b, a % b
    
    print(f"GCD of {original_a} and {original_b} is: {a}")

find_gcd()

# 47.  LCM (Using GCD)

def find_lcm():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    original_a, original_b = a, b
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    lcm = (a * b) // gcd(a, b)
    print(f"LCM of {original_a} and {original_b} is: {lcm}")

find_lcm()

# 48. Palindrome List (Two-Pointer)

def palindrome_list():
    nums = list(map(int, input("Enter numbers: ").split()))
    
    left, right = 0, len(nums) - 1
    is_pal = True
    
    while left < right:
        if nums[left] != nums[right]:
            is_pal = False
            break
        left += 1
        right -= 1
    
    print(f"{nums} is {'a palindrome' if is_pal else 'not a palindrome'}")

palindrome_list()

# 49. Linear Search

def linear_search():
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Enter target: "))
    
    index = -1
    for i in range(len(nums)):
        if nums[i] == target:
            index = i
            break
    
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")

linear_search()

# 50. Binary Search (The Big Boss)

def binary_search():
    nums = list(map(int, input("Enter SORTED numbers: ").split()))
    target = int(input("Enter target: "))
    
    left, right = 0, len(nums) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            found = True
            print(f"Found at index {mid}")
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if not found:
        print("Not found")

binary_search()
