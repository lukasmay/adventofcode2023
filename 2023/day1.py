import re
CONVERT = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '0': '0'
}

def part1(input_file):
    sum  = 0
    with open(input_file) as file:
        for line in file:
            first = str(re.findall(r"\d", line)[0])
            last = str(re.findall(r"\d", line)[-1])
            sum += int(first + last)

    return sum

def part2(input_file):
    sum = 0
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    with open(input_file) as file:
        for line in file:
            indexes = []
            for i in range(len(words)):
                a = [m.start() for m in re.finditer(words[i], line)]
                for z in a:
                    indexes.append((z, words[i]))
            indexes.sort()
            sum += int(CONVERT.get(str(indexes[0][1])) + CONVERT.get(str(indexes[-1][1])))

    return sum

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day1.txt"
    print(part1(input_file))
    print(part2(input_file))



if __name__ == "__main__":
    main()