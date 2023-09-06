import random

def RockPaperScissors (Attack):
    Defense = random.randint(0, 2)

    if   Attack == 'scissors':
        if   Defense == 0: return f'I choose Paper! Aw, I lost!'
        elif Defense == 1: return f'I choose Scissors! huh, a tie'
        elif Defense == 2: return f'I choose Rock! I win!'
    elif Attack == 'paper':
        if   Defense == 0: return f'I choose Rock! Aw, I lost!'
        elif Defense == 1: return f'I choose Paper! huh, a tie'
        elif Defense == 2: return f'I choose Scissors! I win!'
    elif   Attack == 'rock':
        if   Defense == 0: return f'I choose Scissors! Aw, I lost!'
        elif Defense == 1: return f'I choose Rock! huh, a tie'
        elif Defense == 2: return f'I choose Paper! I win!'