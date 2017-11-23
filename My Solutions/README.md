# Coding Problem Solutions
This is a compilation of my write ups of coding problems that I found valuable.

# Math Problems
## Next Permutation
[LeetCode #31](https://leetcode.com/problems/next-permutation/description/)

Just requires implementation of the next lexicographic permutation algorithm. Description can be found in my notes.

# Tree Problems
## Unique Binary Search Trees
[LeetCode #96](https://leetcode.com/problems/unique-binary-search-trees/description/)

This is one of the problems where its better to just know the math formula for it. This is an application of the Catalan numbers.

From Wikipedia: "Cn is the number of non-isomorphic ordered trees with n vertices. (An ordered tree is a rooted tree in which the children of each vertex are given a fixed left-to-right order.)"

Cn = (2n)!/(n+1)!n!

## Binary Tree Maximum Path Sum
[LeetCode #124](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

So the way I thought of this problem is we are finding the maximum path for a node's left and right subtrees, and then combining them with the node to form the maximum path for the entire tree. However there are some conditions we have to be aware of:
- A single node can be the maximum path for the entire tree
- The root may not be part of the final maximum path

So what I did was run DFS on the tree, and then for every node I check whether I should include the left or child's max path sum, or just skip them.

This was the logic I followed:
- If the left or right pathsum added to the node's value results in a larger sum, then include it. If neither does, discard them.
- If the left or right path sum combined with the node results in a larger pathsum than the pathsum of the entire tree, return that path sum instead. (We store subtree's combined pathsum in a variable and update it everytime we encounter a larger one).

My solution beats 99.38% of other Python solutions. Looking at the others, I think its because I'm doing conditional checks instead of assigning left and right subtree's sums to 0 if they are less than then node's value. Using functions like max() and min() does add significant time; looking at the cPython implementations both max() and min() initializes iterators and trys to use them regardless of the given input.

# Dynamic Programming
## Climbing Stairs
[LeetCode #70](https://leetcode.com/problems/climbing-stairs/description/)

This problem is easy but it initially stumped me because I thought there would be more to the relation.

The total number of ways to reach i^th step is equal to sum of the ways of reaching the (i - 1)^th and (i - 2)^th step.

The dp relation can be written as dp[i] = dp[i−1] + dp[i−2]

Even simpler, this is the Fibonacci sequence.