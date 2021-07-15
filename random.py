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


# print("Printing some value")
# for i in range(10, 5):
# 	print(i)



swap_count = 0

def back_propagate(list_s, i, k):
    global swap_count
    while i > 0 and swap_count < k:
        if list_s[i] < list_s[i-1]:
            list_s[i], list_s[i-1] = list_s[i-1], list_s[i]
            swap_count += 1
        else: break
        i -= 1
    return list_s

def solution(S, K):
    global swap_count

    list_s = list(S)
    for i in range(1, len(list_s)):
        if swap_count < K:
            if list_s[i] < list_s[i-1]:
                list_s = back_propagate(list_s, i, K)
        else: break
    
    S = "".join(list_s)
    return S


# A string S is given. In one move, any two adjacent letters can be swapped. For example, given a string "abcd", it's possible to create "bacd", "acbd" or "abdc" in one such move. What is the lexicographically minimum string that can be achieved by at most K moves?

# Write a function:

# def solution(S, K)

# that, given a string S of length N and an integer K, returns the lexicographically minimum string that can be achieved by
#  at most K swaps of any adjacent letters.

# Examples:

# 1. Given S = "decade" and K = 4, your function should return "adcede". Swaps could be:

# decade → dceade,

# dceade → dcaede,

# dcaede → dacede,

# dacede → adcede.

# 2. Given S = "bbbabbb" and K = 2, your function should return "babbbbb". The swaps are:

# bbbabbb → bbabbbb,

# bbabbbb → babbbbb.

# 3. Given S = "abracadabra" and K = 15, your function should return "aaaaabrcdbr".

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# string S consists only of lowercase letters ('a'-'z');
# K is an integer within the range [0..1,000,000,000].



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def inc_char(ch):
    if ch == 'z':
        ch = chr(ord(ch) + 1)
    return chr(ord(ch) + 1)

def back_propergate(s_list, i, k, swap_count, to_swap):
    while i > 0 and swap_count < k:
        if s_list[i] < s_list[i-1]:

            to_swap[s_list[i-1]].remove(i-1)
            to_swap[s_list[i-1]].add(i)

            s_list[i], s_list[i-1] = s_list[i-1], s_list[i]
            swap_count += 1
        else: break
        i -= 1
    return swap_count

def solution(S, K):
    S_list = list(S)
    N = len(S_list)
    swap_count = 0
    to_swap = {}
    min_char = 'a'

    index = 0
    # change this to a while and make sure to account for when index i > K for which we know we can't possibly swap min_char to position 0
    while index < N:
        if swap_count < K:
            if S_list[index] == min_char:
                swap_count = back_propergate(S_list, index, K, swap_count, to_swap)
            else:
                indexes = to_swap.get(S_list[index])
                if indexes is None: indexes = {index}
                else: indexes.add(index)
                to_swap[S_list[index]] = indexes
        else: break

        index += 1
        if index > K: break

    min_char = inc_char(min_char)
    while len(to_swap) > 0 and swap_count < K:
        if to_swap.get(min_char) is not None:
            while len(to_swap[min_char]) > 0:
                min_index = min(to_swap[min_char])
                if min_index
                to_swap[min_char].remove(min_index)

            for i in to_swap[min_char]:
                swap_count = back_propergate(S_list, i, K, swap_count, to_swap)


    S = "".join(S_list)
    return S


my_dic = {}
print(len(my_dic))