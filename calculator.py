class Calculator:

    def __init__(self, num1, num2):
        self.num1= num1 
        self.num2= num2 
    def add(self):
        return self.num1+ self.num2 
    def subtract(self):
         return self.num1- self.num2 
    def multiply(self):
        return self.num1 *self.num2 
    def divide(self):
        return self.num1 /self.num2 
# creating instant of the class 
obj = Calculator(10,2)
# calling method to perform addition operation on given numbers
add= obj.add()
subtraction=obj.subtract()
multiplication=obj.multiply()
division=obj.divide()

print(add)
print(subtraction)
print(multiplication)
print(division)
