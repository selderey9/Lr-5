numbers = []
for i in range(4):
    val = int(input(f"Enter number {i+1}: "))
    numbers.append(val)
result = [max(numbers), min(numbers), len(numbers), sum(numbers)/len(numbers)]
print(",".join(map(str, result)))
