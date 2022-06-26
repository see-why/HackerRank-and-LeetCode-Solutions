# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?isFullScreen=true

def stepPerms(n):
    steps = [1, 2, 3]
    ways = dict()

    def climb(n, steps, ways):
        ret = 0
        for step in steps:
            if n - step == 0:
                ret += 1
            elif n - step > 0:
                if n - step not in ways:
                    ways[n - step] = climb(n - step, steps, ways)
                print(ways[n - step])
                ret += ways[n - step]
        return ret
    
    return climb(n, steps, ways)
