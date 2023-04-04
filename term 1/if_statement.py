#Get the user input and convert it to an integer
user_input = int(input("Enter a number: "))

#If user_input divided by 2 has no remainder then it must be even
if user_input % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd")

    