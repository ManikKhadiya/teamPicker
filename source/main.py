from random import choice
import time 

players = []
file = open('Players.txt', 'r')
players = file.read().splitlines()
print(players[0])
print(players[1])
print(players[2])
print(players[3])
print(players[4])
print(players[5])
print(players[6])
print(players[7])
print(players[8])
print(players[9])
print(players)


print('                                        ')

TeamA = []
TeamB = []

while len(players) > 0:
  playerA = (choice(players))
  print(playerA)
  TeamA.append(playerA)
  players.remove(playerA)
  print('players left:', players)
  
  time.sleep(0.5)
  
  playerB = (choice(players))
  print(playerB)
  TeamB.append(playerB)
  players.remove(playerB)
  print('players left:', players)
  
print(' ')
  
print('teamA:', TeamA)
print(' ')
print('teamB:', TeamB)

