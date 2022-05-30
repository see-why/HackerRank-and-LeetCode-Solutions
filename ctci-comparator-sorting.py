# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?isFullScreen=true


def compareStrings(a, b):
    result = 0

    if a.name > b.name:
        result = 1
    else:
        result = -1
    return result

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f'Player name: {self.name} score: {self.score}'

        
    def comparator(a, b):
        result = 0
        if a.score < b.score:
            result = 1
        elif a.score > b.score:
            result  = -1
        else:
            result = compareStrings(a, b)
        return result
