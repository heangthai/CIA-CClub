while True:
    
    cel = float(input("PLease enter a temperature in Celcius: "))
    fah = (cel * 9/5) + 32
    print(cel, "Celisus is ", fah, "Fahrenheit")
      
    more = input("Do you want to calculate again? y/n ")
    if more == "n":
         print("Thank you!")
         break
