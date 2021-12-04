prev_values = [0, 0, 0]
increased_depths = 0

def push(new_value):
    global prev_values
    prev_values[0], prev_values[1], prev_values[2] = prev_values[1], prev_values[2], new_value

with open("day1.txt", "r") as f:
    for (i, depth) in enumerate(f.readlines()):
        depth = int(depth)
        if i < 3:
            push(depth)
            continue
        previous_sum = sum(prev_values)
        push(depth)
        print(prev_values)
        if sum(prev_values) > previous_sum:
            increased_depths += 1

print(increased_depths)
