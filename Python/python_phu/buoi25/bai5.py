def filter_number(list):
    result = []
    for i in range(len(list)):
        if type(i) == int or type(i) == float:
            result.append(i)
    return result

arr = [4, 5, True, "abc", 6.234]

filtered_list = filter_number(arr)

print("Danh sách sau khi lọc:", filtered_list)