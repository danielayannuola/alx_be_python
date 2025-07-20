# File: multiplication_table.py
# Location: alx_be_python/control-flow/

# Prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using a for loop
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
