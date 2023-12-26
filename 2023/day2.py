
class Round:
    __slots__ = ["red", "green", "blue"]

    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def get_red(self):
        return self.red
    
    def get_green(self):
        return self.green
    
    def get_blue(self):
        return self.blue

    def add_red(self, n):
        self.red += n

    def add_blue(self, n):
        self.blue += n

    def add_green(self, n):
        self.green += n

    def get_total(self):
        return self.red + self.green + self.blue
    
class Game:
    __slots__ = ["rounds", "id"]

    def __init__(self, id):
        self.id = id
        self.rounds = []

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
        pass
    return None

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day2.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == "__main__":
    main()