     team_name: team 14
     strategy_name: reactor b
     strategy_description: depending on the umber of betrays this will do the same

def move(their_history, my_history, my_score, their_score):
    comply = False
    if 'c'not in their_history and their_history >= 1:
        return 'b'
    if 'c' in my_history[-1:] and 'c' not in my_history[-2:-1]:
        comply = True
    if comply:
        return 'c'
    if 'b' not in their_history:
        return 'c'
    if their_history.count('b'):
        if their_history.count('b') == my_history.count('b'):
            return 'c'
        if their_history.count('b') >= my_history.count('b'):
            return 'b'
