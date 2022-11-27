# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if type(age) is not int: print("Please enter a number")
else: 
    noOfYears = int(90-age)
    noOfMonths = int(noOfYears*12)
    noOfWeeks = int(noOfYears*52)
    noOfDays = int(noOfYears*365)
    print(f"you have {noOfYears} years, {noOfMonths} months, {noOfWeeks} weeks and {noOfDays} days to reach 90 years.")
