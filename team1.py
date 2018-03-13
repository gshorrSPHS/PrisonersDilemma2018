import random

team_name = 'one' 
strategy_name = 'Blowfish'
strategy_description = 'Pick c until they pick b'

def move(my_history, their_history, my_score, their_score):
  if len(their_history) == 0:
      return 'c'
  count = 0
  for n in their_history:
    if 'b' == n:
      count += 1
  if count >= 10:
    return 'b'
  elif their_history[-1] == 'b':
    return 'b'
  elif count < 10:
    return 'c'
