def score(game):
    # docstring, kell mindhárom paraméter?
    result = 0
    frame = 1
    in_first_half = True
    for item in range(len(game)):  # i helyett más változónév
        if game[item] == '/':
            result += 10 - last  # last???
        else:
            result += get_value(game[item])
        # if not in_first_half:
            # frame += 1
        if frame < 10 and get_value(game[item]) == 10:
            if game[item] == '/':
                result += get_value(game[item+1])
            elif game[item] == 'X' or game[item] == 'x':
                result += get_value(game[item+1])
                if game[item+2] == '/':
                    result += 10 - get_value(game[item+1])
                else:
                    result += get_value(game[item+2])
        last = get_value(game[item])
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if game[item] == 'X' or game[item] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    # docstring + if in one line
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    # .upper vagy ilyesmi egy ellenőrzés
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
