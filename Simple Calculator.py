import time

# this function add numbers
def sum(x, y):
  return x + y
  
#This function divides the number
def quotient(x, y):
  return x / y
  
# this function subtracts number 
def difference(x, y):
  return x - y
  
# this function multiplies number
def product(x, y):
  return x * y


def LAn():
  print("Calculating")
  time.sleep(0.5)
  print(".")
  time.sleep(0.5)
  print(".")
  time.sleep(0.5)
  print(".")
  time.sleep(1)

print("Welcome to Calculator")
print("")
print("Operations Available")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("")
time.sleep(1)


while True:
    # take input from the user
    operation = input("Select operation(1/2/3/4): ")

    # check if choice is one of the four options
    if operation in ('1', '2', '3', '4'):
      try:
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
      except ValueError:
          print("Invalid input.")
          time.sleep(1)
          continue
      
      if operation == '1':
            LAn()
            print(num1, "+", num2, "=", sum(num1, num2))
      elif operation == '2':
            LAn()
            print(num1, "-", num2, "=", difference(num1, num2))
      elif operation == '3':
            print("Calculating")
            LAn()
            print(num1, "*", num2, "=", product(num1, num2))
      elif operation == '4':
            LAn()
            print(num1, "/", num2, "=", quotient(num1, num2))
      # check if user wants to do another calculation		
      again = input("Do you want to do this again? y/n ")
      if again in ('y', 'Y', 'yes', 'Yes'):
        continue
      elif again in ('n', 'N', 'no', 'No'):
        print("Thank You!")
        break
      else:
        print("Invalid Response")
        break