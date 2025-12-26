# loops.py
# Day 2 Python practice – Loops

print("=== Python Loops ===")

# FOR loop example
print("\nFor Loop:")
for i in range(1, 6):
    print("Number:", i)

# WHILE loop example
print("\nWhile Loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# Loop with condition
print("\nEven numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num)
