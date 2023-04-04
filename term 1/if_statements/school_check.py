user_input = int(input("How old is your child? "))

#Using the and, or conditional operators, we can check multiple conditions in one if statement
#There is a difference between if and elif. Python will only check the elif statements if the statement above
#it is false. Python will check if statements regardless of the above statement.
if user_input >= 6 and user_input <= 9:
    print("Your kid should go to Ormiston Primary School.")
elif user_input >= 10 and user_input <= 14:
    print("Your kid should go to Ormiston Junior College.")
elif user_input >= 15 and user_input <= 18:
    print("Your kid should go to Ormiston Senior College.")
elif user_input <= 5 or user_input > 18:
    print("Your child is the wrong age!")
else:
    print("Invalid input")