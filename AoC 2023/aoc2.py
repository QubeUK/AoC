total = []


def main():
    with open("aoc2.txt", "r") as file:
        for line in file:
            prep(line)
    print(f"Total of Valid Games: {sum(total)}")


def prep(line: str):
    line = line.replace(";",",")
    line = line.replace(", ", ",")
    line = line.replace("\n","")
    line = line.replace(": ", ",")
    line = line.replace(" ",",")
    games = line.split(",")

    it = iter(games)
    cleaned = list(zip(it, it))

    state = "valid"
    # Ruleset 12 Red cubes, 13 Green cubes, and 14 Blue
    for pos in range(1, len(cleaned)):
        if cleaned[pos][1] == "red" and int(cleaned[pos][0]) > 12 or int(cleaned[pos][0]) <= 0:
            state = "invalid"
        if cleaned[pos][1] == "green" and int(cleaned[pos][0]) > 13 or int(cleaned[pos][0]) <= 0:
            state = "invalid"
        if cleaned[pos][1] == "blue" and int(cleaned[pos][0]) > 14 or int(cleaned[pos][0]) <= 0:
            state = "invalid"
    if state == "invalid":
        cleaned.append(("state", "invalid"))
    else:
        cleaned.append(("state", "valid"))

    state = cleaned[-1:]
    if state[0][1] == "valid":
        total.append(int(cleaned[0][1]))

    return total


if __name__ == "__main__":
    main()
