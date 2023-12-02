total = []


def main():
    with open("aoc2.txt", "r") as file:
        for line in file:
            prep(line)
    print(f"Total of all Games: {sum(total)}")


def prep(line: str):
    line = line.replace(";", ",")
    line = line.replace(", ", ",")
    line = line.replace("\n", "")
    line = line.replace(": ", ",")
    line = line.replace(" ", ",")
    games = line.split(",")

    it = iter(games)
    cleaned = list(zip(it, it))

    red = []
    blue = []
    green = []

    for pos in range(1, len(cleaned)):
        if cleaned[pos][1] == "red":
            red.append(int(cleaned[pos][0]))
        if cleaned[pos][1] == "green":
            green.append(int(cleaned[pos][0]))
        if cleaned[pos][1] == "blue":
            blue.append(int(cleaned[pos][0]))

    result = max(red) * max(green) * max(blue)
    total.append(result)
    return total


if __name__ == "__main__":
    main()