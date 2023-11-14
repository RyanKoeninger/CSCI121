num = input("Enter a non-negative integer: ")
dig = input("Enter a digit position: ")
intdig = 10**int(dig)
number = int(num) // 10 ** int(dig) % 10
print("The " + str(10**int(dig)) + "s digit of that integer is " + str(int(number)) + ".")