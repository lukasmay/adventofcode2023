import re

class Part:
    __slots__ = ["number", "locations"]
    def __init__(self, number, locations):
        self.number = number
        self.locations = locations

    def __str__(self):
        return "Number: " + str(self.number) + " Location: " + str(self.locations)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, __value: object) -> bool:
        if not type(self) == type(object):
            if type(object) == int:
                return self.number == object
            return False
        return object.number == self.number
    
    def __lt__(self, object):
        return self.number < object.number

def part1(input_file):
    with open(input_file) as file:
        total = 0
        engine = []
        for line in file:
            engine.append(list(line))

    symbol_location = []
    for i in range(len(engine)):
        for a in range(len(engine[i])):
            if not re.match("\d", engine[i][a]) and not "." == engine[i][a]:
                if not engine[i][a] == "\n":
                    symbol_location.append([i, a])

    number_location = []
    for i in range(len(engine)):
        number = ""
        location = []
        for a in range(len(engine[i])):
            if re.match("\d", engine[i][a]):
                number += str(engine[i][a])
                location.append([i, a])
                if a == len(engine[i])-1:
                    number_location.append(Part(int(number), location))
            else:
                if not number == "":
                    number_location.append(Part(int(number), location))
                number = ""
                location = []
    end = False
    holder = []
    for num in number_location:
        for loc in num.locations:
            for sym in symbol_location:
                if abs(loc[0] - int(sym[0])) <= 1 and abs(loc[1] - int(sym[1])) <= 1:
                    total += num.number
                    end = True
                    holder.append(num)
                    break
            if end:
                end = False
                break

    return total

def part2(input_file):
    with open(input_file) as file:
        pass
    return None

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day3.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == "__main__":
    main()