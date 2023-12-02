
def part1(data : list[str]):
    color_maxes = {
        'red' : 12,
        'green': 13,
        'blue' : 14
    }
    total = 0
    for line in data:
        id, results = split_line(line.strip())
        add_id = True
        for result in results:
            for game in result:
                game_split = game.split(' ')
                value = int(game_split[0])
                color = game_split[1]
                if value > color_maxes[color]:
                    add_id = False
            
        if add_id:
            total += id
    print(total)

def part2(data : list[str]):
    total = 0
    for line in data:
        min_map = {
            'red' : 0,
            'green' : 0,
            'blue' : 0
        }
        id, results = split_line(line.strip())
        for result in results:
            for game in result:
                game_split = game.split(' ')
                value = int(game_split[0])
                color = game_split[1]
                if min_map[color] < value:
                    min_map[color] = value
        total += (min_map['red'] * min_map['green'] * min_map['blue'])   
    print(total)    

def split_line(line : str):
    first_split = line.split(':')
    id_split = first_split[0].split(' ')
    game_id = id_split[1].strip()
    game_results = []
    games_split = first_split[1]
    games_split = games_split.split(';')
    for game in games_split:
        results = game.split(',')
        game = []
        for result in results:
            result = result.strip()
            game.append(result)
        game_results.append(game)
    return int(game_id), game_results


with open('data_set.txt') as f:
    data = f.readlines()

part1(data)
part2(data)