rounds = open('day2/input.txt', 'r').read().split('\n')

shapeScores = {
    #rock
    'A': 1, 'X': 1,
    #paper
    'B': 2, 'Y': 2,
    #scissors
    'C': 3, 'Z': 3 
}

# r-p = 1-2 = -1 = win
# r-s = 1-3 = -2 = lose
# p-r = 2-1 = 1 = lose
# p-s = 2-3 = -1 = win
# s-r = 3-1 = 2 = win
# s-p = 3-2 = 1 = lose
# (-1 or 2)=Win; 0=Draw; else Lose
# W=6; D=3; L=0

totalScore = 0
for round in rounds:
    opponent = shapeScores[round.split(' ')[0]]
    me = shapeScores[round.split(' ')[1]]
    
    roundOutcomeScore = 0 # Lose
    if (opponent-me in [-1, 2]):
        # Win
        roundOutcomeScore = 6
    elif (opponent-me == 0):
        # Draw
        roundOutcomeScore = 3
    
    totalScore += me + roundOutcomeScore
    
print(totalScore)