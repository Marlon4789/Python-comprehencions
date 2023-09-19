
# Return a function

def sum_range(min, max):
    sum = 0
    for i in range(min, max):
        sum += i
    return sum

result = sum_range(1, 10)
print(result)
result_2 = sum_range(result, result + 10)
print(result_2)
