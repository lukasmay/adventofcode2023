class Card:
    __slots__ = ["id", "score", "number"]
    
    def __init__(self, *args):
        if len(args) == 3:
            self.id = args[0]
            self.score = args[1]
            self.number = args[2]
        else:
            win_cards, cards = args[0][args[0].find(":") +1:].split("|")
            win_cards = win_cards.strip().split(" ")
            cards = cards.strip().split(" ")
            count = 0
            for card in cards:
                if card == "":
                    continue
                elif card in win_cards:
                    count += 1

            self.id = int(args[0][5:args[0].find(":")])
            self.score = pow(2,(count-1)) if count > 0 else 0
            self.number = count
    
    def __repr__(self) -> str:
        return "Card: " + str(self.id) + " Score: " + str(self.score) + " Count: " + str(self.number)
    
    def __add__(self, object):
        return self.score + object.score
    
    def __radd__(self, object):
        if object == 0:
            return self.score
        return self.score + object


def part1(input_file):
    with open(input_file) as file:
        cards = []
        for line in file:
            cards.append(Card(line))
        
    return sum(cards)

def part2(input_file):
    with open(input_file) as file:
        total = 0
        cards = []
        for line in file:
            win_cards, my_cards = line[line.find(":") +1:].split("|")
            win_cards = win_cards.strip().split(" ")
            my_cards = my_cards.strip().split(" ")
            
            count = 0
            for card in my_cards:
                if card == "":
                    continue
                elif card in win_cards:
                    count += 1
            cards.append(Card(line[5:line.find(":")], pow(2,(count-1)) if count > 0 else 0, count))
        
    return None

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day4.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == "__main__":
    main()