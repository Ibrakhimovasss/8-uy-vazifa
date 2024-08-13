from os import system
system("cls")
a = int (input("Sonni kiriting: "))
dic = [
    {
        "name" : "bread",
        "price" : 100,
    }, 
    {
        "name" : "wine",
        "price" : 138,
    }, 
    {
        "name" : "meat",
        "price" : 15,
    }, 
    {
        "name" : "water",
        "price" : 1,
    }
]
count = 0
dic.sort(key= lambda x:  x["price"], reverse=True)
for i in dic:
    count += 1
    if count <= a:
        print(f"{i['name']}, {i["price"]}")