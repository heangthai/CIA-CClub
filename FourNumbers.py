while True:

    num1 = float(input("Please enter the 1st number: "))
    num2 = float(input("Please enter the 2nd number: "))
    num3 = float(input("Please enter the 3rd number: "))
    num4 = float(input("Please enter the 4th number: "))
    sum_ = num1 + num2 + num3 + num4
    print("The sum of these numbers are ", sum_)
    more = input("Do you want to calculate again? y/n ")
    if more == "n":
         print("Thank you!")
         break
