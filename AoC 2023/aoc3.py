import re
from queue import Queue

total = []
symbols = []
q_line = []
check = []
q = Queue(maxsize=3)


def main():
    with open("aoc3-test.txt", "r") as file:
        for line in file:
            q.put(line)
            if q.full():
                prep(q)
    print(f"Missing Part Number: {sum(total)}")


def prep(q):
    print(f"\nCurrent Queue: {q.queue}")
    regex = re.compile(r'[@_!#$%^&*+()\-<>?/|}{~:]')
    for y in range(len(q.queue)):
        nums = re.findall(r'\d+', q.queue[y])
        if len(nums) > 0:
            for num in range(len(nums)):
                start = q.queue[y].find(nums[num])
                finish = start + len(nums[num])-1
                q_line.append([y, int(nums[num]), (start, finish)])

        for x in range(len(q.queue[y])):
            if not (regex.search(q.queue[y][x]) is None):
                symbols.append([y, x])

    for row in range(len(q_line)):
        if q_line[row][0] == 1:
            print(f"Working on {q_line[row]}")
            start, finish = q_line[row][2]
            for symbol in symbols:
                print(symbol)
                if symbol[0] == 1 and symbol[0] in range(start, finish+1):
                    print(f"Adding inline {q_line[row][1]}")
                    total.append(q_line[row][1])
                    q_line[row][1] = 0
                if symbol[0] == 0 or symbol[0] == 2:
                    check.append([symbol[1]-1, symbol[1], symbol[1]+1])
                    my_set = {i for lst in check for i in lst}
            for pos in my_set:
                if pos in range(start, finish+1):
                    print(f"Adding above below {q_line[row][1]}")
                    total.append(q_line[row][1])
                    break

            check.clear()
            my_set.clear()

    print(total)
    symbols.clear()
    q_line.clear()
    q.get()
    return q_line


if __name__ == "__main__":
    main()