print("||||          ||||")
print("||||  _/TT\_  ||||")
print("||||  \\\\||//  ||||")
print("||||  '-||-'  ||||")
print("||||          ||||")
print("Welcome to Canada!")
print("------------------")
print()
tempc = int(input("Enter the current temperature in whole degrees Celsius: "))
tempf = (tempc * 9.0) / 5.0 + 32.0
print("That means that it is " + str(int(tempf)) + " degrees Fahrenheit outside.")
print()
print("Let's get the cost of potato chips here in Canadian dollars and cents...")

chipdoll = input("Enter the number of dollars per bag of chips: ")
chipcent = input("Enter the number of cents per bag of chips: ")
bagnum = input("Okay. Enter the number of bags would you like to purchase: ")

if int(bagnum) == 0:
    print ("\nOkay! Thanks for chatting about our beautiful weather.")
else:
    chiptype = input("Enter the chip flavor you prefer [plain, pickle, or ketchup]: ")

    if chiptype != "pickle" and chiptype != "plain" and chiptype != "ketchup":
        chiptype = "plain"
        print("Sounds tasty, but we can only offer you plain chips.")

    totcents = (int(chipcent) * int(bagnum)) % 100 # represents number of cents in final price
    chipcentact = int(chipcent) * int(bagnum) // 100 # represents whole dollars made up of cents
    totdoll = (int(chipdoll) * int(bagnum)) + int(chipcentact)  # represents number of dollars in final price

    if totdoll == 0 and totcents == 0:
        print("\nYour total is $0.00 Canadian.")
        print("Enjoy your free " + chiptype + " chips!")
    else:
        centString = str(totcents)
        if totcents < 10:
            centString = "0" + centString
        print("\nYour total is $"+ str(totdoll) +"."+ centString + " Canadian.")

        toonies = totdoll // 2
        loonies = 0
        if totdoll - (toonies * 2) == 1:
            if totcents != 0:
                toonies = toonies + 1
            else: 
                loonies = 1
        else: 
            if totcents != 0:
                loonies = 1

        paymentString = "Please give me "

        andString = ""

        if toonies > 0 and loonies > 0:
            andString = " and "

        if toonies > 0:
            paymentString = paymentString + str(toonies) + " toonies"
        if loonies > 0:
            paymentString = paymentString + andString + "1 loonie"
        paymentString = paymentString + ". [hit RETURN]: \n"
        if loonies == 0 and toonies == 0:
            paymentString = ""

        payment = input(paymentString)
        print("Thank you! Here are your " + chiptype + " chips.")