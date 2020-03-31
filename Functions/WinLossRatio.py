def win_percentage(wins, losses):
  total_games = wins+losses
  ratio_won = wins/total_games
  return ratio_won*100
  
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100