import re
from queue import Queue

total = []
symbols = []
q_line = []
q = Queue(maxsize=3)


def main():
    with open("aoc3-test.txt", "r") as file:
        for line in file:
            q.put(line)
            if q.full():
                prep(q)
    print(f"Total of Valid Gears: {sum(total)}")


def prep(q):
    print(f"\nCurrent Queue: {q.queue}")
    regex = re.compile(r'[@_!#$%^&*+()\-<>?/|}{~:]')
    for y in range(len(q.queue)):
        nums = re.findall(r'\d+', q.queue[y])
        if len(nums) > 0:
            for num in range(len(nums)):
                start = q.queue[y].find(nums[num])
                finish = start + len(nums[num])
                q_line.append([y, int(nums[num]), (start, finish)])

        for x in range(len(q.queue[y])):
            if not (regex.search(q.queue[y][x]) == None):
                q_line.append([y, x])
        symbols.clear()

    print(q_line)
    ''' do logic here'''

    # total.append(num)
    q_line.clear()
    q.get()
    return q_line


'''
qline if len == 3 NUMBER - Q(0-3), Number. (Start, Finish)
qline if len == 2 SYMBOL - Q(0-3), Position
'''



if __name__ == "__main__":
    main()