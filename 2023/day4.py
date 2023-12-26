class Card:
    def __init__(self, id, score, number) -> None:
        self.id = id
        self.score = score
        self.number = number
    
    def __repr__(self) -> str:
        return "Card: " + str(self.id) + " Score: " + str(self.score)

def part1(input_file):
    with open(input_file) as file:
        total = 0
        for line in file:
            win_cards, cards = line[line.find(":") +1:].split("|")
            win_cards = win_cards.strip().split(" ")
            cards = cards.strip().split(" ")
            
            count = 0
            for card in cards:
                if card == "":
                    continue
                elif card in win_cards:
                    count += 1
            if not count == 0:
                total += pow(2,(count-1))

    return total

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
            cards.append(Card(line[5:line.find(":")], pow(2,(count-1)) if count > 0 else 0))
        
    return None

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day4.txt"
    print(part1(input_file))
    print(part2(input_file))

if __name__ == "__main__":
    main()