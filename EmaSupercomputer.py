# https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true

def twoPluses(grid):
    # Write your code here
    tem = []
    tem.append(["O"] * (n + 2))
    for x in grid:
        tem.append(["O"] + list(x) + ["O"])
    tem.append(["O"] * (n + 2))
    grid = tem
    # print(grid)
    ans=0
    for e in range(1, n + 1):
        for v in range(1, m + 1):
            r = 0
            # check adjacent 4 cells of [e][v] when r >0
            while grid[e + r][v] == "G" and grid[e - r][v] == "G" and grid[e][v + r] == "G" and grid[e][v - r] == "G":
                grid[e + r][v] =grid[e - r][v] =grid[e][v + r] =grid[e][v - r] = "g"#to avoid overlapping of 2 pluses at that instance
                for E in range(1, n + 1):#2nd plus
                    for V in range(1, m + 1):
                        R = 0
                        # check adjacent 4 cells of [e][v] when r >0
                        while grid[E + R][V] == "G" and grid[E - R][V] == "G" and grid[E][V + R] == "G" and grid[E][
                            V - R] == "G":
                            ans=max(ans,(4*r +1)*(4*R +1))
                            R+=1
                r+=1
            #revert back to "G" for each "g"
            r=0
            while grid[e + r][v] == "g" and grid[e - r][v] == "g" and grid[e][v + r] == "g" and grid[e][v - r] == "g":
                grid[e + r][v] = grid[e - r][v] = grid[e][v + r] = grid[e][v - r] = "G"
                r+=1

    return ans
