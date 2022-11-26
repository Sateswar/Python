# numberOfCharacters=len(input("Name : "))
# #numberOfCharacters=(input("Name : "))

# if type(numberOfCharacters) is int: print("Your Name has "+str(numberOfCharacters)+" characters")
# else:print("Input parameter is not a number, please enter a number")
# #print("Your Name has "+ numberOfCharacters+" characters")

# Summing up two digit 
# #########################
# two_digit_number = input("Type a two digit number: ")
# # print(str( int( two_digit_number[0])+ int( two_digit_number[1])))
# # print(type(two_digit_number))
# if type(int(two_digit_number)) is int: print (str( int( two_digit_number[0])+ int( two_digit_number[1])))
# else: print ("Please enter a number")

######### Summing digits of a number #####
inputNumber=input("Type a number ")
sum=0
for i in inputNumber:
  sum=int(i)+sum
  
print (str(sum))
    



