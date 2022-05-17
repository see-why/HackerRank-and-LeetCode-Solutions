# https://www.hackerrank.com/challenges/count-luck/problem?isFullScreen=true

def find(matrix, char):
    char_row = [row for row in range(len(matrix)) if char in matrix[row]][0]
    char_col = matrix[char_row].index(char)
    return char_row, char_col

def sum_coords(a, b):
    return a[0] + b[0], a[1] + b[1]

def find_path(matrix):
    N, M = n, m
    start = find(matrix, 'M')
    end = find(matrix, '*')
    paths = [[start]]
    def get(coord):
        return matrix[coord[0]][coord[1]]
    while paths:
        new_paths = []
        for path in paths:
            for delta in (-1, 0), (1, 0), (0, -1), (0, 1):
                coord = sum_coords(path[-1], delta)
                if (0 <= coord[0] < N and 
                    0 <= coord[1] < M and
                    (len(path) == 1 or coord != path[-2]) and
                    get(coord) != 'X'
                   ):
                       if coord == end:
                           return path + [coord]
                       else:
                           new_paths.append(path + [coord])
        paths = new_paths
    return None

def count_waves(matrix, path):
    N, M = n, m
    def get(coord):
        return matrix[coord[0]][coord[1]]
    count = 0
    for (i, path_coord) in enumerate(path[:-1]):
        neighbors = [sum_coords(path_coord, delta) for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        options = [
            coord for coord in neighbors
            if (0 <= coord[0] < N and 0 <= coord[1] < M and get(coord) != 'X')
        ]
        if len(options) > (2 if i>0 else 1):
            count += 1
    return count

def countLuck(matrix, k):
    # Write your code here
    path = find_path(matrix)
        
    # count waves
    count = count_waves(matrix, path)
    
    # print answer
    return ('Impressed' if k == count else 'Oops!')
