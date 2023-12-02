# Advent of Christmas 2023 Day 1

total = []


def get_nums(string):    
    for index, count in enumerate(string):
        if count.isdigit():
            first = count                    
            break

    for index, count in enumerate(reversed(string)):
        if count.isdigit():
            second = count
            break
    
    number = "".join([first, second])
    total.append(int(number))
    
    return total


with open("aoc1.txt", "r") as file:
    for line in file:
        get_nums(line)

    
print(sum(total))
