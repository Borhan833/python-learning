numbers=[12,5,18,7,30,2,11]
# Calculate total
# Find maximum number
# Find even numbers
# Calculate average
total=0
for num in numbers:
    total += num
print("Total =",total)
max_number = numbers[0]
for num in numbers:
    if num > max_number :
        max_number=num
even=[]
print("Max number = ",max_number)
for num in numbers:
    if num % 2 == 0 :
        even.append(num)
print("Evens = ",even)
average = total / len(numbers)
print("average = ", average)
