# https://www.hackerrank.com/challenges/crossword-puzzle/problem?isFullScreen=true


def crosswordPuzzle(crossword, words):
    # Write your code here
    words = words.split(";")
    class Variable():
        def __init__(self, length, start, stop, direction):
            self.length = length
            self.start = start
            self.stop = stop
            self.start_i, self.start_j = start
            self.stop_i, self.stop_j = stop
            self.cells = set([
                (i, self.start_j) for i in range(self.start_i, self.stop_i + 1)
            ] if direction == "down" else [
                (self.start_i, j) for j in range(self.start_j, self.stop_j + 1)
            ])
            self.direction = direction
            
    def creating_variables():
        variables = []
        for i in range(len(crossword)):
            for j in range(len(crossword)):
                startsword = False
                if crossword[i][j] == "-":
                    if i != len(crossword) - 1 and i != 0:
                        if (crossword[i - 1][j] == "+" or crossword[i - 1][j] == "X") and crossword[i + 1][j] == "-":
                            startsword = True
                    elif i == 0:
                        if crossword[i + 1][j] == "-":
                            startsword = True
                            
                if startsword:
                    length = 0
                    end = 0
                    for k in range(i, len(crossword)):
                        if crossword[k][j] == "-":
                            length += 1
                            end = k
                        else:
                            break
                    var = Variable(length, (i,j), (end, j), "down")
                    variables.append(var)
                   
                if startsword:  #avoid making a second variable at the same point
                    continue
                    
                if crossword[i][j] == "-":
                    if j != len(crossword) - 1 and j != 0:
                        if (crossword[i][j -1] == "+" or crossword[i][j -1] == "X") and crossword[i][j+1] == "-":
                            startsword = True
                    elif j == 0:
                        if crossword[i][j+1] == "-":
                            startsword = True
                if startsword:
                    length = 0
                    end = 0
                    for k in range(j, len(crossword)):
                        if crossword[i][k] == "-":
                            length += 1
                            end = k
                        else:
                            break
                    
                    var = Variable(length, (i,j), (i, end), "across")
                    if var.length > 2:
                        variables.append(var)
        return variables
    
    def unassigned(assignment):
        var = domains.keys() - assignment.keys()
        unassigned_var = random.choice(list(var))
        return unassigned_var
    
    def overlaps(var, n_var):
        intersection = var.cells.intersection(n_var.cells)
        # if "ICELAND" in domains[n_var]:
        #     print(intersection)
        if intersection:
            inter_pos = []
            inter_i, inter_j = intersection.pop()
            for variable in (var, n_var):
                if variable.direction == "down":
                    pos_var = inter_i - variable.start_i
                else:
                    pos_var = inter_j - variable.start_j
                inter_pos.append(pos_var)        
            return inter_pos
            
    def node_consistency():
        for var in domains:
            for val in domains[var].copy():
                if var.length != len(val):
                    domains[var].remove(val)
                    
    def consistent(var, assignment):
        if var.length != len(assignment[var]):
            # domains[var].remove(assignment[var])
            return False
        
        for other_var in assignment:
            if other_var == var:
                continue
            overlap = overlaps(var, other_var)
            if overlap:
                i, j = overlap
                if assignment[var][i] != assignment[other_var][j]:
                    # domains[var].remove(assignment[var])
                    return False
                print(var, assignment[var])
                    
        return True
        
    def backtracking(assignment):
        if len(assignment) == len(domains):
            return assignment
        
        result = None
        var = unassigned(assignment)
        for val in domains[var].copy():
            new_assignment = assignment.copy()
            new_assignment[var] = val
            if consistent(var, new_assignment):
                result = backtracking(new_assignment)
            if result:
                return result
            del new_assignment
            
        return result
    
    def printer(assignment):
        if not assignment:
            return "NO solution"
        
        board = []
        for lines in crossword:
            lines = list(lines)
            board.append(lines)

        
        for var in assignment:
            i, j = var.start
            for val in range(var.length):
                if var.direction == "down":
                    board[i + val][j] = assignment[var][val]
                if var.direction == "across":
                    board[i][j + val] = assignment[var][val]
        # print(board)
        for t in range(len(board)):
            crossword[t] = "".join(board[t])
        return crossword
    
    variables = creating_variables()
    # for vari in variables:
    #     print(vari)
    #     print(vari.length)
    #     print(vari.cells)
    #     print("\n")
    domains = {}
    for i in variables:
        domains[i] = set(words)
    node_consistency()
    prior_assignment = {
        var: domains[var].copy().pop() for var in domains if len(domains[var]) == 1
    }
    assignment = backtracking(prior_assignment)
    return printer(assignment)
