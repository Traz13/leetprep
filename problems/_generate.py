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
        "diagram_svg": """<svg viewBox="0 0 187 82" width="187" height="82" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="20" width="34" height="34" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="23.0" y="42.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">2</text><rect x="46" y="20" width="34" height="34" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="63.0" y="42.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">7</text><rect x="86" y="20" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="103.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">11</text><rect x="126" y="20" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="143.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">15</text><text x="6" y="76" font-size="10.5" fill="var(--text-2)">nums[0] + nums[1] = 2+7 = 9</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 304 156" width="304" height="156" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="62.0" y1="101.71428571428571" x2="182.0" y2="30.285714285714278" stroke="#6ee7b7" stroke-width="2" stroke-dasharray="5,3" opacity="0.8"/><rect x="6" y="16.0" width="32" height="100.0" fill="var(--bg-3)" fill-opacity="1" stroke="var(--line)" stroke-width="1.5"/><text x="22.0" y="10.0" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">7</text><rect x="46" y="101.71428571428571" width="32" height="14.285714285714286" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="62.0" y="95.71428571428571" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">1</text><text x="62.0" y="130" text-anchor="middle" font-size="9.5" fill="#6ee7b7">buy</text><rect x="86" y="44.57142857142857" width="32" height="71.42857142857143" fill="var(--bg-3)" fill-opacity="1" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="38.57142857142857" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">5</text><rect x="126" y="73.14285714285714" width="32" height="42.85714285714286" fill="var(--bg-3)" fill-opacity="1" stroke="var(--line)" stroke-width="1.5"/><text x="142.0" y="67.14285714285714" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">3</text><rect x="166" y="30.285714285714278" width="32" height="85.71428571428572" fill="#f87171" fill-opacity="0.85" stroke="#f87171" stroke-width="1.5"/><text x="182.0" y="24.285714285714278" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">6</text><text x="182.0" y="130" text-anchor="middle" font-size="9.5" fill="#f87171">sell</text><rect x="206" y="58.857142857142854" width="32" height="57.142857142857146" fill="var(--bg-3)" fill-opacity="1" stroke="var(--line)" stroke-width="1.5"/><text x="222.0" y="52.857142857142854" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">4</text><text x="6" y="152" font-size="10.5" fill="#6ee7b7">buy@1 (price 1), sell@4 (price 6) -> profit 5</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 372 130" width="372" height="130" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="56.0" width="32" height="20.0" fill="var(--bg-3)" fill-opacity="0.9" stroke="var(--line)" stroke-width="1.5"/><text x="22.0" y="88.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">-2</text><rect x="46" y="46.0" width="32" height="10.0" fill="var(--bg-3)" fill-opacity="0.9" stroke="var(--line)" stroke-width="1.5"/><text x="62.0" y="41.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">1</text><rect x="86" y="56.0" width="32" height="30.0" fill="var(--bg-3)" fill-opacity="0.9" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="98.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">-3</text><rect x="126" y="16.0" width="32" height="40.0" fill="#ffb454" fill-opacity="0.9" stroke="#ffb454" stroke-width="1.5"/><text x="142.0" y="11.0" text-anchor="middle" font-size="11" fill="#1a1204" font-weight="600">4</text><rect x="166" y="56.0" width="32" height="10.0" fill="#ffb454" fill-opacity="0.9" stroke="#ffb454" stroke-width="1.5"/><text x="182.0" y="78.0" text-anchor="middle" font-size="11" fill="#1a1204" font-weight="600">-1</text><rect x="206" y="36.0" width="32" height="20.0" fill="#ffb454" fill-opacity="0.9" stroke="#ffb454" stroke-width="1.5"/><text x="222.0" y="31.0" text-anchor="middle" font-size="11" fill="#1a1204" font-weight="600">2</text><rect x="246" y="46.0" width="32" height="10.0" fill="#ffb454" fill-opacity="0.9" stroke="#ffb454" stroke-width="1.5"/><text x="262.0" y="41.0" text-anchor="middle" font-size="11" fill="#1a1204" font-weight="600">1</text><rect x="286" y="56.0" width="32" height="50.0" fill="var(--bg-3)" fill-opacity="0.9" stroke="var(--line)" stroke-width="1.5"/><text x="302.0" y="118.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">-5</text><rect x="326" y="16.0" width="32" height="40.0" fill="var(--bg-3)" fill-opacity="0.9" stroke="var(--line)" stroke-width="1.5"/><text x="342.0" y="11.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">4</text><line x1="6" y1="56.0" x2="366" y2="56.0" stroke="var(--line)" stroke-width="1"/><text x="6" y="126" font-size="10.5" fill="#ffb454">highlighted subarray sums to 6</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 138 138" width="138" height="138" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="#fbbf7a" stroke="#ffb454" stroke-width="1.5"/><text x="26.0" y="32.0" text-anchor="middle" font-size="14" fill="#1a1204" font-weight="700">S</text><rect x="48" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="48" width="40" height="40" rx="4" fill="#fbbf7a" stroke="#ffb454" stroke-width="1.5"/><rect x="48" y="48" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="68.0" y="74.0" text-anchor="middle" font-size="14" fill="var(--text-2)" font-weight="700">#</text><rect x="90" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="90" width="40" height="40" rx="4" fill="#fbbf7a" stroke="#ffb454" stroke-width="1.5"/><rect x="48" y="90" width="40" height="40" rx="4" fill="#fbbf7a" stroke="#ffb454" stroke-width="1.5"/><rect x="90" y="90" width="40" height="40" rx="4" fill="#fbbf7a" stroke="#ffb454" stroke-width="1.5"/><text x="110.0" y="116.0" text-anchor="middle" font-size="14" fill="#1a1204" font-weight="700">E</text></svg>""",
        "function_name": "minSteps",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def minSteps(grid):\n    # BFS from (0,0) to (rows-1, cols-1)\n    pass\n",
            "cpp": "int minSteps(vector<vector<int>> grid) {\n    // BFS from (0,0) to (rows-1, cols-1)\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], "expected": 4, "input_display": "grid=[[0,0,0],[0,1,0],[0,0,0]] (3x3, one blocked cell in the middle)",
             "explanation": "The direct diagonal shortcut isn't allowed (only up/down/left/right moves), and the middle cell is blocked, so the shortest path has to go around it -- e.g. (0,0)->(1,0)->(2,0)->(2,1)->(2,2), 4 steps."},
            {"inputs": [[[0, 1], [1, 0]]], "expected": -1, "input_display": "grid=[[0,1],[1,0]] (2x2, no path)",
             "explanation": "The start (0,0) and end (1,1) are both open, but the only two cells connecting them, (0,1) and (1,0), are both blocked -- there's no route at all."},
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
        "diagram_svg": """<svg viewBox="0 0 310 172" width="310" height="172" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="dij-arrow" markerWidth="7" markerHeight="7" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="var(--text-2)"/></marker></defs><line x1="50" y1="83.0" x2="97" y2="50.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dij-arrow)" opacity="0.7"/><text x="75.0" y="62.5" text-anchor="middle" font-size="10.5" fill="var(--text-2)">1</text><line x1="140" y1="50.0" x2="97" y2="116.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dij-arrow)" opacity="0.7"/><text x="120.0" y="79.0" text-anchor="middle" font-size="10.5" fill="var(--text-2)">2</text><line x1="50" y1="83.0" x2="97" y2="116.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dij-arrow)" opacity="0.7"/><text x="75.0" y="95.5" text-anchor="middle" font-size="10.5" fill="var(--text-2)">4</text><line x1="140" y1="116.0" x2="187" y2="83.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dij-arrow)" opacity="0.7"/><text x="165.0" y="95.5" text-anchor="middle" font-size="10.5" fill="var(--text-2)">1</text><circle cx="30" cy="83.0" r="20" fill="var(--bg-3)" stroke="#6ee7b7" stroke-width="2"/><text x="30" y="81.0" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">0</text><text x="30" y="94.0" text-anchor="middle" font-size="8.5" fill="#6ee7b7">d=0</text><circle cx="120" cy="50.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="120" y="48.0" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">1</text><text x="120" y="61.0" text-anchor="middle" font-size="8.5" fill="var(--amber)">d=1</text><circle cx="120" cy="116.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="120" y="114.0" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">2</text><text x="120" y="127.0" text-anchor="middle" font-size="8.5" fill="var(--amber)">d=3</text><circle cx="210" cy="83.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="210" y="81.0" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">3</text><text x="210" y="94.0" text-anchor="middle" font-size="8.5" fill="var(--amber)">d=4</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 176 67" width="176" height="67" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><path d="M18.0,33 Q32.0,12 46.0,33" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.8"/><path d="M74.0,33 Q88.0,12 102.0,33" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.8"/><path d="M130.0,33 Q144.0,12 158.0,33" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.8"/><rect x="6.0" y="33" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="50.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="34.0" y="33" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="46.0" y="50.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="62.0" y="33" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="74.0" y="50.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">[</text><rect x="90.0" y="33" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="50.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">]</text><rect x="118.0" y="33" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="130.0" y="50.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">{</text><rect x="146.0" y="33" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="158.0" y="50.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">}</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 272.0 66" width="272.0" height="66" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="16" width="116.18181818181819" height="30" rx="3" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="65.0909090909091" y="36.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">5</text><rect x="124.18181818181819" y="16" width="116.18181818181819" height="30" rx="3" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="183.27272727272728" y="36.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">5</text><rect x="242.36363636363637" y="16" width="21.636363636363637" height="30" rx="3" fill="#fdba74" fill-opacity="0.85" stroke="#fdba74" stroke-width="1.5"/><text x="254.1818181818182" y="36.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">1</text><text x="6" y="60" font-size="10.5" fill="var(--text-2)">amount 11 = 5 + 5 + 1 (3 coins)</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 376 228" width="376" height="228" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="4" y1="24" x2="368" y2="24" stroke="var(--line)" stroke-width="1" stroke-dasharray="3,3"/><text x="4" y="18" font-size="9.5" fill="var(--text-2)">depth 0</text><line x1="4" y1="84" x2="368" y2="84" stroke="var(--line)" stroke-width="1" stroke-dasharray="3,3"/><text x="4" y="78" font-size="9.5" fill="var(--text-2)">depth 1</text><line x1="4" y1="144" x2="368" y2="144" stroke="var(--line)" stroke-width="1" stroke-dasharray="3,3"/><text x="4" y="138" font-size="9.5" fill="var(--text-2)">depth 2</text><text x="4" y="222" font-size="10.5" fill="var(--amber)">max depth = 3 (deepest row is depth 2)</text><line x1="170.0" y1="24" x2="114.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="170.0" y1="24" x2="282.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="282.0" y1="84" x2="226.0" y2="144" stroke="var(--line)" stroke-width="2"/><line x1="282.0" y1="84" x2="338.0" y2="144" stroke="var(--line)" stroke-width="2"/><circle cx="170.0" cy="24" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="170.0" y="29" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text><circle cx="114.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="114.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">9</text><circle cx="282.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="282.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">20</text><circle cx="226.0" cy="144" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="226.0" y="149" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">15</text><circle cx="338.0" cy="144" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="338.0" y="149" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">7</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 292 140" width="292" height="140" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="14" font-size="11" fill="var(--text-2)">Before</text><rect x="6" y="24" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="22.0" y="44.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="46" y="24" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="62.0" y="44.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">2</text><rect x="86" y="24" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="44.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">3</text><rect x="126" y="24" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="142.0" y="44.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">4</text><rect x="166" y="24" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="182.0" y="44.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">5</text><rect x="206" y="24" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="222.0" y="44.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">6</text><rect x="246" y="24" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="262.0" y="44.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">7</text><text x="6" y="74" font-size="11" fill="var(--text-2)">After rotating right by 3</text><rect x="6" y="80" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="22.0" y="100.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">5</text><rect x="46" y="80" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="62.0" y="100.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">6</text><rect x="86" y="80" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="102.0" y="100.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">7</text><rect x="126" y="80" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="142.0" y="100.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="166" y="80" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="182.0" y="100.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">2</text><rect x="206" y="80" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="222.0" y="100.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">3</text><rect x="246" y="80" width="32" height="30" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="262.0" y="100.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">4</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 460 302" width="460" height="302" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="14" font-size="11" fill="var(--text-2)">Before</text><rect x="6.0" y="22" width="52.705882352941174" height="24" rx="5" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="32.35294117647059" y="39.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[1,3]</text><rect x="32.35294117647059" y="58" width="105.41176470588238" height="24" rx="5" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="85.05882352941177" y="75.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[2,6]</text><rect x="190.47058823529412" y="94" width="52.70588235294119" height="24" rx="5" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="216.8235294117647" y="111.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[8,10]</text><rect x="374.94117647058823" y="130" width="79.05882352941177" height="24" rx="5" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="414.47058823529414" y="147.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[15,18]</text><text x="6" y="180" font-size="11" fill="var(--text-2)">After merging</text><rect x="6.0" y="188" width="131.76470588235296" height="24" rx="5" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="71.88235294117648" y="205.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[1,6]</text><rect x="190.47058823529412" y="224" width="52.70588235294119" height="24" rx="5" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="216.8235294117647" y="241.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[8,10]</text><rect x="374.94117647058823" y="260" width="79.05882352941177" height="24" rx="5" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="414.47058823529414" y="277.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[15,18]</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 274 206" width="274" height="206" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="26.0" y="32.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="48" y="6" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="68.0" y="32.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="90" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="110.0" y="32.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="132" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="152.0" y="32.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="6" y="48" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="26.0" y="74.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="48" y="48" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="68.0" y="74.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="90" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="110.0" y="74.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="132" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="152.0" y="74.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="6" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="26.0" y="116.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="48" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="68.0" y="116.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="90" y="90" width="40" height="40" rx="4" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="110.0" y="116.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="132" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="152.0" y="116.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="6" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="26.0" y="158.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="48" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="68.0" y="158.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="90" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="110.0" y="158.0" text-anchor="middle" font-size="14" fill="var(--text-2)">0</text><rect x="132" y="132" width="40" height="40" rx="4" fill="#f0abfc" fill-opacity="0.85" stroke="#f0abfc" stroke-width="1.5"/><text x="152.0" y="158.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="6" y="185" width="12" height="12" rx="3" fill="#6ee7b7"/><text x="22" y="195" font-size="11" fill="var(--text-1)">Island 1</text><rect x="93.6" y="185" width="12" height="12" rx="3" fill="#93c5fd"/><text x="109.6" y="195" font-size="11" fill="var(--text-1)">Island 2</text><rect x="181.2" y="185" width="12" height="12" rx="3" fill="#f0abfc"/><text x="197.2" y="195" font-size="11" fill="var(--text-1)">Island 3</text></svg>""",
        "function_name": "countIslands",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def countIslands(grid):\n    # your code here\n    pass\n",
            "cpp": "int countIslands(vector<vector<int>> grid) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]], "expected": 3,
             "input_display": "grid=[[1,1,0,0],[1,1,0,0],[0,0,1,0],[0,0,0,1]]",
             "explanation": "The four 1's in the top-left corner all touch each other (directly or through a shared neighbor), so they form one island. The 1 at (2,2) and the 1 at (3,3) don't touch anything -- not even diagonally, which doesn't count -- so each is its own island. Three islands total."},
            {"inputs": [[[0, 0], [0, 0]]], "expected": 0, "input_display": "grid=[[0,0],[0,0]] (all water)"},
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
        "diagram_svg": """<svg viewBox="0 0 272 74" width="272" height="74" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="21.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">e</text><rect x="41" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="56.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="76" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="91.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">e</text><rect x="111" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="126.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">b</text><rect x="146" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="161.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">a</text><rect x="4" y="10" width="104" height="38" rx="6" fill="none" stroke="#6ee7b7" stroke-width="2" stroke-dasharray="5,3"/><text x="6" y="60" font-size="10.5" fill="var(--text-2)">window "ece" has 2 distinct chars (e, c)</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 372 94" width="372" height="94" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="20" width="66" height="30" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="39.0" y="40.0" text-anchor="middle" font-size="10.5" fill="#0a0a0a" font-weight="600">practice</text><rect x="78" y="20" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="111.0" y="40.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">makes</text><rect x="150" y="20" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="183.0" y="40.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">perfect</text><rect x="222" y="20" width="66" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="255.0" y="40.0" text-anchor="middle" font-size="10.5" fill="#0a0a0a" font-weight="600">coding</text><rect x="294" y="20" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="327.0" y="40.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">makes</text><line x1="39.0" y1="64" x2="255.0" y2="64" stroke="#ffb454" stroke-width="1.5"/><text x="147.0" y="78" text-anchor="middle" font-size="10.5" fill="#ffb454">distance = 3</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 402 114" width="402" height="114" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="12" font-size="10.5" fill="var(--text-2)">Before</text><rect x="6" y="20" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="22.0" y="40.0" text-anchor="middle" font-size="13" fill="var(--text-2)" font-weight="600">0</text><rect x="46" y="20" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="62.0" y="40.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="86" y="20" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="40.0" text-anchor="middle" font-size="13" fill="var(--text-2)" font-weight="600">0</text><rect x="126" y="20" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="142.0" y="40.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">3</text><rect x="166" y="20" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="182.0" y="40.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">12</text><text x="6" y="68" font-size="10.5" fill="var(--text-2)">After -- zeroes pushed to the end, order preserved otherwise</text><rect x="6" y="74" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="22.0" y="94.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="46" y="74" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="62.0" y="94.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">3</text><rect x="86" y="74" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="102.0" y="94.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">12</text><rect x="126" y="74" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="142.0" y="94.0" text-anchor="middle" font-size="13" fill="var(--text-2)" font-weight="600">0</text><rect x="166" y="74" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="182.0" y="94.0" text-anchor="middle" font-size="13" fill="var(--text-2)" font-weight="600">0</text></svg>""",
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
[a, b]` means you must take course `b` before course `a`. Return a valid order in which to take all the
courses, or an empty array if it's impossible (which happens exactly when the prerequisites form a cycle).

There's usually more than one valid order. To keep grading deterministic, return the
**lexicographically smallest** one -- whenever more than one course is available to take next, pick the
lowest-numbered one first.""",
        "diagram_svg": """<svg viewBox="0 0 310 168" width="310" height="168" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="dep-arrow" markerWidth="7" markerHeight="7" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="var(--text-2)"/></marker></defs><line x1="50" y1="82.0" x2="97" y2="50.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dep-arrow)" opacity="0.8"/><line x1="50" y1="82.0" x2="97" y2="114.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dep-arrow)" opacity="0.8"/><line x1="140" y1="50.0" x2="187" y2="82.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dep-arrow)" opacity="0.8"/><line x1="140" y1="114.0" x2="187" y2="82.0" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dep-arrow)" opacity="0.8"/><circle cx="30" cy="82.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="30" y="87.0" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">0</text><circle cx="120" cy="50.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="120" y="55.0" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">1</text><circle cx="120" cy="114.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="120" y="119.0" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">2</text><circle cx="210" cy="82.0" r="20" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="210" y="87.0" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">3</text></svg>""",
        "function_name": "courseOrder",
        "params": [{"name": "numCourses", "type": "int"}, {"name": "prerequisites", "type": "vector<vector<int>>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "import heapq\ndef courseOrder(numCourses, prerequisites):\n    # your code here -- use a min-heap for the lexicographically smallest order\n    pass\n",
            "cpp": "vector<int> courseOrder(int numCourses, vector<vector<int>> prerequisites) {\n    // your code here -- use a min-heap (priority_queue<int, vector<int>, greater<int>>)\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], "expected": [0, 1, 2, 3], "input_display": "numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]",
             "explanation": "Course 0 has no prerequisites, so it must go first. That immediately unlocks both 1 and 2 -- pick 1 before 2 since it's lower-numbered. Course 3 needs both 1 and 2 finished, so it can only go last."},
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
        "diagram_svg": """<svg viewBox="0 0 415 92" width="415" height="92" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="6" y1="56" x2="194" y2="56" stroke="var(--line)" stroke-width="1.5"/><rect x="40" y="49.0" width="120" height="14" rx="7.0" fill="#fdba74" fill-opacity="0.3" stroke="#fdba74" stroke-width="1.5"/><circle cx="100" cy="56" r="5" fill="#fdba74" stroke="var(--bg-0)" stroke-width="1"/><text x="100" y="43" text-anchor="middle" font-size="10" fill="#fdba74">heater@2</text><circle cx="40" cy="56" r="5" fill="#93c5fd" stroke="var(--bg-0)" stroke-width="1.5"/><text x="40" y="76" text-anchor="middle" font-size="9.5" fill="var(--text-1)">house@1</text><circle cx="100" cy="56" r="5" fill="#93c5fd" stroke="var(--bg-0)" stroke-width="1.5"/><text x="100" y="76" text-anchor="middle" font-size="9.5" fill="var(--text-1)">house@2</text><circle cx="160" cy="56" r="5" fill="#93c5fd" stroke="var(--bg-0)" stroke-width="1.5"/><text x="160" y="76" text-anchor="middle" font-size="9.5" fill="var(--text-1)">house@3</text><text x="6" y="88" font-size="10.5" fill="var(--text-2)">radius = 1 -- every house falls inside some heater's warm band</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 316 170" width="316" height="170" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="temp-arrow" markerWidth="7" markerHeight="7" refX="5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 Z" fill="#f87171"/></marker></defs><rect x="6" y="81.14285714285714" width="26" height="68.85714285714286" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="19.0" y="75.14285714285714" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">73</text><text x="19.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">0</text><path d="M19.0,81.14285714285714 Q38.0,49.42857142857143 57.0,65.42857142857143" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#temp-arrow)" opacity="0.85"/><rect x="44" y="65.42857142857143" width="26" height="84.57142857142857" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="57.0" y="59.42857142857143" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">74</text><text x="57.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">1</text><path d="M57.0,65.42857142857143 Q76.0,33.71428571428572 95.0,49.71428571428572" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#temp-arrow)" opacity="0.85"/><rect x="82" y="49.71428571428572" width="26" height="100.28571428571428" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="95.0" y="43.71428571428572" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">75</text><text x="95.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">2</text><path d="M95.0,49.71428571428572 Q171.0,18.0 247.0,34.0" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#temp-arrow)" opacity="0.85"/><rect x="120" y="112.57142857142857" width="26" height="37.42857142857143" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="133.0" y="106.57142857142857" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">71</text><text x="133.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">3</text><path d="M133.0,112.57142857142857 Q171.0,80.85714285714286 209.0,96.85714285714286" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#temp-arrow)" opacity="0.85"/><rect x="158" y="144.0" width="26" height="6.0" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="171.0" y="138.0" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">69</text><text x="171.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">4</text><path d="M171.0,144.0 Q190.0,80.85714285714286 209.0,96.85714285714286" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#temp-arrow)" opacity="0.85"/><rect x="196" y="96.85714285714286" width="26" height="53.14285714285714" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="209.0" y="90.85714285714286" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">72</text><text x="209.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">5</text><path d="M209.0,96.85714285714286 Q228.0,18.0 247.0,34.0" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#temp-arrow)" opacity="0.85"/><rect x="234" y="34.0" width="26" height="116.0" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="247.0" y="28.0" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">76</text><text x="247.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">6</text><rect x="272" y="81.14285714285714" width="26" height="68.85714285714286" rx="3" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="285.0" y="75.14285714285714" text-anchor="middle" font-size="11" fill="var(--text-0)" font-weight="600">73</text><text x="285.0" y="164" text-anchor="middle" font-size="9" fill="var(--text-2)">7</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 331 90" width="331" height="90" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="14" width="26" height="28" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="19.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">a</text><rect x="35" y="14" width="26" height="28" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="48.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">a</text><rect x="64" y="14" width="26" height="28" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="77.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">b</text><rect x="93" y="14" width="26" height="28" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><text x="106.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="122" y="14" width="26" height="28" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><text x="135.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="151" y="14" width="26" height="28" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><text x="164.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="180" y="14" width="26" height="28" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><text x="193.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="209" y="14" width="26" height="28" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><text x="222.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="238" y="14" width="26" height="28" rx="4" fill="#f0abfc" stroke="#f0abfc" stroke-width="1.5"/><text x="251.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">a</text><rect x="267" y="14" width="26" height="28" rx="4" fill="#f0abfc" stroke="#f0abfc" stroke-width="1.5"/><text x="280.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">a</text><rect x="296" y="14" width="26" height="28" rx="4" fill="#f0abfc" stroke="#f0abfc" stroke-width="1.5"/><text x="309.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">a</text><text x="33.5" y="62" text-anchor="middle" font-size="12" fill="#6ee7b7" font-weight="700">a2</text><text x="77.0" y="62" text-anchor="middle" font-size="12" fill="#93c5fd" font-weight="700">b</text><text x="164.0" y="62" text-anchor="middle" font-size="12" fill="#fdba74" font-weight="700">c5</text><text x="280.0" y="62" text-anchor="middle" font-size="12" fill="#f0abfc" font-weight="700">a3</text><text x="6" y="82" font-size="10.5" fill="var(--text-2)">compressed: "a2bc5a3"</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 302.0 150.0" width="302.0" height="150.0" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><circle cx="92.0" cy="76.0" r="50.0" fill="#ffb454" fill-opacity="0.12" stroke="#ffb454" stroke-width="1.5" stroke-dasharray="4,3"/><circle cx="92.0" cy="76.0" r="3" fill="#ffb454"/><text x="92.0" y="18.0" text-anchor="middle" font-size="10" fill="#ffb454">query (2,3) r=1</text><circle cx="42.0" cy="76.0" r="5" fill="#6ee7b7" stroke="var(--bg-0)" stroke-width="1"/><text x="50.0" y="70.0" font-size="9.5" fill="var(--text-1)">(1,3)</text><circle cx="142.0" cy="76.0" r="5" fill="#6ee7b7" stroke="var(--bg-0)" stroke-width="1"/><text x="150.0" y="70.0" font-size="9.5" fill="var(--text-1)">(3,3)</text><circle cx="242.0" cy="76.0" r="5" fill="#93c5fd" stroke="var(--bg-0)" stroke-width="1"/><text x="250.0" y="70.0" font-size="9.5" fill="var(--text-1)">(5,3)</text><circle cx="92.0" cy="126.0" r="5" fill="#6ee7b7" stroke="var(--bg-0)" stroke-width="1"/><text x="100.0" y="120.0" font-size="9.5" fill="var(--text-1)">(2,2)</text><text x="6" y="144.0" font-size="10.5" fill="var(--text-2)">3 point(s) inside this circle</text></svg>""",
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
        "description_md": """Given the root of a binary tree, return its *vertical order traversal*.

Picture every node assigned a column number: the root is column 0, and each step down to a left child moves
one column to the left (`col - 1`), while each step to a right child moves one column to the right
(`col + 1`) -- regardless of how deep in the tree that step happens. So a node's column depends only on the
sequence of left/right moves from the root to reach it, not on its depth.

Group node values by column, ordered top-to-bottom (by depth) within each column, and return the columns
ordered from leftmost to rightmost.""",
        "diagram_svg": """<svg viewBox="0 0 296 254" width="296" height="254" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="116.0" y1="30" x2="52.0" y2="96" stroke="var(--line)" stroke-width="2"/><line x1="116.0" y1="30" x2="180.0" y2="96" stroke="var(--line)" stroke-width="2"/><line x1="180.0" y1="96" x2="116.0" y2="162" stroke="var(--line)" stroke-width="2"/><line x1="180.0" y1="96" x2="244.0" y2="162" stroke="var(--line)" stroke-width="2"/><circle cx="116.0" cy="30" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="116.0" y="35" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">3</text><text x="116.0" y="64" text-anchor="middle" font-size="10.5" fill="var(--amber)">col 0</text><circle cx="52.0" cy="96" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="52.0" y="101" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">9</text><text x="52.0" y="130" text-anchor="middle" font-size="10.5" fill="var(--amber)">col -1</text><circle cx="180.0" cy="96" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="180.0" y="101" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">20</text><text x="180.0" y="130" text-anchor="middle" font-size="10.5" fill="var(--amber)">col +1</text><circle cx="116.0" cy="162" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="116.0" y="167" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">15</text><text x="116.0" y="196" text-anchor="middle" font-size="10.5" fill="var(--amber)">col 0</text><circle cx="244.0" cy="162" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="244.0" y="167" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">7</text><text x="244.0" y="196" text-anchor="middle" font-size="10.5" fill="var(--amber)">col +2</text><line x1="20" y1="226" x2="276" y2="226" stroke="var(--line)" stroke-width="1" stroke-dasharray="3,3"/><text x="52.0" y="240" text-anchor="middle" font-size="10" fill="var(--text-2)">-1</text><text x="116.0" y="240" text-anchor="middle" font-size="10" fill="var(--text-2)">0</text><text x="180.0" y="240" text-anchor="middle" font-size="10" fill="var(--text-2)">+1</text><text x="244.0" y="240" text-anchor="middle" font-size="10" fill="var(--text-2)">+2</text></svg>""",
        "function_name": "verticalOrder",
        "params": [{"name": "root", "type": "tree"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "from collections import deque, defaultdict\n\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\ndef verticalOrder(root):\n    # your code here -- BFS tracking column index\n    pass\n",
            "cpp": "// struct TreeNode {\n//     int val;\n//     TreeNode *left;\n//     TreeNode *right;\n//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n// };\n\nvector<vector<int>> verticalOrder(TreeNode* root) {\n    // your code here -- BFS tracking column index (map<int,vector<int>> auto-sorts by key)\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[3, 9, 20, None, None, 15, 7]], "expected": [[9], [3, 15], [20], [7]], "input_display": "tree=[3,9,20,null,null,15,7]",
             "explanation": "Root 3 is column 0. Its left child 9 is column -1; its right child 20 is column 1. 20's own children then shift from column 1: its left child 15 lands back at column 0 (alongside the root), and its right child 7 lands at column 2. Sorted left to right by column: -1 -> [9], 0 -> [3, 15] (3 above 15), 1 -> [20], 2 -> [7]."},
            {"inputs": [[1, 2, 3, 4, 5, 6, 7]], "expected": [[4], [2], [1, 5, 6], [3], [7]], "hidden": True},
        ],
    },
    {
        "id": "push_dominoes",
        "title": "Push Dominoes",
        "difficulty": "Medium",
        "topic": "Strings / Simulation",
        "tags": ["string", "two-pointers", "simulation"],
        "description_md": """A row of dominoes is represented by a string `dominoes` of the same length, where
each character is `R` (that domino has already been pushed to the right), `L` (pushed to the left), or `.`
(still standing upright, not pushed).

Every pushed domino, in turn, pushes the next *standing* domino in front of it in the same direction. If a
standing domino ends up being pushed from both the left and the right at the same moment (because an `R` and
an `L` are advancing toward each other and reach it at the same time), the forces cancel out and it stays
upright.

Return the final string once every domino has either fallen or settled.""",
        "diagram_svg": """<svg viewBox="0 0 432 60" width="432" height="60" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="14" width="26" height="32" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="19.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">L</text><rect x="36" y="14" width="26" height="32" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="49.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">L</text><rect x="66" y="14" width="26" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="79.0" y="35.0" text-anchor="middle" font-size="12" fill="var(--text-2)" font-weight="600"></text><rect x="96" y="14" width="26" height="32" rx="4" fill="#fca5a5" stroke="#fca5a5" stroke-width="1.5"/><text x="109.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">R</text><rect x="126" y="14" width="26" height="32" rx="4" fill="#fca5a5" stroke="#fca5a5" stroke-width="1.5"/><text x="139.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">R</text><rect x="156" y="14" width="26" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="169.0" y="35.0" text-anchor="middle" font-size="12" fill="var(--text-2)" font-weight="600"></text><rect x="186" y="14" width="26" height="32" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="199.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">L</text><rect x="216" y="14" width="26" height="32" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="229.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">L</text><rect x="246" y="14" width="26" height="32" rx="4" fill="#fca5a5" stroke="#fca5a5" stroke-width="1.5"/><text x="259.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">R</text><rect x="276" y="14" width="26" height="32" rx="4" fill="#fca5a5" stroke="#fca5a5" stroke-width="1.5"/><text x="289.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">R</text><rect x="306" y="14" width="26" height="32" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="319.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">L</text><rect x="336" y="14" width="26" height="32" rx="4" fill="#93c5fd" stroke="#93c5fd" stroke-width="1.5"/><text x="349.0" y="35.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="600">L</text><rect x="366" y="14" width="26" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="379.0" y="35.0" text-anchor="middle" font-size="12" fill="var(--text-2)" font-weight="600"></text><rect x="396" y="14" width="26" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="409.0" y="35.0" text-anchor="middle" font-size="12" fill="var(--text-2)" font-weight="600"></text></svg>""",
        "function_name": "pushDominoes",
        "params": [{"name": "dominoes", "type": "string"}],
        "return_type": "string",
        "starter_code": {
            "python": "def pushDominoes(dominoes):\n    # your code here\n    pass\n",
            "cpp": "string pushDominoes(string dominoes) {\n    // your code here\n    return dominoes;\n}\n",
        },
        "test_cases": [
            {"inputs": [".L.R...LR..L.."], "expected": "LL.RR.LLRRLL..", "input_display": 'dominoes=".L.R...LR..L.."',
             "explanation": "Reading left to right: the L at index 1 topples the domino at index 0. The R at index 3 and the L at index 7 push toward each other -- the domino exactly in the middle of that gap (index 5) stays upright since both pushes reach it at the same time, while the rest fall toward whichever push got there first. The L at index 7 and R at index 8 are already adjacent, so nothing happens between them. The R at index 8 and L at index 11 push toward each other across an even gap and split it evenly. Indices 12-13 are past the last L, so nothing ever pushes them and they stay standing."},
            {"inputs": ["RR.L"], "expected": "RR.L", "input_display": 'dominoes="RR.L"',
             "explanation": "The push from the R at index 1 and the push from the L at index 3 both reach the standing domino at index 2 at the same instant, so they cancel and it stays upright -- nothing else moves."},
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
        "diagram_svg": """<svg viewBox="0 0 376 68" width="376" height="68" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="16" width="40" height="28" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="26.0" y="34" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">eat</text><rect x="52" y="16" width="40" height="28" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="72.0" y="34" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">tea</text><rect x="98" y="16" width="40" height="28" rx="4" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="118.0" y="34" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">tan</text><rect x="144" y="16" width="40" height="28" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="164.0" y="34" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">ate</text><rect x="190" y="16" width="40" height="28" rx="4" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="210.0" y="34" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">nat</text><rect x="236" y="16" width="40" height="28" rx="4" fill="#f0abfc" fill-opacity="0.85" stroke="#f0abfc" stroke-width="1.5"/><text x="256.0" y="34" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">bat</text><text x="6" y="60" font-size="10.5" fill="var(--text-2)">3 group(s) -- matching colors are anagrams of each other</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 426 170" width="426" height="170" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="0" y="12" font-size="11" fill="var(--text-2)">Tree 1</text><g transform="translate(0,18)"><line x1="104.0" y1="24" x2="48.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="104.0" y1="24" x2="160.0" y2="84" stroke="var(--line)" stroke-width="2"/><circle cx="104.0" cy="24" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="104.0" y="29" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><circle cx="48.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="48.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text><circle cx="160.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="160.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text></g><text x="228" y="12" font-size="11" fill="var(--text-2)">Tree 2 (children flipped)</text><g transform="translate(228,18)"><line x1="104.0" y1="24" x2="48.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="104.0" y1="24" x2="160.0" y2="84" stroke="var(--line)" stroke-width="2"/><circle cx="104.0" cy="24" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="104.0" y="29" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><circle cx="48.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="48.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text><circle cx="160.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="160.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text></g></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 366 226" width="366" height="226" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="216.0" y1="24" x2="104.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="104.0" y1="84" x2="48.0" y2="144" stroke="var(--line)" stroke-width="2"/><line x1="104.0" y1="84" x2="160.0" y2="144" stroke="var(--line)" stroke-width="2"/><line x1="216.0" y1="24" x2="272.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="272.0" y1="84" x2="328.0" y2="144" stroke="var(--line)" stroke-width="2"/><circle cx="216.0" cy="24" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="216.0" y="29" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><text x="216.0" y="56" text-anchor="middle" font-size="10.5" fill="var(--amber)">#1</text><circle cx="104.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="104.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text><text x="104.0" y="116" text-anchor="middle" font-size="10.5" fill="var(--amber)">#2</text><circle cx="48.0" cy="144" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="48.0" y="149" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text><text x="48.0" y="176" text-anchor="middle" font-size="10.5" fill="var(--amber)">#3</text><circle cx="160.0" cy="144" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="160.0" y="149" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">4</text><text x="160.0" y="176" text-anchor="middle" font-size="10.5" fill="var(--amber)">#4</text><circle cx="272.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="272.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">5</text><text x="272.0" y="116" text-anchor="middle" font-size="10.5" fill="var(--amber)">#5</text><circle cx="328.0" cy="144" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="328.0" y="149" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">6</text><text x="328.0" y="176" text-anchor="middle" font-size="10.5" fill="var(--amber)">#6</text></svg>""",
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
        "description_md": """You're given a list of `products` and a `searchWord` that a user is typing one
character at a time. After each character they've typed so far (i.e. for every prefix of `searchWord`, from
length 1 up to the full word), suggest up to 3 products from `products` that start with that prefix --
whichever 3 come first alphabetically, if more than 3 match.

Return a list with one entry per prefix length (so its length always equals `len(searchWord)`), where each
entry is that prefix's list of up to 3 suggested products, in alphabetical order.""",
        "diagram_svg": """<svg viewBox="0 0 334 132" width="334" height="132" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="22.0" font-family="SF Mono, Consolas, monospace" font-size="11" fill="#ffb454">"m"</text><rect x="70" y="8" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="108.0" y="22.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mobile</text><rect x="154" y="8" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="192.0" y="22.0" text-anchor="middle" font-size="10" fill="var(--text-1)">moneypot</text><rect x="238" y="8" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="276.0" y="22.0" text-anchor="middle" font-size="10" fill="var(--text-1)">monitor</text><text x="6" y="46.0" font-family="SF Mono, Consolas, monospace" font-size="11" fill="#ffb454">"mo"</text><rect x="70" y="32" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="108.0" y="46.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mobile</text><rect x="154" y="32" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="192.0" y="46.0" text-anchor="middle" font-size="10" fill="var(--text-1)">moneypot</text><rect x="238" y="32" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="276.0" y="46.0" text-anchor="middle" font-size="10" fill="var(--text-1)">monitor</text><text x="6" y="70.0" font-family="SF Mono, Consolas, monospace" font-size="11" fill="#ffb454">"mou"</text><rect x="70" y="56" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="108.0" y="70.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mouse</text><rect x="154" y="56" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="192.0" y="70.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mousepad</text><text x="6" y="94.0" font-family="SF Mono, Consolas, monospace" font-size="11" fill="#ffb454">"mous"</text><rect x="70" y="80" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="108.0" y="94.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mouse</text><rect x="154" y="80" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="192.0" y="94.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mousepad</text><text x="6" y="118.0" font-family="SF Mono, Consolas, monospace" font-size="11" fill="#ffb454">"mouse"</text><rect x="70" y="104" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="108.0" y="118.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mouse</text><rect x="154" y="104" width="76" height="18" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="192.0" y="118.0" text-anchor="middle" font-size="10" fill="var(--text-1)">mousepad</text></svg>""",
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
             "input_display": 'products=[...], searchWord="mouse"',
             "explanation": "After typing 'm' and 'mo', all 5 products still match, so the 3 alphabetically-first ones show: mobile, moneypot, monitor. Once 'mou' is typed, only mouse and mousepad still match the prefix -- and they keep matching for 'mous' and 'mouse' too, since both those words contain 'mouse' as a prefix."},
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
        "diagram_svg": """<svg viewBox="0 0 300 200" width="300" height="200" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="16" font-size="11" fill="var(--text-2)">Before</text><text x="168" y="16" font-size="11" fill="var(--text-2)">After one step</text><rect x="6" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="26" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="90" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="68" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="6" y="110" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="48" y="110" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="90" y="110" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="6" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="168" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="210" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="252" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="168" y="68" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="210" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="252" y="68" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="168" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="210" y="110" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="252" y="110" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="168" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="210" y="152" width="40" height="40" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><rect x="252" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/></svg>""",
        "function_name": "gameOfLife",
        "params": [{"name": "board", "type": "vector<vector<int>>"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "def gameOfLife(board):\n    # your code here\n    pass\n",
            "cpp": "vector<vector<int>> gameOfLife(vector<vector<int>> board) {\n    // your code here\n    return board;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]], "expected": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
             "input_display": "board=[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]",
             "explanation": "Cell (0,1) starts alive but has only 1 live neighbor (diagonally down-right at (1,2)), so it dies of underpopulation. Cell (1,0) starts dead but has exactly 3 live neighbors -- (0,1), (2,0), and (2,1) -- so it comes alive. Cell (2,2) starts alive with 2 live neighbors, which is enough to survive unchanged."},
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
        "diagram_svg": """<svg viewBox="0 0 160 160" width="160" height="160" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="cyc-arrow" markerWidth="7" markerHeight="7" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="#f87171"/></marker></defs><path d="M70.0,42.0 Q58.0,68.5 70.0,95.0" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#cyc-arrow)" opacity="0.85"/><path d="M70.0,98.0 Q82.0,71.5 70.0,45.0" fill="none" stroke="#f87171" stroke-width="1.8" marker-end="url(#cyc-arrow)" opacity="0.85"/><circle cx="70.0" cy="24.0" r="18" fill="var(--bg-3)" stroke="#f87171" stroke-width="2"/><text x="70.0" y="29.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">0</text><circle cx="70.0" cy="116.0" r="18" fill="var(--bg-3)" stroke="#f87171" stroke-width="2"/><text x="70.0" y="121.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 372 104" width="372" height="104" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="39.0" y="26.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">practice</text><rect x="78" y="6" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="111.0" y="26.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">makes</text><rect x="150" y="6" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="183.0" y="26.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">perfect</text><rect x="222" y="6" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="255.0" y="26.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">coding</text><rect x="294" y="6" width="66" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="327.0" y="26.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)" font-weight="600">makes</text><line x1="39.0" y1="52" x2="255.0" y2="52" stroke="#6ee7b7" stroke-width="1.5"/><text x="147.0" y="66" text-anchor="middle" font-size="10" fill="#6ee7b7">"coding"-"practice" = 3</text><line x1="255.0" y1="78" x2="327.0" y2="78" stroke="#fdba74" stroke-width="1.5"/><text x="291.0" y="92" text-anchor="middle" font-size="10" fill="#fdba74">"makes"-"coding" = 1</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 292 76" width="292" height="76" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="14" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="23.0" y="36.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">4</text><rect x="46" y="14" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="63.0" y="36.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">5</text><rect x="86" y="14" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="103.0" y="36.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">6</text><rect x="126" y="14" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="143.0" y="36.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">7</text><rect x="166" y="14" width="34" height="34" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="183.0" y="36.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">0</text><rect x="206" y="14" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="223.0" y="36.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="246" y="14" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="263.0" y="36.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">2</text><line x1="163.0" y1="8" x2="163.0" y2="56" stroke="#f87171" stroke-width="1.5" stroke-dasharray="4,3"/><text x="163.0" y="68" text-anchor="middle" font-size="9.5" fill="#f87171">rotation point</text></svg>""",
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
        "description_md": """You're playing Snakes and Ladders on an `n x n` board, given as a 2D array where
`board[0]` is the *top* row and `board[n-1]` is the *bottom* row (matching how the board is normally drawn).

Squares are numbered 1 to n² starting at the **bottom-left** square, moving right across the bottom row, then
continuing on the row above it moving *left*, then right again on the row above that, and so on -- alternating
direction each row, snaking upward until it reaches n² at the top row. Each square holds `-1` (nothing
special) or a destination square number (the top of a ladder or the head of a snake).

Starting on square 1, each move advances you by 1 to 6 squares (like a die roll) to any square number from
`current + 1` up to `current + 6`, as long as that number doesn't exceed n². If the square you land on has a
ladder/snake destination (not `-1`), you immediately move to that destination instead -- and destinations are
never themselves another ladder/snake start, so there's no chaining.

Return the minimum number of moves to reach square n², or `-1` if it's not reachable.""",
        "diagram_svg": """<svg viewBox="0 0 264 264" width="264" height="264" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="arrow-up" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#6ee7b7"/></marker><marker id="arrow-down" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f87171"/></marker></defs><rect x="6" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="11" y="19" font-size="9" fill="var(--text-2)">36</text><rect x="48" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="53" y="19" font-size="9" fill="var(--text-2)">35</text><rect x="90" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="95" y="19" font-size="9" fill="var(--text-2)">34</text><rect x="132" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="137" y="19" font-size="9" fill="var(--text-2)">33</text><rect x="174" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="179" y="19" font-size="9" fill="var(--text-2)">32</text><rect x="216" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="221" y="19" font-size="9" fill="var(--text-2)">31</text><rect x="6" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="11" y="61" font-size="9" fill="var(--text-2)">25</text><rect x="48" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="53" y="61" font-size="9" fill="var(--text-2)">26</text><rect x="90" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="95" y="61" font-size="9" fill="var(--text-2)">27</text><rect x="132" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="137" y="61" font-size="9" fill="var(--text-2)">28</text><rect x="174" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="179" y="61" font-size="9" fill="var(--text-2)">29</text><rect x="216" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="221" y="61" font-size="9" fill="var(--text-2)">30</text><rect x="6" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="11" y="103" font-size="9" fill="var(--text-2)">24</text><rect x="48" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="53" y="103" font-size="9" fill="var(--text-2)">23</text><rect x="90" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="95" y="103" font-size="9" fill="var(--text-2)">22</text><rect x="132" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="137" y="103" font-size="9" fill="var(--text-2)">21</text><rect x="174" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="179" y="103" font-size="9" fill="var(--text-2)">20</text><rect x="216" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="221" y="103" font-size="9" fill="var(--text-2)">19</text><rect x="6" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="11" y="145" font-size="9" fill="var(--text-2)">13</text><rect x="48" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="53" y="145" font-size="9" fill="var(--text-2)">14</text><rect x="90" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="95" y="145" font-size="9" fill="var(--text-2)">15</text><rect x="132" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="137" y="145" font-size="9" fill="var(--text-2)">16</text><rect x="174" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="179" y="145" font-size="9" fill="var(--text-2)">17</text><rect x="216" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="221" y="145" font-size="9" fill="var(--text-2)">18</text><rect x="6" y="174" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="11" y="187" font-size="9" fill="var(--text-2)">12</text><rect x="48" y="174" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="53" y="187" font-size="9" fill="var(--text-2)">11</text><rect x="90" y="174" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="95" y="187" font-size="9" fill="var(--text-2)">10</text><rect x="132" y="174" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="137" y="187" font-size="9" fill="var(--text-2)">9</text><rect x="174" y="174" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="179" y="187" font-size="9" fill="var(--text-2)">8</text><rect x="216" y="174" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="221" y="187" font-size="9" fill="var(--text-2)">7</text><rect x="6" y="216" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="11" y="229" font-size="9" fill="var(--text-2)">1</text><rect x="48" y="216" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="53" y="229" font-size="9" fill="var(--text-2)">2</text><rect x="90" y="216" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="95" y="229" font-size="9" fill="var(--text-2)">3</text><rect x="132" y="216" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="137" y="229" font-size="9" fill="var(--text-2)">4</text><rect x="174" y="216" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="179" y="229" font-size="9" fill="var(--text-2)">5</text><rect x="216" y="216" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="221" y="229" font-size="9" fill="var(--text-2)">6</text><path d="M69.0,153.0 Q69.0,76.0 69.0,27.0" fill="none" stroke="#6ee7b7" stroke-width="2.5" marker-end="url(#arrow-up)" opacity="0.9"/><path d="M195.0,153.0 Q111.0,139.0 27.0,153.0" fill="none" stroke="#f87171" stroke-width="2.5" marker-end="url(#arrow-down)" opacity="0.9"/><path d="M69.0,237.0 Q90.0,181.0 111.0,153.0" fill="none" stroke="#6ee7b7" stroke-width="2.5" marker-end="url(#arrow-up)" opacity="0.9"/></svg>""",
        "function_name": "snakesAndLadders",
        "params": [{"name": "board", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "from collections import deque\ndef snakesAndLadders(board):\n    # your code here -- BFS over square numbers 1..n*n\n    pass\n",
            "cpp": "int snakesAndLadders(vector<vector<int>> board) {\n    // your code here -- BFS over square numbers 1..n*n\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[-1, -1], [-1, 3]]], "expected": 1, "input_display": "board=[[-1,-1],[-1,3]]",
             "explanation": "This is a 2x2 board, so squares are numbered 1-4: square 1 is bottom-left (board[1][0]), square 2 is bottom-right (board[1][1]), square 3 is top-right (board[0][1]) -- the row above reads right-to-left -- and square 4 is top-left (board[0][0]). From square 1, one die roll can reach square 4 directly, and board[0][0] is -1 (no ladder there), so you land on square 4 = n^2 in a single move."},
            {"inputs": [[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]],
             "expected": 4, "input_display": "board=[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]] (see diagram above)",
             "explanation": "One 4-move path: from square 1, roll to square 2 (a ladder straight up to 15). From 15, roll to square 17 (a snake down to 13). From 13, roll to square 14 (a ladder up to 35). From 35, roll to square 36 = n^2 and you're done -- 4 moves, matching the two green (ladder) and one red (snake) arrow in the diagram above."},
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
        "diagram_svg": """<svg viewBox="0 0 480 216" width="480" height="216" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="dup-arrow" markerWidth="7" markerHeight="7" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="var(--text-2)"/></marker></defs><line x1="124.56230589874906" y1="33.58013454126451" x2="161.48671229137716" y2="60.407286106861854" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dup-arrow)" opacity="0.85"/><line x1="163.913763274502" y1="83.3309109462683" x2="84.66881871681585" y2="140.90573329685427" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dup-arrow)" opacity="0.85"/><line x1="137.758232266309" y1="142.66908905373168" x2="58.51328770862283" y2="85.09426670314572" stroke="var(--text-2)" stroke-width="1.5" marker-end="url(#dup-arrow)" opacity="0.85"/><line x1="85.67946183494195" y1="153.2492235949962" x2="131.32053816505805" y2="153.2492235949962" stroke="#f87171" stroke-width="1.5" marker-end="url(#dup-arrow)" opacity="0.85"/><line x1="56.08623672549799" y1="83.3309109462683" x2="135.33118128318415" y2="140.90573329685427" stroke="#f87171" stroke-width="1.5" marker-end="url(#dup-arrow)" opacity="0.85"/><circle cx="110.0" cy="23.0" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="110.0" y="28.0" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">0</text><circle cx="178.47606917325106" cy="72.75077640500379" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="178.47606917325106" y="77.75077640500379" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">1</text><circle cx="152.32053816505805" cy="153.2492235949962" r="18" fill="var(--bg-3)" stroke="#f87171" stroke-width="2"/><text x="152.32053816505805" y="158.2492235949962" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">2</text><circle cx="67.67946183494195" cy="153.2492235949962" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="67.67946183494195" y="158.2492235949962" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">3</text><circle cx="41.52393082674894" cy="72.75077640500379" r="18" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="41.52393082674894" y="77.75077640500379" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">4</text><text x="10" y="212" font-size="10.5" fill="#f87171">indices 3 and 4 both point to 2 -- that's the cycle entry, the duplicate</text></svg>""",
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
        "description_md": """You're implementing a key-value store where every value is stored with a
timestamp, so you can ask "what was this key's value at (or just before) time T?"

You're given a list of `operations` to apply in order, where each one is one of:
- `["set", key, value, timestamp]` -- store `value` for `key` at the given `timestamp`. For any single key,
  the timestamps across its `set` calls only ever increase (never out of order).
- `["get", key, timestamp]` -- look up `key`'s value as of that `timestamp`: specifically, the value from the
  most recent `set` for that key whose timestamp is `<= timestamp`. If no such `set` exists yet (either the
  key was never set, or every `set` for it happened after this timestamp), the answer is `""`.

Return the results of every `get`, in the order they appear in `operations` (a `set` doesn't produce an
output).""",
        "diagram_svg": """<svg viewBox="0 0 372.6 126" width="372.6" height="126" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="36.3" y1="60" x2="336.3" y2="60" stroke="var(--line)" stroke-width="1.5"/><circle cx="46.3" cy="60" r="5" fill="#6ee7b7" stroke="var(--bg-0)" stroke-width="1.5"/><text x="46.3" y="48" text-anchor="middle" font-size="10" fill="#6ee7b7">set "bar" @1</text><circle cx="256.3" cy="60" r="5" fill="#6ee7b7" stroke="var(--bg-0)" stroke-width="1.5"/><text x="256.3" y="48" text-anchor="middle" font-size="10" fill="#6ee7b7">set "bar2" @4</text><line x1="46.3" y1="68" x2="46.3" y2="90" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="3,2"/><text x="46.3" y="102" text-anchor="middle" font-size="10" fill="#93c5fd">get@1</text><text x="46.3" y="118" text-anchor="middle" font-size="10" fill="#93c5fd" font-weight="700">-&gt; "bar"</text><line x1="186.3" y1="68" x2="186.3" y2="90" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="3,2"/><text x="186.3" y="102" text-anchor="middle" font-size="10" fill="#93c5fd">get@3</text><text x="186.3" y="118" text-anchor="middle" font-size="10" fill="#93c5fd" font-weight="700">-&gt; "bar"</text><line x1="256.3" y1="68" x2="256.3" y2="90" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="3,2"/><text x="256.3" y="102" text-anchor="middle" font-size="10" fill="#93c5fd">get@4</text><text x="256.3" y="118" text-anchor="middle" font-size="10" fill="#93c5fd" font-weight="700">-&gt; "bar2"</text><line x1="326.3" y1="68" x2="326.3" y2="90" stroke="#93c5fd" stroke-width="1.5" stroke-dasharray="3,2"/><text x="326.3" y="102" text-anchor="middle" font-size="10" fill="#93c5fd">get@5</text><text x="326.3" y="118" text-anchor="middle" font-size="10" fill="#93c5fd" font-weight="700">-&gt; "bar2"</text></svg>""",
        "function_name": "timeMapOperations",
        "params": [{"name": "operations", "type": "vector<vector<string>>"}],
        "return_type": "vector<string>",
        "starter_code": {
            "python": "def timeMapOperations(operations):\n    # your code here -- store (timestamp, value) per key, binary search on get\n    pass\n",
            "cpp": "vector<string> timeMapOperations(vector<vector<string>> operations) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[["set", "foo", "bar", "1"], ["get", "foo", "1"], ["get", "foo", "3"], ["set", "foo", "bar2", "4"], ["get", "foo", "4"], ["get", "foo", "5"]]],
             "expected": ["bar", "bar", "bar2", "bar2"], "input_display": "operations=[set foo bar @1, get foo @1, get foo @3, set foo bar2 @4, get foo @4, get foo @5]",
             "explanation": "After 'set foo=bar @1', both 'get foo @1' and 'get foo @3' return 'bar' -- timestamp 1 is still the most recent set at or before either of those times. Once 'set foo=bar2 @4' happens, 'get foo @4' and 'get foo @5' both switch to 'bar2', since @4 is now the most recent set at or before both query times."},
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
        "diagram_svg": """<svg viewBox="0 0 138 138" width="138" height="138" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="#60a5fa" fill-opacity="0.85" stroke="#60a5fa" stroke-width="1.5"/><text x="26.0" y="25.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">1</text><text x="26.0" y="39.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#1</text><rect x="48" y="6" width="40" height="40" rx="4" fill="#74a7e5" fill-opacity="0.85" stroke="#74a7e5" stroke-width="1.5"/><text x="68.0" y="25.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">2</text><text x="68.0" y="39.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#2</text><rect x="90" y="6" width="40" height="40" rx="4" fill="#88a9d0" fill-opacity="0.85" stroke="#88a9d0" stroke-width="1.5"/><text x="110.0" y="25.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">3</text><text x="110.0" y="39.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#3</text><rect x="6" y="48" width="40" height="40" rx="4" fill="#ebb269" fill-opacity="0.85" stroke="#ebb269" stroke-width="1.5"/><text x="26.0" y="67.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">4</text><text x="26.0" y="81.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#8</text><rect x="48" y="48" width="40" height="40" rx="4" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="68.0" y="67.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">5</text><text x="68.0" y="81.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#9</text><rect x="90" y="48" width="40" height="40" rx="4" fill="#9cabbc" fill-opacity="0.85" stroke="#9cabbc" stroke-width="1.5"/><text x="110.0" y="67.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">6</text><text x="110.0" y="81.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#4</text><rect x="6" y="90" width="40" height="40" rx="4" fill="#d7b07e" fill-opacity="0.85" stroke="#d7b07e" stroke-width="1.5"/><text x="26.0" y="109.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">7</text><text x="26.0" y="123.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#7</text><rect x="48" y="90" width="40" height="40" rx="4" fill="#c3ae92" fill-opacity="0.85" stroke="#c3ae92" stroke-width="1.5"/><text x="68.0" y="109.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">8</text><text x="68.0" y="123.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#6</text><rect x="90" y="90" width="40" height="40" rx="4" fill="#b0aca7" fill-opacity="0.85" stroke="#b0aca7" stroke-width="1.5"/><text x="110.0" y="109.0" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">9</text><text x="110.0" y="123.0" text-anchor="middle" font-size="8.5" fill="#0a0a0a">#5</text></svg>""",
        "function_name": "spiralOrder",
        "params": [{"name": "matrix", "type": "vector<vector<int>>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def spiralOrder(matrix):\n    # your code here\n    pass\n",
            "cpp": "vector<int> spiralOrder(vector<vector<int>> matrix) {\n    // your code here\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5], "input_display": "matrix=[[1,2,3],[4,5,6],[7,8,9]]",
             "explanation": "Across the top row (1, 2, 3), down the right column (6, 9), back across the bottom row right-to-left (8, 7), up the left column (4), then the one cell left in the center (5)."},
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
        "diagram_svg": """<svg viewBox="0 0 460 226" width="460" height="226" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="14" font-size="11" fill="var(--text-2)">Target: [0, 10]</text><rect x="6.0" y="20" width="448.0" height="8" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1"/><rect x="6.0" y="40" width="89.60000000000001" height="22" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="50.800000000000004" y="53.0" text-anchor="middle" font-size="10.5" fill="#0a0a0a" font-weight="600">[0,2]</text><rect x="185.20000000000002" y="70" width="89.6" height="22" rx="4" fill="var(--bg-3)" fill-opacity="0.85" stroke="var(--line)" stroke-width="1.5"/><text x="230.0" y="83.0" text-anchor="middle" font-size="10.5" fill="var(--text-2)" font-weight="600">[4,6]</text><rect x="364.40000000000003" y="100" width="89.59999999999997" height="22" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="409.20000000000005" y="113.0" text-anchor="middle" font-size="10.5" fill="#0a0a0a" font-weight="600">[8,10]</text><rect x="50.800000000000004" y="130" width="358.4" height="22" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="230.0" y="143.0" text-anchor="middle" font-size="10.5" fill="#0a0a0a" font-weight="600">[1,9]</text><rect x="50.800000000000004" y="160" width="179.2" height="22" rx="4" fill="var(--bg-3)" fill-opacity="0.85" stroke="var(--line)" stroke-width="1.5"/><text x="140.4" y="173.0" text-anchor="middle" font-size="10.5" fill="var(--text-2)" font-weight="600">[1,5]</text><rect x="230.0" y="190" width="179.2" height="22" rx="4" fill="var(--bg-3)" fill-opacity="0.85" stroke="var(--line)" stroke-width="1.5"/><text x="319.6" y="203.0" text-anchor="middle" font-size="10.5" fill="var(--text-2)" font-weight="600">[5,9]</text></svg>""",
        "function_name": "videoStitching",
        "params": [{"name": "clips", "type": "vector<vector<int>>"}, {"name": "time", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def videoStitching(clips, time):\n    # your code here -- greedy interval covering\n    pass\n",
            "cpp": "int videoStitching(vector<vector<int>> clips, int time) {\n    // your code here -- greedy interval covering\n    return -1;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10], "expected": 3, "input_display": "clips=[...], time=10",
             "explanation": "One way to cover [0,10] with 3 clips: [0,2] covers the start, [1,9] extends coverage all the way to 9, and [8,10] (overlapping [1,9] at 8-9) extends the last bit to 10. No pair of clips can bridge the full span, so 3 is the minimum."},
            {"inputs": [[[0, 1], [1, 2]], 5], "expected": -1, "input_display": "clips=[[0,1],[1,2]], time=5",
             "explanation": "The available clips only ever cover up to time 2, but [0,time]=[0,5] needs coverage all the way to 5. There's a gap from 2 to 5 that no clip fills, so it's impossible."},
            {"inputs": [[[0, 5]], 5], "expected": 1, "hidden": True},
        ],
    },
    {
        "id": "minesweeper_reveal",
        "title": "Minesweeper Reveal",
        "difficulty": "Medium",
        "topic": "Arrays / DFS-BFS",
        "tags": ["array", "dfs", "bfs", "matrix"],
        "description_md": """You're given a Minesweeper `board` where every cell is either `'M'` (an
unrevealed mine) or `'E'` (unrevealed and safe), and a single `click = [row, col]` on a cell that's guaranteed
to currently be `'E'`. Simulate what happens after that one click:

- If the clicked cell has **no mines** among its up-to-8 neighbors (horizontally, vertically, and diagonally
  adjacent), reveal it as `'B'`, then automatically "click" every one of its neighbors too, applying these
  same rules to each -- this is what causes a click on an empty area to reveal a whole open region at once.
- If the clicked cell **does** have at least one adjacent mine, just reveal it as that count, e.g. `'3'` --
  and don't chain-reveal its neighbors.

(This function is only ever asked to click on a safe `'E'` cell, so you don't need to handle clicking directly
on a mine.) Return the board after the click and any resulting chain reveals.""",
        "diagram_svg": """<svg viewBox="0 0 468 200" width="468" height="200" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="16" font-size="11" fill="var(--text-2)">Before</text><text x="252" y="16" font-size="11" fill="var(--text-2)">After click</text><rect x="6" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="132" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="174" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="110.0" y="94.0" text-anchor="middle" font-size="13" fill="var(--text-2)" font-weight="600">?</text><rect x="132" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="174" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="132" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="174" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="152" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="1.5"/><text x="26.0" y="178.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">click</text><rect x="48" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="90" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="132" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="174" y="152" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="252" y="26" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="294" y="26" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="314.0" y="52.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="336" y="26" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="378" y="26" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="398.0" y="52.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="420" y="26" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="252" y="68" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="294" y="68" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="314.0" y="94.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="336" y="68" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><text x="356.0" y="94.0" text-anchor="middle" font-size="13" fill="#fca5a5" font-weight="600">M</text><rect x="378" y="68" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="398.0" y="94.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="420" y="68" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="252" y="110" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="294" y="110" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="314.0" y="136.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="336" y="110" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="356.0" y="136.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="378" y="110" width="40" height="40" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="398.0" y="136.0" text-anchor="middle" font-size="13" fill="var(--amber)" font-weight="600">1</text><rect x="420" y="110" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="252" y="152" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="294" y="152" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="336" y="152" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="378" y="152" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/><rect x="420" y="152" width="40" height="40" rx="4" fill="#1e2b22" stroke="#2f5c43" stroke-width="1.5"/></svg>""",
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
             "input_display": "4x5 board with one mine, click=[3,0]",
             "explanation": "Clicking [3,0] has zero adjacent mines, so it reveals as 'B' and the flood-fill spreads to every neighbor, and keeps spreading through any neighbor that *also* has zero adjacent mines. It stops the instant it hits a cell with a nonzero count -- that cell reveals its count but does not pass the reveal along to its own neighbors. That's why [0][2] is left completely untouched ('E'): all four of its neighbors ([0][1], [0][3], [1][1], [1][3]) have exactly one adjacent mine each, so none of them are zero-count cells that would have flood-filled onward to reach it. The mine at [1,2] itself stays 'M' since the flood-fill never clicks directly on a mine."},
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
        "diagram_svg": """<svg viewBox="0 0 383 202" width="383" height="202" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="48" y="6" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="90" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="132" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="174" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="6" y="48" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="48" y="48" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="90" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="132" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="174" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="6" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="48" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="90" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="132" y="90" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="174" y="90" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="6" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="48" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="90" y="132" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><rect x="132" y="132" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><rect x="174" y="132" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="6" y="196" font-size="10.5" fill="var(--text-2)">1 distinct shape(s) -- matching colors are the same shape</text></svg>""",
        "function_name": "numDistinctIslands",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def numDistinctIslands(grid):\n    # your code here -- DFS recording each cell's offset from the island's start cell\n    pass\n",
            "cpp": "int numDistinctIslands(vector<vector<int>> grid) {\n    // your code here -- DFS recording each cell's offset from the island's start cell\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]], "expected": 1,
             "input_display": "grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]",
             "explanation": "There are two separate 2x2 island blobs -- one at the top-left, one at the bottom-right -- but they're the exact same shape (a 2x2 square), just shifted to a different position. Since only the shape matters, not the location, they count as 1 distinct shape."},
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
        "diagram_svg": """<svg viewBox="0 0 300 158" width="300" height="158" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="16" font-size="11" fill="var(--text-2)">Start</text><text x="168" y="16" font-size="11" fill="var(--text-2)">4 minutes later</text><rect x="6" y="26" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="48" y="26" width="40" height="40" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><rect x="90" y="26" width="40" height="40" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><rect x="6" y="68" width="40" height="40" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><rect x="48" y="68" width="40" height="40" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><rect x="90" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="6" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="48" y="110" width="40" height="40" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><rect x="90" y="110" width="40" height="40" rx="4" fill="#fdba74" stroke="#fdba74" stroke-width="1.5"/><rect x="168" y="26" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="210" y="26" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="252" y="26" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="168" y="68" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="210" y="68" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="252" y="68" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="168" y="110" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><rect x="210" y="110" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/><rect x="252" y="110" width="40" height="40" rx="4" fill="#7f1d1d" stroke="#f87171" stroke-width="1.5"/></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 420 144" width="420" height="144" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6.0" y="14" width="408.0" height="22" rx="5" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="210.0" y="30.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[0,30]</text><rect x="74.0" y="48" width="68.0" height="22" rx="5" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="108.0" y="64.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[5,10]</text><rect x="210.0" y="82" width="68.0" height="22" rx="5" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="244.0" y="98.0" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">[15,20]</text><line x1="74.0" y1="8" x2="74.0" y2="116" stroke="#f87171" stroke-width="1.5" stroke-dasharray="4,3"/><text x="74.0" y="132" text-anchor="middle" font-size="10.5" fill="#f87171">2 overlapping @ t=5</text></svg>""",
        "function_name": "minMeetingRooms",
        "params": [{"name": "intervals", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def minMeetingRooms(intervals):\n    # your code here -- sort starts and ends separately, sweep\n    pass\n",
            "cpp": "int minMeetingRooms(vector<vector<int>> intervals) {\n    // your code here -- sort starts and ends separately, sweep\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[0, 30], [5, 10], [15, 20]]], "expected": 2, "input_display": "intervals=[[0,30],[5,10],[15,20]]",
             "explanation": "[5,10] and [15,20] never overlap each other, but [0,30] spans the entire time range and overlaps both of them individually. At any moment during [5,10] (or during [15,20]), both that meeting and [0,30] are in progress, so 2 rooms are needed at once -- but never 3, since [5,10] and [15,20] don't overlap each other."},
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
        "diagram_svg": """<svg viewBox="0 0 376.06 124" width="376.06" height="124" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="39.01" y="78" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><rect x="39.01" y="60" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><rect x="39.01" y="42" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><text x="62.01" y="106" text-anchor="middle" font-size="10.5" fill="var(--text-1)">level 2</text><text x="62.01" y="118" text-anchor="middle" font-size="9" fill="var(--text-2)">3 tasks, 1 round(s)</text><rect x="165.02999999999997" y="78" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><rect x="165.02999999999997" y="60" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><text x="188.02999999999997" y="106" text-anchor="middle" font-size="10.5" fill="var(--text-1)">level 3</text><text x="188.02999999999997" y="118" text-anchor="middle" font-size="9" fill="var(--text-2)">2 tasks, 1 round(s)</text><rect x="291.04999999999995" y="78" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><rect x="291.04999999999995" y="60" width="46" height="16" rx="2" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1"/><rect x="291.04999999999995" y="42" width="46" height="16" rx="2" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1"/><rect x="291.04999999999995" y="24" width="46" height="16" rx="2" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1"/><text x="314.04999999999995" y="106" text-anchor="middle" font-size="10.5" fill="var(--text-1)">level 4</text><text x="314.04999999999995" y="118" text-anchor="middle" font-size="9" fill="var(--text-2)">4 tasks, 2 round(s)</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 194 162" width="194" height="162" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="133.0" y1="20" x2="65.0" y2="66" stroke="var(--line)" stroke-width="2"/><line x1="65.0" y1="66" x2="31.0" y2="112" stroke="var(--line)" stroke-width="2"/><line x1="65.0" y1="66" x2="99.0" y2="112" stroke="var(--line)" stroke-width="2"/><line x1="133.0" y1="20" x2="167.0" y2="66" stroke="var(--line)" stroke-width="2"/><circle cx="133.0" cy="20" r="15" fill="var(--bg-3)" stroke="#ffb454" stroke-width="2"/><text x="133.0" y="24" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="700">*</text><circle cx="65.0" cy="66" r="15" fill="var(--bg-3)" stroke="#ffb454" stroke-width="2"/><text x="65.0" y="70" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="700">+</text><circle cx="31.0" cy="112" r="15" fill="var(--bg-3)" stroke="#6ee7b7" stroke-width="2"/><text x="31.0" y="116" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="700">2</text><circle cx="99.0" cy="112" r="15" fill="var(--bg-3)" stroke="#6ee7b7" stroke-width="2"/><text x="99.0" y="116" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="700">1</text><circle cx="167.0" cy="66" r="15" fill="var(--bg-3)" stroke="#6ee7b7" stroke-width="2"/><text x="167.0" y="70" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="700">3</text></svg>""",
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
        "diagram_svg": """<svg viewBox="0 0 96 96" width="96" height="96" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="26.0" y="32.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text><rect x="48" y="6" width="40" height="40" rx="4" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="68.0" y="32.0" text-anchor="middle" font-size="10" fill="#0a0a0a" font-weight="600">0&#8594;1</text><rect x="6" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" fill-opacity="0.85" stroke="var(--line)" stroke-width="1.5"/><text x="26.0" y="74.0" text-anchor="middle" font-size="14" fill="var(--text-2)" font-weight="600">0</text><rect x="48" y="48" width="40" height="40" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="68.0" y="74.0" text-anchor="middle" font-size="14" fill="#0a0a0a" font-weight="600">1</text></svg>""",
        "function_name": "largestIsland",
        "params": [{"name": "grid", "type": "vector<vector<int>>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def largestIsland(grid):\n    # your code here -- label each island with its size, then try flipping each 0\n    pass\n",
            "cpp": "int largestIsland(vector<vector<int>> grid) {\n    // your code here -- label each island with its size, then try flipping each 0\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 0], [0, 1]]], "expected": 3, "input_display": "grid=[[1,0],[0,1]]",
             "explanation": "The two 1's at (0,0) and (1,1) aren't connected -- they only touch diagonally, which doesn't count. Flipping the 0 at (0,1) works because it's adjacent to (0,0) in its row AND to (1,1) in its column, joining all three cells into a single island of size 3. (Flipping (1,0) instead gives the same result by symmetry.)"},
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
        "diagram_svg": """<svg viewBox="0 0 212 90" width="212" height="90" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="7" y="10" width="58" height="24" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="36.0" y="26" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">cat</text><rect x="67" y="10" width="78" height="24" rx="4" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="106.0" y="26" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">sand</text><rect x="147" y="10" width="58" height="24" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="176.0" y="26" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">dog</text><rect x="7" y="50" width="78" height="24" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="46.0" y="66" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">cats</text><rect x="87" y="50" width="58" height="24" rx="4" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="116.0" y="66" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">and</text><rect x="147" y="50" width="58" height="24" rx="4" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="176.0" y="66" text-anchor="middle" font-size="11" fill="#0a0a0a" font-weight="600">dog</text></svg>""",
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
             "input_display": 's="catsanddog", wordDict=["cat","cats","and","sand","dog"]',
             "explanation": "'catsanddog' can be fully broken into dictionary words two different ways: 'cat' + 'sand' + 'dog', or 'cats' + 'and' + 'dog'. Both use only words from wordDict and together account for every character in s, so both are valid sentences."},
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
        "diagram_svg": """<svg viewBox="0 0 264 96" width="264" height="96" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="14" font-size="10" fill="var(--text-2)">insert 1</text><text x="6" y="40" font-size="12" fill="var(--text-0)" font-family="SF Mono, Consolas, monospace">[1]</text><text x="6" y="64" font-size="10.5" fill="#ffb454">2 &#215; median = 2</text><text x="90" y="14" font-size="10" fill="var(--text-2)">insert 2</text><text x="90" y="40" font-size="12" fill="var(--text-0)" font-family="SF Mono, Consolas, monospace">[1 2]</text><text x="90" y="64" font-size="10.5" fill="#ffb454">2 &#215; median = 3</text><text x="174" y="14" font-size="10" fill="var(--text-2)">insert 3</text><text x="174" y="40" font-size="12" fill="var(--text-0)" font-family="SF Mono, Consolas, monospace">[1 2 3]</text><text x="174" y="64" font-size="10.5" fill="#ffb454">2 &#215; median = 4</text></svg>""",
        "function_name": "medianStreamDoubled",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "import heapq\ndef medianStreamDoubled(nums):\n    # your code here -- two heaps, return 2*median after each insertion\n    pass\n",
            "cpp": "vector<int> medianStreamDoubled(vector<int> nums) {\n    // your code here -- two heaps (priority_queue), return 2*median after each insertion\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3]], "expected": [2, 3, 4], "input_display": "nums=[1,2,3] (insert one at a time)",
             "explanation": "After inserting just 1, the median is 1, so 2*median = 2. After inserting 1 and 2, the numbers seen so far are {1,2} and the median of an even-sized set is the average of the two middle values: (1+2)/2 = 1.5, so 2*median = 3. After inserting 1, 2, and 3, the median of {1,2,3} is the middle value 2, so 2*median = 4."},
            {"inputs": [[2, 1, 5, 7, 2, 0, 5]], "expected": [4, 3, 4, 7, 4, 4, 4], "hidden": True},
            {"inputs": [[5]], "expected": [10], "hidden": True},
        ],
    },

    # ---- added from the LeetCode practice-list screenshot ----

    {
        "id": "take_gifts_richest_pile",
        "title": "Take Gifts From the Richest Pile",
        "difficulty": "Easy",
        "topic": "Array / Heap",
        "tags": ["array", "heap"],
        "description_md": """You're given an array `gifts` of pile sizes. In one operation, take the pile with
the most gifts and replace it with `floor(sqrt(pile))` gifts remaining. Do this `k` times, then return the
total number of gifts remaining across all piles.""",
        "diagram_svg": """<svg viewBox="0 0 428 158" width="428" height="158" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="12" font-size="10.5" fill="var(--text-2)">Before -> after one operation (max pile replaced by floor(sqrt))</text><rect x="6" y="95.5" width="34" height="22.5" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="1.5"/><text x="23.0" y="89.5" text-anchor="middle" font-size="10.5" fill="var(--text-1)">25</text><rect x="48" y="60.4" width="34" height="57.6" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="1.5"/><text x="65.0" y="54.4" text-anchor="middle" font-size="10.5" fill="var(--text-1)">64</text><rect x="90" y="109.9" width="34" height="8.1" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="1.5"/><text x="107.0" y="103.9" text-anchor="middle" font-size="10.5" fill="var(--text-1)">9</text><rect x="132" y="114.4" width="34" height="3.6" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="1.5"/><text x="149.0" y="108.4" text-anchor="middle" font-size="10.5" fill="var(--text-1)">4</text><rect x="174" y="28.0" width="34" height="90.0" fill="none" stroke="var(--text-2)" stroke-width="1.5" stroke-dasharray="4,3"/><text x="191.0" y="22.0" text-anchor="middle" font-size="10.5" fill="var(--text-1)">100</text><rect x="174" y="109.0" width="34" height="9.0" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="191.0" y="132" text-anchor="middle" font-size="10.5" fill="#ffb454" font-weight="700">&#8595; 10</text></svg>""",
        "function_name": "pickGifts",
        "params": [{"name": "gifts", "type": "vector<int>"}, {"name": "k", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def pickGifts(gifts, k):\n    # your code here -- repeatedly replace the max pile with its floor(sqrt)\n    pass\n",
            "cpp": "int pickGifts(vector<int> gifts, int k) {\n    // your code here -- repeatedly replace the max pile with its floor(sqrt)\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[25, 64, 9, 4, 100], 4], "expected": 29, "input_display": "gifts=[25,64,9,4,100], k=4"},
            {"inputs": [[1, 1, 1, 1], 4], "expected": 4, "input_display": "gifts=[1,1,1,1], k=4"},
            {"inputs": [[1], 1000000000], "expected": 1, "hidden": True},
            {"inputs": [[2, 4, 8, 16], 1], "expected": 18, "hidden": True},
        ],
    },
    {
        "id": "can_place_flowers",
        "title": "Can Place Flowers",
        "difficulty": "Easy",
        "topic": "Array / Greedy",
        "tags": ["array", "greedy"],
        "description_md": """You have a long flowerbed `flowerbed` where `0` is empty and `1` already has a
flower planted; flowers can't be planted in adjacent plots. Given an integer `n`, return whether `n` new
flowers can be planted without violating the no-adjacent rule.""",
        "diagram_svg": """<svg viewBox="0 0 212 54" width="212" height="54" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="12" width="34" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="23.0" y="33.0" text-anchor="middle" font-size="15" fill="#0a0a0a" font-weight="600">&#10047;</text><rect x="46" y="12" width="34" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="63.0" y="33.0" text-anchor="middle" font-size="15" fill="var(--text-2)" font-weight="600"></text><rect x="86" y="12" width="34" height="32" rx="4" fill="#f0abfc" stroke="#f0abfc" stroke-width="1.5"/><text x="103.0" y="33.0" text-anchor="middle" font-size="15" fill="#0a0a0a" font-weight="600">&#10047;</text><rect x="126" y="12" width="34" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="143.0" y="33.0" text-anchor="middle" font-size="15" fill="var(--text-2)" font-weight="600"></text><rect x="166" y="12" width="34" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="183.0" y="33.0" text-anchor="middle" font-size="15" fill="#0a0a0a" font-weight="600">&#10047;</text></svg>""",
        "function_name": "canPlaceFlowers",
        "params": [{"name": "flowerbed", "type": "vector<int>"}, {"name": "n", "type": "int"}],
        "return_type": "bool",
        "starter_code": {
            "python": "def canPlaceFlowers(flowerbed, n):\n    # your code here\n    pass\n",
            "cpp": "bool canPlaceFlowers(vector<int> flowerbed, int n) {\n    // your code here\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 0, 0, 0, 1], 1], "expected": True, "input_display": "flowerbed=[1,0,0,0,1], n=1"},
            {"inputs": [[1, 0, 0, 0, 1], 2], "expected": False, "input_display": "flowerbed=[1,0,0,0,1], n=2"},
            {"inputs": [[0, 0, 1, 0, 0], 1], "expected": True, "hidden": True},
            {"inputs": [[0], 1], "expected": True, "hidden": True},
        ],
    },
    {
        "id": "zero_array_transformation_i",
        "title": "Zero Array Transformation I",
        "difficulty": "Medium",
        "topic": "Array / Prefix Sum",
        "tags": ["array", "prefix-sum", "difference-array"],
        "description_md": """You're given an integer array `nums` and a list of `queries`, where each
`queries[i] = [li, ri]` describes an index range.

Process the queries **in order**. For each query, you may choose *any subset* of the indices in `[li, ri]`
(including none of them, or all of them) and decrement each chosen index by 1. You don't have to pick the
same indices every time -- each query is an independent choice, limited only to that query's range.

Return `true` if there's some way to make these choices, across all the queries, that leaves `nums` entirely
zero by the end. Return `false` if no sequence of choices can do it.""",
        "diagram_svg": """<svg viewBox="0 0 180 118" width="180" height="118" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="48" y="6" width="120" height="12" rx="3" fill="#93c5fd" fill-opacity="0.3" stroke="#93c5fd" stroke-width="1"/><rect x="6" y="22" width="120" height="12" rx="3" fill="#93c5fd" fill-opacity="0.3" stroke="#93c5fd" stroke-width="1"/><rect x="6" y="48" width="36" height="32" rx="4" fill="#f87171" stroke="#f87171" stroke-width="1.5"/><text x="24.0" y="69.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">4</text><text x="24.0" y="94" text-anchor="middle" font-size="9.5" fill="var(--text-2)">cov 1</text><rect x="48" y="48" width="36" height="32" rx="4" fill="#f87171" stroke="#f87171" stroke-width="1.5"/><text x="66.0" y="69.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">3</text><text x="66.0" y="94" text-anchor="middle" font-size="9.5" fill="var(--text-2)">cov 2</text><rect x="90" y="48" width="36" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="108.0" y="69.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">2</text><text x="108.0" y="94" text-anchor="middle" font-size="9.5" fill="var(--text-2)">cov 2</text><rect x="132" y="48" width="36" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="150.0" y="69.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><text x="150.0" y="94" text-anchor="middle" font-size="9.5" fill="var(--text-2)">cov 1</text></svg>""",
        "function_name": "isZeroArray",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "queries", "type": "vector<vector<int>>"}],
        "return_type": "bool",
        "starter_code": {
            "python": "def isZeroArray(nums, queries):\n    # your code here -- difference array of query coverage counts\n    pass\n",
            "cpp": "bool isZeroArray(vector<int> nums, vector<vector<int>> queries) {\n    // your code here -- difference array of query coverage counts\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 0, 1], [[0, 2]]], "expected": True, "input_display": "nums=[1,0,1], queries=[[0,2]]",
             "explanation": "The single query [0,2] covers every index. Choose to decrement indices 0 and 2 (but not 1), giving [0,0,0]."},
            {"inputs": [[4, 3, 2, 1], [[1, 3], [0, 2]]], "expected": False, "input_display": "nums=[4,3,2,1], queries=[[1,3],[0,2]]",
             "explanation": "Index 0 is only ever inside one query's range ([0,2]), so it can be decremented at most once total across both queries -- but nums[0]=4 would need to be decremented four times. No sequence of choices can catch it up."},
            {"inputs": [[0, 0, 0], []], "expected": True, "hidden": True},
            {"inputs": [[5], [[0, 0]]], "expected": False, "hidden": True},
        ],
    },
    {
        "id": "squares_of_sorted_array",
        "title": "Squares of a Sorted Array",
        "difficulty": "Easy",
        "topic": "Array / Two Pointers",
        "tags": ["array", "two-pointers"],
        "description_md": """Given an integer array `nums` sorted in non-decreasing order, return an array of
the squares of each number, also sorted in non-decreasing order.

**Follow-up they'll ask:** can you do it in O(n) instead of sorting the squared array?""",
        "diagram_svg": """<svg viewBox="0 0 202 116" width="202" height="116" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="12" font-size="10.5" fill="var(--text-2)">nums (sorted)</text><rect x="6" y="22" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="22.0" y="42.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">-4</text><rect x="44" y="22" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="60.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">-1</text><rect x="82" y="22" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="98.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">0</text><rect x="120" y="22" width="32" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="136.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">3</text><rect x="158" y="22" width="32" height="30" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="174.0" y="42.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">10</text><text x="6" y="68" font-size="10.5" fill="var(--text-2)">squares, in result order (two pointers pick the larger |value| each step)</text><rect x="6" y="76" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="22.0" y="96.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">0</text><rect x="44" y="76" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="60.0" y="96.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="82" y="76" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="98.0" y="96.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">9</text><rect x="120" y="76" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="136.0" y="96.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">16</text><rect x="158" y="76" width="32" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="174.0" y="96.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">100</text></svg>""",
        "function_name": "sortedSquares",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def sortedSquares(nums):\n    # your code here -- two pointers from both ends\n    pass\n",
            "cpp": "vector<int> sortedSquares(vector<int> nums) {\n    // your code here -- two pointers from both ends\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[-4, -1, 0, 3, 10]], "expected": [0, 1, 9, 16, 100], "input_display": "nums=[-4,-1,0,3,10]"},
            {"inputs": [[-7, -3, 2, 3, 11]], "expected": [4, 9, 9, 49, 121], "input_display": "nums=[-7,-3,2,3,11]"},
            {"inputs": [[-5, -3, -2, -1]], "expected": [1, 4, 9, 25], "hidden": True},
            {"inputs": [[0]], "expected": [0], "hidden": True},
        ],
    },
    {
        "id": "expression_add_operators",
        "title": "Expression Add Operators",
        "difficulty": "Hard",
        "topic": "Math / Backtracking",
        "tags": ["math", "string", "backtracking"],
        "description_md": """Given a string `num` containing only digits and an integer `target`, return all
ways to insert the binary operators `+`, `-`, and `*` (not unary) between the digits so the resulting
expression evaluates to `target`. Numbers in the expression can't have leading zeros unless the number itself
is `0`. Return the expressions in any order (grading here ignores order).""",
        "diagram_svg": """<svg viewBox="0 0 168 94" width="168" height="94" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="14" font-size="10.5" fill="var(--text-2)">digits "123" -> target 6</text><rect x="6" y="24" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="41" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">1</text><text x="27.5" y="42" text-anchor="middle" font-size="13" fill="#ffb454" font-weight="700">+</text><rect x="33" y="24" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="45.0" y="41" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">2</text><text x="54.5" y="42" text-anchor="middle" font-size="13" fill="#ffb454" font-weight="700">+</text><rect x="60" y="24" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="72.0" y="41" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">3</text><text x="95" y="42" font-size="11" fill="var(--text-2)">= 6</text><rect x="6" y="58" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="75" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">1</text><text x="27.5" y="76" text-anchor="middle" font-size="13" fill="#ffb454" font-weight="700">*</text><rect x="33" y="58" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="45.0" y="75" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">2</text><text x="54.5" y="76" text-anchor="middle" font-size="13" fill="#ffb454" font-weight="700">*</text><rect x="60" y="58" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="72.0" y="75" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">3</text><text x="95" y="76" font-size="11" fill="var(--text-2)">= 6</text></svg>""",
        "function_name": "addOperators",
        "params": [{"name": "num", "type": "string"}, {"name": "target", "type": "int"}],
        "return_type": "vector<string>",
        "unordered": True,
        "starter_code": {
            "python": "def addOperators(num, target):\n    # your code here -- backtrack over digit splits and operators, watch for leading zeros\n    pass\n",
            "cpp": "vector<string> addOperators(string num, int target) {\n    // your code here -- backtrack over digit splits and operators, watch for leading zeros\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": ["123", 6], "expected": ["1+2+3", "1*2*3"], "input_display": 'num="123", target=6',
             "explanation": "Splitting the digits as 1, 2, 3 and inserting operators: 1+2+3=6 and 1*2*3=6 both hit the target. Other splits/operators (like 12+3=15, or 1-2+3=2) don't."},
            {"inputs": ["232", 8], "expected": ["2*3+2", "2+3*2"], "input_display": 'num="232", target=8'},
            {"inputs": ["105", 5], "expected": ["1*0+5", "10-5"], "hidden": True},
            {"inputs": ["00", 0], "expected": ["0+0", "0-0", "0*0"], "hidden": True},
        ],
    },
    {
        "id": "longest_substring_no_repeat",
        "title": "Longest Substring Without Repeating Characters",
        "difficulty": "Medium",
        "topic": "String / Sliding Window",
        "tags": ["string", "sliding-window", "hash-map"],
        "description_md": """Given a string `s`, return the length of the longest substring without repeating
characters.""",
        "diagram_svg": """<svg viewBox="0 0 292 74" width="292" height="74" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="21.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">a</text><rect x="41" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="56.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">b</text><rect x="76" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="91.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">c</text><rect x="111" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="126.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">a</text><rect x="146" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="161.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">b</text><rect x="181" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="196.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">c</text><rect x="216" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="231.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">b</text><rect x="251" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="266.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">b</text><rect x="4" y="10" width="104" height="38" rx="6" fill="none" stroke="#6ee7b7" stroke-width="2" stroke-dasharray="5,3"/><text x="6" y="60" font-size="10.5" fill="var(--text-2)">window "abc" -- next char repeats 'a'</text></svg>""",
        "function_name": "lengthOfLongestSubstring",
        "params": [{"name": "s", "type": "string"}],
        "return_type": "int",
        "starter_code": {
            "python": "def lengthOfLongestSubstring(s):\n    # your code here -- sliding window with last-seen index\n    pass\n",
            "cpp": "int lengthOfLongestSubstring(string s) {\n    // your code here -- sliding window with last-seen index\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": ["abcabcbb"], "expected": 3, "input_display": 's="abcabcbb"'},
            {"inputs": ["bbbbb"], "expected": 1, "input_display": 's="bbbbb"'},
            {"inputs": ["pwwkew"], "expected": 3, "hidden": True},
            {"inputs": [""], "expected": 0, "hidden": True},
        ],
    },
    {
        "id": "container_most_water",
        "title": "Container With Most Water",
        "difficulty": "Medium",
        "topic": "Array / Two Pointers",
        "tags": ["array", "two-pointers", "greedy"],
        "description_md": """Given `n` non-negative integers `height` where each represents a vertical line at
that index, find two lines that together with the x-axis form a container holding the most water. Return the
maximum area.""",
        "diagram_svg": """<svg viewBox="0 0 354 154" width="354" height="154" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="72" y="21.0" width="238" height="105.0" fill="#60a5fa" fill-opacity="0.25" stroke="#60a5fa" stroke-width="1" stroke-dasharray="4,3"/><rect x="6" y="111.0" width="28" height="15.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="20.0" y="105.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">1</text><text x="20.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">0</text><rect x="44" y="6.0" width="28" height="120.0" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="58.0" y="20.0" text-anchor="middle" font-size="11" fill="#1a1204" font-weight="600">8</text><text x="58.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">1</text><rect x="82" y="36.0" width="28" height="90.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="96.0" y="50.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">6</text><text x="96.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">2</text><rect x="120" y="96.0" width="28" height="30.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="134.0" y="110.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">2</text><text x="134.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">3</text><rect x="158" y="51.0" width="28" height="75.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="172.0" y="65.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">5</text><text x="172.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">4</text><rect x="196" y="66.0" width="28" height="60.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="210.0" y="80.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">4</text><text x="210.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">5</text><rect x="234" y="6.0" width="28" height="120.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="248.0" y="20.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">8</text><text x="248.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">6</text><rect x="272" y="81.0" width="28" height="45.0" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="286.0" y="95.0" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">3</text><text x="286.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">7</text><rect x="310" y="21.0" width="28" height="105.0" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="324.0" y="35.0" text-anchor="middle" font-size="11" fill="#1a1204" font-weight="600">7</text><text x="324.0" y="140" text-anchor="middle" font-size="9" fill="var(--text-2)">8</text><text x="6" y="148" font-size="10.5" fill="#60a5fa">height[1]=8, height[8]=7, width=7 -&gt; area=49</text></svg>""",
        "function_name": "maxArea",
        "params": [{"name": "height", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def maxArea(height):\n    # your code here -- two pointers from both ends, move the shorter line\n    pass\n",
            "cpp": "int maxArea(vector<int> height) {\n    // your code here -- two pointers from both ends, move the shorter line\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "expected": 49, "input_display": "height=[1,8,6,2,5,4,8,3,7]"},
            {"inputs": [[1, 1]], "expected": 1, "input_display": "height=[1,1]"},
            {"inputs": [[4, 3, 2, 1, 4]], "expected": 16, "hidden": True},
            {"inputs": [[1, 2, 1]], "expected": 2, "hidden": True},
        ],
    },
    {
        "id": "max_consecutive_ones_iii",
        "title": "Max Consecutive Ones III",
        "difficulty": "Medium",
        "topic": "Array / Sliding Window",
        "tags": ["array", "sliding-window", "binary-search"],
        "description_md": """Given a binary array `nums` and an integer `k`, return the maximum number of
consecutive `1`s achievable if you may flip at most `k` zeros to `1`s.""",
        "diagram_svg": """<svg viewBox="0 0 397 74" width="397" height="74" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="21.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="41" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="56.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="76" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="91.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="111" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="126.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">0</text><rect x="146" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="161.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">0</text><rect x="181" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="196.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">0</text><rect x="216" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="231.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="251" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="266.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="286" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="301.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="321" y="14" width="30" height="30" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="336.0" y="34.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="356" y="14" width="30" height="30" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="371.0" y="34.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">0</text><rect x="144" y="10" width="209" height="38" rx="6" fill="none" stroke="#6ee7b7" stroke-width="2" stroke-dasharray="5,3"/><text x="6" y="60" font-size="10.5" fill="var(--text-2)">flip the two 0's in this window -- 6 consecutive 1's</text></svg>""",
        "function_name": "longestOnes",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "k", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def longestOnes(nums, k):\n    # your code here -- sliding window, shrink when zero-count exceeds k\n    pass\n",
            "cpp": "int longestOnes(vector<int> nums, int k) {\n    // your code here -- sliding window, shrink when zero-count exceeds k\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2], "expected": 6, "input_display": "nums=[1,1,1,0,0,0,1,1,1,1,0], k=2"},
            {"inputs": [[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3], "expected": 10, "input_display": "nums=[...], k=3"},
            {"inputs": [[0, 0, 0, 1], 0], "expected": 1, "hidden": True},
            {"inputs": [[1, 1, 1], 0], "expected": 3, "hidden": True},
        ],
    },
    {
        "id": "kth_smallest_sorted_matrix",
        "title": "Kth Smallest Element in a Sorted Matrix",
        "difficulty": "Medium",
        "topic": "Array / Binary Search",
        "tags": ["array", "binary-search", "heap", "matrix"],
        "description_md": """Given an `n x n` `matrix` where each row and column is sorted ascending, and an
integer `k`, return the `k`th smallest element in the matrix (by overall sorted order, not distinct values).

**Follow-up they'll ask:** can you avoid flattening and sorting the whole matrix -- binary search on value or
a k-way heap merge?""",
        "diagram_svg": """<svg viewBox="0 0 138 138" width="138" height="138" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="26.0" y="32.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">1</text><rect x="48" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="68.0" y="32.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">5</text><rect x="90" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="110.0" y="32.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">9</text><rect x="6" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="26.0" y="74.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">10</text><rect x="48" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="68.0" y="74.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">11</text><rect x="90" y="48" width="40" height="40" rx="4" fill="#ffb454" stroke="#ffb454" stroke-width="1.5"/><text x="110.0" y="74.0" text-anchor="middle" font-size="13" fill="#1a1204" font-weight="600">13</text><rect x="6" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="26.0" y="116.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">12</text><rect x="48" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="68.0" y="116.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">13</text><rect x="90" y="90" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="110.0" y="116.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">15</text></svg>""",
        "function_name": "kthSmallest",
        "params": [{"name": "matrix", "type": "vector<vector<int>>"}, {"name": "k", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def kthSmallest(matrix, k):\n    # your code here\n    pass\n",
            "cpp": "int kthSmallest(vector<vector<int>> matrix, int k) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], "expected": 13, "input_display": "matrix=[[1,5,9],[10,11,13],[12,13,15]], k=8",
             "explanation": "Flattening every value and sorting gives [1,5,9,10,11,12,13,13,15] -- note 13 shows up twice since it appears twice in the matrix, and duplicates aren't collapsed. The 8th value in that sorted order is 13."},
            {"inputs": [[[-5]], 1], "expected": -5, "input_display": "matrix=[[-5]], k=1"},
            {"inputs": [[[1, 2], [1, 3]], 2], "expected": 1, "hidden": True},
            {"inputs": [[[1, 2], [1, 3]], 3], "expected": 2, "hidden": True},
        ],
    },
    {
        "id": "rank_transform_matrix",
        "title": "Rank Transform of a Matrix",
        "difficulty": "Hard",
        "topic": "Array / Union Find",
        "tags": ["array", "union-find", "sorting", "matrix"],
        "description_md": """Given an `m x n` `matrix`, return a matrix `answer` of the same size where
`answer[i][j]` is the *rank* of `matrix[i][j]` -- think of rank as "how many distinct value-tiers have I seen
so far, scanning by value from smallest to largest." Ranks must satisfy:
- Ranks are positive integers, and the smallest rank used is 1.
- For any two cells in the **same row or same column**: if one's value is smaller, its rank must be strictly
  smaller. If the values are equal, they must get the *same* rank.
- Cells that don't share a row or column with each other have no ordering constraint between them -- their
  ranks are only pinned down by the chains of shared rows/columns connecting them to everything else.
- Subject to those constraints, ranks should be as small as possible.

Note that equal values can force a rank to propagate across the whole matrix: if `matrix[0][0] == matrix[0][5]`
(same row) and `matrix[0][5] == matrix[9][5]` (same column), all three cells must share one rank, even though
`matrix[0][0]` and `matrix[9][5]` don't directly share a row or column.""",
        "diagram_svg": """<svg viewBox="0 0 96 96" width="96" height="96" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="26.0" y="25.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><text x="26.0" y="41.0" text-anchor="middle" font-size="9.5" fill="var(--amber)">rank 1</text><rect x="48" y="6" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="68.0" y="25.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text><text x="68.0" y="41.0" text-anchor="middle" font-size="9.5" fill="var(--amber)">rank 2</text><rect x="6" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="26.0" y="67.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text><text x="26.0" y="83.0" text-anchor="middle" font-size="9.5" fill="var(--amber)">rank 2</text><rect x="48" y="48" width="40" height="40" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="68.0" y="67.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">4</text><text x="68.0" y="83.0" text-anchor="middle" font-size="9.5" fill="var(--amber)">rank 3</text></svg>""",
        "function_name": "matrixRankTransform",
        "params": [{"name": "matrix", "type": "vector<vector<int>>"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "def matrixRankTransform(matrix):\n    # your code here -- process values in increasing order, union-find by row/col\n    pass\n",
            "cpp": "vector<vector<int>> matrixRankTransform(vector<vector<int>> matrix) {\n    // your code here -- process values in increasing order, union-find by row/col\n    return matrix;\n}\n",
        },
        "test_cases": [
            {"inputs": [[[1, 2], [3, 4]]], "expected": [[1, 2], [2, 3]], "input_display": "matrix=[[1,2],[3,4]]",
             "explanation": "1 is the smallest in its row and column, so it gets rank 1. Both 2 (same row as 1) and 3 (same column as 1) must rank above it, so each gets rank 2 -- they don't share a row or column with each other, so nothing forces them to match. 4 shares a row with 3 and a column with 2, so it must rank above both: rank 3."},
            {"inputs": [[[7, 7], [7, 7]]], "expected": [[1, 1], [1, 1]], "input_display": "matrix=[[7,7],[7,7]]",
             "explanation": "Every cell has the same value and every cell shares a row or column with another cell in the group (directly or through a chain), so all four are forced to the same rank: 1."},
            {"inputs": [[[1, 3], [2, 4]]], "expected": [[1, 2], [2, 3]], "hidden": True},
            {"inputs": [[[5]]], "expected": [[1]], "hidden": True},
        ],
    },
    {
        "id": "longest_increasing_subsequence",
        "title": "Longest Increasing Subsequence",
        "difficulty": "Medium",
        "topic": "Array / Dynamic Programming",
        "tags": ["array", "dynamic-programming", "binary-search"],
        "description_md": """Given an integer array `nums`, return the length of the longest strictly
increasing subsequence.

**Follow-up they'll ask:** can you do it in O(n log n) with patience sorting / binary search instead of the
O(n^2) DP?""",
        "diagram_svg": """<svg viewBox="0 0 326 80" width="326" height="80" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="20" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="23.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">10</text><text x="23.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">0</text><rect x="46" y="20" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="63.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">9</text><text x="63.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">1</text><rect x="86" y="20" width="34" height="34" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="103.0" y="42.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">2</text><text x="103.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">2</text><rect x="126" y="20" width="34" height="34" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="143.0" y="42.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">5</text><text x="143.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">3</text><rect x="166" y="20" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="183.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">3</text><text x="183.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">4</text><rect x="206" y="20" width="34" height="34" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="223.0" y="42.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">7</text><text x="223.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">5</text><rect x="246" y="20" width="34" height="34" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="263.0" y="42.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">101</text><text x="263.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">6</text><rect x="286" y="20" width="34" height="34" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="303.0" y="42.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">18</text><text x="303.0" y="67" text-anchor="middle" font-size="9" fill="var(--text-2)">7</text></svg>""",
        "function_name": "lengthOfLIS",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def lengthOfLIS(nums):\n    # your code here\n    pass\n",
            "cpp": "int lengthOfLIS(vector<int> nums) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[10, 9, 2, 5, 3, 7, 101, 18]], "expected": 4, "input_display": "nums=[10,9,2,5,3,7,101,18]"},
            {"inputs": [[0, 1, 0, 3, 2, 3]], "expected": 4, "input_display": "nums=[0,1,0,3,2,3]"},
            {"inputs": [[7, 7, 7, 7, 7, 7, 7]], "expected": 1, "hidden": True},
            {"inputs": [[4, 10, 4, 3, 8, 9]], "expected": 3, "hidden": True},
        ],
    },
    {
        "id": "jump_game",
        "title": "Jump Game",
        "difficulty": "Medium",
        "topic": "Array / Greedy",
        "tags": ["array", "greedy", "dynamic-programming"],
        "description_md": """Given an array `nums` where `nums[i]` is the maximum jump length from index `i`,
starting at index 0, return whether you can reach the last index.""",
        "diagram_svg": """<svg viewBox="0 0 262 134" width="262" height="134" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="jump-arrow" markerWidth="7" markerHeight="7" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="#93c5fd"/></marker></defs><path d="M23.0,90 Q77.0,44 131.0,90" fill="none" stroke="#93c5fd" stroke-width="1.5" marker-end="url(#jump-arrow)" opacity="0.75"/><path d="M77.0,90 Q158.0,34 239.0,90" fill="none" stroke="#93c5fd" stroke-width="1.5" marker-end="url(#jump-arrow)" opacity="0.75"/><rect x="6.0" y="73" width="34" height="34" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="23.0" y="95.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text><text x="23.0" y="124" text-anchor="middle" font-size="9" fill="var(--text-2)">0</text><rect x="60.0" y="73" width="34" height="34" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="77.0" y="95.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text><text x="77.0" y="124" text-anchor="middle" font-size="9" fill="var(--text-2)">1</text><rect x="114.0" y="73" width="34" height="34" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="131.0" y="95.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><text x="131.0" y="124" text-anchor="middle" font-size="9" fill="var(--text-2)">2</text><rect x="168.0" y="73" width="34" height="34" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="185.0" y="95.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><text x="185.0" y="124" text-anchor="middle" font-size="9" fill="var(--text-2)">3</text><rect x="222.0" y="73" width="34" height="34" rx="4" fill="var(--bg-3)" stroke="var(--line)" stroke-width="1.5"/><text x="239.0" y="95.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">4</text><text x="239.0" y="124" text-anchor="middle" font-size="9" fill="var(--text-2)">4</text></svg>""",
        "function_name": "canJump",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "bool",
        "starter_code": {
            "python": "def canJump(nums):\n    # your code here -- track farthest reachable index\n    pass\n",
            "cpp": "bool canJump(vector<int> nums) {\n    // your code here -- track farthest reachable index\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": [[2, 3, 1, 1, 4]], "expected": True, "input_display": "nums=[2,3,1,1,4]"},
            {"inputs": [[3, 2, 1, 0, 4]], "expected": False, "input_display": "nums=[3,2,1,0,4]"},
            {"inputs": [[0]], "expected": True, "hidden": True},
            {"inputs": [[1, 0, 1, 0]], "expected": False, "hidden": True},
        ],
    },
    {
        "id": "add_two_integers",
        "title": "Add Two Integers",
        "difficulty": "Easy",
        "topic": "Math",
        "tags": ["math"],
        "description_md": """Given two integers `num1` and `num2`, return their sum.""",
        "diagram_svg": """<svg viewBox="0 0 274 56" width="274" height="56" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="12" width="46" height="32" rx="5" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="29.0" y="33" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">12</text><text x="83.0" y="33" text-anchor="middle" font-size="16" fill="var(--text-2)">+</text><rect x="114" y="12" width="46" height="32" rx="5" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="137.0" y="33" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">5</text><text x="191.0" y="33" text-anchor="middle" font-size="16" fill="var(--text-2)">=</text><rect x="222" y="12" width="46" height="32" rx="5" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="245.0" y="33" text-anchor="middle" font-size="14" fill="var(--text-0)" font-weight="600">17</text></svg>""",
        "function_name": "sumTwoIntegers",
        "params": [{"name": "num1", "type": "int"}, {"name": "num2", "type": "int"}],
        "return_type": "int",
        "starter_code": {
            "python": "def sumTwoIntegers(num1, num2):\n    # your code here\n    pass\n",
            "cpp": "int sumTwoIntegers(int num1, int num2) {\n    // your code here\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [12, 5], "expected": 17, "input_display": "num1=12, num2=5"},
            {"inputs": [-10, 4], "expected": -6, "input_display": "num1=-10, num2=4"},
            {"inputs": [0, 0], "expected": 0, "hidden": True},
            {"inputs": [-100, 100], "expected": 0, "hidden": True},
        ],
    },
    {
        "id": "longest_consecutive_sequence",
        "title": "Longest Consecutive Sequence",
        "difficulty": "Medium",
        "topic": "Array / Hashing",
        "tags": ["array", "hash-map"],
        "description_md": """Given an unsorted array of integers `nums`, return the length of the longest
consecutive elements sequence, in O(n) time (no sorting).""",
        "diagram_svg": """<svg viewBox="0 0 240 56" width="240" height="56" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="12" width="32" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="22.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">1</text><rect x="44" y="12" width="32" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="60.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">2</text><rect x="82" y="12" width="32" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="98.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">3</text><rect x="120" y="12" width="32" height="32" rx="4" fill="#6ee7b7" stroke="#6ee7b7" stroke-width="1.5"/><text x="136.0" y="33.0" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="600">4</text><rect x="158" y="12" width="32" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="174.0" y="33.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">100</text><rect x="196" y="12" width="32" height="32" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="212.0" y="33.0" text-anchor="middle" font-size="13" fill="var(--text-1)" font-weight="600">200</text></svg>""",
        "function_name": "longestConsecutive",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "int",
        "starter_code": {
            "python": "def longestConsecutive(nums):\n    # your code here -- hash set, only start counting from run starts\n    pass\n",
            "cpp": "int longestConsecutive(vector<int> nums) {\n    // your code here -- hash set, only start counting from run starts\n    return 0;\n}\n",
        },
        "test_cases": [
            {"inputs": [[100, 4, 200, 1, 3, 2]], "expected": 4, "input_display": "nums=[100,4,200,1,3,2]"},
            {"inputs": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expected": 9, "input_display": "nums=[0,3,7,2,5,8,4,6,0,1]"},
            {"inputs": [[]], "expected": 0, "hidden": True},
            {"inputs": [[1, 2, 0, 1]], "expected": 3, "hidden": True},
        ],
    },
    {
        "id": "same_tree",
        "title": "Same Tree",
        "difficulty": "Easy",
        "topic": "Tree / DFS",
        "tags": ["tree", "dfs", "recursion"],
        "description_md": """Given the roots of two binary trees `p` and `q`, return whether they are
structurally identical with the same node values.""",
        "diagram_svg": """<svg viewBox="0 0 426 170" width="426" height="170" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="0" y="12" font-size="11" fill="var(--text-2)">Tree p</text><g transform="translate(0,18)"><line x1="104.0" y1="24" x2="48.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="104.0" y1="24" x2="160.0" y2="84" stroke="var(--line)" stroke-width="2"/><circle cx="104.0" cy="24" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="104.0" y="29" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><circle cx="48.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="48.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text><circle cx="160.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="160.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text></g><text x="228" y="12" font-size="11" fill="var(--text-2)">Tree q (identical)</text><g transform="translate(228,18)"><line x1="104.0" y1="24" x2="48.0" y2="84" stroke="var(--line)" stroke-width="2"/><line x1="104.0" y1="24" x2="160.0" y2="84" stroke="var(--line)" stroke-width="2"/><circle cx="104.0" cy="24" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="104.0" y="29" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">1</text><circle cx="48.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="48.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">2</text><circle cx="160.0" cy="84" r="17" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="160.0" y="89" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">3</text></g></svg>""",
        "function_name": "isSameTree",
        "params": [{"name": "p", "type": "tree"}, {"name": "q", "type": "tree"}],
        "return_type": "bool",
        "starter_code": {
            "python": "# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\n\ndef isSameTree(p, q):\n    # your code here\n    pass\n",
            "cpp": "// struct TreeNode {\n//     int val;\n//     TreeNode *left;\n//     TreeNode *right;\n//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}\n// };\n\nbool isSameTree(TreeNode* p, TreeNode* q) {\n    // your code here\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3], [1, 2, 3]], "expected": True, "input_display": "p=[1,2,3], q=[1,2,3]"},
            {"inputs": [[1, 2], [1, None, 2]], "expected": False, "input_display": "p=[1,2], q=[1,null,2]"},
            {"inputs": [[], []], "expected": True, "hidden": True},
            {"inputs": [[1, 2, 1], [1, 1, 2]], "expected": False, "hidden": True},
        ],
    },
    {
        "id": "asteroid_collision",
        "title": "Asteroid Collision",
        "difficulty": "Medium",
        "topic": "Array / Stack",
        "tags": ["array", "stack", "simulation"],
        "description_md": """You're given an array `asteroids` of integers representing asteroids in a row, all
moving at the same speed. For each asteroid, the absolute value represents its size, and the sign represents
its direction: positive means moving right, negative means moving left.

Each asteroid keeps moving in its direction until it either flies off the end of the row or meets another
asteroid coming toward it. When two asteroids meet:
- The smaller one explodes and disappears.
- If they're the same size, both explode.
- Two asteroids moving in the *same* direction never meet, no matter their sizes (they're moving at the same
  speed, so the one behind never catches up).

Note that a surviving asteroid can go on to meet *another* asteroid further down the line -- collisions can
chain.

Return the array of asteroids that remain once no more collisions can happen, in their original left-to-right
order.""",
        "diagram_svg": """<svg viewBox="0 0 174 148" width="174" height="148" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="6" y="16" font-size="11" fill="var(--text-2)">Before</text><rect x="6" y="26" width="40" height="30" rx="5" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="26.0" y="46" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="700">10</text><text x="34" y="72" text-anchor="middle" font-size="13" fill="#6ee7b7">&#8594;</text><rect x="60" y="26" width="40" height="30" rx="5" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="80.0" y="46" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="700">2</text><text x="88" y="72" text-anchor="middle" font-size="13" fill="#6ee7b7">&#8594;</text><rect x="114" y="26" width="40" height="30" rx="5" fill="#93c5fd" fill-opacity="0.85" stroke="#93c5fd" stroke-width="1.5"/><text x="134.0" y="46" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="700">5</text><text x="126" y="72" text-anchor="middle" font-size="13" fill="#93c5fd">&#8592;</text><text x="6" y="82" font-size="11" fill="var(--text-2)">After</text><rect x="6" y="92" width="40" height="30" rx="5" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="1.5"/><text x="26.0" y="112" text-anchor="middle" font-size="13" fill="#0a0a0a" font-weight="700">10</text><text x="34" y="138" text-anchor="middle" font-size="13" fill="#6ee7b7">&#8594;</text></svg>""",
        "function_name": "asteroidCollision",
        "params": [{"name": "asteroids", "type": "vector<int>"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def asteroidCollision(asteroids):\n    # your code here -- stack simulation\n    pass\n",
            "cpp": "vector<int> asteroidCollision(vector<int> asteroids) {\n    // your code here -- stack simulation\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[5, 10, -5]], "expected": [5, 10], "input_display": "asteroids=[5,10,-5]",
             "explanation": "The 10 (moving right) and the -5 (moving left) meet; 10 is bigger, so it survives and -5 explodes. The 5 and 10 are both moving right, so they never meet each other."},
            {"inputs": [[8, -8]], "expected": [], "input_display": "asteroids=[8,-8]",
             "explanation": "8 and -8 meet and are exactly the same size, so both explode."},
            {"inputs": [[10, 2, -5]], "expected": [10], "input_display": "asteroids=[10,2,-5]",
             "explanation": "This is a chain reaction. The 2 and -5 meet first: -5 is bigger, so 2 explodes and -5 keeps moving left. -5 then meets the 10 behind it: 10 is bigger, so -5 explodes too, leaving only 10."},
            {"inputs": [[-2, -1, 1, 2]], "expected": [-2, -1, 1, 2], "hidden": True},
        ],
    },
    {
        "id": "final_array_state_k_mult_i",
        "title": "Final Array State After K Multiplication Operations I",
        "difficulty": "Easy",
        "topic": "Array / Simulation",
        "tags": ["array", "math", "simulation"],
        "description_md": """Given `nums`, and integers `k` and `multiplier`, perform `k` operations: each
operation finds the minimum value in `nums` (the leftmost such index if there's a tie) and multiplies it by
`multiplier`. Return `nums` after all `k` operations.""",
        "diagram_svg": """<svg viewBox="0 0 409 150" width="409" height="150" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="87.5" width="32" height="22.5" fill="none" stroke="var(--text-2)" stroke-width="1.5" stroke-dasharray="4,3"/><text x="22.0" y="81.5" text-anchor="middle" font-size="10.5" fill="var(--text-1)">2</text><rect x="6" y="20.0" width="32" height="90.0" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="22.0" y="124" text-anchor="middle" font-size="10.5" fill="#ffb454" font-weight="700">8</text><rect x="46" y="98.75" width="32" height="11.25" fill="none" stroke="var(--text-2)" stroke-width="1.5" stroke-dasharray="4,3"/><text x="62.0" y="92.75" text-anchor="middle" font-size="10.5" fill="var(--text-1)">1</text><rect x="46" y="65.0" width="32" height="45.0" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="62.0" y="124" text-anchor="middle" font-size="10.5" fill="#ffb454" font-weight="700">4</text><rect x="86" y="76.25" width="32" height="33.75" fill="none" stroke="var(--text-2)" stroke-width="1.5" stroke-dasharray="4,3"/><text x="102.0" y="70.25" text-anchor="middle" font-size="10.5" fill="var(--text-1)">3</text><rect x="86" y="42.5" width="32" height="67.5" fill="#ffb454" fill-opacity="0.85" stroke="#ffb454" stroke-width="1.5"/><text x="102.0" y="124" text-anchor="middle" font-size="10.5" fill="#ffb454" font-weight="700">6</text><rect x="126" y="53.75" width="32" height="56.25" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="1.5"/><text x="142.0" y="47.75" text-anchor="middle" font-size="10.5" fill="var(--text-1)">5</text><rect x="166" y="42.5" width="32" height="67.5" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="1.5"/><text x="182.0" y="36.5" text-anchor="middle" font-size="10.5" fill="var(--text-1)">6</text><text x="6" y="146" font-size="10.5" fill="var(--text-2)">nums=[2,1,3,5,6], k=5, multiplier=2 -> after all 5 operations</text></svg>""",
        "function_name": "getFinalState",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "k", "type": "int"}, {"name": "multiplier", "type": "int"}],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def getFinalState(nums, k, multiplier):\n    # your code here\n    pass\n",
            "cpp": "vector<int> getFinalState(vector<int> nums, int k, int multiplier) {\n    // your code here\n    return nums;\n}\n",
        },
        "test_cases": [
            {"inputs": [[2, 1, 3, 5, 6], 5, 2], "expected": [8, 4, 6, 5, 6], "input_display": "nums=[2,1,3,5,6], k=5, multiplier=2",
             "explanation": "[2,1,3,5,6] -> multiply the 1 (index 1): [2,2,3,5,6] -> two 2's are now tied for smallest, so multiply the leftmost one (index 0): [4,2,3,5,6] -> multiply the remaining 2 (index 1): [4,4,3,5,6] -> multiply the 3 (index 2): [4,4,6,5,6] -> two 4's are tied again, multiply the leftmost (index 0): [8,4,6,5,6]. That's all 5 operations."},
            {"inputs": [[1, 2], 3, 4], "expected": [16, 8], "input_display": "nums=[1,2], k=3, multiplier=4"},
            {"inputs": [[1, 1, 1], 1, 2], "expected": [2, 1, 1], "hidden": True},
            {"inputs": [[5], 3, 1], "expected": [5], "hidden": True},
        ],
    },
    {
        "id": "generate_parentheses",
        "title": "Generate Parentheses",
        "difficulty": "Medium",
        "topic": "String / Backtracking",
        "tags": ["string", "backtracking", "dynamic-programming"],
        "description_md": """Given `n` pairs of parentheses, return all combinations of well-formed
parenthesis strings (grading here ignores order).""",
        "diagram_svg": """<svg viewBox="0 0 176 501" width="176" height="501" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><g transform="translate(0,0)"><path d="M74.0,61 Q88.0,40 102.0,61" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.8"/><path d="M46.0,61 Q88.0,26 130.0,61" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.8"/><path d="M18.0,61 Q88.0,12 158.0,61" fill="none" stroke="#93c5fd" stroke-width="1.5" opacity="0.8"/><rect x="6.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="34.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="46.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="62.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="74.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="90.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="118.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="130.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="146.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="158.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text></g><g transform="translate(0,99)"><path d="M46.0,61 Q60.0,40 74.0,61" fill="none" stroke="#6ee7b7" stroke-width="1.5" opacity="0.8"/><path d="M102.0,61 Q116.0,40 130.0,61" fill="none" stroke="#6ee7b7" stroke-width="1.5" opacity="0.8"/><path d="M18.0,61 Q88.0,12 158.0,61" fill="none" stroke="#6ee7b7" stroke-width="1.5" opacity="0.8"/><rect x="6.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="34.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="46.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="62.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="74.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="90.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="118.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="130.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="146.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="158.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text></g><g transform="translate(0,198)"><path d="M46.0,61 Q60.0,40 74.0,61" fill="none" stroke="#fdba74" stroke-width="1.5" opacity="0.8"/><path d="M18.0,61 Q60.0,26 102.0,61" fill="none" stroke="#fdba74" stroke-width="1.5" opacity="0.8"/><path d="M130.0,61 Q144.0,40 158.0,61" fill="none" stroke="#fdba74" stroke-width="1.5" opacity="0.8"/><rect x="6.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="34.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="46.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="62.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="74.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="90.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="118.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="130.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="146.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="158.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text></g><g transform="translate(0,297)"><path d="M18.0,61 Q32.0,40 46.0,61" fill="none" stroke="#f0abfc" stroke-width="1.5" opacity="0.8"/><path d="M102.0,61 Q116.0,40 130.0,61" fill="none" stroke="#f0abfc" stroke-width="1.5" opacity="0.8"/><path d="M74.0,61 Q116.0,26 158.0,61" fill="none" stroke="#f0abfc" stroke-width="1.5" opacity="0.8"/><rect x="6.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="34.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="46.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="62.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="74.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="90.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="118.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="130.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="146.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="158.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text></g><g transform="translate(0,396)"><path d="M18.0,61 Q32.0,40 46.0,61" fill="none" stroke="#fca5a5" stroke-width="1.5" opacity="0.8"/><path d="M74.0,61 Q88.0,40 102.0,61" fill="none" stroke="#fca5a5" stroke-width="1.5" opacity="0.8"/><path d="M130.0,61 Q144.0,40 158.0,61" fill="none" stroke="#fca5a5" stroke-width="1.5" opacity="0.8"/><rect x="6.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="18.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="34.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="46.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="62.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="74.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="90.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="102.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text><rect x="118.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="130.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">(</text><rect x="146.0" y="61" width="24" height="24" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1.5"/><text x="158.0" y="78.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">)</text></g></svg>""",
        "function_name": "generateParenthesis",
        "params": [{"name": "n", "type": "int"}],
        "return_type": "vector<string>",
        "unordered": True,
        "starter_code": {
            "python": "def generateParenthesis(n):\n    # your code here -- backtrack, only add ')' if it stays valid\n    pass\n",
            "cpp": "vector<string> generateParenthesis(int n) {\n    // your code here -- backtrack, only add ')' if it stays valid\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [3], "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"], "input_display": "n=3"},
            {"inputs": [1], "expected": ["()"], "input_display": "n=1"},
            {"inputs": [2], "expected": ["(())", "()()"], "hidden": True},
        ],
    },
    {
        "id": "evaluate_division",
        "title": "Evaluate Division",
        "difficulty": "Medium",
        "topic": "Array / Graph",
        "tags": ["array", "string", "graph", "union-find", "dfs"],
        "description_md": """Given `equations` of variable pairs `[Ai, Bi]` and integer `values` where
`Ai / Bi = values[i]`, answer each query in `queries` (`[Cj, Dj]` meaning `Cj / Dj`).

To keep this judge's comparisons exact (no floating point), `values` and results are integers: if a queried
variable is unknown, or the true ratio between the two variables isn't a whole number, return `-1` for that
query. Otherwise return the whole-number ratio.""",
        "diagram_svg": """<svg viewBox="0 0 300 240" width="300" height="240" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><defs><marker id="eq-arrow" markerWidth="7" markerHeight="7" refX="6" refY="2.5" orient="auto"><path d="M0,0 L6,2.5 L0,5 Z" fill="var(--amber)"/></marker></defs><line x1="140.0" y1="47.32050807568877" x2="187.7820323027551" y2="130.08141571295792" stroke="var(--amber)" stroke-width="1.8" marker-end="url(#eq-arrow)" opacity="0.85"/><rect x="149.89101615137756" y="79.70096189432334" width="28" height="16" fill="var(--bg-1)"/><text x="163.89101615137756" y="91.70096189432334" text-anchor="middle" font-size="11" fill="var(--amber)">2</text><line x1="179.2820323027551" y1="150.0" x2="83.71796769724492" y2="150.00000000000003" stroke="var(--amber)" stroke-width="1.8" marker-end="url(#eq-arrow)" opacity="0.85"/><rect x="117.5" y="141.0" width="28" height="16" fill="var(--bg-1)"/><text x="131.5" y="153.0" text-anchor="middle" font-size="11" fill="var(--amber)">3</text><circle cx="130.0" cy="30.0" r="20" fill="var(--bg-3)" stroke="var(--text-1)" stroke-width="2"/><text x="130.0" y="35.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">a</text><circle cx="199.2820323027551" cy="150.0" r="20" fill="var(--bg-3)" stroke="var(--text-1)" stroke-width="2"/><text x="199.2820323027551" y="155.0" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">b</text><circle cx="60.717967697244916" cy="150.00000000000003" r="20" fill="var(--bg-3)" stroke="var(--text-1)" stroke-width="2"/><text x="60.717967697244916" y="155.00000000000003" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="600">c</text></svg>""",
        "function_name": "calcEquation",
        "params": [
            {"name": "equations", "type": "vector<vector<string>>"},
            {"name": "values", "type": "vector<int>"},
            {"name": "queries", "type": "vector<vector<string>>"},
        ],
        "return_type": "vector<int>",
        "starter_code": {
            "python": "def calcEquation(equations, values, queries):\n    # your code here -- build a weighted graph, DFS/BFS to accumulate the ratio along a path\n    pass\n",
            "cpp": "vector<int> calcEquation(vector<vector<string>> equations, vector<int> values, vector<vector<string>> queries) {\n    // your code here -- build a weighted graph, DFS/BFS to accumulate the ratio along a path\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[["a", "b"], ["b", "c"]], [2, 3], [["a", "c"], ["a", "a"], ["a", "e"], ["x", "x"]]],
             "expected": [6, 1, -1, -1], "input_display": 'equations=[[a,b],[b,c]], values=[2,3], queries=[[a,c],[a,a],[a,e],[x,x]]',
             "explanation": "a/b=2 and b/c=3, so chaining them gives a/c = (a/b) * (b/c) = 2 * 3 = 6. a/a=1 trivially since a is a known variable. a/e=-1 because e never appears in any equation. x/x=-1 too -- even though it looks trivial, x was never introduced by any equation, so it's unknown."},
            {"inputs": [[["a", "b"]], [10], [["a", "b"], ["b", "a"], ["a", "a"], ["b", "b"], ["a", "c"]]],
             "expected": [10, -1, 1, 1, -1], "input_display": 'equations=[[a,b]], values=[10], queries=[[a,b],[b,a],[a,a],[b,b],[a,c]]'},
            {"inputs": [[["a", "b"], ["b", "c"], ["c", "d"]], [2, 2, 2], [["a", "d"], ["d", "a"], ["a", "c"]]],
             "expected": [8, -1, 4], "hidden": True},
        ],
    },
    {
        "id": "ransom_note",
        "title": "Ransom Note",
        "difficulty": "Easy",
        "topic": "Hash Table / String",
        "tags": ["hash-table", "string"],
        "description_md": """Given two strings `ransomNote` and `magazine`, return whether `ransomNote` can be
constructed from letters of `magazine` (each letter in `magazine` can only be used once).""",
        "diagram_svg": """<svg viewBox="0 0 88 90" width="88" height="90" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><text x="23.0" y="16" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="700">a</text><rect x="6" y="24" width="34" height="26" rx="4" fill="#6ee7b7" fill-opacity="0.2" stroke="#6ee7b7" stroke-width="1.5"/><text x="23.0" y="41" text-anchor="middle" font-size="11" fill="#6ee7b7">need 2</text><rect x="6" y="54" width="34" height="26" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="23.0" y="71" text-anchor="middle" font-size="11" fill="var(--text-1)">have 2</text><text x="65.0" y="16" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="700">b</text><rect x="48" y="24" width="34" height="26" rx="4" fill="#6ee7b7" fill-opacity="0.2" stroke="#6ee7b7" stroke-width="1.5"/><text x="65.0" y="41" text-anchor="middle" font-size="11" fill="#6ee7b7">need 0</text><rect x="48" y="54" width="34" height="26" rx="4" fill="var(--bg-2)" stroke="var(--line)" stroke-width="1"/><text x="65.0" y="71" text-anchor="middle" font-size="11" fill="var(--text-1)">have 1</text></svg>""",
        "function_name": "canConstruct",
        "params": [{"name": "ransomNote", "type": "string"}, {"name": "magazine", "type": "string"}],
        "return_type": "bool",
        "starter_code": {
            "python": "def canConstruct(ransomNote, magazine):\n    # your code here\n    pass\n",
            "cpp": "bool canConstruct(string ransomNote, string magazine) {\n    // your code here\n    return false;\n}\n",
        },
        "test_cases": [
            {"inputs": ["a", "b"], "expected": False, "input_display": 'ransomNote="a", magazine="b"'},
            {"inputs": ["aa", "ab"], "expected": False, "input_display": 'ransomNote="aa", magazine="ab"'},
            {"inputs": ["aa", "aab"], "expected": True, "hidden": True},
            {"inputs": ["", "abc"], "expected": True, "hidden": True},
        ],
    },
    {
        "id": "top_k_frequent_elements",
        "title": "Top K Frequent Elements",
        "difficulty": "Medium",
        "topic": "Array / Heap",
        "tags": ["array", "heap", "hash-map", "bucket-sort"],
        "description_md": """Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. The test cases here are built so the top-`k` set is always unambiguous (no tie sits right at the
boundary) -- return them in any order (grading here ignores order).

**Follow-up they'll ask:** can you beat sorting all values by frequency (O(n log n))? Bucket sort by frequency,
or a size-k min-heap, both get you to O(n).""",
        "diagram_svg": """<svg viewBox="0 0 213 124" width="213" height="124" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><rect x="6" y="24" width="34" height="60" rx="3" fill="#ffb454" fill-opacity="0.9" stroke="#ffb454" stroke-width="1.5"/><text x="23.0" y="18" text-anchor="middle" font-size="11" fill="#ffb454" font-weight="600">x3</text><text x="23.0" y="100" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">1</text><rect x="50" y="44" width="34" height="40" rx="3" fill="#ffb454" fill-opacity="0.9" stroke="#ffb454" stroke-width="1.5"/><text x="67.0" y="38" text-anchor="middle" font-size="11" fill="#ffb454" font-weight="600">x2</text><text x="67.0" y="100" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">2</text><rect x="94" y="64" width="34" height="20" rx="3" fill="var(--bg-3)" fill-opacity="0.9" stroke="var(--line)" stroke-width="1.5"/><text x="111.0" y="58" text-anchor="middle" font-size="11" fill="var(--text-1)" font-weight="600">x1</text><text x="111.0" y="100" text-anchor="middle" font-size="12" fill="var(--text-0)" font-weight="600">3</text><text x="6" y="118" font-size="10.5" fill="#ffb454">top 2 by frequency, highlighted</text></svg>""",
        "function_name": "topKFrequent",
        "params": [{"name": "nums", "type": "vector<int>"}, {"name": "k", "type": "int"}],
        "return_type": "vector<int>",
        "unordered": True,
        "starter_code": {
            "python": "def topKFrequent(nums, k):\n    # your code here -- count frequencies, then bucket sort or heap by count\n    pass\n",
            "cpp": "vector<int> topKFrequent(vector<int> nums, int k) {\n    // your code here -- count frequencies, then bucket sort or heap by count\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 1, 1, 2, 2, 3], 2], "expected": [1, 2], "input_display": "nums=[1,1,1,2,2,3], k=2",
             "explanation": "1 appears 3 times, 2 appears 2 times, 3 appears once. The two most frequent values are 1 and 2 -- the diagram above shows this exact example."},
            {"inputs": [[1], 1], "expected": [1], "input_display": "nums=[1], k=1"},
            {"inputs": [[4, 4, 4, 6, 6, 7, 7, 7, 7], 2], "expected": [7, 4], "hidden": True},
            {"inputs": [[5, 3, 1, 1, 1, 3, 73, 1], 1], "expected": [1], "hidden": True},
        ],
    },
    {
        "id": "permutations",
        "title": "Permutations",
        "difficulty": "Medium",
        "topic": "Array / Backtracking",
        "tags": ["array", "backtracking", "recursion"],
        "description_md": """Given an array `nums` of distinct integers, return all possible permutations of it.

To keep this judge's comparisons exact -- unlike most backtracking problems here, the order of results matters
to how equality is checked, not just which permutations are present -- return them in the order standard
backtracking produces: at each position, try the not-yet-used numbers in the same relative order they appear
in the input array.""",
        "diagram_svg": """<svg viewBox="0 0 380 120" width="380" height="120" xmlns="http://www.w3.org/2000/svg" font-family="SF Mono, Cascadia Code, Consolas, monospace"><line x1="190.0" y1="16" x2="50.0" y2="54" stroke="var(--line)" stroke-width="2"/><line x1="50.0" y1="54" x2="20" y2="100" stroke="var(--line)" stroke-width="2"/><line x1="50.0" y1="54" x2="80" y2="100" stroke="var(--line)" stroke-width="2"/><line x1="190.0" y1="16" x2="170.0" y2="54" stroke="var(--line)" stroke-width="2"/><line x1="170.0" y1="54" x2="140" y2="100" stroke="var(--line)" stroke-width="2"/><line x1="170.0" y1="54" x2="200" y2="100" stroke="var(--line)" stroke-width="2"/><line x1="190.0" y1="16" x2="290.0" y2="54" stroke="var(--line)" stroke-width="2"/><line x1="290.0" y1="54" x2="260" y2="100" stroke="var(--line)" stroke-width="2"/><line x1="290.0" y1="54" x2="320" y2="100" stroke="var(--line)" stroke-width="2"/><circle cx="190.0" cy="16" r="11" fill="var(--bg-3)" stroke="var(--text-2)" stroke-width="2"/><text x="190.0" y="20" text-anchor="middle" font-size="10" fill="var(--text-2)">?</text><circle cx="50.0" cy="54" r="15" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="50.0" y="59" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="700">1</text><circle cx="20" cy="100" r="15" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="2"/><text x="20" y="105" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">123</text><circle cx="80" cy="100" r="15" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="2"/><text x="80" y="105" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">132</text><circle cx="170.0" cy="54" r="15" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="170.0" y="59" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="700">2</text><circle cx="140" cy="100" r="15" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="2"/><text x="140" y="105" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">213</text><circle cx="200" cy="100" r="15" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="2"/><text x="200" y="105" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">231</text><circle cx="290.0" cy="54" r="15" fill="var(--bg-3)" stroke="var(--amber)" stroke-width="2"/><text x="290.0" y="59" text-anchor="middle" font-size="13" fill="var(--text-0)" font-weight="700">3</text><circle cx="260" cy="100" r="15" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="2"/><text x="260" y="105" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">312</text><circle cx="320" cy="100" r="15" fill="#6ee7b7" fill-opacity="0.85" stroke="#6ee7b7" stroke-width="2"/><text x="320" y="105" text-anchor="middle" font-size="12" fill="#0a0a0a" font-weight="700">321</text></svg>""",
        "function_name": "permute",
        "params": [{"name": "nums", "type": "vector<int>"}],
        "return_type": "vector<vector<int>>",
        "starter_code": {
            "python": "def permute(nums):\n    # your code here -- backtrack, trying unused numbers in input order at each step\n    pass\n",
            "cpp": "vector<vector<int>> permute(vector<int> nums) {\n    // your code here -- backtrack, trying unused numbers in input order at each step\n    return {};\n}\n",
        },
        "test_cases": [
            {"inputs": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
             "input_display": "nums=[1,2,3]",
             "explanation": "Pick the first number from {1,2,3} in order, then the second from whatever's left (the third is then forced) -- that produces exactly these 6 orderings, matching the tree above."},
            {"inputs": [[0, 1]], "expected": [[0, 1], [1, 0]], "input_display": "nums=[0,1]", "hidden": True},
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
