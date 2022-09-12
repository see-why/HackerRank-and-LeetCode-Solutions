
# https://www.hackerrank.com/challenges/matrix/problem?isFullScreen=true


class Set:
    def __init__(self, city, machine):
        self.cities = set([city])
        self.machine = machine

def minTime(roads, machines):
    # Write your code here
    total = 0
    mach = set(machines)
    city_to_set, sets = dict(), dict()
    for c1, c2, t in sorted(roads, key=lambda x: x[2], reverse=True):
        # add new sets for the cities if they don't have one yet
        city_to_set[c1] = city_to_set.get(c1, Set(c1, c1 in mach))
        city_to_set[c2] = city_to_set.get(c2, Set(c2, c2 in mach))
        # get the sets
        s1, s2 = city_to_set[c1], city_to_set[c2]
        # if already in the same set, skip
        if s1 == s2:
            continue
        # if they both containe machines, add to total
        if s1.machine and s2.machine:
            total += t
            continue
        # 1 or less are machines, so merge the sets
        s1.cities.update(s2.cities)
        # update if combined set contains machines
        s1.machine = s1.machine or s2.machine
        # update the city to set mapping
        for c in s2.cities:
            city_to_set[c] = s1

    return total
