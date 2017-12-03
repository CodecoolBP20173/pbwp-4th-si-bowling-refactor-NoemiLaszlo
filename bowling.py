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
        # if at last subframe of the frame or if the player rolls a strike, increase frame
        if not has_frame_more_rolls or game[roll].upper() == 'X':
            has_frame_more_rolls = False
            frame += 1
        # determine if frame has more rolls or frame should be increased
        has_frame_more_rolls = not has_frame_more_rolls
    return final_score


def get_value(roll_symbol):
    '''This function returns the score of one roll'''
    if roll_symbol.isdigit() and len(roll_symbol) == 1:
        # return roll result including and ignoring 0 as an input for sake of simplicity
        return int(roll_symbol)
    elif roll_symbol.upper() == 'X' or roll_symbol == '/':
        return 10
    elif roll_symbol == '-':
        return 0
    else:
        raise ValueError()
