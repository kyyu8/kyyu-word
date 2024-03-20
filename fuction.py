#create a 2D list (array)
from array import *
#Glasses of water per day in a week
water = [[11, 12, 5, 2],
         [15, 6, 10],
         [10, 8, 12, 5],
         [12, 15, 8, 6]]
print(water) #printing the array
print(water[3][3]) #printing specific element
print(water[2]) #printing row number 2

for row in range(0,len(water),1):
    for column in range(0, len(water[row]), 1):
        if (row == 1 & column == 2):
            water[row][column] = "I see you"
        print(water[row][column], end=" ")
    print(end="\n")
ac = [0, 8, 13, 9, 7],
         [9, 8, 12, 19],
         [8, 15, 17],
print(ac)
print(ac[6])
print(ac[6][5])