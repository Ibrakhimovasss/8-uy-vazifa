from os import system
system("cls")

soz = input("Sozni kiriting: ")

right_hand = [1, 2, 3, 4, 5, "Q", "A", "Z", "W", "S", "X", "E", "D", "G", "R", "F", "V", "T", "G", "B"]
left_hand = [6, 7, 8, 9, 0, "Y", "H", "N", "U", "J", "M", "I", "K", ",", ".", "O", "L", "P", ":", "/"]

count1 = 0
count2 = 0

right_hand_u = []
left_hand_u = []

for i in right_hand:
    right_hand_u.append(str(i).upper())

for i in left_hand:
    left_hand_u.append(str(i).upper())

for i in soz.upper():
    if i in right_hand_u:
        count1 += 1
    elif i in left_hand_u:
        count2 += 1

print(f"O'ng qo'lda {count1} ta belgi yozilgan!")
print(f"Chap qo'lda {count2} ta belgi yozilgan!")
