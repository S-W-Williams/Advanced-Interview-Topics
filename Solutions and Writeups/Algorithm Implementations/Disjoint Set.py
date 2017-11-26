class DisjointSet:
    def __init__(self):
        self.parents = dict()
        self.ranks = dict()
        return

    def create(self, x):
        self.parents[x] = x
        self.ranks[x] = 0
        return
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def merge(self, x, y):
        a = self.find(x)
        b = self.find(y)

        if self.ranks[a] > self.ranks[b]:
            self.parents[b] = a
        elif self.ranks[a] < self.ranks[b]:
            self.parents[a] = b
        else:
            self.parents[b] = a
            self.ranks[a] += 1
        return
