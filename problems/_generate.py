"""
Run this to (re)generate the problem JSON files in this directory.
Add a new dict to PROBLEMS and re-run to add your own problems later.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

PROBLEMS = [
    {
        "id": "pair_sum_indices",
        "title": "Pair Sum Indices",
        "difficulty": "Easy",
        "topic": "Arrays / Hashing",
        "tags": ["array", "hash-map"],
        "description_md": """Given an array of integers `nums` and an integer `target`, return the indices of the
two numbers that add up to `target`.

Assume exactly one valid pair exists, and you may not use the same element twice.
Return the indices in the order you find them scanning left to right (lower index first).

**Follow-up they'll ask:** can you do it in one pass instead of two?""",
        "function_name": "pairSumIndices",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "target", "type": "int"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def pairSumIndices(nums, target):\n    # your code here\n    pass\n",
            "cpp": "vector<int> pairSumIndices(vector<int> nums, int target) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[2, 7, 11, 15], 9], "expected": [0, 1], "input_display": "nums=[2,7,11,15], target=9"},
            {"inputs": [[3, 2, 4], 6], "expected": [1, 2], "input_display": "nums=[3,2,4], target=6"},
            {"inputs": [[3, 3], 6], "expected": [0, 1], "input_display": "nums=[3,3], target=6"},
            {"inputs": [[-1, -2, -3, -4, -5], -8], "expected": [2, 4], "hidden": True},
            {"inputs": [[0, 4, 3, 0], 0], "expected": [0, 3], "hidden": True},
        ],
    },
    {
        "id": "best_trade_window",
        "title": "Best Trade Window",
        "difficulty": "Easy",
        "topic": "Arrays / Greedy",
        "tags": ["array", "greedy", "one-pass"],
        "description_md": """You're given an array `prices` where `prices[i]` is the price of a stock on day `i`.

You may buy on one day and sell on a later day (at most one transaction).
Return the maximum profit you can achieve. If no profit is possible, return 0.

**Follow-up they'll ask:** what if you could hold multiple positions, or trade with a cooldown day?""",
        "function_name": "maxProfit",
        "params": [{"name": "prices", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def maxProfit(prices):\n    # your code here\n    pass\n",
            "cpp": "int maxProfit(vector<int> prices) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[7, 1, 5, 3, 6, 4]], "expected": 5, "input_display": "prices=[7,1,5,3,6,4]"},
            {"inputs": [[7, 6, 4, 3, 1]], "expected": 0, "input_display": "prices=[7,6,4,3,1]"},
            {"inputs": [[1, 2]], "expected": 1, "hidden": True},
            {"inputs": [[2, 4, 1, 7]], "expected": 6, "hidden": True},
            {"inputs": [[5]], "expected": 0, "hidden": True},
        ],
    },
    {
        "id": "max_subarray_sum",
        "title": "Maximum Contiguous Sum",
        "difficulty": "Medium",
        "topic": "Arrays / DP",
        "tags": ["array", "dynamic-programming", "kadane"],
        "description_md": """Given an integer array `nums`, find the contiguous subarray (containing at least
one number) with the largest sum, and return that sum.

**Follow-up they'll ask:** can you also return the actual subarray boundaries, not just the sum? What about
the divide-and-conquer O(n log n) approach vs the O(n) one?""",
        "function_name": "maxSubArray",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def maxSubArray(nums):\n    # your code here\n    pass\n",
            "cpp": "int maxSubArray(vector<int> nums) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], "expected": 6, "input_display": "nums=[-2,1,-3,4,-1,2,1,-5,4]"},
            {"inputs": [[1]], "expected": 1, "input_display": "nums=[1]"},
            {"inputs": [[5, 4, -1, 7, 8]], "expected": 23, "hidden": True},
            {"inputs": [[-1, -2, -3]], "expected": -1, "hidden": True},
        ],
    },
    {
        "id": "grid_min_steps",
        "title": "Warehouse Grid Traversal",
        "difficulty": "Medium",
        "topic": "Graphs / BFS",
        "tags": ["bfs", "grid", "graph"],
        "description_md": """A rectangular warehouse floor is represented as a grid where `0` is open floor and
`1` is a blocked shelf. A robot starts at the northwest corner `(0,0)` and needs to reach the southeast
corner `(rows-1, cols-1)`, moving one cell at a time in the four cardinal directions.

Return the minimum number of steps required, or `-1` if the southeast corner is unreachable.

This is a direct analog of a real Anduril phone-screen question (minimum steps NW corner -> SE corner of a
building). **Follow-up they'll ask:** what if diagonal moves were allowed, or cells had different traversal costs?""",
        "function_name": "minSteps",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def minSteps(grid):\n    # BFS from (0,0) to (rows-1, cols-1)\n    pass\n",
            "cpp": "int minSteps(vector<vector<int>> grid) {\n    // BFS from (0,0) to (rows-1, cols-1)\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], "expected": 4, "input_display": "3x3 grid, one blocked cell in middle"},
            {"inputs": [[[0, 1], [1, 0]]], "expected": -1, "input_display": "2x2 grid, no path"},
            {"inputs": [[[0]]], "expected": 0, "hidden": True},
            {"inputs": [[[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]], "expected": 13, "hidden": True},
        ],
    },
    {
        "id": "network_delay_dijkstra",
        "title": "Sensor Network Shortest Delay",
        "difficulty": "Medium",
        "topic": "Graphs / Dijkstra",
        "tags": ["dijkstra", "graph", "priority-queue"],
        "description_md": """You have `n` nodes (labeled `0` to `n-1`) representing sensors in a network, and a
list of directed edges `edges`, where each edge is `[u, v, w]` meaning it takes `w` time units to send a
signal from node `u` to node `v`.

Given a source node `src`, return an array `dist` where `dist[i]` is the shortest time to reach node `i`
from `src`. If a node is unreachable, its value should be `-1`.

This is essentially the Dijkstra's-algorithm question Anduril is known to ask directly.
**Follow-up they'll ask:** how does your solution change with negative edge weights? What's the complexity
with a binary heap vs a Fibonacci heap?""",
        "function_name": "shortestDelays",
        "params": [
            {"name": "n", "type": "int"},
            {"name": "edges", "type": "vector<vector<int>>"},
            {"name": "src", "type": "int"},
        ],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def shortestDelays(n, edges, src):\n    # Dijkstra from src over n nodes; -1 for unreachable\n    pass\n",
            "cpp": "vector<int> shortestDelays(int n, vector<vector<int>> edges, int src) {\n    // Dijkstra from src over n nodes; -1 for unreachable\n    return vector<int>(n, -1);\n}\n",
        },
        "test_cases": [
            {"inputs": [4, [[0, 1, 1], [1, 2, 2], [0, 2, 4], [2, 3, 1]], 0], "expected": [0, 1, 3, 4],
             "input_display": "n=4, edges=[[0,1,1],[1,2,2],[0,2,4],[2,3,1]], src=0"},
            {"inputs": [3, [[0, 1, 5]], 0], "expected": [0, 5, -1], "input_display": "n=3, edges=[[0,1,5]], src=0"},
            {"inputs": [1, [], 0], "expected": [0], "hidden": True},
            {"inputs": [5, [[0, 1, 2], [0, 2, 5], [1, 2, 1], [1, 3, 7], [2, 4, 1], [3, 4, 1]], 0], "expected": [0, 2, 3, 9, 4], "hidden": True},
        ],
    },
    {
        "id": "valid_bracket_sequence",
        "title": "Valid Bracket Sequence",
        "difficulty": "Easy",
        "topic": "Strings / Stack",
        "tags": ["string", "stack"],
        "description_md": """Given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[`, `]`,
determine if the input string has correctly matched and nested brackets.

Return `true` if valid, `false` otherwise.""",
        "function_name": "isValidBrackets",
        "params": [{"name": "s", "type": "string"}],
        "return_type": "bool",
        "starter_code": {
            "python": "def isValidBrackets(s):\n    # your code here\n    pass\n",
            "cpp": "bool isValidBrackets(string s) {\n    // your code here\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": ["()[]{}"], "expected": True, "input_display": 's="()[]{}"'},
            {"inputs": ["(]"], "expected": False, "input_display": 's="(]"'},
            {"inputs": ["([{}])"], "expected": True, "hidden": True},
            {"inputs": ["("], "expected": False, "hidden": True},
            {"inputs": [""], "expected": True, "hidden": True},
        ],
    },
    {
        "id": "min_coins_for_amount",
        "title": "Minimum Coins for Amount",
        "difficulty": "Medium",
        "topic": "Dynamic Programming",
        "tags": ["dp", "unbounded-knapsack"],
        "description_md": """You're given an array `coins` representing available coin denominations (unlimited
supply of each) and an integer `amount`. Return the fewest number of coins needed to make up `amount`.

If it's not possible, return `-1`.

**Follow-up they'll ask:** how would you also return which coins were used, not just the count?""",
        "function_name": "minCoins",
        "params": [{"name": "coins", "type": "vector<int>"}, {"name": "amount", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def minCoins(coins, amount):\n    # your code here\n    pass\n",
            "cpp": "int minCoins(vector<int> coins, int amount) {\n    // your code here\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 5], 11], "expected": 3, "input_display": "coins=[1,2,5], amount=11"},
            {"inputs": [[2], 3], "expected": -1, "input_display": "coins=[2], amount=3"},
            {"inputs": [[1], 0], "expected": 0, "hidden": True},
            {"inputs": [[1, 3, 4], 6], "expected": 2, "hidden": True},
        ],
    },
    {
        "id": "tree_max_depth",
        "title": "Binary Tree Max Depth",
        "difficulty": "Easy",
        "topic": "Trees / DFS",
        "tags": ["tree", "dfs", "recursion"],
        "description_md": """Given the root of a binary tree, return its maximum depth (the number of nodes
along the longest path from the root down to the farthest leaf).

The tree is provided as a level-order array where `null` marks a missing child (same convention LeetCode
uses). It will be built into a `TreeNode` tree for you automatically -- your function receives the root.""",
        "function_name": "maxDepth",
        "params": [{"name": "root", "type": "tree"}],
        "return_type": "int",
        "starter_code": {
            "python": "# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\ndef maxDepth(root):\n    # root is a TreeNode or None\n    pass\n",
            "cpp": "// struct TreeNode {\n//     int val;\n//     TreeNode *left;\n//     TreeNode *right;\n//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n// };\n\nint maxDepth(TreeNode* root) {\n    // root is a TreeNode* or nullptr\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[3, 9, 20, None, None, 15, 7]], "expected": 3, "input_display": "tree=[3,9,20,null,null,15,7]"},
            {"inputs": [[1, None, 2]], "expected": 2, "input_display": "tree=[1,null,2]"},
            {"inputs": [[]], "expected": 0, "hidden": True},
            {"inputs": [[1, 2, 3, 4, None, None, None, 5]], "expected": 4, "hidden": True},
        ],
    },
    {
        "id": "rotate_array_k",
        "title": "Rotate Array In Place",
        "difficulty": "Medium",
        "topic": "Arrays",
        "tags": ["array", "in-place"],
        "description_md": """Given an array `nums`, rotate it to the right by `k` steps, and return the rotated
array.

**Follow-up they'll ask:** can you do this in O(1) extra space? (Hint: reverse the whole array, then reverse
each segment.)""",
        "function_name": "rotateArray",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "k", "type": "int"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def rotateArray(nums, k):\n    # your code here\n    pass\n",
            "cpp": "vector<int> rotateArray(vector<int> nums, int k) {\n    // your code here\n    return nums;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3, 4, 5, 6, 7], 3], "expected": [5, 6, 7, 1, 2, 3, 4], "input_display": "nums=[1..7], k=3"},
            {"inputs": [[-1, -100, 3, 99], 2], "expected": [3, 99, -1, -100], "input_display": "nums=[-1,-100,3,99], k=2"},
            {"inputs": [[1, 2], 3], "expected": [2, 1], "hidden": True},
        ],
    },
    {
        "id": "merge_overlapping_intervals",
        "title": "Merge Overlapping Intervals",
        "difficulty": "Medium",
        "topic": "Arrays / Sorting",
        "tags": ["array", "sorting", "intervals"],
        "description_md": """Given an array of intervals `intervals` where `intervals[i] = [start, end]`, merge
all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals
in the input, sorted by start.""",
        "function_name": "mergeIntervals",
        "params": [{"name": "intervals", "type": "vector<vector<int>>"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "def mergeIntervals(intervals):\n    # your code here\n    pass\n",
            "cpp": "vector<vector<int>> mergeIntervals(vector<vector<int>> intervals) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 3], [2, 6], [8, 10], [15, 18]]], "expected": [[1, 6], [8, 10], [15, 18]],
             "input_display": "intervals=[[1,3],[2,6],[8,10],[15,18]]"},
            {"inputs": [[[1, 4], [4, 5]]], "expected": [[1, 5]], "input_display": "intervals=[[1,4],[4,5]]"},
            {"inputs": [[[1, 4], [0, 4]]], "expected": [[0, 4]], "hidden": True},
        ],
    },
    {
        "id": "count_islands",
        "title": "Count Connected Regions",
        "difficulty": "Medium",
        "topic": "Graphs / DFS-BFS",
        "tags": ["graph", "dfs", "grid", "union-find"],
        "description_md": """Given a 2D grid of `1`s (land) and `0`s (water), return the number of islands.
An island is a group of `1`s connected 4-directionally, and the grid is bounded on all four edges by water.

**Follow-up they'll ask:** how would this scale if the grid were streamed in tiles too large to fit in
memory at once? (Union-Find with tile boundary stitching is the answer they're fishing for.)""",
        "function_name": "countIslands",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def countIslands(grid):\n    # your code here\n    pass\n",
            "cpp": "int countIslands(vector<vector<int>> grid) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]], "expected": 3,
             "input_display": "4x4 grid with three islands"},
            {"inputs": [[[0, 0], [0, 0]]], "expected": 0, "input_display": "all water"},
            {"inputs": [[[1, 1, 1], [1, 1, 1]]], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "longest_substring_k_distinct",
        "title": "Longest Substring With K Distinct Chars",
        "difficulty": "Medium",
        "topic": "Strings / Sliding Window",
        "tags": ["string", "sliding-window", "two-pointer"],
        "description_md": """Given a string `s` and an integer `k`, return the length of the longest substring
that contains at most `k` distinct characters.

**Follow-up they'll ask:** how would you extend this to a streaming input where you can't re-scan from the
start?""",
        "function_name": "longestKDistinct",
        "params": [{"name": "s", "type": "string"}, {"name": "k", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def longestKDistinct(s, k):\n    # sliding window\n    pass\n",
            "cpp": "int longestKDistinct(string s, int k) {\n    // sliding window\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": ["eceba", 2], "expected": 3, "input_display": 's="eceba", k=2'},
            {"inputs": ["aa", 1], "expected": 2, "input_display": 's="aa", k=1'},
            {"inputs": ["a", 0], "expected": 0, "hidden": True},
            {"inputs": ["abcadcacacaca", 3], "expected": 11, "hidden": True},
        ],
    },

    # ---- added from the Anduril 40-question list ----

    {
        "id": "shortest_word_distance",
        "title": "Shortest Word Distance",
        "difficulty": "Easy",
        "topic": "Arrays / Strings",
        "tags": ["array", "string"],
        "description_md": """Given an array of strings `wordsDict` and two different strings `word1` and
`word2` that are both guaranteed to appear in the array, return the shortest distance between their two
closest occurrences.""",
        "function_name": "shortestWordDistance",
        "params": [{"name": "wordsDict", "type": "vector<string>"}, {"name": "word1", "type": "string"}, {"name": "word2", "type": "string"}],
        "return_type": "int",
        "starter_code": {
            "python": "def shortestWordDistance(wordsDict, word1, word2):\n    # your code here\n    pass\n",
            "cpp": "int shortestWordDistance(vector<string> wordsDict, string word1, string word2) {\n    // your code here\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"], "expected": 3,
             "input_display": 'wordsDict=[...], word1="coding", word2="practice"'},
            {"inputs": [["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"], "expected": 1,
             "input_display": 'wordsDict=[...], word1="makes", word2="coding"'},
            {"inputs": [["a", "c", "b", "a"], "a", "b"], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "move_zeroes",
        "title": "Move Zeroes",
        "difficulty": "Easy",
        "topic": "Arrays / Two Pointers",
        "tags": ["array", "two-pointers"],
        "description_md": """Given an integer array `nums`, move all `0`s to the end of it while maintaining
the relative order of the non-zero elements. Return the resulting array.""",
        "function_name": "moveZeroes",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def moveZeroes(nums):\n    # your code here\n    pass\n",
            "cpp": "vector<int> moveZeroes(vector<int> nums) {\n    // your code here\n    return nums;\n}\n",
        },
        "test_cases": [
            {"inputs": [[0, 1, 0, 3, 12]], "expected": [1, 3, 12, 0, 0], "input_display": "nums=[0,1,0,3,12]"},
            {"inputs": [[0]], "expected": [0], "input_display": "nums=[0]"},
            {"inputs": [[1, 2, 3]], "expected": [1, 2, 3], "hidden": True},
            {"inputs": [[0, 0, 0, 1]], "expected": [1, 0, 0, 0], "hidden": True},
        ],
    },
    {
        "id": "course_schedule_ii",
        "title": "Course Schedule II",
        "difficulty": "Medium",
        "topic": "Graphs / Topological Sort",
        "tags": ["graph", "topological-sort", "bfs"],
        "description_md": """You have `numCourses` courses labeled `0` to `numCourses-1`. `prerequisites[i] =
[a, b]` means you must take course `b` before course `a`. Return a valid order to take all courses, or an
empty array if it's impossible (a cycle exists).

To keep the judge deterministic, return the **lexicographically smallest** valid order (always pick the
lowest-numbered course with no remaining prerequisites at each step -- a min-heap instead of a plain queue).""",
        "function_name": "courseOrder",
        "params": [{"name": "numCourses", "type": "int"}, {"name": "prerequisites", "type": "vector<vector<int>>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "import heapq\ndef courseOrder(numCourses, prerequisites):\n    # your code here -- use a min-heap for the lexicographically smallest order\n    pass\n",
            "cpp": "vector<int> courseOrder(int numCourses, vector<vector<int>> prerequisites) {\n    // your code here -- use a min-heap (priority_queue<int, vector<int>, greater<int>>)\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], "expected": [0, 1, 2, 3], "input_display": "numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]"},
            {"inputs": [2, [[1, 0]]], "expected": [0, 1], "input_display": "numCourses=2, prerequisites=[[1,0]]"},
            {"inputs": [2, [[1, 0], [0, 1]]], "expected": [], "hidden": True},
            {"inputs": [1, []], "expected": [0], "hidden": True},
        ],
    },
    {
        "id": "heaters",
        "title": "Heaters",
        "difficulty": "Medium",
        "topic": "Arrays / Binary Search",
        "tags": ["array", "binary-search", "two-pointers"],
        "description_md": """Given the positions of houses `houses` and heaters `heaters` on a number line,
every heater has the same warm radius. Return the minimum radius so that every house is covered by at least
one heater.""",
        "function_name": "findRadius",
        "params": [{"name": "houses", "type": "vector<int>"}, {"name": "heaters", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def findRadius(houses, heaters):\n    # your code here\n    pass\n",
            "cpp": "int findRadius(vector<int> houses, vector<int> heaters) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3], [2]], "expected": 1, "input_display": "houses=[1,2,3], heaters=[2]"},
            {"inputs": [[1, 2, 3, 4], [1, 4]], "expected": 1, "input_display": "houses=[1,2,3,4], heaters=[1,4]"},
            {"inputs": [[1, 5], [2]], "expected": 3, "hidden": True},
        ],
    },
    {
        "id": "daily_temperatures",
        "title": "Daily Temperatures",
        "difficulty": "Medium",
        "topic": "Arrays / Monotonic Stack",
        "tags": ["array", "stack", "monotonic-stack"],
        "description_md": """Given an array `temperatures`, return an array `answer` where `answer[i]` is the
number of days you'd have to wait after day `i` to get a warmer temperature. If there's no future day with a
warmer temperature, put `0`.""",
        "function_name": "dailyTemperatures",
        "params": [{"name": "temperatures", "type": "vector<int>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def dailyTemperatures(temperatures):\n    # your code here -- monotonic stack\n    pass\n",
            "cpp": "vector<int> dailyTemperatures(vector<int> temperatures) {\n    // your code here -- monotonic stack\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[73, 74, 75, 71, 69, 72, 76, 73]], "expected": [1, 1, 4, 2, 1, 1, 0, 0], "input_display": "temperatures=[73,74,75,71,69,72,76,73]"},
            {"inputs": [[30, 40, 50, 60]], "expected": [1, 1, 1, 0], "input_display": "temperatures=[30,40,50,60]"},
            {"inputs": [[30, 60, 90]], "expected": [1, 1, 0], "hidden": True},
        ],
    },
    {
        "id": "string_compression",
        "title": "String Compression",
        "difficulty": "Medium",
        "topic": "Strings / Two Pointers",
        "tags": ["string", "two-pointers"],
        "description_md": """Given a string `s` of lowercase letters, compress consecutive runs of the same
character into the character followed by the run length -- but omit the count when a run has length 1 (e.g.
`"aabcccccaaa"` becomes `"a2bc5a3"`, not `"a2b1c5a3"`). Return the compressed string.""",
        "function_name": "compress",
        "params": [{"name": "s", "type": "string"}],
        "return_type": "string",
        "starter_code": {
            "python": "def compress(s):\n    # your code here\n    pass\n",
            "cpp": "string compress(string s) {\n    // your code here\n    return \"\";\n}\n",
        },
        "test_cases": [
            {"inputs": ["aabcccccaaa"], "expected": "a2bc5a3", "input_display": 's="aabcccccaaa"'},
            {"inputs": ["abbbbbbbbbbbb"], "expected": "ab12", "input_display": 's="abbbbbbbbbbbb"'},
            {"inputs": ["abcdef"], "expected": "abcdef", "hidden": True},
            {"inputs": [""], "expected": "", "hidden": True},
        ],
    },
    {
        "id": "points_inside_circle_queries",
        "title": "Points Inside Circle Queries",
        "difficulty": "Medium",
        "topic": "Arrays / Geometry",
        "tags": ["array", "geometry"],
        "description_md": """Given integer coordinate `points` and a list of `queries` where each query is
`[x, y, r]` describing a circle, return an array where each entry is the count of points lying inside or on
the boundary of that circle.""",
        "function_name": "countPoints",
        "params": [{"name": "points", "type": "vector<vector<int>>"}, {"name": "queries", "type": "vector<vector<int>>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def countPoints(points, queries):\n    # your code here\n    pass\n",
            "cpp": "vector<int> countPoints(vector<vector<int>> points, vector<vector<int>> queries) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]], "expected": [3, 2, 2],
             "input_display": "points=[[1,3],[3,3],[5,3],[2,2]], queries=[[2,3,1],[4,3,1],[1,1,2]]"},
            {"inputs": [[[1, 1], [3, 4]], [[1, 1, 0]]], "expected": [1], "hidden": True},
        ],
    },
    {
        "id": "binary_tree_vertical_order",
        "title": "Binary Tree Vertical Order Traversal",
        "difficulty": "Medium",
        "topic": "Trees / BFS",
        "tags": ["tree", "bfs", "hash-map"],
        "description_md": """Given the root of a binary tree, return the vertical order traversal: group node
values by column (root is column 0, left child is column-1, right child is column+1), ordered top-to-bottom
within each column, columns ordered left to right.""",
        "function_name": "verticalOrder",
        "params": [{"name": "root", "type": "tree"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "from collections import deque, defaultdict\n\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\ndef verticalOrder(root):\n    # your code here -- BFS tracking column index\n    pass\n",
            "cpp": "// struct TreeNode {\n//     int val;\n//     TreeNode *left;\n//     TreeNode *right;\n//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n// };\n\nvector<vector<int>> verticalOrder(TreeNode* root) {\n    // your code here -- BFS tracking column index (map<int,vector<int>> auto-sorts by key)\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[3, 9, 20, None, None, 15, 7]], "expected": [[9], [3, 15], [20], [7]], "input_display": "tree=[3,9,20,null,null,15,7]"},
            {"inputs": [[1, 2, 3, 4, 5, 6, 7]], "expected": [[4], [2], [1, 5, 6], [3], [7]], "hidden": True},
        ],
    },
    {
        "id": "push_dominoes",
        "title": "Push Dominoes",
        "difficulty": "Medium",
        "topic": "Strings / Simulation",
        "tags": ["string", "two-pointers", "simulation"],
        "description_md": """A row of dominoes is given as a string of `L`, `R`, and `.` (standing). `R` means
that domino was pushed right, `L` means pushed left, and a pushed domino pushes the next standing domino in
the same direction. If a domino is pushed from both sides at once, it stays standing. Return the final
state.""",
        "function_name": "pushDominoes",
        "params": [{"name": "dominoes", "type": "string"}],
        "return_type": "string",
        "starter_code": {
            "python": "def pushDominoes(dominoes):\n    # your code here\n    pass\n",
            "cpp": "string pushDominoes(string dominoes) {\n    // your code here\n    return dominoes;\n}\n",
        },
        "test_cases": [
            {"inputs": [".L.R...LR..L.."], "expected": "LL.RR.LLRRLL..", "input_display": 'dominoes=".L.R...LR..L.."'},
            {"inputs": ["RR.L"], "expected": "RR.L", "input_display": 'dominoes="RR.L"'},
            {"inputs": ["..."], "expected": "...", "hidden": True},
        ],
    },
    {
        "id": "group_anagrams",
        "title": "Group Anagrams",
        "difficulty": "Medium",
        "topic": "Arrays / Hashing",
        "tags": ["array", "hash-map", "string"],
        "description_md": """Given an array of strings `strs`, group the anagrams together. Return the groups
in any order (grading here ignores group order and order within each group).""",
        "function_name": "groupAnagrams",
        "params": [{"name": "strs", "type": "vector<string>"}],
        "return_type": "vector<vector<string>>",
        "unordered": True,
        "starter_code": {
            "python": "def groupAnagrams(strs):\n    # your code here\n    pass\n",
            "cpp": "vector<vector<string>> groupAnagrams(vector<string> strs) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [["eat", "tea", "tan", "ate", "nat", "bat"]], "expected": [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
             "input_display": 'strs=["eat","tea","tan","ate","nat","bat"]'},
            {"inputs": [[""]], "expected": [[""]], "hidden": True},
            {"inputs": [["a"]], "expected": [["a"]], "hidden": True},
        ],
    },
    {
        "id": "flip_equivalent_binary_trees",
        "title": "Flip Equivalent Binary Trees",
        "difficulty": "Medium",
        "topic": "Trees / DFS",
        "tags": ["tree", "dfs", "recursion"],
        "description_md": """Two binary trees are *flip equivalent* if one can be turned into the other by
flipping any number of nodes' left and right children. Given the roots of two trees, return whether they're
flip equivalent.""",
        "function_name": "flipEquiv",
        "params": [{"name": "root1", "type": "tree"}, {"name": "root2", "type": "tree"}],
        "return_type": "bool",
        "starter_code": {
            "python": "# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\ndef flipEquiv(root1, root2):\n    # your code here\n    pass\n",
            "cpp": "// struct TreeNode {\n//     int val;\n//     TreeNode *left;\n//     TreeNode *right;\n//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n// };\n\nbool flipEquiv(TreeNode* root1, TreeNode* root2) {\n    // your code here\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3], [1, 3, 2]], "expected": True, "input_display": "tree1=[1,2,3], tree2=[1,3,2]"},
            {"inputs": [[1, 2, 3], [1, 2, 4]], "expected": False, "input_display": "tree1=[1,2,3], tree2=[1,2,4]"},
            {"inputs": [[], []], "expected": True, "hidden": True},
            {"inputs": [[1], [1]], "expected": True, "hidden": True},
        ],
    },
    {
        "id": "flatten_binary_tree_preorder",
        "title": "Flatten Binary Tree (Preorder)",
        "difficulty": "Medium",
        "topic": "Trees / DFS",
        "tags": ["tree", "dfs", "recursion"],
        "description_md": """Given the root of a binary tree, flatten it to match the preorder traversal --
return the preorder sequence of values (the actual LeetCode version turns this into an in-place linked list;
here just return the value order, which is the core of the algorithm either way).""",
        "function_name": "flattenPreorder",
        "params": [{"name": "root", "type": "tree"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\ndef flattenPreorder(root):\n    # your code here\n    pass\n",
            "cpp": "// struct TreeNode {\n//     int val;\n//     TreeNode *left;\n//     TreeNode *right;\n//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n// };\n\nvector<int> flattenPreorder(TreeNode* root) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 5, 3, 4, None, 6]], "expected": [1, 2, 3, 4, 5, 6], "input_display": "tree=[1,2,5,3,4,null,6]"},
            {"inputs": [[]], "expected": [], "hidden": True},
        ],
    },
    {
        "id": "search_suggestions_system",
        "title": "Search Suggestions System",
        "difficulty": "Medium",
        "topic": "Strings / Binary Search",
        "tags": ["array", "string", "binary-search", "trie"],
        "description_md": """Given `products` and a `searchWord`, for every prefix of `searchWord` (typed one
character at a time) return up to 3 lexicographically-smallest products that start with that prefix.""",
        "function_name": "suggestedProducts",
        "params": [{"name": "products", "type": "vector<string>"}, {"name": "searchWord", "type": "string"}],
        "return_type": "vector<vector<string>>",
        "starter_code": {
            "python": "def suggestedProducts(products, searchWord):\n    # your code here\n    pass\n",
            "cpp": "vector<vector<string>> suggestedProducts(vector<string> products, string searchWord) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"],
             "expected": [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]],
             "input_display": 'products=[...], searchWord="mouse"'},
            {"inputs": [["havana"], "havana"], "expected": [["havana"]] * 6, "hidden": True},
        ],
    },
    {
        "id": "game_of_life",
        "title": "Game of Life",
        "difficulty": "Medium",
        "topic": "Arrays / Simulation",
        "tags": ["array", "matrix", "simulation"],
        "description_md": """Given an `m x n` board where `1` is a live cell and `0` is dead, compute the next
state per Conway's rules (a live cell with 2-3 live neighbors survives; a dead cell with exactly 3 live
neighbors becomes alive; all other cells die or stay dead). Return the new board.""",
        "function_name": "gameOfLife",
        "params": [{"name": "board", "type": "vector<vector<int>>"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "def gameOfLife(board):\n    # your code here\n    pass\n",
            "cpp": "vector<vector<int>> gameOfLife(vector<vector<int>> board) {\n    // your code here\n    return board;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]], "expected": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
             "input_display": "board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]"},
            {"inputs": [[[1, 1], [1, 0]]], "expected": [[1, 1], [1, 1]], "hidden": True},
        ],
    },
    {
        "id": "course_schedule",
        "title": "Course Schedule",
        "difficulty": "Medium",
        "topic": "Graphs / Cycle Detection",
        "tags": ["graph", "topological-sort", "bfs"],
        "description_md": """You have `numCourses` courses and a list of prerequisite pairs `[a, b]` meaning
`b` must be completed before `a`. Return whether it's possible to finish all courses (i.e. the prerequisite
graph has no cycle).""",
        "function_name": "canFinish",
        "params": [{"name": "numCourses", "type": "int"}, {"name": "prerequisites", "type": "vector<vector<int>>"}],
        "return_type": "bool",
        "starter_code": {
            "python": "def canFinish(numCourses, prerequisites):\n    # your code here\n    pass\n",
            "cpp": "bool canFinish(int numCourses, vector<vector<int>> prerequisites) {\n    // your code here\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": [2, [[1, 0]]], "expected": True, "input_display": "numCourses=2, prerequisites=[[1,0]]"},
            {"inputs": [2, [[1, 0], [0, 1]]], "expected": False, "input_display": "numCourses=2, prerequisites=[[1,0],[0,1]]"},
            {"inputs": [5, [[1, 0], [2, 1], [3, 2], [4, 3]]], "expected": True, "hidden": True},
        ],
    },
    {
        "id": "shortest_word_distance_ii",
        "title": "Shortest Word Distance II",
        "difficulty": "Medium",
        "topic": "Arrays / Design",
        "tags": ["array", "hash-map", "two-pointers", "design"],
        "description_md": """This is the "design" variant of Shortest Word Distance: you'll be asked many
`(word1, word2)` queries against the same `wordsDict`, so precompute once and answer each query efficiently.

Given `wordsDict` and a list of `queries` (each `[word1, word2]`), return an array of shortest distances, one
per query, using the precompute-then-two-pointer approach rather than rescanning the whole array each time.""",
        "function_name": "wordDistanceQueries",
        "params": [{"name": "wordsDict", "type": "vector<string>"}, {"name": "queries", "type": "vector<vector<string>>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def wordDistanceQueries(wordsDict, queries):\n    # your code here -- precompute positions per word, then two-pointer merge per query\n    pass\n",
            "cpp": "vector<int> wordDistanceQueries(vector<string> wordsDict, vector<vector<string>> queries) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [["practice", "makes", "perfect", "coding", "makes"], [["coding", "practice"], ["makes", "coding"]]],
             "expected": [3, 1], "input_display": "wordsDict=[...], queries=[[coding,practice],[makes,coding]]"},
            {"inputs": [["a", "b", "a", "c", "b"], [["a", "b"], ["a", "c"]]], "expected": [1, 1], "hidden": True},
        ],
    },
    {
        "id": "search_rotated_sorted_array",
        "title": "Search in Rotated Sorted Array",
        "difficulty": "Medium",
        "topic": "Arrays / Binary Search",
        "tags": ["array", "binary-search"],
        "description_md": """An ascending array with distinct values was rotated at an unknown pivot. Given
the rotated array `nums` and a `target`, return its index, or `-1` if not present -- in O(log n).""",
        "function_name": "searchRotated",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "target", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def searchRotated(nums, target):\n    # your code here -- modified binary search\n    pass\n",
            "cpp": "int searchRotated(vector<int> nums, int target) {\n    // your code here -- modified binary search\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[4, 5, 6, 7, 0, 1, 2], 0], "expected": 4, "input_display": "nums=[4,5,6,7,0,1,2], target=0"},
            {"inputs": [[4, 5, 6, 7, 0, 1, 2], 3], "expected": -1, "input_display": "nums=[4,5,6,7,0,1,2], target=3"},
            {"inputs": [[1], 0], "expected": -1, "hidden": True},
        ],
    },
    {
        "id": "snakes_and_ladders",
        "title": "Snakes and Ladders",
        "difficulty": "Medium",
        "topic": "Graphs / BFS",
        "tags": ["bfs", "matrix", "graph"],
        "description_md": """An `n x n` board is numbered 1 to n² in a boustrophedon (back-and-forth) pattern
starting bottom-left. Each square is `-1` (nothing) or a number (a snake/ladder destination). From square
`i`, one move goes to any of `i+1` .. `i+6` (whichever exist), then immediately follows a snake/ladder if
present. Return the minimum number of moves to reach square n², or `-1` if impossible.""",
        "function_name": "snakesAndLadders",
        "params": [{"name": "board", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "from collections import deque\ndef snakesAndLadders(board):\n    # your code here -- BFS over square numbers 1..n*n\n    pass\n",
            "cpp": "int snakesAndLadders(vector<vector<int>> board) {\n    // your code here -- BFS over square numbers 1..n*n\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]],
             "expected": 4, "input_display": "6x6 board with a couple of ladders"},
            {"inputs": [[[-1, -1], [-1, 3]]], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "find_duplicate_number",
        "title": "Find the Duplicate Number",
        "difficulty": "Medium",
        "topic": "Arrays / Two Pointers",
        "tags": ["array", "two-pointers", "binary-search"],
        "description_md": """Given an array `nums` of `n+1` integers where each value is in `[1, n]` and
exactly one value repeats (possibly more than once), find the duplicate -- without modifying the array and
using O(1) extra space (Floyd's cycle detection, treating the array as a linked list via `i -> nums[i]`).""",
        "function_name": "findDuplicate",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def findDuplicate(nums):\n    # your code here -- Floyd's cycle detection\n    pass\n",
            "cpp": "int findDuplicate(vector<int> nums) {\n    // your code here -- Floyd's cycle detection\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 3, 4, 2, 2]], "expected": 2, "input_display": "nums=[1,3,4,2,2]"},
            {"inputs": [[3, 1, 3, 4, 2]], "expected": 3, "input_display": "nums=[3,1,3,4,2]"},
            {"inputs": [[1, 1]], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "time_based_key_value_store",
        "title": "Time Based Key-Value Store",
        "difficulty": "Medium",
        "topic": "Design / Binary Search",
        "tags": ["hash-map", "binary-search", "design"],
        "description_md": """Design a time-based key-value store, exercised here as a single batch of
`operations`. Each operation is either `["set", key, value, timestamp]` (timestamps for a given key are
non-decreasing) or `["get", key, timestamp]`. A `get` should return the value set for that key at the
largest recorded timestamp `<= timestamp`, or `""` if none exists. Return the list of outputs for the `get`
operations, in order (nothing is returned for `set`).""",
        "function_name": "timeMapOperations",
        "params": [{"name": "operations", "type": "vector<vector<string>>"}],
        "return_type": "vector<string>",
        "starter_code": {
            "python": "def timeMapOperations(operations):\n    # your code here -- store (timestamp, value) per key, binary search on get\n    pass\n",
            "cpp": "vector<string> timeMapOperations(vector<vector<string>> operations) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[["set", "foo", "bar", "1"], ["get", "foo", "1"], ["get", "foo", "3"], ["set", "foo", "bar2", "4"], ["get", "foo", "4"], ["get", "foo", "5"]]],
             "expected": ["bar", "bar", "bar2", "bar2"], "input_display": "operations=[set foo bar @1, get foo @1, get foo @3, set foo bar2 @4, get foo @4, get foo @5]"},
            {"inputs": [[["get", "missing", "1"]]], "expected": [""], "hidden": True},
        ],
    },
    {
        "id": "spiral_matrix",
        "title": "Spiral Matrix",
        "difficulty": "Medium",
        "topic": "Arrays / Simulation",
        "tags": ["array", "matrix", "simulation"],
        "description_md": """Given an `m x n` matrix, return all elements in clockwise spiral order starting
from the top-left.""",
        "function_name": "spiralOrder",
        "params": [{"name": "matrix", "type": "vector<vector<int>>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def spiralOrder(matrix):\n    # your code here\n    pass\n",
            "cpp": "vector<int> spiralOrder(vector<vector<int>> matrix) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5], "input_display": "matrix=[[1,2,3],[4,5,6],[7,8,9]]"},
            {"inputs": [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "hidden": True},
            {"inputs": [[[1]]], "expected": [1], "hidden": True},
        ],
    },
    {
        "id": "video_stitching",
        "title": "Video Stitching",
        "difficulty": "Medium",
        "topic": "Arrays / Greedy",
        "tags": ["array", "greedy", "dynamic-programming"],
        "description_md": """You need to cover the interval `[0, time]` using `clips`, where each clip is
`[start, end]`. Return the minimum number of clips needed, or `-1` if it's not possible.""",
        "function_name": "videoStitching",
        "params": [{"name": "clips", "type": "vector<vector<int>>"}, {"name": "time", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def videoStitching(clips, time):\n    # your code here -- greedy interval covering\n    pass\n",
            "cpp": "int videoStitching(vector<vector<int>> clips, int time) {\n    // your code here -- greedy interval covering\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10], "expected": 3, "input_display": "clips=[...], time=10"},
            {"inputs": [[[0, 1], [1, 2]], 5], "expected": -1, "input_display": "clips=[[0,1],[1,2]], time=5"},
            {"inputs": [[[0, 5]], 5], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "minesweeper_reveal",
        "title": "Minesweeper Reveal",
        "difficulty": "Medium",
        "topic": "Arrays / DFS-BFS",
        "tags": ["array", "dfs", "bfs", "matrix"],
        "description_md": """Given a Minesweeper `board` (`'M'` mine, `'E'` unrevealed empty) and a `click`
`[row, col]`, simulate one click: if it's a mine, reveal `'X'`; otherwise reveal it as the count of adjacent
mines (as a digit string), and if the count is 0, reveal it as `'B'` and recursively flood-fill all 8
neighbors the same way. Return the resulting board.""",
        "function_name": "updateBoard",
        "params": [{"name": "board", "type": "vector<vector<string>>"}, {"name": "click", "type": "vector<int>"}],
        "return_type": "vector<vector<string>>",
        "starter_code": {
            "python": "def updateBoard(board, click):\n    # your code here -- flood fill from click\n    pass\n",
            "cpp": "vector<vector<string>> updateBoard(vector<vector<string>> board, vector<int> click) {\n    // your code here -- flood fill from click\n    return board;\n}\n",
        },
        "test_cases": [
            {"inputs": [[["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]], [3, 0]],
             "expected": [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]],
             "input_display": "4x5 board with one mine, click=[3,0]"},
            {"inputs": [[["E", "E"], ["E", "E"]], [0, 0]], "expected": [["B", "B"], ["B", "B"]], "hidden": True},
        ],
    },
    {
        "id": "number_of_distinct_islands",
        "title": "Number of Distinct Islands",
        "difficulty": "Medium",
        "topic": "Graphs / DFS",
        "tags": ["graph", "dfs", "hash-map", "grid"],
        "description_md": """Given a binary `grid`, an island is a group of `1`s connected 4-directionally.
Two islands are considered the same if one can be translated (not rotated or reflected) to exactly match the
other. Return the number of distinct island shapes.""",
        "function_name": "numDistinctIslands",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def numDistinctIslands(grid):\n    # your code here -- DFS recording each cell's offset from the island's start cell\n    pass\n",
            "cpp": "int numDistinctIslands(vector<vector<int>> grid) {\n    // your code here -- DFS recording each cell's offset from the island's start cell\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]], "expected": 1,
             "input_display": "grid with two identically-shaped 2x2 islands"},
            {"inputs": [[[1, 0], [0, 1]]], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "rotting_oranges",
        "title": "Rotting Oranges",
        "difficulty": "Medium",
        "topic": "Graphs / BFS",
        "tags": ["bfs", "matrix", "grid"],
        "description_md": """A grid has `0` (empty), `1` (fresh orange), or `2` (rotten orange). Every minute,
any fresh orange 4-directionally adjacent to a rotten one becomes rotten. Return the minimum minutes until no
fresh orange remains, or `-1` if impossible.""",
        "function_name": "orangesRotting",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "from collections import deque\ndef orangesRotting(grid):\n    # your code here -- multi-source BFS from all initially-rotten oranges\n    pass\n",
            "cpp": "int orangesRotting(vector<vector<int>> grid) {\n    // your code here -- multi-source BFS from all initially-rotten oranges\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], "expected": 4, "input_display": "grid=[[2,1,1],[1,1,0],[0,1,1]]"},
            {"inputs": [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]], "expected": -1, "input_display": "grid=[[2,1,1],[0,1,1],[1,0,1]] (isolated fresh orange)"},
            {"inputs": [[[0, 2]]], "expected": 0, "hidden": True},
        ],
    },
    {
        "id": "meeting_rooms_ii",
        "title": "Meeting Rooms II",
        "difficulty": "Medium",
        "topic": "Arrays / Greedy",
        "tags": ["array", "sorting", "greedy", "heap"],
        "description_md": """Given meeting time `intervals` `[start, end]`, return the minimum number of
conference rooms required so no two overlapping meetings share a room.""",
        "function_name": "minMeetingRooms",
        "params": [{"name": "intervals", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def minMeetingRooms(intervals):\n    # your code here -- sort starts and ends separately, sweep\n    pass\n",
            "cpp": "int minMeetingRooms(vector<vector<int>> intervals) {\n    // your code here -- sort starts and ends separately, sweep\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 30], [5, 10], [15, 20]]], "expected": 2, "input_display": "intervals=[[0,30],[5,10],[15,20]]"},
            {"inputs": [[[7, 10], [2, 4]]], "expected": 1, "input_display": "intervals=[[7,10],[2,4]]"},
            {"inputs": [[[1, 5], [5, 10]]], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "min_rounds_complete_tasks",
        "title": "Minimum Rounds to Complete All Tasks",
        "difficulty": "Medium",
        "topic": "Arrays / Greedy",
        "tags": ["array", "hash-map", "greedy"],
        "description_md": """Each task has a difficulty level in `tasks`. In one round you can complete either
2 or 3 tasks of the *same* difficulty level. Return the minimum rounds to complete all tasks, or `-1` if
impossible (some difficulty level appears exactly once).""",
        "function_name": "minimumRounds",
        "params": [{"name": "tasks", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def minimumRounds(tasks):\n    # your code here -- count frequencies, ceil(count/3) per group, -1 if any count==1\n    pass\n",
            "cpp": "int minimumRounds(vector<int> tasks) {\n    // your code here\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[2, 2, 3, 3, 2, 4, 4, 4, 4]], "expected": 4, "input_display": "tasks=[2,2,3,3,2,4,4,4,4]"},
            {"inputs": [[2, 3, 3]], "expected": -1, "input_display": "tasks=[2,3,3] (task level 2 appears once)"},
            {"inputs": [[1, 1]], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "evaluate_rpn",
        "title": "Evaluate Reverse Polish Notation",
        "difficulty": "Medium",
        "topic": "Arrays / Stack",
        "tags": ["array", "math", "stack"],
        "description_md": """Evaluate an arithmetic expression given as `tokens` in Reverse Polish (postfix)
Notation. Valid operators are `+ - * /`; division truncates toward zero. Return the result.""",
        "function_name": "evalRPN",
        "params": [{"name": "tokens", "type": "vector<string>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def evalRPN(tokens):\n    # your code here -- stack-based evaluation\n    pass\n",
            "cpp": "int evalRPN(vector<string> tokens) {\n    // your code here -- stack-based evaluation\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [["2", "1", "+", "3", "*"]], "expected": 9, "input_display": 'tokens=["2","1","+","3","*"]'},
            {"inputs": [["4", "13", "5", "/", "+"]], "expected": 6, "input_display": 'tokens=["4","13","5","/","+"]'},
            {"inputs": [["-4", "2", "/"]], "expected": -2, "hidden": True},
        ],
    },
    {
        "id": "making_a_large_island",
        "title": "Making A Large Island",
        "difficulty": "Hard",
        "topic": "Graphs / DFS",
        "tags": ["graph", "dfs", "grid", "union-find"],
        "description_md": """Given an `n x n` binary `grid`, you may change at most one `0` to a `1`. Return
the size of the largest island possible afterward (an island is a 4-directionally connected group of `1`s).""",
        "function_name": "largestIsland",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def largestIsland(grid):\n    # your code here -- label each island with its size, then try flipping each 0\n    pass\n",
            "cpp": "int largestIsland(vector<vector<int>> grid) {\n    // your code here -- label each island with its size, then try flipping each 0\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 0], [0, 1]]], "expected": 3, "input_display": "grid=[[1,0],[0,1]]"},
            {"inputs": [[[1, 1], [1, 0]]], "expected": 4, "input_display": "grid=[[1,1],[1,0]]"},
            {"inputs": [[[1, 1], [1, 1]]], "expected": 4, "hidden": True},
        ],
    },
    {
        "id": "word_break_ii",
        "title": "Word Break II",
        "difficulty": "Hard",
        "topic": "Strings / Backtracking",
        "tags": ["string", "dynamic-programming", "backtracking", "memoization"],
        "description_md": """Given a string `s` and a dictionary `wordDict`, return all possible sentences
(space-separated, in any order -- grading here ignores order) formed by breaking `s` into a sequence of
dictionary words. Use memoization; the naive version times out on longer inputs.""",
        "function_name": "wordBreakSentences",
        "params": [{"name": "s", "type": "string"}, {"name": "wordDict", "type": "vector<string>"}],
        "return_type": "vector<string>",
        "unordered": True,
        "starter_code": {
            "python": "def wordBreakSentences(s, wordDict):\n    # your code here -- memoized backtracking\n    pass\n",
            "cpp": "vector<string> wordBreakSentences(string s, vector<string> wordDict) {\n    // your code here -- memoized backtracking\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": ["catsanddog", ["cat", "cats", "and", "sand", "dog"]], "expected": ["cat sand dog", "cats and dog"],
             "input_display": 's="catsanddog", wordDict=["cat","cats","and","sand","dog"]'},
            {"inputs": ["aaaa", ["a", "aa"]], "expected": ["a a a a", "a a aa", "a aa a", "aa a a", "aa aa"], "hidden": True},
        ],
    },
    {
        "id": "median_data_stream_doubled",
        "title": "Median From a Data Stream",
        "difficulty": "Hard",
        "topic": "Design / Heaps",
        "tags": ["heap", "design", "two-heaps"],
        "description_md": """Design a structure that supports adding numbers from a stream and querying the
running median after each addition, using two heaps (a max-heap for the lower half, a min-heap for the
upper half) rather than re-sorting every time.

To keep this judge's integer-only comparisons exact (no floating point), return `2 x median` after each
insertion instead of the median itself -- this is always a whole number.""",
        "function_name": "medianStreamDoubled",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "import heapq\ndef medianStreamDoubled(nums):\n    # your code here -- two heaps, return 2*median after each insertion\n    pass\n",
            "cpp": "vector<int> medianStreamDoubled(vector<int> nums) {\n    // your code here -- two heaps (priority_queue), return 2*median after each insertion\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3]], "expected": [2, 3, 4], "input_display": "nums=[1,2,3] (insert one at a time)"},
            {"inputs": [[2, 1, 5, 7, 2, 0, 5]], "expected": [4, 3, 4, 7, 4, 4, 4], "hidden": True},
            {"inputs": [[5]], "expected": [10], "hidden": True},
        ],
    },
]


def main():
    for p in PROBLEMS:
        path = os.path.join(HERE, f"{p['id']}.json")
        with open(path, "w") as f:
            json.dump(p, f, indent=2)
        print("wrote", path)


if __name__ == "__main__":
    main()
