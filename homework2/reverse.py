digit = input("Enter a 3-digit integer: ")
dig3 = int(digit) //100 % 10
dig2 = int(digit) //10 % 10
dig1 = int(digit) % 10
print(str(dig1) + str(dig2) + str(dig3))