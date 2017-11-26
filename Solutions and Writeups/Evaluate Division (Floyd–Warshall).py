from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dist = defaultdict(dict)
        for i in range(len(equations)):
            n = equations[i][0]
            d = equations[i][1]
            dist[n][d] = values[i]
            dist[n][n] = 1
            dist[d][d] = 1
            dist[d][n] = float(1) / values[i]
            
        for k in dist.keys():
            for i in dist[k]:
                for j in dist[k]:
                    dist[i][j] = dist[i][k] * dist[k][j]
        
        res = []
        for n,d in queries:
            if n in dist and d in dist[n]:
                res.append(dist[n][d])
            else:
                res.append(-1)
        return res
