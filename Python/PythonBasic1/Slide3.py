# def switch_case(argument):
#     switcher={
#         1:"T2",
#         2:"T3",
#         3:"T4",
#         4:"T5",
#         5:"T6",
#         6:"T7",
#         7:"CN",
#     }
#     return switcher.get(argument,"Khong xac dinh")
# day_in_week=input("Nhap ngay trong tuan")
# print(switch_case(int(day_in_week)))


################################################################
# list=['banana','apple','orange','mango']
# for i in list:
#     print("I have : ",i)


################################################################
# i=0
# while i<=10:
#     print(i)
#     i+=1


################################################################
def HCN():
    length=int(input("Enter the length of the rectangle: "))
    width=int(input("Enter the width of the rectangle: "))
    for i in range (length) :
        for j in range (width):
            print("*", end="")
        print()
HCN()