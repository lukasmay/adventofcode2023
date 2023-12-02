import re

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
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    convert = {
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
    with open(input_file) as file:
        for line in file:
            indexes = []
            for i in range(len(words)):
                if not line.find(words[i]) == -1:
                    indexes.append(words[i])
            sum += int(convert.get(indexes[0]) + convert.get(indexes[-1]))

    return sum

def convert_written_numbers(text):
  # Create a regular expression to match written numbers.
  number_regex = re.compile(r'\d+')

  # Find all written numbers in the text.
  numbers = number_regex.findall(text)

  # Convert each written number to a number.
  for number in numbers:
    text = text.replace(number, str(int(number)))

  # Return the converted text.
  return text

def main():
    input_file = "/Users/lukasmay/git/adventofcode2023/Input/day1.txt"
    print(part1(input_file))
    print(part2(input_file))



if __name__ == "__main__":
    main()