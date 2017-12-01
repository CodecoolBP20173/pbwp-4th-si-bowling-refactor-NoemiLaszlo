def score(game):
    '''This function is "plays" the game frame by frame and returns the final score '''
    final_score = 0
    frame = 1
    has_frame_more_rolls = True
    for roll in range(len(game)):
        # if the player rolls spare
        if game[roll] == '/':
            final_score += 10 - get_value(game[roll-1]) if roll > 0 else 0
        else:
            final_score += get_value(game[roll])
        # counting points through the game
        if frame < 10 and get_value(game[roll]) == 10:
            if game[roll] == '/':
                final_score += get_value(game[roll+1])
            elif game[roll].upper() == 'X':
                final_score += get_value(game[roll+1])
                if game[roll+2] == '/':
                    final_score += 10 - get_value(game[roll+1])
                else:
                    final_score += get_value(game[roll+2])
        # komment
        if not has_frame_more_rolls:
            frame += 1
        # komment
        if has_frame_more_rolls is True:  # in_first_half = not in_first_half
            has_frame_more_rolls = False
        else:
            has_frame_more_rolls = True
        # komment
        if game[roll].upper() == 'X':
            has_frame_more_rolls = True
            frame += 1
    return final_score


def get_value(char):
    '''This function returns the score of one roll'''
    if char.isdigit() and len(char) == 1:
        return int(char)
    elif char.upper() == 'X' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
