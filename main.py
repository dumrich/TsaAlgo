# Program 1: Basketball App

def CalculatePointsTotals(pointsList):
    '''
    Find Total Number of Points for a given list
    '''
    total=0
    for value, points in enumerate(reversed(pointsList), start=1):
        total = total + (value*points)

    return total

def CalculateWinner(TotalPointList):
    '''
    Calculate Winner based on a pointList
    '''
    ApplesPointList, BananasPointList = TotalPointList[:3], TotalPointList[3:]
    # Check manually who won the game by comparing point totals
    if CalculatePointsTotals(ApplesPointList) > CalculatePointsTotals(BananasPointList):
        return 'A'
    elif CalculatePointsTotals(BananasPointList) > CalculatePointsTotals(ApplesPointList):
        return 'B'
    else:
        return 'T'

if __name__=='__main__':
    # returns 'T'
    print(CalculateWinner([7,3,0,6,4,1]))
    # returns 'B'
    print(CalculateWinner([10,3,7,8,9,6]))

# Program 2: Optometerist

def GridBoard(OrientationString):
    GridBoard = [[1, 2],
                 [3, 4]]
    MoveList = list(OrientationString)
    for move in MoveList:

        if move == 'H':
            GridBoard[0], GridBoard[1] = GridBoard[1], GridBoard[0] 
        elif move == 'V':
            GridBoard[0][1], GridBoard[0][0] = GridBoard[0][0], GridBoard[0][1]
            GridBoard[1][1], GridBoard[1][0] = GridBoard[1][0], GridBoard[1][1]
    return f'{GridBoard[0]},\n{GridBoard[1]}'

if __name__=='__main__':
    print(GridBoard('HV'))
    print(GridBoard('VVHH'))

