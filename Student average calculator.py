marks = []

for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))
    marks.append(mark)

average = sum(marks) / len(marks)

print("Average =", average)
