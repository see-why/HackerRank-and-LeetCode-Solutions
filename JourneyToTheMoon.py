# https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true

class DisjointSet:
    parent = {}

    # perform MakeSet operation
    def makeSet(self, universe):

        # create `n` disjoint sets (one for each item)
        for i in universe:
            self.parent[i] = i

    # Find the root of the set in which element `k` belongs
    def Find(self, k):

        # if `k` is root
        if self.parent[k] == k:
            return k
        # recur for the parent until we find the root
        return self.Find(self.parent[k])

    # Perform Union of two subsets
    def Union(self, a, b):

        # find the root of the sets in which elements
        # `x` and `y` belongs
        x = self.Find(a)
        y = self.Find(b)

        self.parent[x] = y


def getSets(universe, ds):
    return [ds.Find(i) for i in universe]


def journeyToMoon(no_of_astronauts, astronaut):

    # universe of items i.e astronauts
    universe = list(range(no_of_astronauts))

    # initialize disjoint set
    ds = DisjointSet()

    # create a singleton set for each astronaut
    ds.makeSet(universe)

    for pair in astronaut:
        # Union all astronaut that are from the same country
        ds.Union(*pair)

    sets = getSets(universe, ds)

    # Count the no. of astronauts in each country
    astronauts_each_country = Counter(sets)

    # initialize no. of valid pairs i.e pair of 2 astronauts from different countries
    no_of_valid_pairs = 0

    remaining_astronauts = no_of_astronauts
    # Count possible pairs
    for astronauts_in_country in astronauts_each_country.values():
        remaining_astronauts -= astronauts_in_country
        no_of_valid_pairs += astronauts_in_country * remaining_astronauts

    return no_of_valid_pairs
