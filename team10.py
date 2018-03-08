####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random 

team_name = 'Zignatious' # Only 10 chars displayed.
strategy_name = 'Operation Copy Cat'
strategy_description = 'Start by betraying then take the most recent response from their_history and return that.'

def Op_CC(my_history, their_history, my_score, their_score):
    if  len(my_history) == 0:
        return 'b'
    else:
        return their_history[-1]



def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = Op_CC(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
              ", ".join(["'" + my_history + "'", "'" + their_history + "'",
                         str(my_score), str(their_score)]) +
              ") returned " + "'" + real_result + "'" +
              " and should have returned '" + result + "'")
        return False
