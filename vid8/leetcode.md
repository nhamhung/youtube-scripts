# 📚 Array / String

### 💡 **Key Points**

- Both Array and String can be accessed by indexing
- Both Subarray and Substring can be created by slicing
- Must avoid accessing out-of-bound index

### 📌 **Question Types**

- Iterate forward / backward in Array/String using pointers (Merge Sorted Array, Remove Element, Remove Duplicates from Sorted Array I/II, Find the Index of the First Occurrence in a String)
- Combine with other data structure like Dictionary (Majority Element)
- Manipulate Array / String (Rotate Array)
- Find min/max or accumulate some amount while traversing Array / String (Best Time to Buy and Sell Stock I/II)
- Recursion, DP, Greedy on Array / String (Jump Game I/II)
- Precomputation to reduce time complexity (Product of Array Except Self)
- Build String (Roman to Integer, Integer to Roman)
- String processing (Length of Last Word, Longest Common Prefix, Text Justification)

---

# 👯‍♂️ 2 Pointers

### 💡 **Key Points**

- Where should we initialise 2 pointers (start or end)
- Any existing property of array if we can make use of (sorted)
- When to advance each pointer and what happens after they terminate (meet each other or cannot advance anymore)

### 📌 **Question Types**

- 2 pointers at 2 ends:
  - Input is sorted -> contract left and right pointer until condition is met (2 Sum, 3 Sum)
  - Check if 2 left and right boundaries keep matching while contracting (Valid Palindrome)
  - Greedily contract left or right to maximise some metric (Container With Most Water)
- 2 pointers at 2 starts:
  - Advance each pointer based on some condition and check final state if desired (Is Subsequence)

---

# 🪟 Sliding Window

### 💡 **Key Points**

- How to track / update current window state after advancing right or contracting left
- How to check if current window meets condition
- How to determine whether we have contracted left enough such that window is no longer valid

### 📌 **General Pattern**

- 2 pointers left and right at 0 marking window boundary
- At each iteration after advancing right, update current window state
- While current window state satisfying some condition -> update global min/max and contract left until window is reset to fail condition unless we advance right again
- Keep advancing right while right < n

---

# 🧮 Matrix

### 💡 **Key Points**

- Be familiar with 2D array processing using indexes (i, j)
- Be familiar with getting valid neighbors of (i, j) such that they are not out of bound

### 📌 **Question Types**

- Use a list of sets representing rows, cols, diagonals, antidiagonals, 3x3 boxes to record each row, col, diagonal, antidiagonal, box's state (Valid Sudoku, Set Matrix Zeroes)
- Use variables representing top, left, right, bottom to define boundaries and contract them gradually to control iteration from outer to inner layers (Spiral Matrix, Rotate Image)
- Create a copy of existing matrix to track its current state while we modify the original matrix simultaneously and in-place based on this state (Game of Life)

---

# 🗂️ Hashmap

### 💡 **Key Points**

- Know what key -> value mapping to create to can help solve the problem

### 📌 **Question Types**

- Create a mapping of character -> character count for 2 strings comparison (Ransom Note, Valid Anagram, Group Anagrams)
- Create a strict 1-to-1 mapping of character -> some other character / word to check for strict correspondence (Isomorphic Strings, Word Pattern)
- Create a mapping of value -> index to record the position of this value (Two Sum, Contains Duplicate II)
- Create a visited set to check if an element has existed before (Happy Number, Longest Consecutive Sequence)

---

# 📆 Intervals

### 💡 **Key Points**

- Know when there is overlap
- Rebuild current interval until there's no more overlap

### 📌 **General Pattern**

- Sort intervals by start time
- For every consecutive intervals, compare next interval's start time with current interval's start / end time to check for complete / partial overlap
- If there's overlap, rebuild current interval by min(2 start times) and max(2 end times) if we want to merge intervals (Merge Intervals and Insert Interval) or max(2 start times) and min(2 end times) if we want to only get the overlap (Minimum Number of Arrows to Burst Balloons)
- Repeat these steps until there's no more overlap with subsequent intervals

