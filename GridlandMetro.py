# https://www.hackerrank.com/challenges/gridland-metro/problem?isFullScreen=true

def gridlandMetro(n, m, k, track):
    # Write your code here
    spots = n*m
    rows = dict()

    for row in track: 
        r = row[0]
        c1 = row[1]
        c2 = row[2]
        if r not in rows:
            rows[r] = (c1, c2)
        else:
            rows[r] = (min(c1, rows[r][0]), max(c2, rows[r][1]))

    for (c1, c2) in rows.values():
        length = (c2 - c1) + 1
        spots -= length

    return spots
