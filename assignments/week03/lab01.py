# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
if age >= 60 :
    print("You are Senior")
elif age >= 30:
    print ("You are Adult")
elif age >= 13:
    print ("You are Teenager")
elif age >= 0:
    print("You are Child")
else:
    print ("plese do it again")