---

# 🧱 Stack

### 💡 **Key Points**

- Know the condition when to push onto or pop off the stack
- Always ensure stack is not empty before popping off

### 📌 **Question Types**

- Check for valid opening and closing bracket pairs (Valid Parentheses):

  - Append opening brackets to stack
  - If receives a closing bracket, pop of stack if it's not empty and has a matching opening bracket. Otherwise return False
  - Check if all bracket pairs can be processed

- Construct directory path corresponding to push by "some directory name" or pop by ".." (Simplify Path)

- Evaluate mathematical expression (Evaluate Reverse Polish Notation):

  - If token is number then push onto stack
  - Elif token is binary operator then pop top 2 elements from stack, perform computation and push result back on stack

- Perform O(1) Min/Max stack (Min Stack):
  - Each time we push a new element on stack, also attach a corresponding min / max value
  - This min / max value is determined by comparing new element with existing min / max value at the top
  - This min / max at the top determines min / max value at each state of the stack and can be retrieved in O(1)

---

# 🔗 Linked List

### 💡 **Key Points**

- Use Sentinel Node when possible to handle edge case especially when we have to delete node
- When iterating through a linked list, use a separate pointer node and to not lose current head pointer
- For linked list traversal, ensure correct termination by checking whether pointer is not None or pointer.next is not None

### 📌 **Question Types**

- Detect cycle with slow and fast pointers (Linked List Cycle):

  - Ensure linked list has at least 1 element. Initialise slow = head which travels 1 step at a time, fast = head.next which travels 2 steps at a time
  - If fast and slow meet, there's cycle
  - Otherwise, if fast is None or fast.next is None without meeting slow, there's no cycle

- Combine 2 linked lists into 1 using 2 pointers (Add Two Numbers, Merge Two Sorted Lists)
- Deep copy a linked list using preorder DFS with a mapping of old to new node acting as a visited set (Copy List with Random Pointer)

- Reverse entire or a subset of linked list using 3 variables temp, curr, prev (Reverse Linked List II):

  - temp = curr.next to temporarily hold curr's next as we will update curr.next pointer
  - curr.next = prev to point curr to prev
  - prev = curr as curr will be advanced to temp
  - curr = temp to keep reversing next elements

- Pre-advance 1 pointer by k to let slower pointer access last kth node with 1 traversal (Remove Nth Node From End of List)
- Remove consecutive duplicates with 2 pointers (Remove Duplicates from Sorted List II)
- Join last node with first node to complete cycle to rotate a linked list (Rotate List)
- Combine hash table and doubly linked list to build a LRU cache

---

# 🌳 Binary Tree

### 💡 **Key Points**

- Know when to use recursion for tree
- Know preorder, inorder, postorder traversal on tree
- Know DFS, BFS on tree
- Know backtracking on tree

### 📌 **Question Types**

- Recursion (Maximum Depth of Binary Tree, Same Tree, Invert Binary Tree, Symmetric Tree, Flatten Binary Tree to Linked List, Path Sum, Count Complete Tree Nodes, Lowest Common Ancestor of a Binary Tree)
- Preorder, Inorder, Postorder traversal (Construct Binary Tree from Preorder and Inorder Traversal, Construct Binary Tree from Inorder and Postorder Traversal, Sum Root to Leaf Numbers, Binary Search Tree Iterator)
- Run BFS on tree (Populate Next Right Pointers in Each Node II, Binary Tree Right Side View, Average of Levels in Binary Tree, Binary Tree Level Order Traversal, Binary Tree Zigzag Level Order Traversal)
- Backtracking on tree (Sum Root to Leaf Numbers)

---

# 🌲 Binary Search Tree

### 💡 **Key Points**

- Know balanced and ordered properties of BST
- Know inorder traversal, BFS, DFS on tree

