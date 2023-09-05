import random

def RockPaperScissors (Attack):
    Defense = random.randint(0, 2)
    if   Attack == 'scissors':
        if   Defense == 0: return f'Paper! Aw, I lost!'
        elif Defense == 1: return f'Scissors! a tie?'
        elif Defense == 2: return f'Rock! I win!'
    elif Attack == 'paper':
        if   Defense == 0: return f'Rock! Aw, I lost!'
        elif Defense == 1: return f'Paper! a tie?'
        elif Defense == 2: return f'Scissors! I win!'
    elif   Attack == 'rock':
        if   Defense == 0: return f'Scissors! Aw, I lost!'
        elif Defense == 1: return f'Rock! a tie?'
        elif Defense == 2: return f'Paper! I win!'