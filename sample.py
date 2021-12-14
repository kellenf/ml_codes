import numpy as np
def sample(number: list):
    num_sum = sum(number)
    new_num = number[:]
    new_num = new_num / num_sum
    for i in range(1, len(new_num)):
        new_num[i] += new_num[i - 1]
    
    i, j = 0, len(new_num) - 1
    rn = np.random.randn()
    index = 0
    while i < j:
        mid = (i + j) / 2
        if new_num[mid] >= rn:
            index = mid
            j = mid - 1
        else:
            i = mid + 1
    return number[index]

def find_first_large(number, value):
    i, j = 0, len(number) - 1
    index = -1
    while i < j:
        mid = (i + j) // 2
        if number[mid] < value:
            i = mid + 1
        else:
            j = mid - 1
            index = mid
    if  i == j and index == -1:
        index = i
    if index == -1:
        return -1
    return number[index]

number = [0, 4, 7, 9, 11, 22, 33]
print(find_first_large(number, 13))
print(find_first_large(number, 24))
print(find_first_large(number, 9))