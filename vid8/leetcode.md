# 📚 Array / String

### 💡 Key Points

- Both Array and String can be accessed by indexing
- Both Subarray and Substring can be created by slicing
- Avoid accessing out-of-bound index

### 🧩 Question Types

- Iterate forward/backward using pointers  
  _e.g._ Merge Sorted Array, Remove Element, Find Index of First Occurrence in a String
- Combine with data structures like Dictionary  
  _e.g._ Majority Element
- Manipulate values  
  _e.g._ Rotate Array
- Find min/max or accumulate values  
  _e.g._ Best Time to Buy and Sell Stock I/II
- Use Recursion / DP / Greedy  
  _e.g._ Jump Game I/II
- Precomputation to optimize  
  _e.g._ Product of Array Except Self
- Build or process strings  
  _e.g._ Roman to Integer, Longest Common Prefix

---

# 👫 Two Pointers

### 💡 Key Points

- Decide initialization point: start vs. end
- Leverage properties (e.g. sorted array)
- Understand when and how pointers move or terminate

### 🧩 Question Types

- **Two pointers at both ends**

  - Sorted input → shrink towards each other  
    _e.g._ Two Sum, 3 Sum
  - Check for matching ends  
    _e.g._ Valid Palindrome
  - Greedily contract to maximize/minimize  
    _e.g._ Container With Most Water

- **Two pointers from start**
  - Advance based on condition  
    _e.g._ Is Subsequence

---

# 🔍 Sliding Window

### 💡 Key Points

- Track and update current window state
- Validate if the window meets conditions
- Know when to contract the left pointer

### 🧩 General Pattern

1. Use `left` and `right` to define window
2. Update window state after expanding `right`
3. While valid:
   - Update global min/max
   - Contract `left` until invalid
4. Repeat until `right < n`

---

# 🧮 Matrix

### 💡 Key Points

- Use `(i, j)` for 2D processing
- Get valid neighbors without going out-of-bounds

### 🧩 Question Types

- Track row/col/box state  
  _e.g._ Valid Sudoku, Set Matrix Zeroes
- Spiral or rotate using boundary pointers  
  _e.g._ Spiral Matrix, Rotate Image
- Modify in-place using copy  
  _e.g._ Game of Life

---

# 🗃️ Hash Map

### 💡 Key Points

- Create key-value mappings to solve problems

### 🧩 Question Types

- Char count comparison  
  _e.g._ Ransom Note, Group Anagrams
- Strict one-to-one mapping  
  _e.g._ Isomorphic Strings, Word Pattern
- Map value to index  
  _e.g._ Two Sum
- Visited set for uniqueness  
  _e.g._ Happy Number

---

# 🕒 Intervals

### 💡 Key Points

- Identify overlaps
- Rebuild intervals as needed

### 🧩 General Pattern

1. Sort by start time
2. Compare current and next for overlap
3. Merge or isolate based on need:
   - Merge → `min(start), max(end)`
   - Overlap → `max(start), min(end)`
4. Repeat until no more overlaps

---

# 🧱 Stack

### 💡 Key Points

- Know push/pop conditions
- Check for empty before popping

### 🧩 Question Types

- Bracket validation  
  _e.g._ Valid Parentheses
- Directory path simplification  
  _e.g._ Simplify Path
- Reverse Polish notation  
  _e.g._ Evaluate Reverse Polish Notation
- Min/Max Stack tracking  
  _e.g._ Min Stack

---

# 🔗 Linked List

### 💡 Key Points

- Use Sentinel Node for edge cases
- Preserve head with separate pointer
- Careful pointer termination

### 🧩 Question Types

- Detect cycle  
  _e.g._ Linked List Cycle
- Merge/Add two lists  
  _e.g._ Merge Two Sorted Lists
- Deep copy with DFS  
  _e.g._ Copy List with Random Pointer
- Reverse list  
  _e.g._ Reverse Linked List II
- Nth node from end  
  _e.g._ Remove Nth Node From End of List
- Rotate / remove duplicates / LRU cache

---

# 🌳 Binary Tree

### 💡 Key Points

- Use recursion for structure traversal
- Understand all three DFS orders
- Know BFS and backtracking strategies

### 🧩 Question Types

- Recursive traversal  
  _e.g._ Invert Binary Tree, Path Sum
- Preorder / Inorder / Postorder  
  _e.g._ Tree Construction, Sum Root to Leaf
- BFS on tree  
  _e.g._ Right Side View, Level Order
- Tree backtracking  
  _e.g._ Sum Root to Leaf Numbers

---

# 🌲 Binary Search Tree (BST)

### 💡 Key Points

- Understand BST properties (ordered, balanced)
- Inorder = sorted values

### 🧩 Question Types

- DFS  
  _e.g._ Minimum Absolute Difference in BST
- Inorder traversal  
  _e.g._ Kth Smallest Element
- Range validation  
  _e.g._ Validate BST

---

# 🌐 Graph

### 💡 Key Points

- Frame problems as graphs
- Use visited set for cycles
- Understand BFS / DFS / Topo sort

### 🧩 Question Types

- BFS/DFS on grid  
  _e.g._ Number of Islands
- Use dictionary as adjacency list  
  _e.g._ Clone Graph
- Build graph then traverse  
  _e.g._ Evaluate Division
- Topological Sort  
  _e.g._ Course Schedule I/II

---

# 🔤 Trie

### 💡 Key Points

- Build and search using nodes
- Traverse recursively

### 🧩 Question Types

- Construct/search trie  
  _e.g._ Implement Prefix Tree

---

# 🧩 Backtracking

### 💡 Key Points

- Use Sets/Lists to build paths
- Determine valid candidates
- Understand base case vs. recursion

### 🧩 General Pattern

1. Define state (index, path, visited)
2. Base case: when solution/path is ready
3. Try candidates:
   - Add to path
   - Recurse
   - Remove from path (backtrack)

---

# 🧮 Binary Search

### 💡 Key Points

- Classic `left`, `right`, `mid` pattern
- Use sorted/half-sorted array properties

### 🧩 General Pattern

1. Use iterative binary search
2. In variants, check sorted half

---

# 🔺 Heap

### 💡 Key Points

- Know Min/Max Heap properties
- Common ops: `heappush`, `heappop`

### 🧩 Question Types

- K-th largest  
  _e.g._ Kth Largest Element in Array

---

# 📐 Dynamic Programming (DP)

### 💡 Key Points

- Cache states: (i, j, k, ...)
- Build up from subproblems

### 🧩 General Pattern

- **Memoization**:

  - Recursive + cache + base case

- **Bottom-up**:
  - Init DP table
  - Fill based on previous cells
