while True:
    
    l = float(input("Please enter the Length of your cuboid (rectangular prism): "))
    w = float(input("Please enter the Width of your cuboid (rectangular prism): "))
    h = float(input("Please enter the Height of your cuboid (rectangular prism): "))

    volume = l * w * h
    SA = 2*(l*h + w*h + l*w )

    print("The Volume of your rectangular Prism (CUBOID) is ", volume,)
    print("The Surface Area of your rectangular Prism (CUBOID) is ", SA,)
          
    more = input("Do you want to calculate again? y/n ")
    if more == "n":
         print("Thank you!")
         break
