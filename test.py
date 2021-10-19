def solution(A):
    d_sum = find_max_sum(A) # Our desired sum value
    
    for i in range(3):
        row_sum = sum_axis(A, i)
        if row_sum < d_sum:
            diff = d_sum - row_sum

            for j in range(3):
                col_sum = sum_axis(A, j, 1)
                if col_sum + diff <= d_sum:
                    A[i*3 + j] += diff
                    break
    return A

def find_max_sum(A):
    max_sum = 0
    axis = 0
    index = 0
    while index < 3:
        r_sum = sum_axis(A, index, axis)
        max_sum = r_sum if r_sum > max_sum else max_sum

        index += 1
        if index == 3 and axis == 0:
            axis = 1
            index = 0
            
    return max_sum

# index: Index to sum
# axis: weather row (0) or column (1)
def sum_axis(A, index, axis=0):
    r_sum = 0
    if axis == 0: # sum row
        for i in range(3):
            r_sum += A[index*3 + i]
    else: # for column
        for i in range(3):
            r_sum += A[i*3 + index]

    return r_sum

