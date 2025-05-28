import random

inp = input("Die to roll: ").lower()

vals = inp.split("d", 1)
num_die = int(vals[0])
num_sides = int(vals[1])

rolls = []
for i in range(num_die):
	rolls.append(random.randint(1, num_sides))

rolls_sorted = []
for roll in rolls:
	rolls_sorted.append(roll)

rolls_sorted.sort()

print("Unsorted: " + str(rolls))
print("  Sorted: " + str(rolls_sorted))

roll_sum = 0
for roll in rolls:
	roll_sum += roll

print("Sum: " + str(roll_sum))
print("Average: " + str(roll_sum / num_die))
print("Median: " + str(rolls_sorted[num_die // 2]))
print("Min: " + str(rolls_sorted[0]))
print("Max: " + str(rolls_sorted[-1]))