# Advanced Interview Topics
I found many of the interview study guides I came across to be lacking in topics beyond basic data structures and common algorithms. This is my compilation of more advanced topics/concepts that may be asked at Google/Facebook and other companies that have interviews on the harder end.

Will include topic notes as they are finished being formatted.

# Table of Contents

- ## Arrays:
	- [Selection Algorithms](#selection-algorithms)
	  - Quickselect for finding kth smallest element
	  - Deterministic Selection for guaranteed O(N)
	- Recursive Bottom Up Merge Sort
	  - Used to sort array in-place with constant space
  
- ## Strings:
	- Rabin–Karp
	- Knuth–Morris–Pratt
	- Boyer–Moore
  
- ## Graphs:
	- ### Basics:
		- Topological Sorting
		- Connected Components
		- Strongly Connected Components
		- Disjoint-Set (Union-Find)
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
- Selection Algorithms
	- An example of a selection problem is selecting the kth smallest element from an unsorted collection of n elements. Can be solved in O(N Log N) time using sorting, but we can do better.
	- O(N) approach for solving selection problems is called Prune and Search (variant of divide and conquer)
	- Common strategy of rune and search algorithms:
		-  Choose an “approximate median” m∗ 
		-  Partition S into three subsequences: 
			-  L: elements in S less than m∗ . 
			- E: elements in S equal to m∗
			- G: elements in S greater than m∗ 
		- Recursively select L, E, or G as appropriate
	- Randomized Quick-Select:
		- Average O(N), O(N2) worst case.
		- When recursively selecting:
			- if k ≤ |L| then
				- quickSelect(L, k)
			- else if k ≤ |L| + |E| then
				- return x
			- else
				- quickSelect(G, k − |L| − |E|)
				
	- Deterministic Selection:
		- Always O(N)
		- Deterministic meaning will always have same runtime for given inputs
		- Idea is to deterministically pick the pivot instead of randomly
		- Algorithm:
			- Partition the set S into  ceiling(n/5) groups of size 5 each (except, possibly, for one group).
			- Sort each group and identify its median element.
			- Apply the algorithm recursively on these ceiling(n/5) “baby medians” to find their median.
			- Use this element (the median of the baby medians) as the pivot and proceed as in the quick-select algorithm.
