#Python program to create calculator

class Calculator:
    def sum(self,a,b):
        return(a+b)
    
    def substract(self,a,b):
        return(a-b)
    
    def multiply(self,a,b):
        return(a*b)
    
    def divison(self,a,b):
        return(a/b)
    
cal = Calculator()

num1 = int(input("enter 1st Integer Number = "))
num2 = int(input("Enter 2nd Integer Number = "))

addition = cal.sum(num1,num2)
print(f"Sum of {num1} and {num2} = {addition}")

substraction = cal.substract(num1, num2)
print(f"Substraction of {num1} and {num2} is {substraction}")

multiplication = cal.multiply(num1,num2)
print(f"Multiplication of {num1} and {num2} is {multiplication}")

divison = cal.divison(num1,num2)
print(f"Divison of {num1} and {num2} is {divison}")
