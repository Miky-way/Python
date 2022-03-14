# Memory locations in python are integer and can be gotten using the id() function
# E.g;
# tuple1 = (1, 2, 3, 4, 5)
# tuple1_id = id(tuple1)
# print("Tuple1:", tuple1, "\nTuple1 id:", tuple1_id)

# tuple2 = (1, 2, 3, 4, 5)
# tuple2_id = id(tuple2)
# print("Tuple2:", tuple2, "\nTuple2 id:", tuple2_id)

# print(hash(tuple1), hash(tuple2))

# # UNDERSTAND MEMORY LOCATIONS
# # HASHING AND HASH VALUES
# # id() FUNTION IN PYTHON

'''CHECK THIS OUT'''
result = 1 < 2 < 6 < 4 < 5 # So you can combine operators like this... WAWU
print(result)


'''AWESOME ZIP FUNCTION'''
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
# write your for loop here
for l, x, y, z in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(l, x, y, z))


cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))


'''UNZIPING'''
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
names, heights = zip(*cast)


'''ENUMERATE'''
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, name in enumerate(cast):
    cast[i] = name+' {}'.format(heights[i])



'''LIST COMPREHENSIONS'''
capitalized_cast = [name.title() for name in cast]

squares = [x**2 for x in range(9) if x % 2 == 0] # With if condition

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)] # With if else condition


''' Codality fast and ferious solutions 1'''
def solution1(A):
    total_times = set()
    divisor = 7 + 10**9

    for pom in range(len(A)-1): # pom => position of motorway
        total_times.add(cal_total_time(A, pom))
 
    return min(total_times) % divisor

def cal_total_time(A, pom): 
    total_time = 0
    N = len(A)
    for i in range(N-1):
        if i < pom:
            total_time += A[pom] - A[i]
        elif i > pom:
            total_time += A[N-1] - A[i]

    return total_time


''' Codality fast and ferious solutions 2'''
def solution2(A):
    N = len(A)
    divisor = 7 + 10**9
    mid_index = (N-1) // 2 # index of mid position

    difference = {}
    lower = mid_index # used to traverse lower end
    upper = mid_index+1 # used to travers upper end

    while lower >= 0 or upper < N-1:
        if lower >= 0:
            diff = A[lower+1] - A[lower]
            if diff not in difference:
                difference[diff] = lower

        if upper < N-1:
            diff = A[upper+1] - A[upper]
            if diff not in difference:
                difference[diff] = upper

        lower -= 1
        upper += 1

    pom = difference[max(difference)]

    return cal_total_time(A, pom) % divisor

''' Codality fast and ferious solutions 3'''
def solution3(A):
    N = len(A)
    divisor = 7 + 10**9
    mid_index = (N-1) // 2 # index of mid position

    difference = {}
    lower = mid_index # used to traverse lower end
    upper = mid_index+1 # used to travers upper end

    while lower >= 0 or upper < N-1:
        if lower >= 0:
            diff = A[lower+1] - A[lower]
            if diff not in difference:
                difference[diff] = lower

        if upper < N-1:
            diff = A[upper+1] - A[upper]
            if diff not in difference:
                difference[diff] = upper

        lower -= 1
        upper += 1

    pom = find_optimized_index(difference, mid_index)

    return cal_total_time(A, pom) % divisor

def find_optimized_index(difference, mid_index):
    max1 = [0, 0]
    max2 = [0, 0]
    for key, value in difference.items():
        if key > max1[0]:
            max2[0] = max1[0]
            max2[1] = max1[1]
            max1[0] = key
            max1[1] = value

    if mid_index-max1[1] >= mid_index-1 and mid_index-max2[1] < mid_index-1:
        return max2[1]
    else: return max1[1]

def solution4(A):
    N = len(A)
    divisor = 7 + 10**9
    
    current_cost = 0
    for i in range(1, N-1): current_cost += A[N-1] - A[i]

    best = current_cost # Starting with  the total_time for motorway in postion 0

    for i in range(1, N-1):
        current_cost -= A[N-1] - A[i]
        current_cost += i * (A[i] - A[i-1])

        best = min(best, current_cost)

    return best % divisor

# A = [10, 20, 21, 27, 29, 30, 36, 40]
A = [10, 20, 21, 24, 31, 33, 40, 44]

print('Solution 1 = ', solution1(A))
print('Solution 2 = ', solution2(A))
print('Solution 3 = ', solution3(A))
print('Solution 4 = ', solution4(A))

print('')

print('Sum with pom=0: ', cal_total_time(A, 0))
print('Sum with pom=1: ', cal_total_time(A, 1))
print('Sum with pom=2: ', cal_total_time(A, 2))
print('Sum with pom=3: ', cal_total_time(A, 3))
print('Sum with pom=4: ', cal_total_time(A, 4))
print('Sum with pom=5: ', cal_total_time(A, 5))
print('Sum with pom=6: ', cal_total_time(A, 6))
print('Sum with pom=7: ', cal_total_time(A, 7))

# Golden badge: https://app.codility.com/cert/view/cert7PGVY8-S5KVSFU9R6HD2XKZ/
# Silver badge: https://app.codility.com/cert/view/certXN9YU5-82W34B7ZWM7JDE96/







# Find common char
def common_chars(str1, str2):
    str1 = set(str1) # Returns all unique characters in str1 as a set
    common_chars = set()
    for char in str2:
        if char in str1:
            common_chars.add(char)
    return common_chars
