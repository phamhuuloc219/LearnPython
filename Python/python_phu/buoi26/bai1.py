def reverse_list(list):
    result = []
    for i in range(len(list)):
        result.insert(0, list[i])
    return result

arr = [5,6,3,1,64]
print(reverse_list(arr)) 