import math
def operations():
    print("")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Remainder")
    print("7. Square root")
    print("E. Exit the calculator")
    print("")

def addition():
     add1, add2 = get_numbers()
     show_result(add1 + add2)

def subtract():
     sub1, sub2 = get_numbers()
     show_result(sub1 - sub2)

def multiplication():
     mul1, mul2 = get_numbers()
     show_result(mul1 * mul2)
                        
def division():
     try:
         div1, div2 = get_numbers()
         show_result(div1 / div2)

     except ZeroDivisionError:
         input("Cannot divide a number by 0 ")
     
def exponent():
     exp1, exp2 = get_numbers()
     show_result(exp1 ** exp2)

def remainder():
     try:
         rem1, rem2 = get_numbers()
         show_result(rem1 % rem2)

     except ZeroDivisionError:
         input("Cannot divide a number by 0 ")
     

def square_root():
     try:
         sqr = float(input("Insert a value: "))

         if sqr < 0:
             print("Cannot calculate the square root of a negative number")
         else:
             show_result(math.sqrt(sqr))

     except ValueError:
         input("Invalid value ")
      

def get_numbers():
     while True:
          try:
               num1 = float(input("Insert the first value: "))
               num2 = float(input("Insert the second value: "))
               return num1, num2
          
          except ValueError:
              input("Invalid value ")

def show_result(result):
     input(f"Result: {result}")
  
while True:
 #This shows the operations you can do
 operations()

 #This ask which operation you want to do
 question = input("Which option would you like?: ").strip().lower()

 #This shows what you choosed in "question"
 if question == "1":
     addition()
 elif question == "2":
     subtract()
 elif question == "3":
     multiplication()
 elif question == "4":
     division()
 elif question == "5":
     exponent()
 elif question == "6":
     remainder()
 elif question == "7":
     square_root()
 elif question == "e":
     break
 else:
     input("This option does not exist, choose 1-7 or press E to exit")
