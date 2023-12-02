# Advent of Christmas 2023 Day 1
total = []
result = []


def main():
    with open("aoc1.txt", "r") as file:
        for line in file:
            get_nums(convert_num(line))
    print(f"Total: {sum(total)}")


def convert_num(line: str) -> str:
    temp = []
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in words:
        first = line.find(word)
        second = line.rfind(word)
        if first != second:
            for r in (("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"),
                      ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")):
                word = word.replace(*r)
            result.append((word, second))

        if first != -1:
            for r in (("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"),
                      ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")):
                word = word.replace(*r)
            result.append((word, first))

    for x in range(len(result)):
        temp = list(line)
        temp[result[x][1]] = result[x][0]
        line = "".join(temp)

    get_vals = list([val for val in line if val.isnumeric()])
    line = "".join(get_vals)

    result.clear()
    temp.clear()
    return line


def get_nums(string: str) -> list:
    for _, count in enumerate(string):
        if count.isdigit():
            first = count
            break

    for _, count in enumerate(reversed(string)):
        if count.isdigit():
            second = count
            break

    number = "".join([first, second])
    total.append(int(number))
    return total


if __name__ == "__main__":
    main()