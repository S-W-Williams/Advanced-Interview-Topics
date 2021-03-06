# Table of Contents

## Arrays:
- [Selection Algorithms](#selection-algorithms)
  - Quickselect for finding kth smallest element
  - Deterministic Selection for guaranteed O(N)
- [Iterative Bottom Up Merge Sort](#bottom-up-merge-sort)
  - Used to sort array in-place with constant space
- Circular Array
- Suffix Array
- Dutch National Flag Problem
- [Open Addressing](#open-addressing)

## Strings:
- [Rabin–Karp](#rabin-karp)
- Rolling Hash
- Sliding Window Technique

## Trees:
- [Self-Balancing BSTs](#self-balancing-bsts)
- [Prefix Tree (Trie)](#prefix-tree)
- [B-Tree](#b-tree)
- Recursive Traversals
- Iterative Traversals
- [Tree Reconstruction From Traversals](#tree-reconstruction-from-traversals)
- [Threaded Binary Trees](#threaded-binary-trees)
- Segment Tree
- Binary Index Tree (Fenwick Tree)
- [Fibonacci Heaps](#fibonacci-heaps)

## Math:
- [P, NP, NP-Completeness](#p-np-np-completeness)
- Discrete Probability
- [Generating Permutations](#generating-permutations)
- [Counting](#counting)
- Master Theorem
- Euclidean Algorithm
- Modular Exponentiation
- Karatsuba Multiplication

## Graphs:

### Basics:
- [Connected Components](#connected-components)
- [Strongly Connected Components](#strongly-connected-components)
- [Topological Sorting](#topological-sort)
- [Disjoint-Set (Union-Find)](#disjoint-set-union-find)
- Biconnected Components

### Paths:
- [Dijkstra's](#dijkstras-shortest-path-algorithm)
- [Bellman-Ford](#bellman-ford)
- A*
- Floyd-Warshall
- Johnson's Algorithm
- Widest Path problem

### Eulerian Graphs:
- [Trails and Cycles](#eulerian-trails-and-cycles)
- [Hierholzer's Algorithm](#hierholzers-algorithm)
- [Fleury’s Algorithm](#fleurys-algorithm)

### Minimum Spanning Trees:
- [Kruskal's](#kruskals-algorithm)
- [Prim's](#prims-algorithm)
- Borůvka's
- Edmonds' (arborescences)

### Independent Sets
- Largest Independent Set (Dynamic Programming)

### Bipartite Graphs (pronounced bi·par·tite):
- Given a bipartite graph, separate the vertices into two sets
- Testing bipartiteness
- Maximum Bipartite Matching
- Hopcroft–Karp Algorithm

### Flows and Cuts: http://www.ics.uci.edu/~goodrich/teach/graph/notes/MaxFlow.pdf
- Flow network
- Maximum Flow
- Ford–Fulkerson/Edmonds–Karp
- Minimum Cuts
- Max-Flow and Min-Cut

### Matchings:
- Stable marriage
- Gale–Shapley

### Graph Coloring:
- Greedy coloring
- 4-color theorem
- 5-color theorem
- k-degenerate graph

### Miscellaneous:
- Small-world network
- Arboricity

## Computational Geometry:
- Convex Hulls
  - Used to solve Maximum-Density Segment Problem
- Closest pairs

## Dynamic Programming

- Shortest/Longest Path in DAGs
- [0/1 Knapsack](#01-knapsack)
- Weighted Interval Scheduling
- Coin Change
- Chain Matrix Multiplication
- [Edit Distance](#edit-distance)
- [Longest Increasing Subsequence](#longest-increasing-subsequence)
- Longest Common Subsequence

## Bit Manipulation

- Bits and Bytes
- Counting Set Bits

## Famous Problems/Applications:

- [Huffman encoding](#huffman-encoding)
- [Set Cover](#set-cover)
- [Knight's Tour](#knights-tour)
- N-Queens
- Rat in a Maze
- Traveling Salesman
- Route Inspection

# Arrays
## Selection Algorithms
From *Algorithm Design and Applications* 

An example of a selection problem is selecting the kth smallest element from an unsorted collection of n elements. Can be solved in O(N Log N) time using sorting, but we can do better.

O(N) approach for solving selection problems is called Prune and Search (variant of divide and conquer)

### Common strategy of rune and search algorithms:
```
-  Choose an “approximate median” m∗ 
-  Partition S into three subsequences: 
	-  L: elements in S less than m∗ . 
	- E: elements in S equal to m∗
	- G: elements in S greater than m∗ 
- Recursively select L, E, or G as appropriate
```
### Randomized Quick-Select:
Time complexity is O(N) on average and O(N^2) on worst case.

When recursively selecting:

```
	- if k ≤ |L| then
		- quickSelect(L, k)
	- else if k ≤ |L| + |E| then
		- return x
	- else
		- quickSelect(G, k − |L| − |E|)
```
### Deterministic Selection:

Deterministic meaning algorithm will always have same runtime for given inputs, this time complexity is O(N). Idea is to deterministically pick the pivot instead of randomly selecting it.

Algorithm:

```
	- Partition the set S into  ceiling(n/5) groups of size 5 each (except, possibly, for one group).
	- Sort each group and identify its median element.
	- Apply the algorithm recursively on these ceiling(n/5) “baby medians” to find their median.
	- Use this element (the median of the baby medians) as the pivot and proceed as in the quick-select algorithm.
```

## Bottom Up Merge Sort
Useful for stable sorting in place without extra space. 

Description from Algorithmist.com.

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

## Open Addressing

 Open addressing is a method of collision resolution (the other common one is chaining). If the bucket a key is hashed to is already used, a probe sequence is started until a free bucket is found.

Types of probing sequences:

- Linear probing

- - The distance between probes is constant (i.e. 1, when probe examines consequent slots)

- Quadratic probing

  - The distance between probes increases by certain constant at each step (in this case distance to the      first slot depends on step number quadratically)

- Double hashing

- - The distance between probes is calculated using another hash function.

Example of linear probing when a collision occurs:

![linear probing](https://i.imgur.com/479y5g4.png)

If we need to delete a value/key, we must mark the key as deleted instead of actually removing it or else probing sequences will find wrong keys.

Example of the array after a deletion:

![deletion example](https://i.imgur.com/mrDhfTk.png)

# Strings

## Rabin-Karp
From Erik Demaine's MIT 6.006:

String matching algorithm with linear O(|s| + |t|) time complexity. 

Used to solve the problem "Given s and t, does s occur as a substring in t?".

Uses rolling hash and sliding window of size |s| on t and compare hash values.

When the hash value of the window matches hash of s, check the characters one by one for a match. If they are all equal, we have found a match. If they are not equal, keep going.

The probability of matching hash values being a collision should happen with the probability of 1/|s|

Algorithm:
```
- Compute hash of s
- Compute hash of the first |s| characters in t 
- For i in range(len(s), len(t): 
	- Compare hash values of s and the window
	- If no match, remove first character and add the next character
```
# Math
## P, NP, NP-Completeness
Definitions from Erik Demaine's MIT 6.006:
- **P** = {problems that can be solved in polynomial time}
- **NP** = {decision problems solvable in polynomial time via a "lucky" algorithm}
  - **Lucky algorithm**: a magical algorithm that always makes a right guess among the given set of choices
  - Another definition: **NP** = {decision problems with solutions that can be verified in polynomial time}
    - Verified meaning can prove it and check the proof in polynomial time
- **EXP** = {problems that can be solved in exponential time 2^n^c}
- **RE** = {problems solvable in finite time}
- **NP-Hard** is NP and above.
- **NP-Complete** is NP and also in NP-hard.
- **Weakly NP-complete** are NP-complete problems with peseudo-polynomial time algorithms
- **P != NP**: can be thought of as "can't engineer luck". Generating (proofs of) solutions can be harder than checking them.

Assuming **P != NP**: P ⊂ NP ⊂ EXP ⊂ RE

A **nondeterministic algorithm** is an algorithm that, even for the same input, can exhibit different behaviors on different runs.
Nondeterministic algorithms are often used to find an approximation to a solution, when the exact solution would be too costly to obtain using a deterministic one.

**The nondeterministic model**:
```
- Algorithm makes guesses
	- List of choices, and a choice is determined, and says yes/no
- Guesses are guaranteed to lead to a yes if possible
```

**Pseudo-Polynomial**: A numeric algorithm runs in pseudo-polynomial time if it is polynomial in the value of the input but exponential in the size of input.
- Key point here is for numeric algorithms, size refers to length of the binary string

For example in the given function below:
```
- For n in range(3127):
	- Do something that is O(1)
```
The size of the input is not 3127, but rather Log(3127), which is approximately 12 bits long. Thus the time complexity is O(2^Log(N)), which is exponential.  

## Generating Permutations
From Sandra Irani's Discrete Math Course Notes.

To generate permutations in lexicographic order:

```
- Initialize a list P
- While P != reverse(P):
	- P = GetNext(P)
- Output P
```
The GetNext() function works as follows:
```
- Find the largest index k such that nums[k] < nums[k + 1]. 
- If no such index exists, then the permutation is sorted in descending order, just reverse it. 
 	- For example, the next permutation of [3, 2, 1] is [1, 2, 3].
- Find the largest index l greater than k such that nums[k] < nums[l].
- Swap the value of nums[k] with that of nums[l].
- Reverse the sequence from nums[k + 1] up to and including the last element in the array.
```
E.g. for the set (8,2,5,3,7,6,4,1):
- Find the largest value that has a larger after it
  - 3 is the largest k
    - Since the only choices are 2 and 3
    - 2 < 5 and 3 < 7
- Then we look for the next value larger than Pk that is as closest to the end
  - In other words, the highest j value where Pj > Pk and j > k
  - In this case j is 4 
- Swap Pj and Pk
  - (8, 2, 5, **4**, 7, 6, **3**, 1)
- Then reverse the order of Pk+1 to end:
  - (8, 2, 5, 4, **1, 3, 6, 7**)

## Counting
<img src="https://i.imgur.com/sLUOSpk.png=250px" height="70%" width="70%"><br>

From Professor Sandra Irani's Discrete Math Course Notes:

### The Product Rule:

	- Cartesian product of the sets
	- |S1|x|S2|x..|Sn|
	- E.g. Picking lunch combinations
		○ |Entrees| x |Sides| x |Drinks|
	- However if picking an element decreases the number of choices…
		○ E.g. picking distinct pin numbers of length 4
			§ 10 * 9 * 8 * 7
			§ Since once we pick a number we cannot use it again
		○ This is an r-permutation, P(n, k), n choose k
		○ From n choices, choose k
			- n!/(n−k)!
### Counting Strings:
	- Essentially product rule
	- Set of choices is {0, 1}
	- For length n, 2n

### The Sum Rule:
	- Picking 1 from the union of two sets
	- E.g. |Drinks| = |Hot Drinks| + |Cold Drinks|
	- |Entrees| x |Sides| x |Drinks|

### Counting Passwords:
	- E.g. how many passwords of length 7
		○ If password must be under case letters or digits
		○ 10 digits (0-9), 26 letters in alphabet
		○ 36 choices at any index in the string
			§ Therefore 367 possible combinations
		○ If string must start with a letter
			§ 26 * 367
	- E.g. how many passwords of length 6,7, or 8?
		○ Sum Rule
			- Passwords of length 6 + length 7 + length 8
			- 366 + 367 + 368 

### Counting Subsets:
	- When order doesn't matter
	- This is an combination C(n, r)
	- n!/r!(n−r)!
	- From n distinct choices, pick r identical roles
	- E.g. student council from students
		○ Students are distinct, student council role is not C(100, 10)
	- E.g. 10 same prizes to distribute to students, with at most 1 per person
		○ If prizes were distinct we would use permutation P(100, 10)

		○ If at most 1 per person was not a restriction, choices do not decrease 

### Counting Strings with subsets:
	- E.g. how phone numbers of length 10 have exactly three 2s?
	- C(10, 2) * 97 
	- This is because we cannot select any more 2's after three of them, so the set of choices becomes {0, 1, 3, 4, 5, 6, 7, 8, 9} with a cardinality of 9.
	- We have picked 3 digits already, so there are only 7 more choices left.
		○ Product rule gives us 97 

### Counting by Complement:
	- How many selections have at least something.
	- E.g. how many 5-card hands have exactly 1 club
		○ 52 cards in a deck, 12 cards in a suite
		○ Find how 5-card hands do not have any clubs
			§ C(39, 12)
			§ We then subtract this from the total amount of 5-card hands
		○ So C(52, 12) - C(39, 12)

### Permutations with Repetition:
	- If all items are distinct, it is the factorial of the amount of items
	- If there are repeating item, for reach repeating item, divide by factorial of it
	- For example, for MISSISSIPPI
		○ 11 characters, so 11!
		○ 4 Is, 4 Ss, 2 Ps
		○ 11! / (4!4!2!)
		○ Can also be written as C(11, 4) x C(7, 4) x C(3, 2) x C(1, 1)
	- General Rule is:
		○ R1 copies of ck
		○ R2 copies of ck
		○ Rk copies of ck
		○ C(n, r1) x C(n-r1, r2) …
	- Another way is:
		- n!/((R)!(R2)!..(Rk)!)

### Counting Subsets with Repetition
	- Think in terms of binary strings
	- 0s sectioned off by 1s
	- 0001000100 
	- The number of ways to select n items from m varieties (distinct choices):
		C(n + m - 1, m - 1)

# Trees
## Self-Balancing BSTs

This page section covers only AVL and Red-Black trees. Note that there are other kinds of self-balancing BSTs.

AVL Trees:

```
- Have the following properties:
	- The sub-trees of every node differ in height by at most one
	- Every sub-tree is an AVL tree
Rotations are preformed during insertion is balance factor is exceeded
```

Red-Black Trees:

```
- Root is black
- NIL nodes are used for leaves to denote None
- All leaves (NIL nodes) are black
- Cannot have two 
- Every path from root to a NULL node has same number of black nodes
- Each inserted node is red and tree is rotated if a property is violated
```

AVL Trees are better for look-up intensive applications that Red-Black Trees because they are more strictly balanced.

Both AVL and Red-Black trees have the following time complexities:

| Operation | Average  | Worst Case |
| --------- | -------- | ---------- |
| Space     | O(n)     | O(n)       |
| Search    | O(log n) | O(log n)   |
| Insert    | O(log n) | O(log n)   |
| Delete    | O(log n) | O(log n)   |

## Prefix Tree

Also known as a trie. 

```
- Is pronounced as the middle syllable of retrieval. 
- O(w) search, w being the length of the query.
- Space complexity is O(N*K)
- Easy to implement with a dictionary.
	- Textbook implementations generally use an array of the 26 alphabet characters.
- Every node should also keep track of whether it is the ending letter of a word or not.
- Root can also be empty node to denote multiple starting prefixes.
```

Example Trie:

![trie](https://i.imgur.com/3lBoUqi.png)

Variations: 

- **Ternary search tree** (pronounced turn-a-ry):
  - Type of trie where nodes are ordered like BSTs nodes
  - 3 children instead of 2
  - More space efficient at the cost of speed
- **Radix tree** 
  - A compressed trie
  - Has a variation of it called Patricia tree

Example Radix Tree:

![radix tree](https://i.imgur.com/0OdKrOR.png)

Trie implementation with dictionaries:

```python
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.keys
        for c in word:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]
        cur[0] = True
        return
            
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.keys
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        if 0 in cur:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.keys
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True 
```
## B-Tree

Self-balancing tree with all O(Log N) operations. B-trees are optimized for systems that read and write large blocks of data, it is commonly used in databases and file systems.

Idea is to organize data within the tree to correspond to sectors on disk.
Read one disk sector at a time. One page corresponds to one tree node.
Root node is stored in memory at all times, access nodes when we need to read from disk sectors.

Every single read causes a whole sector to be loaded from the drive, so might as well take advantage of it.

O(n) space and O(log n) search/insert/delete operations.

## Tree Reconstruction From Traversals

To reconstruct a binary tree from its traversals, we need an in-order traversal along with one other.

The only following 3 combinations can reconstruct a tree:

- In-order and pre-order
- In-order and post-order
- In-order and level-order (breadth-first traversal)

## Threaded Binary Trees

Definition: "A binary tree is *threaded* by making all right child pointers that would normally be null point to the inorder successor of the node (**if** it exists), and all left child pointers that would normally be null point to the inorder predecessor of the node" (Van Wyk Christopher).

Threaded Binary Trees allow for inorder and preorder traversals without using extra space. These traversals are called *morris* traversals, named after [James H. Morris](http://www.cs.cmu.edu/~jhm/).

Pseudo code for inorder traversal and preorder traversals from Geeksforgeeks:

```
For inorder traversal:
1. Initialize current as root 
2. While current is not NULL
   If current does not have left child
      a) Print current node
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as right child of the rightmost 
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left
```

Inorder morris traversal visualization:

![inorder morris traversal](https://i.imgur.com/2qZYGng.png)

Another inorder visualization can be found [here](https://i.imgur.com/ZJSPuTI.jpg).

```
For preorder traversal
1. Initialize current as root
2. While current is not NULL
	If current does not have left child
		a) Print the current node
		b) Move to right child.
	Else
		Make the right child of the inorder predecessor point to the current node and 
		check for the following cases:
			If the right child of the inorder predecessor already points to the current node.
				a) Set right child to NULL
				b) Move to right child of current node.
			If the right child is NULL
				a) Set it to current node. 
				b) Print current node’s data
				c) Move to left child of current node.
```

Preorder morris traversal visualization:

![preorder morris traversal](https://i.imgur.com/LmDdgQW.png)

Morris traversal requires being able to modify the tree, however the tree is restored to its original form during the traversals. 

## Segment Trees

Source: LeetCode

A segment tree is a binary tree where each node represents an interval. Generally a node would store one or more properties of an interval which can be queried later.

Used to solve numerous range query problems like finding minimum, maximum, sum, greatest common divisor, least common denominator in array in logarithmic time.

What does a segment tree contain?

```
- Let arr[] be an array of size n.
- The root of our segment tree typically represents the entire interval of data we are interested in. This would be arr[0:n-1].
- Each leaf of the tree represents a range comprising of just a single element.Thus the leaves represent arr[0], arr[1] and so on till arr[n-1].
- The internal nodes of the tree would represent the merged or union result of their children nodes.
- Each of the children nodes could represent approximately half of the range represented by their parent.
```



## Fibonacci Heaps

Advantage is O(1) amortized complexity for decrease key operations. Used in optimized
version of Dijkstra's algorithm with O(E + V Log V) time complexity.

| Operation    | Average  |
| ------------ | -------- |
| Insert       | Θ(1)     |
| Find-min     | Θ(1)     |
| Delete-min   | O(log n) |
| Decrease-key | Θ(1)     |
| Merge        | Θ(1)     |

# Graphs

Note that for Big O notation of graph algorthims, E and V is actually |E| and |V|. I omitted the cardinality notation for simplicity. 

## Cycle Detection
To find cycles in both directed and undirected graphs, using DFS allows for an O(E + V) approach. Union-Find can also be used on directed graphs for an O(E Log V) approach. O(E + V)  scales slower than O(E Log V) and so DFS is the best approach.

For DFS cycle detection we can think of each vertex as a child in the recursion tree. If DFS gets called on a vertex that is a parent in the recursion tree then there is a cycle in the graph. 

## Connected Components
We can find connected components in a undirected graph by doing a DFS on the entire graph. During the DFS, we keep a counter to number the component each vertex belongs to. We increment the counter each time explore is called from the main DFS function. 

The important here to note is that DFS must be run on the entire graph, meaning we must iterate through all the vertices in the graph and recursively explore each vertex. Keep track of which vertices have been visited, and skip the ones that have been visited.

DFS for finding connected components:
```
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
```

## Strongly Connected Components
We can also find strongly connected components in directed graphs using DFS with O(E + V) time complexity. The algorithm given in *Algorithms* suggests doing DFS on the graph while keeping track of the pre-visit and post-visit time of each vertex. The vertex with the highest post-visit time will belong to a sink SCC. Knowing this, we then transpose (also called reverse) the graph, and then do a DFS for finding connected components on the reversed graph starting with the highest post-time vertex. Repeat until we have visited all vertexes in the stack. 

We can simplify this by keeping track of the order the vertices are processed in a stack. Once DFS is done, the vertex at the top of the stack is the one with the highest post-visit time.

SCC-DFS:
```
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
```

ExplorePV never pops from s, instead it marks u as visited, recursively calls itself on u's neighbors that have not been visited, and then pushes u to the stack. 

```
- Visited[u] = True
- For neighbors v that have not been visited:
	- ExplorePV(v, s)
- Push u to s
```

ExploreSCC marks u as visited, puts u into the scc at key c, and then calls itself on u's neighbors that have not been visited.

```
- Visited[u] = True
- Put u into the set at scc[c]
- For neighbors v that have no been visited:
	- ExploreSCC(v, c, scc)
```

To transpose/invert a graph:
```
- Create a dictionary r of adjacency lists
- For each vertex u in the original graph:
	- For each neighboring vertex v:
		- Add u to the adjacency list of v
		- r[v].add(u)
```

## Topological Sort
Topological sort, or topological ordering, of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

Used for dependency resolution, prerequisites planning, etc.

Any DAG has at least one topological ordering. DFS allows for linear time construction.

A very simple DFS approach is to order the vertices in decreasing order of their post visit times. This is because of the follow property:
- In a DAG, every edge leads to a vertex with a lower post number

Recall that determining the post visit times of vertices can be simplified using a stack. The last vertex pushed onto the stack has the highest post visit time. 

Once DFS is done, the vertex at the top of the stack is the one with the highest post-visit time.
```
Explore(u):
- Visited[u] = True
- For neighbors v that have not been visited:
	○ ExplorePV(v, s)
- Push u to stack
```
However this DFS approach will not work if there is cycle, so we must modify it to account for them. The following pseudo-code is from Wikipedia:

```
 function visit(node n)
    if n has a permanent mark then return
    if n has a temporary mark then stop (not a DAG)
    mark n temporarily
    for each node m with an edge from n to m do
        visit(m)
    mark n permanently
    add n to head of L
```

Another algorithm for topological sorting is Kahn's algorithm (the psuedo-code from *Algorithms*).

We will keep an array in[u] which holds the indegree (number of incoming edges) of each node. For a source, this value is zero. We will also keep a linked list of source nodes.

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

At the end we can check to see if the graph has edges to see if there is a cycle or not. If the degree of vertex is greater than 0, then there is a cycle.

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

## Dijkstra’s Shortest Path Algorithm

Implementation can vary a lot. Most textbooks give the pseudo-code for the version that uses a min-heap and decrease-key method. However, decrease-key requires extra space to keep track of the location of each node in the heap. Implementations that uses heaps have a time complexity of O((E + V) Log V), which can be simplified to O(E Log V) for connected graphs.

Other version is to simply enqueue the neighbor whenever a new minimum is found. Time complexity for the priority queue will be O(E), so time complexity will still be O(E Log V). 

Fibonacci heap is most optimal implementation with a time complexity of O(E + V Log V), but likely to be unnecessary for sparse graphs. 

```
Dijkstra's Shortest Path O(E Log V):
	- Create distance and parent maps. 
	- Create priority queue (key for each vertex is its value in distance map).
	- For each vertex in graph, set distance as infinity.
	- Set source distance to 0.
	- Enqueue source vertex. 
		○ If using a min heap, enqueue all the vertices, and then decrease their key instead of enqueuing when a new cost is found.
			§ To decrease key we update the value of the node in the heap and then bubble it up.
	- While queue is not empty:
		○ Get next vertex with lowest cost v
		○ For all neighbors u:
			§ If dist(v) + cost(u) < dist(u):
				□ Update distance and parent values in the respective maps
				□ enqueue(u)
	- Return parent map. Can also return distance map if path costs are needed.

To build path recursively look up destination parent from parent map. 
	- For base case check if edge has parent, if not then it is the source.
	- Then look up parent of the destination edge.
	- Recursive call is createPath(parents, parent) + parent
```

Dijkstra's does not work on graphs with negative weights because once a node has been dequeued it assumes the shortest path to that node has been found.

## Bellman-Ford
O(V*E) Algorithm used to find shortest paths in graphs with negative weights. Can also detect negative cycles.

Idea is to update all the edges |V| - 1 times. This ensures that shortest path from the source to all vertices have been found. Then we do one more iteration, and if any distance can be updated then there is a negative cycle.
```
Bellman-Ford:
	- Declare a distance and parent dictionary
	- Set all distances to infinity and vertices' parents to itself.
	- Set source distance to 0
	- Loop for |V| - 1 times:
		○ For all edges(u, v) with weight w in graph G:
			§ If distance[u] is infinity, we skip it
			§ Otherwise:
				□ If distance[u] + w < distance[v]:
					® Update distance and parent of v
Loop one more time, and if any shorter distances are found, we know a negative cycle exists. 
```

## Kruskal’s Algorithm
Greedy algorithm for finding minimum spanning tree of a graph. Time complexity is O(|E| log |V|).

Idea is to start with an empty tree T, and while the size of T is |V| - 1 edges,
repeatedly take the smallest edge from the graph and insert it into the tree. Ensure that adding the edge does not create a cycle (skip the edge if it does). 

Kruskal's can be implemented efficiently using the Disjoint-Set structure. The implementation varies depending on the representation of the graph. 

```
To find a MST (there can be multiple) in a graph G:
- Declare empty set T to hold the MST.
- Create a set in the Disjoint-Set for every edge in G.
- Sort all the edges in G by their weight value and put them in a priority queue.
- While there are less than |V| - 1 edges in T:
	- Pop the next smallest edge (u, v) from the priority queue
	- Get the parent of u and the parent of v
		- Ensure that they do not equal each other
	- Add the edge to T
	- Merge the sets of u and v in the Disjoint-Set.
- Return T
```

The reason we stop when size of T is equal to |V| - 1 is each vertex in an MST can only have one edge connecting it to another vertex. The amount of edges |E| in a connected graph cannot be less than |V| - 1, so we do not need to check if the priority queue is empty. If we are given a graph with more than one connected component then this does not apply.


## Prim’s Algorithm
Greedy algorithm for finding minimum spanning tree in an undirected graph. Idea is to start out with a vertex, and repeatedly add the next reachable vertex with the lowest edge cost until all vertices are in the MST.

When implemented using a Fibonacci heap its time complexity is O(E + V Log V), otherwise O(E Log V).

Prim's algorithm is similar to Dijkstra's shortest path algorithm. We declare a distance and parent dictionary. Set all distances to infinity and all vertices' parents to itself. Pick a vertex as the starting vertex and set its distance to 0.

A major difference between Prim's and Dijkstra's is for Prim's we only keep track of the shortest edge (recall in Dijkstra's we add the edge value to the previous value). 

If implemented using a heap, we must enqueue all vertices at the beginning. The key is the smallest edge value of each vertex. When a smaller distance value is found we do a decrease key operation.

Can also be implemented using a priority queue with a set keeping track of visited vertices. Visited means the vertex has been popped from the queue. We only update and enqueue neighboring vertices of a vertex if it has not been visited and has a shorter distance than what is stored in the distance dictionary. 

## Eulerian Trails and Cycles
An Euler trail:

- visits every edge in the graph exactly once (vertices may well be crossed more than once)
- is a trail that crosses every edge exactly once without repeating, if it ends at the initial vertex then it is a Euler cycle.

An undirected graph has an Eulerian cycle if and only if every vertex has even degree, and all of its vertices with nonzero degree belong to a single connected component.

How to tell if a undirected graph is Eulerian or not?
```
- Eulerian Cycle
	- An undirected graph has Eulerian cycle if following two conditions are true.
		- All vertices with non-zero degree are connected.
			- We don’t care about vertices with zero degree because we only need to visit edges.
		- All vertices have even degree.

- Eulerian Trail
	- An undirected graph has Eulerian Path if following two conditions are true.
		- All vertices with non-zero degree are connected.
		- If 0 or 2 vertices have odd degree and all other vertices have even degree. 
		- Only 1 vertex odd degree vertex is not possible in an undirected graph (sum of all degrees is always even in an undirected graph)
```

How to check if a directed graph is Eulerian?
```
- Eulerian Cycle
	- A directed graph has an Eulerian circuit if it is connected and each vertex has the same in-degree as out-degree.
	
- Eulerian Trial
	- A directed graph has an Eulerian path if it is connected and each vertex except 2 have the same in-degree as out-degree
	- One of those 2 vertices must have an out-degree 1 larger than its in-degree 
		- This is the start vertex
	- The other vertex must have an in-degree 1 larger than its out-degree
		- This is the end vertex
```

## Hierholzer’s Algorithm
For finding Eulerian Circuits in O(E+V) time complexity.

Algorithm for undirected graphs:
```
- Start with an empty stack and an empty circuit (Eulerian path).
	- If all vertices have even degree - choose any of them.
	- If there are exactly 2 vertices having an odd degree - choose one of them.
	- Otherwise no Euler circuit or path exists.
- If it has neighbors: 
	- Add the vertex to the stack and set it as the current vertex
	- Take any of its neighbors, remove the edge between that neighbor and the vertex, and set the neighbor as the current vertex.
- If current vertex has no neighbors:
	- Add it to circuit, pop the next vertex from the stack 
- Repeat until the current vertex has no more neighbors and the stack is empty.
- Note that obtained circuit will be in reverse order - from end vertex to start vertex.
```

Algorithm for directed graphs:
```
- Start with an empty stack and an empty circuit
	- If all vertices have same out-degrees as in-degrees - choose any of them.
	- Otherwise choose the vertex whose out-degree is 1 larger than its in-degree.
		- See Eulerian Path requirements for details
- If current vertex has no out edges:
	- Add it to circuit, pop the next vertex from the stack and set it as the current one.
- If current vertex has out edges:
	- Add the vertex to the stack, take any of its neighbors, remove the edge between that vertex and selected neighbor, and set that neighbor as the current vertex.
	- Repeat until the current vertex has no more out edges and the stack is empty.
```

## Fleury’s Algorithm
Like Hierholzer's algorithm, Fleury's algorithm is used for finding Eulerian Trial/Cycles. Fluery's has worse time complexity with O((E+V)^2), but it is easier to implement for Eulerian trail problems.

Picking the starting edge for Fleury's is the same as in Hierholzer's. The idea behind Fluery's is "don't burn bridges". A bridge being the only edge connecting a vertex to another. 

If we have a choice between a bridge and a non-bridge, always choose the non-bridge.

This can be implemented by checking if removing a given edge between v and u will make u have a degree of 0. The algorithm stops when there are not more edges.

# Dynamic Programming

## 0/1 Knapsack
Given an array of values, an array of weights, and capacity W, what is most valuable combination of items that can fit in W?

We define K(w,j) as the maximum value achievable using a knapsack of capacity w and items 1 through j.

The answer we want is K(W, n), with n being the size of the value/weight arrays.

K(W, n) expressed in terms of smaller subproblems: either item j is needed to achieve the optimal value, or it isn't needed (Dasgupta et al., 2007).

![0/1 knapsack recurrence relation](https://i.imgur.com/mjnqDgk.png)


## Longest Increasing Subsequence

The LIS problem asks "given an unsorted array of integers, find the length of longest increasing subsequence".

Can be solved in O(N^2) time with dynamic programming, however the optimal O(N Log N) solution uses binary search.

![longest increasing subsequence recurrence relation](https://i.imgur.com/Qmp9RJo.png)

For every index i in the input array A, we find the max previous entry (A[j] :where j < i) for values less than A[i] and increment it. When implementing, be sure to handle the case where there aren't any values less than A[i].

## Edit Distance
Given two strings, x and y, find the minimum number of steps required to convert x to y.

Edit distance can be expressed as E(i, j), where i and j are indexes of each string. E(i,j) can be expressed in terms of three smaller subproblems:

```
Case 1:
E(i-1, j)
The rightmost character is x[i]

Case 2:
E(i, j-1)
The rightmost character is y[j]

Case 3:
E(i-1, j-1)
The rightmost character is x[i] and y[j]
```
![edit distance recurrence relation](https://i.imgur.com/ykxilkm.png)

Diff(x,y) being a function that returns 0 or 1 depending on if the characters match or not.

# Famous Problems

## Huffman Coding
Greedy algorithm for text compression. O(N Log N) time complexity where n is the number of unique characters.

Idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. The most frequent character gets the smallest code and the least frequent character gets the largest code. 

Must keep prefix-free property: no code can be a prefix of another.

Two parts:
```
- Build a Huffman Tree from input characters.
- Traverse the Huffman Tree and assign codes to characters.
```
To build the Huffman Tree:
```
- Create a node for every unique character in string S storing the character and its frequency.
- Put all nodes in into a priority queue
- While there are 2 items in the queue:
	○ Extract the min t1
	○ Extract the min t2
	○ Create a node with left of t1 and right of t2, and value is t1 + t2
	○ Enqueue this node (note how this node stores no character)
- When there is 1 item left in the queue, that node is the root of the our tree.
```
Assign codes to characters:
```
- We traverse the tree starting from the root.
- Every left branch adds a 0 to the end of the code
- Every right branch adds a 1 to the end of the code
- We arbitrarily choose the assignments, left can also be 1 as long as right is 0. 
- When we reach a leaf node, the leaf stores the character associated with they key built from traversing to it
```
To decode we run the string through the tree. For every 0 we got left, every 1 we go right. Once we reach a leaf, store the character and start over from the root.

An example of a Huffman tree:
<br><img src="https://i.imgur.com/LfRqswX.png" height="50%" width="50%"><br>

## Set Cover
Given a universe U of n elements, a collection of subsets of U say S = {S1, S2…,Sm} where every subset Si has an associated cost. Find a minimum cost sub collection of S that covers all elements of U.

NP-complete problem. Greedy algorithm can only approximate. 

Greedy approach is:
- In each step, choose the set Si containing the most uncovered points. Repeat until all points are covered.

Suppose: 
```
- S1 = {1, 2, 3, 8, 9, 10}
- S2 = {1, 2, 3, 4, 5}
- S3 = {4, 5, 7}
- S4 = {5, 6, 7}
- S5 = {6, 7, 8, 9, 10}
```
Our Greedy algorithm selects the largest set, S1 = {1, 2, 3, 8, 9, 10}. 
Excluding the points from the sets already selected, we are left with the sets:
	- {4, 5}, {4, 5, 7}, {5, 6, 7}, and {6, 7}. 

At best, we must select two of these remaining sets for their union to encompass all possible points, resulting in a total of 3 sets. 
The greedy algorithm could now pick the set {4, 5, 7}, followed by the set {6}.

## Knight’s Tour
From Geeksforgeeks.

Backtracking problem. A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square only once. 

The knight's tour problem is an instance of the more general Hamiltonian path problem in graph theory. Unlike the Hamiltonian path problem, the knight's tour problem can be solved in linear time.

Backtracking approach:
```
- If all squares are visited 
	- print the solution
- Else
	- Add one of the next moves to solution vector and recursively check if this move leads to a solution.
		- (A Knight can make maximum eight moves. We choose one of the 8 moves in this step).
	- If the move chosen in the above step doesn't lead to a solution then remove this move from the solution vector and we try other moves.
	- If none of the alternatives work then return false.
		- Returning false will remove the previously added item in recursion. 
		- If false is returned by the initial call of recursion then "no solution exists"
```
Linear solution is Warnsdorf's rule:
```
- We can start from any initial position of the knight on the board.
- We always move to an adjacent, unvisited square with minimal degree
	- degree means number of unvisited adjacent
```
Significance of Warnsdorf's rule:
- Although the Hamiltonian path problem is NP-hard in general, on many graphs that occur in practice this heuristic is able to successfully locate a solution in linear time. The knight's tour is a special case (Wikipedia).
