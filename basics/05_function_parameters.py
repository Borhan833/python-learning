def hello(name):
    print("Hello ", name)
hello(input("What is your name? "))
print("-" * 15)
def multiply(a , b):
    return a * b
result=multiply(int(input("First number: ")),int(input("Second number: ")))
print(result)
print("-" * 15)
def rectangle_area(length , width):
    return length * width
area = rectangle_area(int(input("Length: ")),int(input("Width: ")))
print("rectangle area: " , area)
print("-" * 15)
def student_result(name,score):
    if score >= 10 :
        print(name , " passed.")
    else:
        print(name , " failed.")
student_result(input("Please enter student name: ") , int(input("Please enter student score: ")))
