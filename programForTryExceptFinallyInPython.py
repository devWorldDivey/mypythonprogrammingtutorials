""" Program for try except finally in python """
number1 = int(input("Enter a number"))
number2 = int(input("Enter another number"))
try:
    print("When First number is divided by second we get ", (number1//number2))
except Exception as e:
    print(e)
finally:
    print("Program Closed")