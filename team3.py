# from __future__ import print_function
# import random
#
# #def test_move(my_history, their_history, my_score, their_score)
#
# #def historia:
#
# def my_history(word,letter):
#     count = 0
#     for a in word:
#         if a == letter:
#             count += 1
#             print count
#
# my_history('kjlasdfklaijosdfjkadskjfjklasdfjklasdfjklasdjklfjklasdfjklasdfjlkadsjfl','a')
#
# # def their _ history
#
# # can only return a lowercase b or c
# # betray the first time, but then always collude
# # only variables we have are: my_history, their_history,
# # my_score, and their_score
# # if len(my_history) == 0:
# #     return 'b'
# # else:
# #     return 'c'
#
# # how to alternate b & c
# # if it's an odd turn betray, even turn collude
# # odd numbers have a remainder of 1 when divide by 2
# # if len(my_history) % 2 == 1: #odd turn
# #     return 'b'
# # else:
# #     return 'c'
#
# # check if they betray in the first 3 turns. If they did
# # we will betray forever, otherwise collude
# # if len(my_history) < 3:
# #     return 'c'
# # elif 'b' == their_history[0] or 'b' == their_history[1] or 'b' == their_history[2]:
# #     return 'b'
# # else:
# #     return 'c'
#









####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

# outta 200

team_name = '3'  # Only 10 chars displayed.
strategy_name = 'naivety until broken'
strategy_description = 'picks c always'


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

    return c


def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
              ", ".join(["'" + my_history + "'", "'" + their_history + "'",
                         str(my_score), str(their_score)]) +
              ") returned " + "'" + real_result + "'" +
              " and should have returned '" + result + "'")
        return False


if __name__ == 'Ashton':

    # Test 1: Betray on first move.
    if test_move(my_history='',
                 their_history='',
                 my_score=0,
                 their_score=0,
                 result='c'):
        print 'Test passed'
        # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbbbbb',
              their_history='cccccc',
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0,
              their_score=0,
              result='c')