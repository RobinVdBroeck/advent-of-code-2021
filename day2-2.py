position = [0, 0]
aim = 0

with open("day2-1.txt", "r") as f:
    for l in f.readlines():
       [instruction, instruction_size] = l.split()
       if instruction == 'forward':
           position[0] += int(instruction_size)
           position[1] += aim * int(instruction_size)
       elif instruction == 'down':
           aim += int(instruction_size)
       elif instruction == 'up':
           aim -= int(instruction_size)
       else:
           print("Unknown instruction")

print(position)
print(position[0] * position[1])
