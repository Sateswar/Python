# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(',')
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)


#Write your code below this row 👇
lenth=0
totalHeight=0
for height in student_heights:
    lenth=lenth+1
    totalHeight=totalHeight+height

averageHeight=totalHeight/lenth
print("Length of student_heights list is : " + str(lenth))
print("averageHeight height of student_heights is : " +str(averageHeight))



