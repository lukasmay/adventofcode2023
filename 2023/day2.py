
def part1(input_file):
    total = 0
    with open(input_file) as file:
        for line in file:
            number = int(line[5:line.find(":")])
            line = line[line.find(":") + 2:]
            valid = True
            for round in line.split(";"):
                round = round.strip()
                for draw in round.split(","):
                    draw = draw.strip()
                    if draw[draw.find(" ")+1:] == "blue":
                        if int(draw[:draw.find(" ")]) > 14:
                            valid = False
                    elif draw[draw.find(" ")+1:] == "green":
                        if int(draw[:draw.find(" ")]) > 13:
                            valid = False
                    elif draw[draw.find(" ")+1:] == "red":
                        if int(draw[:draw.find(" ")]) > 12:
                            valid = False
            if valid:
                total += number
    return total

def part2(input_file):
    with open(input_file) as file:
        total = 0
        for line in file:
            line = line[line.find(":") + 2:]
            red = 0
            green = 0
            blue = 0
            for round in line.split(";"):
                round = round.strip()
                for draw in round.split(","):
                    draw = draw.strip()
                    if draw[draw.find(" ")+1:] == "blue":
                        if int(draw[:draw.find(" ")]) > blue:
                            blue = int(draw[:draw.find(" ")])
                    elif draw[draw.find(" ")+1:] == "green":
                        if int(draw[:draw.find(" ")]) > green:
                            green = int(draw[:draw.find(" ")])
                    elif draw[draw.find(" ")+1:] == "red":
                        if int(draw[:draw.find(" ")]) > red:
                            red = int(draw[:draw.find(" ")])
            total += red * blue * green

    return total

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day2.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == "__main__":
    main()