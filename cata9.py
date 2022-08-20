# Task

# Write a function that accepts fight string consists of only small letters and * which means a bomb drop place.
# Return who wins the fight after bombs are exploded.
# When the left side wins return Left side wins!, 
# when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:
#  w - 4
#  p - 3 
#  b - 2
#  s - 1
  
#  m - 4
#  q - 3 
#  d - 2
#  z - 1

def alphabet_war(fight):
    if len(fight) == fight.count('*'):
        return "Let's fight again!"
    fight = ' ' + fight + ' '
    while '*' in fight:
        if fight[fight.find("*") - 1] != '*' and fight[fight.find("*") + 1] != '*':
            fight = fight.replace(fight[fight.find("*") - 1] + fight[fight.find("*")] + fight[fight.find("*") + 1], '_')
        elif fight[fight.find("*") - 1] == '*' and fight[fight.find("*") + 1] != '*':
            fight = fight.replace(fight[fight.find("*")] + fight[fight.find("*") + 1], '_')
        elif fight[fight.find("*") - 1] != '*' and fight[fight.find("*") + 1] == '*':
            fight = fight.replace(fight[fight.find("*") - 1] + fight[fight.find("*")], '_')
        else:
            fight = fight.replace(fight[fight.find("*")], '_')
        print(fight)
    count = 0
    count += fight.count('s') + fight.count('b')*2 + fight.count('p')*3 + fight.count('w')*4 + \
             fight.count('m')*(-4) + fight.count('q')*(-3) + fight.count('d')*(-2) + fight.count('z')*(-1)
    print(count)
    if count:
        return "Right side wins!" if count < 0 else "Left side wins!"
    return "Let's fight again!"
