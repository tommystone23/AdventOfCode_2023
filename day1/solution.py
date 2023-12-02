
def part1(data: list[str]):
    total : int = 0
    for line in data:
        char_digit_array = []
        for char in line:
            if char.isdigit():
                char_digit_array.append(char)
            
        last_index = len(char_digit_array)
        if last_index:
            tmp_str = char_digit_array[0] + char_digit_array[last_index - 1]
            total += int(tmp_str)
    print(total)


def part2(data : list[str]):
    word_to_digit = {
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }

    total : int = 0
    for line in data:
        char_digit_array = []
        for i in range(len(line)):
            for key in word_to_digit.keys():
                if line[i:i+len(key)] == key:
                    char_digit_array.append(word_to_digit[key])
                    i += (len(key) - 1)
                    break
            if line[i].isdigit():
                char_digit_array.append(line[i])
        last_index = len(char_digit_array)
        if last_index:
            tmp_str = char_digit_array[0] + char_digit_array[last_index - 1]
            total += int(tmp_str)
    print(total)

with open('data_set.txt') as f:
    data = f.readlines()

part1(data)
part2(data)