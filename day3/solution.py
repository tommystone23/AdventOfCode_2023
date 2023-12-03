
def part1(data : list[str]):
    total = 0
    for i in range(len(data)):
        j = 0
        while j < len(data[i]):
            if data[i][j].isdigit():
                value, index_jump = resolve_engine_nb(data, i, j)
                if index_jump:
                    j += (index_jump - 1)
                total += value
            j += 1
    print(total)

def resolve_engine_nb(data : list[str], i, j):
    str_engine_nb = ''
    while j < len(data[i]) and data[i][j].isdigit():
        str_engine_nb = str_engine_nb + data[i][j]
        j += 1
    if not str_engine_nb:
        return 0, 0

    engine_nb_length = len(str_engine_nb)
    engine_nb = int(str_engine_nb)

    j -= engine_nb_length

    # Check for symbols
    if check_for_symbols(data, engine_nb_length, i, j):
        return engine_nb, engine_nb_length

    return 0, engine_nb_length

def check_for_symbols(data : list[str], engine_nb_length, initial_i, initial_j):
    symbols = ['!', '@', '#', '$', '%',
        '^', '&', '*', '(', ')',
        '-', '=', '+', '/']
    neg_offset_i = 1 if initial_i > 0 else 0
    pos_offset_i = 1 if initial_i < (len(data) - 1) else 0
    neg_offset_j = 1 if initial_j > 0 else 0
    pos_offset_j = engine_nb_length if (initial_j + engine_nb_length) < len(data[initial_i]) else 0
    for j in range((initial_j - neg_offset_j), (initial_j + pos_offset_j + 1)):
        if ((data[initial_i - neg_offset_i][j] in symbols) or
            (data[initial_i][j] in symbols) or 
            (data[initial_i + pos_offset_i][j] in symbols)):
            return True
    return False

def part2(data : list[str]):
    total = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '*':
                total += resolve_engine_ratio(data, i, j)
    print(total)
    
def resolve_engine_ratio(data : list[str], i, j):
    neg_offset_i = 1 if i > 0 else 0
    pos_offset_i = 1 if i < (len(data) - 1) else 0
    neg_offset_j = 1 if j > 0 else 0
    pos_offset_j = 2 if (j + 2) < len(data[i]) else 0
    valid_nbs = []
    used_indexes = []
    for k in range((j - neg_offset_j), (j + pos_offset_j)):
        if (data[i - neg_offset_i][k].isdigit() and
            not [i - neg_offset_i, k] in used_indexes):
            indexes, value = get_full_number(data, i - neg_offset_i, k)
            used_indexes = used_indexes + indexes
            valid_nbs.append(value)
        if (data[i][k].isdigit() and
            not [i, k] in used_indexes):
            indexes, value = get_full_number(data, i, k)
            used_indexes = used_indexes + indexes
            valid_nbs.append(value)
        if (data[i + pos_offset_i][k].isdigit() and
            not [i + pos_offset_i, k] in used_indexes):
            indexes, value = get_full_number(data, i + pos_offset_i, k)
            used_indexes = used_indexes + indexes
            valid_nbs.append(value)
    if len(valid_nbs) == 2:
        return (int(valid_nbs[0]) * int(valid_nbs[1]))
    return 0 

def get_full_number(data : list[str], i , j):
    indexes = []
    str_nb = data[i][j]
    indexes.append([i, j])
    # check to the left
    j_cp = j - 1
    while j_cp >= 0 and data[i][j_cp].isdigit():
        str_nb = data[i][j_cp] + str_nb
        indexes.append([i, j_cp])
        j_cp -= 1
    # check to the right
    j_cp = j + 1
    while j_cp < len(data[i]) and data[i][j_cp].isdigit():
        str_nb = str_nb + data[i][j_cp]
        indexes.append([i, j_cp])
        j_cp += 1

    return indexes, int(str_nb)

with open('data_set.txt') as f:
    data = f.readlines()

part1(data)
part2(data)