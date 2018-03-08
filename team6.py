####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'sophialind'  # Only 10 chars displayed.
strategy_name = 'The sneak attack'
strategy_description = 'When they betray we betray or every 10th'


def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.

    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty.
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].

    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.


    # if they betray then each of the three turns after, we betray. If they decide to bbcb than we would do cbbbbbb
    if len(their_history)>0 and 'b' in their_history[-1]:
        return 'b'
    elif len(their_history)>1 and 'b' in their_history[-2]:
        return 'b'
    elif len(their_history)>2 and 'b' in their_history[-3]:
        return 'b'
    # if any of the turns aren't divisible by 10 then collude
    elif len(my_history) % 10 == 0 and len(my_history) != 0:
        return 'b'
    else:
        return 'c'


def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +", ".join(["'" + my_history + "'", "'" + their_history + "'",str(my_score), str(their_score)]) +") returned " + "'" + real_result + "'" +" and should have returned '" + result + "'")
        return False


if __name__ == '__main__':

    # Test 1: Betray on first move.
    if test_move(my_history='',
                 their_history='',
                 my_score=0,
                 their_score=0,
                 result='c'):
        print 'Test passed'
        # Test 2: If they decide to bbcb than we would do cbbbbbb
    test_move(my_history='cbbb',
              their_history='bbcb',
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move().
              my_score=0,
              their_score=0,
              result='b')