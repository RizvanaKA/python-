import math
start = int(input("Enter the start of the range"))
end = int(input("Enter the end of the range" ))
result = []
for i in range(int(math.sqrt(start)), int(math.sqrt(end)) + 1):
    square = i * i
    if 1000 <= square <= 9999:
        if all(int(digit) % 2 == 0 for digit in str(square)):
            result.append(square)
if result:
    print("Four-digit perfect squares with all even digits:", result)
else:
    print("No four-digit perfect squares with all even digits found.")
