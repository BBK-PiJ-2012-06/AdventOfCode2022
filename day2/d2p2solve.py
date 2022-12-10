strategies = open('day2/input.txt', 'r').read().split('\n')

strategyScores = {
    'A X': 3, # lose to rock (play scissors): 3(s)+0(l) 
    'A Y': 4, # draw with rock (play rock): 1(r)+3(d) 
    'A Z': 8, # win against rock (play paper): 2(p)+6(w) 
    'B X': 1, # lose to paper (play rock): 1(r)+0(l) 
    'B Y': 5, # draw with paper (play paper): 2(p)+3(d) 
    'B Z': 9, # win against paper (play scissors): 3(s)+6(w)
    'C X': 2, # lose to scissors (play paper): 2(p)+0(l) 
    'C Y': 6, # draw with scissors (play scissors): 3(s)+3(d) 
    'C Z': 7, # win against scissors (play rock): 1(r)+6(w) 
}

totalScore = 0
for strategy in strategies:  
    totalScore += strategyScores[strategy]
    
print(totalScore)