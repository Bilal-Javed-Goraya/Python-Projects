def checkPassword(password):
    upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
    length = len(password)

    if (length < 6):
        print("Password must be at least 6 characters long!\n")
    else:
        for i in range(0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1


    if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is medium.\n")
    else:
        if (upperChars == 0):
            print("Password must contain at least one uppercase character!\n")
        if (lowerChars == 0):
            print("Password must contain at least one lowercase character!\n")
        if (specialChars == 0):
            print("Password must contain at least one special character!\n")
        if (digits == 0):
            print("Password must contain at least one digit!\n")

password = input("Please enter password: ")
checkPassword(password)