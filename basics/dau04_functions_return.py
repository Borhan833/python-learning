#Hello Function
def hello():
    print("Hello")
hello()
#Function to add two numbers
def add_two_numbers(a , b):
    return a + b
result=add_two_numbers(int(input("Please enter first number: ")) ,int(input("Please enter second number: ")))
print(result)
#The square function of a number
def square(number):
    return number**2
num =int(input("Please enter number: "))
result=square(num)
print(result)
#Age calculation function
def age(birth_year):
    now=2026
    return now - birth_year
birth=int(input("Birth year: "))
user_age = age(birth)
print(user_age)
