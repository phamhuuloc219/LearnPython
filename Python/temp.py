# #Slide 2
# birth_year=int(input("Enter your birth year: "))
# current_year=2024
# age=current_year-birth_year
# print("Current age: ", age)

# #Slide 3
# length_rec=int(input("Enter your length rectangle: "))
# width_rec=int(input("Enter your width rectangle: "))
# for i in range (length_rec) :
#     for j in range (width_rec) :
#         print("*",end="")
#     print()

# #Slide 4
# count=0
# sentence="Hello, I'm PHL, a student at NTU. Today, I learning Python. I'm fine"
# check=str(input("Enter a word: "))
# sentence_chuyen=sentence.split()
# for i in sentence_chuyen :
#     if(i==check):
#         count+=1
# print(count)

# def tinh_giai_thua(n):
#     giai_thua = 1
#     if n == 0:
#         return 1
#     else:
#         for i in range(1, n + 1):
#             giai_thua *= i
#         return giai_thua
# n = int(input(""))
# kq = tinh_giai_thua(n)
# print(kq)

# def tim_phep_hop(A, m, B, n):
#     i = 0
#     j = 0
#     prev_a = -1
#     prev_b = -1

#     print("", end="")

#     while i < m and j < n:
#         if A[i] < B[j]:
#             if A[i] != prev_a:
#                 print(A[i], end=" ")
#                 prev_a = A[i]
#             i += 1
#         elif B[j] < A[i]:
#             if B[j] != prev_b:
#                 print(B[j], end=" ")
#                 prev_b = B[j]
#             j += 1
#         else:
#             if A[i] != prev_a:
#                 print(A[i], end=" ")
#                 prev_a = A[i]
#             i += 1
#             j += 1

#     while i < m:
#         if A[i] != prev_a:
#             print(A[i], end=" ")
#             prev_a = A[i]
#         i += 1

#     while j < n:
#         if B[j] != prev_b:
#             print(B[j], end=" ")
#             prev_b = B[j]
#         j += 1

#     print()


# line = input().split()
# m = int(line[0])
# A = [int(x) for x in line[1:]]
# line = input().split()
# n = int(line[0])
# B = [int(x) for x in line[1:]]

# A.sort()
# B.sort()
# tim_phep_hop(A, m, B, n)

# def sap_xep(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def Giao(setA, setB):
#     result = []
#     for element in setA:
#         if element in setB:
#             result.append(element)

#     if result:
#         result.sort()
#         for item in result:
#             print(item, end=' ')
#     else:
#         print("none")


# sizeA = int(input())
# setA = list(map(int, input().split()))

# sizeB = int(input())
# setB = list(map(int, input().split()))

# Giao(setA, setB)


# def sap_xep(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# def Giao(setA, setB):
#     result = []
#     for element in setA:
#         if element in setB:
#             result.append(element)

#     if result:
#         result.sort()
#         for item in result:
#             print(item, end=' ')
#     else:
#         print("none")

# def tim_phep_hop(A, B):
#     i = 0
#     j = 0
#     prev_a = -1
#     prev_b = -1
#     hop = []

#     while i < len(A) and j < len(B):
#         if A[i] < B[j]:
#             if A[i] != prev_a:
#                 hop.append(A[i])
#                 prev_a = A[i]
#             i += 1
#         elif B[j] < A[i]:
#             if B[j] != prev_b:
#                 hop.append(B[j])
#                 prev_b = B[j]
#             j += 1
#         else:
#             if A[i] != prev_a:
#                 hop.append(A[i])
#                 prev_a = A[i]
#             i += 1
#             j += 1

#     while i < len(A):
#         if A[i] != prev_a:
#             hop.append(A[i])
#             prev_a = A[i]
#         i += 1

#     while j < len(B):
#         if B[j] != prev_b:
#             hop.append(B[j])
#             prev_b = B[j]
#         j += 1

#     return hop

# line = input().split()
# m = int(line[0])
# A = [int(x) for x in line[1:]]

# line = input().split()
# n = int(line[0])
# B = [int(x) for x in line[1:]]

# sap_xep(A)
# sap_xep(B)

# Giao(A, B) 
# print()
# hop_result = tim_phep_hop(A, B)
# print(*hop_result)

def sapXep(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def timGiao(setA, setB):
    result = []
    for element in setA:
        if element in setB:
            result.append(element)

    if result:
        result.sort()
        print(*result, end=' ')
    else:
        print("none")

def timHop(A, B):
    i = 0
    j = 0
    prev_a = -1
    prev_b = -1
    union_result = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            if A[i] != prev_a:
                union_result.append(A[i])
                prev_a = A[i]
            i += 1
        elif B[j] < A[i]:
            if B[j] != prev_b:
                union_result.append(B[j])
                prev_b = B[j]
            j += 1
        else:
            if A[i] != prev_a:
                union_result.append(A[i])
                prev_a = A[i]
            i += 1
            j += 1

    while i < len(A):
        if A[i] != prev_a:
            union_result.append(A[i])
            prev_a = A[i]
        i += 1

    while j < len(B):
        if B[j] != prev_b:
            union_result.append(B[j])
            prev_b = B[j]
        j += 1

    return union_result


line = input().split()
m = int(line[0])
A = [int(x) for x in line[1:]]

line = input().split()
n = int(line[0])
B = [int(x) for x in line[1:]]


sapXep(A)
sapXep(B)


timGiao(A, B)
print()

kqHop = timHop(A, B)
print(*kqHop)

# def calculate_set_difference(A, B):
#     return sorted(list(set(A) - set(B)))

# def main():
#     A_input = input("").split()
#     B_input = input("").split()

#     A = [int(x) if x.isdigit() else x for x in A_input]
#     B = [int(x) if x.isdigit() else x for x in B_input]

#     difference = calculate_set_difference(A, B)

#     if len(difference) == 0:
#         print("None")
#     else:
#         print(" ".join(str(x) for x in difference))


# main()

def calculate_set_difference(A, B):
    difference = []
    for element in A:
        if element not in B:
            difference.append(element)
    return sorted(difference)


def hieuAB():
    A_input = input("")
    A_input = A_input.split()
    A_count = int(A_input[0])
    A_elements = [int(x) if x.isdigit() else x for x in A_input[1:]]

    B_input = input("")
    B_input = B_input.split()
    B_count = int(B_input[0])
    B_elements = [int(x) if x.isdigit() else x for x in B_input[1:]]

    # Tính hiệu của hai tập hợp A và B
    difference = calculate_set_difference(A_elements, B_elements)

    # In kết quả
    if len(difference) == 0:
        print("None")
    else:
        difference_str = [str(x) for x in difference]
        difference_output = " ".join(difference_str)
        print(difference_output)
hieuAB()