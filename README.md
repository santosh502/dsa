# DSA Mastery Program

A comprehensive Data Structures & Algorithms training program with 419 curated problems across 19 topics.

## Structure

```
.
├── tracker.html          # Interactive progress tracker
├── problems.json         # All 419 problems (curated, versioned)
├── solutions/            # Python solutions (you solve these)
│   ├── TEMPLATE.py       # Solution template format
│   ├── single_number.py
│   ├── two_sum.py
│   └── ...
└── README.md
```

## For Trainees

**1. Copy to your repo:**
```bash
cp tracker.html dsa-tracker.html
open dsa-tracker.html  # in browser
```

**2. Start tracking:**
- Open the tracker in your browser
- Solve problems on LeetCode
- Check off problems as you complete them
- Progress auto-saves to your browser

**3. Review solutions:**
- Click "Sol" button on any problem to see the reference solution
- Study the approach and implementation
- Try similar problems to reinforce the pattern

## For Lead (Solution Submission)

**1. Solve a problem and create the solution file:**
```bash
cd solutions/
# Create file with snake_case name: single_number.py
```

**2. Follow the template format:**
```python
"""
Problem: Single Number
LeetCode: 136
Pattern: Bit Manipulation
Difficulty: E

Time Complexity: O(n)
Space Complexity: O(1)

Approach: Use XOR — duplicate bits cancel out
"""

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**3. Commit to Git:**
```bash
git add solutions/single_number.py
git commit -m "Solution: Single Number (Bit Manipulation)"
git push
```

## Problem Selection

- **419 problems** across 19 DSA topics
- **Pattern-based** (not random) — mirrors real interview patterns
- **Curated** from LeetCode, NeetCode, GeeksforGeeks
- **Difficulty**: 90 Easy (21%), 264 Medium (63%), 65 Hard (15%)

## Topics Covered

Arrays & Strings, Hashing, Sliding Window, Two Pointers, Stacks & Queues, Heap / Priority Queue, Linked Lists, Trees & BST, Graphs, Greedy, Dynamic Programming, Backtracking, Sorting & Binary Search, Math & Bit Manipulation, Matrix, Intervals, Trie, Advanced Data Structures, Advanced Strings

## Expected Timeline

- **Casual pace**: 6-8 months @ 5 hrs/week (1-2 problems/day)
- **Intensive**: 2-3 months @ 10+ hrs/week (4-5 problems/day)
- **Target**: Solve 70%+ of problems to feel confident in interviews

## Resources

- [LeetCode](https://leetcode.com) — Primary problem source
- [NeetCode](https://neetcode.io) — Video explanations for patterns
- [GeeksforGeeks](https://www.geeksforgeeks.org/dsa) — Theory & implementation reference
- [CSES Problem Set](https://cses.fi/problemset/) — Advanced algorithmic problems

Happy coding! 🚀
