from os import system
from json import dumps
system("cls")
#O'shish tartibida joylash

a = str(int(input("Enter a number: ")))

dic  = {}

for i in a:
    dic[i] = a.count(i)
print(dumps(dic, indent = 2))