### 📌 **Question Types**

- DFS (Minimum Absolute Difference in BST)
- Inorder (Minimum Absolute Difference in BST, Kth Smallest Element in a BST)
- Recursive traversal with valid range (Validate Binary Search Tree)

---

# 🌐 Graph

### 💡 **Key Points**

- Know how to formulate a problem as a graph problem
- Use a visited set to detect/prevent cycles
- Know BFS, DFS on graph
- Know how to get valid neighbors of current node
- Know how to construct weighted, unweighted, unidirectional, bidirectional graph with adjacent list/matrix
- Know Topological Sort on graph

### 📌 **Question Types**

- DFS, BFS on 2D graph (Number of Islands, Surrounded Regions, Clone Graph, Minimum Genetic Mutation)
- Use additional data structure such as Dictionary (Clone Graph)
- Construct then traverse graph (Evaluate Division, Course Schedule I/II)
- Topological Sort (Course Schedule I/II)

---

# 🔤 Trie

### 💡 **Key Points**

- Know how to construct a trie from words
- Know how to search for a word in trie
- Recursive traversal on trie

### 📌 **Question Types**

- Construct and search in a trie (Implement Prefix Tree, Design Add and Search Words Data Structure)

---

# 🔁 Backtracking

### 💡 **Key Points**

- Know how to use mutable data structures such as Set or List to try a candidate then backtrack
- Know how to keep track of current state and terminating condition to stop recursion
- Know how to determine valid candidates to try and backtrack on
- Know 2 types of backtracking: return some output solution or some True/False condition

### 📌 **General Pattern**

- First, determine what variables are enough to keep track of current state (some index i, j, ...) or build up solution (some List, Set, ... representing path or visited) for backtracking function
- In backtracking function:
  - Determines terminal condition (when index or path reaching certain length) -> collect a candidate solution or return True/False
  - Determines all valid candidates for trying:
    - Add candidate to path or visited
    - Recursively call backtracking function to try
    - Remove candidate from path or visited to backtrack

---

# 🔎 Binary Search

### 💡 **Key Points**

- Familiar with standard iterative binary search using left and right pointers when the entire array is sorted and unique (no duplicates)

### 📌 **General Pattern**

- Start with standard iterative binary search using left and right pointers
- For extended variants of binary search:
  - Determine whether there's any half that is surely sorted to take advantage of it

---

# 🛷 Heap

### 💡 **Key Points**

- Know properties of Min/Max Heap
- Know common operations on Heap like heappush, heappop

### 📌 **Question Types**

- Get k-th largest element (Kth Largest Element in an Array):
  - Create a min heap and keep adding elements from original list to this heap while maintaining its fixed size to k
  - Do it by checking after adding each element if min heap size > k -> we pop current min to maintain property that this heap always store k largest elements
  - To return kth largest element, pop current min of final min heap

---

# 📐 DP

### 💡 **Key Points**

- Either memoization or bottom-up needs to cache some state (i, j, k, ...) so it's important to determine which variables are enough to track current state
- Think of how a problem(i, j, k, ...) can be constructed by one or many subproblems(i - ..., j - ..., k - ...)
- For memoization, subproblems can be represented as recursive calls which help to build up current state
- For DP, subproblems can be represented as neighboring cells which helps to build up current cell

### 📌 **General Pattern**

- Memoization:

  - Define helper function with parameters as the state required to represent current node in the recurrence tree such as current index i
  - Define base case and recurrence relation to perform computation for current node based on recursive computation from children nodes (subproblems of smaller size)
  - Also, use a memo dictionary to cache the result of this state to prevent repeated computation

- Bottom-up:
  - Initialise 1D or 2D DP array with i or i and j representing current state of problem we need to solve
  - Pre-populate dp[i] or dp[i][j] for base cases
  - Start to gradually build up solutions for subsequent cells based on neighboring cells which has already been computed in previous iterations
