from os import system
system("cls")

a = int(input("Element sonini kiriting: "))
lst = []
for i in range(a):
    b = input()
    lst.append(b)
# print(lst)
for i in range(len(lst) - 1):
    if int(lst[i]) > 0 and int(lst[i + 1]) > 0 or int(lst[i]) < 0 and int(lst[i + 1]) < 0 :
        print(lst[i], lst[i + 1])
    
