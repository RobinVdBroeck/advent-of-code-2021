from typing import List

def to_dec(input: str) -> int:
    return int(input, 2)

def solve(bytes: List[str]) -> int:
    most_common = '' 
    least_common = ''

    for position in range(0, len(bytes[0])):
        zeros = 0
        ones = 0
        for byte in bytes:
            value = byte[position]
            if value == "0":
                zeros += 1
            elif value == "1":
                ones += 1
            else:
                print(f"unknown value {value}")
        if zeros > ones:
            most_common += '0'
            least_common += '1'
        else:
            most_common += '1'
            least_common += '0'

    for (position, result) in enumerate(most_common):
        print(f"Most common in position {position} is {result}")

    most_common = to_dec(most_common)
    least_common = to_dec(least_common)
    print(f"most_common = {most_common} ({bin(most_common)})")
    print(f"least_common = {least_common} ({bin(least_common)})")
    result = most_common * least_common
    return result

if __name__ == '__main__':
    bytes: List[str] = []
    with open("day3.txt", "r") as file:
        for l in file.readlines():
            if l.strip() == "":
                continue
            bytes.append(l.strip())
    result = solve(bytes)
    print(result)
            
