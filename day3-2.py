from typing import List, Iterable, Union
from math import pow, sqrt, ceil
from assertpy import assert_that

class BinaryValue(object):
    def __init__(self, value: Union[str, int, List[int]], size = 64):
        """ Construct a binary value on either a binary string, an integer or
        a list of bits.
        The list of bits should be ordered from biggest bit to smallest bit.
        This means that [1, 0] = 2, and [1, 1, 0] = 6"""
        if isinstance(value, str):
            self._value = int(value, 2)
        elif isinstance(value, list):
            result = 0
            for (power, value) in enumerate(reversed(value)):
                if value == 1:
                    result = result + int(pow(2, power))
                elif value != 0:
                    raise ValueError
            self._value = result
        else:
            self._value = value
        self._size = size

    def __getitem__(self, idx: int) -> int:
        """ idx starts from biggest to smalles. Ie BinaryValue(6)[0] will
        return 1, because it's binary repr is 0b110 """  
        binary =  bin(self._value)[2:]
        binary = binary.zfill(self._size) 
        try:
            str_repr = binary[idx]
            if str_repr == "0":
                return 0
            elif str_repr == "1":
                return 1
            else:
                raise ValueError(str_repr)
        except IndexError:
           return 0


    def __len__(self) -> int:
        for i in range(0, self._size):
            result = pow(2, i)
            if result > self._value:
                return i - 1
        raise ValueError

    def __eq__(self, other) -> bool:
        if isinstance(other, BinaryValue):
            return self._value == other._value
        else:
            return False
    
    def __repr__(self):
        return f"BinaryValue({bin(self._value)} {self._value})"

    def __hash__(self):
        return hash(self._value)

    def value(self) -> int:
        return self._value

    def take_until_bit(self, end_bit: int) -> "BinaryValue":
        """ Take bit until end_bit. Note: bit 0 is here the biggest bit """
        binary =  bin(self._value)[2:]
        result = list()
        for i in range(0, end_bit):
            result.append(int(binary[i], 2))

        return BinaryValue(list(reversed(result)))

    def as_bits(self) -> Iterable[int]:
        for i in range(0, len(self)):
            yield self[i]

    def iter(self) -> Iterable[int]:
        return self.as_bits()

    def invert(self) -> "BinaryValue":
        result = list()
        for bit in reversed(list(self.as_bits())):
            if bit == 0:
                result.append(1)
            else:
                result.append(0)
        return BinaryValue(result)


def read_to_list(filename: str) -> List[str]:
    bytes: List[str] = []
    with open(filename, "r") as file:
        for l in file.readlines():
            if l.strip() == "":
                continue
            bytes.append(l.strip())
    return bytes


def most_common_bit(bytes: Iterable[BinaryValue], position: int):
    zeros = 0
    ones = 0
    for byte in bytes:
        value = byte[position]
        if value == 0:
            zeros += 1
        elif value == 1:
            ones += 1
        else:
            raise ValueError(value)
        
    if zeros > ones:
        return 0
    elif ones > zeros:
        return 1
    else:
        return None


def solve(rows: List[str]) -> int:
    return 0

def calc_oxygen_rating(rows: List[BinaryValue], size: int) -> int:
    remaining = set(rows)
    most_common = most_common_bit(rows, 0) 
    if most_common is None:
        most_common = 1

    for position in range(0, size):
        new_most_common = most_common_bit(remaining, position)
        if new_most_common != None:
            most_common = new_most_common

        print(position, remaining, most_common)
        for value in remaining.copy():
            if value[position] != most_common:
                remaining.remove(value)

    print(list(remaining)[0].value())
    return list(remaining)[0].value()
    


def test():
    assert_that(BinaryValue(22).value()).is_equal_to(22)
    assert_that(BinaryValue("10110").value()).is_equal_to(22)
    assert_that(BinaryValue([1, 0, 1, 1, 0]).value()).is_equal_to(22)

    input = read_to_list("day3-test.txt")
    size = len(input[0])
    print(size)
    binary = [BinaryValue(x, size) for x in input]
    most_common = [most_common_bit(binary, i) for i in range(0, size)] 
    assert_that(most_common, "most common bit").is_equal_to([1,0,1,1,0])
    oxygen = calc_oxygen_rating(binary, size)
    assert_that(oxygen, "calc oxygen rating").is_equal_to(23)
    print("all tests succeed")

if __name__ == '__main__':
    test()
    # result = solve(read_to_list("day3.txt"))
    # print(result)
            
