try:
    age = int(input("Enter the age of the candidate: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        str1 = "You need to wait " + str(18 - age) + " more year(s) to vote."
        raise ValueError(str1)
except ValueError as e:
    print(e)
