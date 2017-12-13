# Practice	 Problem Solutions
Compilation of my write ups for coding problems that I found valuable.

# Bit Manipulation
## Gray Code
[LeetCode #89](https://leetcode.com/problems/gray-code/description/)

This problem can be solved using backtracking/DFS, but it is better to just learn what Gray code (aka reflected binary code) is. 
https://www.allaboutcircuits.com/technical-articles/gray-code-basics/

From Wikipedia:
```
/*
 * This function converts an unsigned binary
 * number to reflected binary Gray code.
 *
 * The operator >> is shift right. The operator ^ is exclusive or.
 */
unsigned int binaryToGray(unsigned int num)
{
    return num ^ (num >> 1);
}
```

# Graph Problems
## Evaluate Division
[LeetCode #399](https://leetcode.com/problems/evaluate-division/description/)

This is straightfoward to solve as a graph problem; the numerators and denominators are vertices and the equations are weighted edges. There are other solutions that involve putting the values in another data tructure and then doing DFS/BFS search, but looking at the queries we can see this is a variation of the all-pairs shortest path problem. I think this problem is trying to test if we know Floyd-Warshall. Floyd–Warshall is actually very easy to memorize - we test every edge for every pair. I have more details written up in my graph notes, but the main part of the algorithm is:
```python
for k from 1 to |V|:
  for i from 1 to |V|:
    for j from 1 to |V|:
      if dist[i][j] > dist[i][k] + dist[k][j]:
             dist[i][j] = dist[i][k] + dist[k][j]
```

## Alien Dictionary
[LeetCode #269](https://leetcode.com/problems/alien-dictionary/description/)

Like the other graph problems this one is easy if we can see that it is indeed a graph problem. Trying to come up with our own logic for solving the problem seems too impratical. All this problem requires is a topological sort and returning the ordering. Knowing how lexicographic works is important, we can only deduce a relationship from the ordering of the first character in each word, or the character after a common prefix. We know w < e < r because those are the first characters in each word, and we know t < f and r < t because those come after the prefixes wr and e, respectively. 

If we look at these relations as edges of a graph, we can do a topological sort and get the ordering. If there is no topological ordering, we return an empty string.

That example doesn't quite show why topological sort is needed because the nodes and edges are already in correct order (w < e < r < t < f), but for a case like [ab, adc], we know that b < d but no information about a and c, but we still need to include them in the result. This mimics the case when topological sort finds vertices with degrees of 0.

## Minimum Height Trees
[LeetCode #310](https://leetcode.com/problems/minimum-height-trees/description/)

This question is hard to understand if unfamiliar with the properties of rooted trees. The key to this problem is knowing that there can only be either 1 or 2 nodes that are the root of a minimum height tree in a graph.

The algorithm is to remove leaf nodes one layer at a time and stop when only 1 or 2 nodes remain. The resulting nodes are the nodes of the minimum height trees. We can use a queue, enqueue all current leaf nodes, then as they are removed enqueue any neighbor whose new degree is 1. Removing a node in this case means decreasing the degrees of all its neighbors and the total vertex count by 1. Note that the loop condition refers to the total vertex not the length of the queue.

# Math Problems
## Next Permutation
[LeetCode #31](https://leetcode.com/problems/next-permutation/description/)

This problem just requires implementation of the next lexicographic permutation algorithm. We can of course come up with our own logic to solve it, but I'm guessing the interviewer will be more pleased if we identify that there is an algorithm for the problem. The algorithm from Wikipedia is:

```
- Find the largest index k such that nums[k] < nums[k + 1]. 
- If no such index exists, then the permutation is sorted in descending order, just reverse it. 
  - For example, the next permutation of [3, 2, 1] is [1, 2, 3].
- Find the largest index l greater than k such that nums[k] < nums[l].
- Swap the value of nums[k] with that of nums[l].
- Reverse the sequence from nums[k + 1] up to and including the last element in the array.
```

# Tree Problems
## Binary Search Tree Iterator

[LeetCode #173](https://leetcode.com/problems/binary-search-tree-iterator/description/)

This can be solved easily with O(h) space and amortized O(1) time by pushing the nodes in the path to the left most leaf onto a stack. Every time next() is called, pop from the stack. This is the smallest node not yet iterated over.

If the popped node has a right child, the next smallest will be in that right child's subtree, so we push the path to the left most leaf onto a stack again. If the popped node does not have a right child, the next smallest is it's parent. Repeat every time a node is popped until stack is empty.

The problem has a more optimal solution with O(1) space and amortized O(1) time by using a threaded binary tree and doing a Morris traversal.

See: https://discuss.leetcode.com/topic/24442/my-java-solution-with-o-1-space-and-o-1-amortized-time-using-morris-tree-traversal/2

## Unique Binary Search Trees

[LeetCode #96](https://leetcode.com/problems/unique-binary-search-trees/description/)

This is one of the problems where its better to just know the formula for it. This is an application of the Catalan numbers. From Wikipedia: "Cn is the number of non-isomorphic ordered trees with n vertices. (An ordered tree is a rooted tree in which the children of each vertex are given a fixed left-to-right order.)"
```
Cn = (2n)!/(n+1)!n!
```
## Binary Tree Maximum Path Sum
[LeetCode #124](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

The way I thought of this problem is we are finding the maximum path for a node's left and right subtrees, and then combining them with the node to form the maximum path for the entire tree. However there are some conditions we have to be aware of:
- A single node can be the maximum path for the entire tree
- The root may not be part of the final maximum path

So what I did was run DFS on the tree, and then for every node I check whether I should include the left or child's max path sum, or just skip them.

This was the logic I followed:
- If the left or right pathsum added to the node's value results in a larger sum, then include it. If neither does, discard them.
- If the left or right path sum combined with the node results in a larger pathsum than the pathsum of the entire tree, return that path sum instead. (We store subtree's combined pathsum in a variable and update it everytime we encounter a larger one).

My solution beats 99.38% of other Python solutions. Looking at the others, I think its because I'm doing conditional checks instead of assigning left and right subtree's sums to 0 if they are less than then node's value. Using functions like max() and min() does add significant time; looking at the cPython implementations both max() and min() initializes iterators and trys to use them regardless of the given input.

# Backtracking

### Word Search

[LeetCode#79](https://leetcode.com/problems/word-search/description/)

This problem is a good refresher on DFS backtracking. It is important to keep in mind that the value returned by the call at depth 0 (the root) of the recursion tree is the final return value.

Thus we must let the root function know when we successfully find a word.

Another restriction is is the same letter cell may not be used more than once, so we must keep track of visited coordinates for each DFS individually. One accomplish this is to use a visited set, with the penalty of using extra space. However if we are allowed to modify the board, we can set a flag for visited coordinates, and then restore them as the DFS is backtracking.

```python
class Solution(object):
    def __init__(self):
        self.cords = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = '#'
                    if self._dfs(board, word, i, j, 0):
                        return True
                    board[i][j] = temp
        return False
        
    def _dfs(self, board, word, i, j, n):
        if n == len(word) - 1:
            return True
        for y,x in self.cords:
            y += i
            x += j
            if y >= 0 and y < len(board) and x >= 0 and x < len(board[i]):
                if board[y][x] == word[n+1]:
                    temp = board[y][x]
                    board[y][x] = '#'
                    if self._dfs(board, word, y, x, n+1):
                        return True
                    board[y][x] = temp
        return False
```



# Dynamic Programming

## Climbing Stairs
[LeetCode #70](https://leetcode.com/problems/climbing-stairs/description/)

This problem is easy but it is over to think the recurrence relation. The total number of ways to reach i^th step is equal to sum of the ways of reaching the (i - 1)^th and (i - 2)^th step.

Thus, the dp relation can be written as dp[i] = dp[i−1] + dp[i−2]. This is just the Fibonacci sequence.
