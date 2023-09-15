
split = int(input("How many people should they bill split to? "))
tax = float(input("What is the tax rate in % ? "))
service = float(input("What is the service rate in % ? "))
numdish = int(input("What is the number of dishes?(5 max) "))

if numdish == 1:
 Dish1 = input("What is the name of your first dish? ")
 price1 = float(input("What is the price of your first dish? "))
 numdish - 1
 

if numdish == 2:
 Dish1 = input("What is the name of your first dish? ")
 price1 = float(input("What is the price of your first dish? "))
 numdish - 1
 Dish2 = input("What is the name of your second dish? ")
 price2 = float(input("What is the price of your second dish? "))
 numdish - 1

if numdish == 3:
 Dish1 = input("What is the name of your first dish? ")
 price1 = float(input("What is the price of your first dish? "))
 numdish - 1
 Dish2 = input("What is the name of your second dish? ")
 price2 = float(input("What is the price of your second dish? "))
 numdish - 1
 Dish3 = input("What is the name of your third dish? ")
 price3 = float(input("What is the price of your third dish? "))
 numdish - 1

if numdish == 4:
 Dish1 = input("What is the name of your first dish? ")
 price1 = float(input("What is the price of your first dish? "))
 numdish - 1
 Dish2 = input("What is the name of your second dish? ")
 price2 = float(input("What is the price of your second dish? "))
 numdish - 1
 Dish3 = input("What is the name of your third dish? ")
 price3 = float(input("What is the price of your third dish? "))
 numdish - 1
 Dish4 = input("What is the name of your fourth dish? ")
 price4 = float(input("What is the price of your fourth dish? "))
 numdish - 1
 
if numdish == 5:
 Dish1 = input("What is the name of your first dish? ")
 price1 = float(input("What is the price of your first dish? "))
 numdish - 1
 Dish2 = input("What is the name of your second dish? ")
 price2 = float(input("What is the price of your second dish? "))
 numdish - 1
 Dish3 = input("What is the name of your third dish? ")
 price3 = float(input("What is the price of your third dish? "))
 numdish - 1
 Dish4 = input("What is the name of your fourth dish? ")
 price4 = float(input("What is the price of your fourth dish? "))
 numdish - 1
 Dish5 = input("What is the name of your fifth dish? ")
 price5 = float(input("What is the price of your fifth dish? "))
 numdish - 1

print("================ Restaurant Bill ================")
if numdish == 1:
 print("Cost for dish 1 '",Dish1,"' : $" ,price1, "Tax: $", price1*(tax/100), "Service: $", price1*(tax/100))
 Totalcost = price1 + price1*(tax/100) + price1*(tax/100)
 print("Subtotal per person: $", Totalcost/split)
 print("Total: $",Totalcost)

if numdish == 2:
 print("Cost for dish 1 '",Dish1,"' : $" ,price1, "Tax: $", price1*(tax/100), "Service: $", price1*(tax/100))
 print("Cost for dish 2 '",Dish2,"' : $" ,price2, "Tax: $", price2*(tax/100), "Service: $", price2*(tax/100))
 cost1 = price1 + price1*(tax/100) + price1*(service/100)
 cost2 = price2 + price2*(tax/100) + price2*(service/100)
 Totalcost = cost1 + cost2
 print("Subtotal per person: $", Totalcost/split)
 print("Total: $",Totalcost)

if numdish == 3:
 print("Cost for dish 1 '",Dish1,"' : $" ,price1, "Tax: $", price1*(tax/100), "Service: $", price1*(tax/100))
 print("Cost for dish 2 '",Dish2,"' : $" ,price2, "Tax: $", price2*(tax/100), "Service: $", price2*(tax/100))
 print("Cost for dish 3 '",Dish3,"' : $" ,price3, "Tax: $", price3*(tax/100), "Service: $", price3*(tax/100))
 cost1 = price1 + price1*(tax/100) + price1*(service/100)
 cost2 = price2 + price2*(tax/100) + price2*(service/100)
 cost3 = price3 + price3*(tax/100) + price3*(service/100)
 Totalcost = cost1 + cost2 + cost3
 print("Subtotal per person: $", Totalcost/split)
 print("Total: $",Totalcost)

if numdish == 4:
 print("Cost for dish 1 '",Dish1,"' : $" ,price1, "Tax: $", price1*(tax/100), "Service: $", price1*(tax/100))
 print("Cost for dish 1 '",Dish2,"' : $" ,price2, "Tax: $", price2*(tax/100), "Service: $", price2*(tax/100))
 print("Cost for dish 3 '",Dish3,"' : $" ,price3, "Tax: $", price3*(tax/100), "Service: $", price3*(tax/100))
 print("Cost for dish 4 '",Dish4,"' : $" ,price4, "Tax: $", price4*(tax/100), "Service: $", price4*(tax/100))
 cost1 = price1 + price1*(tax/100) + price1*(service/100)
 cost2 = price2 + price2*(tax/100) + price2*(service/100)
 cost3 = price3 + price3*(tax/100) + price3*(service/100)
 cost4 = price4 + price4*(tax/100) + price4*(service/100)
 Totalcost = cost1 + cost2 + cost3 + cost4
 print("Subtotal per person: $", Totalcost/split)
 print("Total: $",Totalcost)

if numdish == 5:
 print("Cost for dish 1 '",Dish1,"' : $" ,price1, "Tax: $", price1*(tax/100), "Service: $", price1*(tax/100))
 print("Cost for dish 1 '",Dish2,"' : $" ,price2, "Tax: $", price2*(tax/100), "Service: $", price2*(tax/100))
 print("Cost for dish 3 '",Dish3,"' : $" ,price3, "Tax: $", price3*(tax/100), "Service: $", price3*(tax/100))
 print("Cost for dish 4 '",Dish4,"' : $" ,price4, "Tax: $", price4*(tax/100), "Service: $", price4*(tax/100))
 print("Cost for dish 5 '",Dish5,"' : $" ,price5, "Tax: $", price5*(tax/100), "Service: $", price5*(tax/100))
 cost1 = price1 + price1*(tax/100) + price1*(service/100)
 cost2 = price2 + price2*(tax/100) + price2*(service/100)
 cost3 = price3 + price3*(tax/100) + price3*(service/100)
 cost4 = price4 + price4*(tax/100) + price4*(service/100)
 cost5 = price5 + price5*(tax/100) + price5*(service/100)
 Totalcost = cost1 + cost2 + cost3 + cost4 + cost5
 print("Subtotal per person: $", Totalcost/split)
 print("Total: $",Totalcost)

print("================================================")
print("Thank you for visiting!")
print("We hope you come back soon!") 
