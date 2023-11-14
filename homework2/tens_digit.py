number = input("Enter an integer that is larger than 9: ")
quotient = (int(number) // 10)
remainder = (int(quotient) % 10)
print("It has a tens digit of " + str(remainder) + ".")