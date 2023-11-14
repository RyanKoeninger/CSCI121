num = int(input("Enter a three digit number: "))

ones = num % 10
tens = (num // 10) % 10
hunds = (num // 100) % 10

if num < 0:
    print("That number is negative.")
    print("Please try again.")

elif num < 10:
    print("That number has only one digit.")
    print("Please try again.")

elif num < 100:
    print("That number has only two digits.")
    print("Please try again.")

else:
    print("Thank you.")
    print("Its hundreds digit is " + str(hunds) + ".")
    print("Its tens digit is " + str(tens) + ".")
    print("Its ones digit is " + str(ones) + ".")
    

