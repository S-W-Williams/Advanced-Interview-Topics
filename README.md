# Advanced Interview Topics
I found many of the interview study guides I came across to be lacking in topics beyond basic data structures and common algorithms. This is my compilation of more advanced topics/concepts that may be asked at Google/Facebook and other companies that have interviews on the harder end.

Will include topic notes as they are finished being formatted.

# Table of Contents

- ## Arrays:
	- [Selection Algorithms](#selection-algorithms)
	  - Quickselect for finding kth smallest element
	  - Deterministic Selection for guaranteed O(N)
	- [Recursive Bottom Up Merge Sort](#bottom-up-merge-sort)
	  - Used to sort array in-place with constant space
  
- ## Strings:
	- [Rabin–Karp](#rabin-karp)
	- Knuth–Morris–Pratt
	- Boyer–Moore
  
- ## Graphs:
- ### Basics:
	- [Connected Components](#connected-components)
	- [Strongly Connected Components](#strongly-connected-components)
	- [Topological Sorting](#topological-sort)
	- [Disjoint-Set (Union-Find)](#disjoint-set-union-find)
	- Biconnected Components
	
- ### Paths:
	- Dijkstra's
	- Bellman-Ford
	- A*
	- Floyd-Warshall
	- Johnson's Algorithm
	- Widest Path problem

- ### Euler Tours:
	- Fleury's Algorithm
	- Hierholzer's Algorithm

- ### Minimum Spanning Trees:
	- Kruskal's
	- Prim's
	- Edmonds' (arborescences)

- ### Independent Sets
	- Largest Independent Set (Dynamic Programming)

- ### Bipartite Graphs (pronounced bi·par·tite):
	- Given a bipartite graph, separate the vertices into two sets
	- Testing bipartiteness
	- Maximum Bipartite Matching
	- Hopcroft–Karp Algorithm

- ### Flows and Cuts: http://www.ics.uci.edu/~goodrich/teach/graph/notes/MaxFlow.pdf
	- Flow network
	- Maximum Flow
	- Ford–Fulkerson/Edmonds–Karp
	- Minimum Cuts
	- Max-Flow and Min-Cut

- ### Matchings:
	- Stable marriage
	- Gale–Shapley

- ### Graph Coloring:
	- Greedy coloring
	- 4-color theorem
	- 5-color theorem
	- k-degenerate graph

- ### Miscellaneous:
	- Small-world network
	- Arboricity

- ## Computational Geometry:
	- Convex Hulls
		- Used to solve Maximum-Density Segment Problem
	- Closest pairs
	
# Arrays
## Selection Algorithms
An example of a selection problem is selecting the kth smallest element from an unsorted collection of n elements. Can be solved in O(N Log N) time using sorting, but we can do better.

O(N) approach for solving selection problems is called Prune and Search (variant of divide and conquer)

### Common strategy of rune and search algorithms:
-  Choose an “approximate median” m∗ 
-  Partition S into three subsequences: 
	-  L: elements in S less than m∗ . 
	- E: elements in S equal to m∗
	- G: elements in S greater than m∗ 
- Recursively select L, E, or G as appropriate

### Randomized Quick-Select:
- Average O(N), O(N2) worst case.
- When recursively selecting:
	- if k ≤ |L| then
		- quickSelect(L, k)
	- else if k ≤ |L| + |E| then
		- return x
	- else
		- quickSelect(G, k − |L| − |E|)
				
### Deterministic Selection:
- Always O(N)
- Deterministic meaning will always have same runtime for given inputs
- Idea is to deterministically pick the pivot instead of randomly
- Algorithm:
	- Partition the set S into  ceiling(n/5) groups of size 5 each (except, possibly, for one group).
	- Sort each group and identify its median element.
	- Apply the algorithm recursively on these ceiling(n/5) “baby medians” to find their median.
	- Use this element (the median of the baby medians) as the pivot and proceed as in the quick-select algorithm.
	
## Bottom Up Merge Sort
Useful for stable sorting in place without extra space. 

Description from http://www.algorithmist.com/index.php/Merge_sortt

Bottom-up merge sort is a non-recursive variant of the merge sort, in which the array is sorted by a sequence of passes. During each pass, the array is divided into blocks of size m (initially m = 1). Every two adjacent blocks are merged (as in normal merge sort), and the next pass is made with a twice larger value of m.

Note: while it says to merge the blocks "as in normal merge sort", I found the easiest way to do this in place is to swap elements.

Pseudo Code:
```python
Input: array a[] indexed from 0 to n-1. 
m = 1
while m < n do 
	i = 0
	while i < n-m do
		merge subarrays a[i..i+m-1] and a[i+m .. min(i+2*m-1,n-1)] in-place.
		i = i + 2 * m
	m = m * 2
```

An implemention I managed to come up with:
```python
def inplaceMergeSort(a):
    if len(a) < 2:
        return a
    m = 1
    while m < (len(a) - 1) // 2:
        i = 0
        while i + m < len(a):
            j = i
            while j < i + m:
                if a[j] > a[i+m]:
                    a[j],a[i+m] = a[i+m],a[j]
                j += 1
            i += 2*m
        m *= 2
    i = m
    j = 0
    while i < len(a):
        if a[j] > a[i]:
            a[j],a[i] = a[i],a[j]
        j += 1
        if j == i:
            i += 1
    return 
```

In the final loop, we start storing the final sorted subarray at index 0, and every time we increment the size. Once the final sorted subarray is bigger than the sorted left size, we start taking elements from the right side and then also decreasing the size of the subarray.

# Strings
## Rabin-Karp
String matching algorithm with linear O(|s| + |t|) time complexity. 

Used to solve the problem "Given s and t, does s occur as a substring in t?".

Uses rolling hash and sliding window of size |s| on t and compare hash values.

When the hash value of the window matches hash of s, check the characters one by one for a match. If they are all equal, we have found a match. If they are not equal, keep going.

The probability of matching hash values being a collision should happen with the probability of 1/|s|

Algorithm:
- Compute hash of s
- Compute hash of the first |s| characters in t 
- For i in range(len(s), len(t): 
	- Compare hash values of s and the window
	- If no match, remove first character and add the next character

# Graphs
Note that for Big O notation of graph algorthims, E and V is actually |E| and |V|. I omitted the cardinality notation for simplicity. 

## Cycle Detection
To find cycles in both directed and undirected graphs, using DFS allows for an O(E + V) approach. Union-Find can also be used on directed graphs for an O(E Log V) approach. O(E + V)  scales slower than O(E Log V) and so DFS is the best approach.

For DFS cycle detection we can think of each vertex as a child in the recursion tree. If DFS gets called on a vertex that is a parent in the recursion tree then there is a cycle in the graph. 

## Connected Components
We can find connected components in a undirected graph by doing a DFS on the entire graph. During the DFS, we keep a counter to number the component each vertex belongs to. We increment the counter each time explore is called from the main DFS function. 

The important here to note is that DFS must be run on the entire graph, meaning we must iterate through all the vertices in the graph and recursively explore each vertex. Keep track of which vertices have been visited, and skip the ones that have been visited.

DFS for finding connected components:
- Create visited set
- Create dictionary to store connected components scc
- Set counter c to 0
- For all vertices v in graph G:
	- If v is not visited:
		- Increment counter
		- Explore(v, c, scc)
		
The Explore function assigns v to the connected component set c, and then recursively explorers the neighbors of v.
- Mark v as visited
- Add v to the set in stored in connected components dictionary at key c
- For all neighbors u of v that have not been visited:
	- Explore(u, c)
	
## Strongly Connected Components
We can also find strongly connected components in directed graphs using DFS with O(E + V) time complexity. The algorithm given in Algorithms by S. Dasgupta, C.H. Papadimitriou, and U.V. Vazirani suggests doing DFS on the graph while keeping track of the pre-visit and post-visit time of each vertex. The vertex with the highest post-visit time will belong to a sink SCC. Knowing this, we then transpose (also called reverse) the graph, and then do a DFS for finding connected components on the reversed graph starting with the highest post-time vertex. Repeat until we have visited all vertexes in the stack. 

We can simplify this by keeping track of the order the vertices are processed in a stack. Once DFS is done, the vertex at the top of the stack is the one with the highest post-visit time.

SCC-DFS:
- Create empty stack s
- Create strongly connected components dictionary scc
- Create visited set
- For each vertex u in graph G:
	- If u is not visited:
		- ExplorePV(u, s)
- Get the inverse of G
- Create and set counter c to 0
- Clear the visited set
- While stack is not empty:
	- Pop a vertex u
	- If u is not visited:
		- Increment counter
		- ExploreSCC(u, c, scc)

ExplorePV never pops from s, instead it marks u as visited, recursively calls itself on u's neighbors that have not been visited, and then pushes u to the stack. 
- Visited[u] = True
- For neighbors v that have not been visited:
	- ExplorePV(v, s)
- Push u to s

ExploreSCC marks u as visited, puts u into the scc at key c, and then calls itself on u's neighbors that have not been visited.
- Visited[u] = True
- Put u into the set at scc[c]
- For neighbors v that have no been visited:
	- ExploreSCC(v, c, scc)

To transpose/invert a graph:
- Create a dictionary r of adjacency lists
- For each vertex u in the original graph:
	- For each neighboring vertex v:
		- Add u to the adjacency list of v
		- r[v].add(u)
		
## Topological Sort
Topological sort, or topological ordering, of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

Used for dependency resolution, prerequisites planning, etc.

Any DAG has at least one topological ordering. DFS allows for linear time construction.

A very simple DFS approach is to order the vertices in decreasing order of their post visit times. This is because of the follow property:
- In a DAG, every edge leads to a vertex with a lower post number

Recall that determining the post visit times of vertices can be simplified using a stack. The last vertex pushed onto the stack has the highest post visit time. 

Once DFS is done, the vertex at the top of the stack is the one with the highest post-visit time.

Explore(u):
- Visited[u] = True
- For neighbors v that have not been visited:
	○ ExplorePV(v, s)
- Push u to stack

Another algorithm for topological sorting, from Algorithms by S. Dasgupta, C.H. Papadimitriou, and U.V. Vazirani is below.

We will keep an array in[u] which holds the indegree (number of incoming edges) of each node. For a source, this value is zero. We will also keep a linked list of source nodes.

```
(Set the in array)
for all u ∈ V: in[u] ← 0
for all edges (u,w) ∈ E: in[w] ← in[w]+1
	
(Check for sources)
L ← empty linked list
for all u ∈ V:
  if in[u] is 0: add u to L

for i=1 to |V|:
Let u be the first node on L; output it and remove it from L.
(Remove u; update indegrees.)
for each edge (u,w) ∈ E:
    in[w] ← in−1
    if in[w] is 0: add w to L.
```

## Disjoint-Set (Union-Find)
Keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

Search and merge runtimes are O(α(n)), which is the inverse Ackermann function (grows very slow).

Idea is to have trees that represent sets. Each node in the tree points to its parent, and the root points to itself. The root is the element that represents the set, meaning when two sets are compared we are comparing the roots. 

Straight forward to implement using an array, but using a map/dictionary instead allows more flexibility with keys for the vertices. However, this affects the runtime as hashing is amortized O(1), so inverse Ackermann is not guaranteed. 

Declare 2 dictionaries, one for parent and one for rank. The parent of every element is initially itself and the rank is 0. The rank is used for determining which set will be the parent when 2 sets are merged.

Finding the root of a tree involves repeatedly looking up the parent of a node until its parent is itself. 

When merging 2 sets, find the root of each sets. Make the set with the larger rank the parent of the smaller set. If the ranks are equal, pick either one and the increment the rank of the one chosen to be parent; do not update rank otherwise. 

Path compression is done to flatten the tree to ensure quick lookups. This is done by making each element points of its parent during the find operation. In the end each node in the tree should point directly to its parent.

My implemention:
```python
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
            self.parents[x] =  self.find(self.parents[x])
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
```
