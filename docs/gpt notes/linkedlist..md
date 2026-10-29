# Linked Lists: Complete LeetCode Roadmap

This is the checklist to master before tackling Linked List Medium/Hard problems, especially for Google-style interviews. Follow the order; you don't need to master every advanced algorithm before starting Mediums.

## 1. Core topics checklist


## Your study checklist

0/36 completed

### A. Fundamentals

Singly, doubly and circular linked lists

Nodes, head, tail, next pointers and references

Traversal, search, insertion and deletion

Dummy/sentinel nodes

Handling empty, single-node and two-node lists

Reference identity vs node value equality

### B. Pointer manipulation

Reversing a list iteratively and recursively

Reversing a sublist between positions

Swapping nodes and swapping pairs

Reordering a list

Merging two sorted lists

Splitting a list into halves

Deleting nodes without losing the remaining list

### C. Essential techniques

Slow and fast pointers

Finding the middle node

Cycle detection (Floyd's algorithm)

Finding the cycle entry point

Finding the intersection of two lists

Kth node from the end (two pointers)

In-place list partitioning

### D. Advanced patterns

In-place merging and sorting

Merge sort on linked lists

Palindrome checking

Addition of numbers represented by lists

Copying lists with random pointers

Reverse nodes in groups of k

Rotate a list

Flattening multilevel linked lists

Designing an LRU cache (hash map + doubly linked list)

### E. Problem-solving skills

Draw pointer changes before coding

Maintain head/tail and loop invariants

Identify when a dummy node simplifies logic

Track saved next pointers before rewiring

Prove termination and avoid cycles

Analyze O(n) time and O(1) auxiliary space

Use recursion safely and understand call-stack space

## 2. Algorithms and patterns you must know

| Algorithm / technique                     | Where it is used                              |
| ----------------------------------------- | --------------------------------------------- |
| Fast & slow pointers (Floyd's)            | Middle, cycle detection, cycle entry          |
| Two pointers with a gap                   | Nth node from end, removing nodes             |
| In-place reversal                         | Reverse list, reverse groups, reorder         |
| Dummy node + sentinel                     | Insertion, deletion, merging                  |
| Merge two sorted lists                    | Sorted merge, merge sort                      |
| Divide and conquer                        | Merge sort, splitting lists                   |
| Hash map / set                            | Intersection, random-pointer copying, caching |
| Recursion / backtracking through pointers | Recursive reversal, recursive merging         |
| Stack                                     | Palindrome checking, reversing order          |
| Min-heap / priority queue                 | Merge \\(k\\) sorted lists                    |
| Doubly linked list + hash map             | LRU cache                                     |
| Pointer splicing                          | Reordering, partitioning, moving sublists     |

Priority: Master the first six techniques before attempting Hard problems. Learn heaps and cache design when you reach those problem patterns.

## 3. Best resources

[Leetcode 25: Reverse Nodes in k-Group | by Rutuja Bhombe | Medium](https://images.openai.com/static-rsc-4/nouPFLDtOOx0ZKahjiUObXkkNM68vSByMemfat-HAQrA1NHlBKU8H7f6R42OCnyb10Mjh6k-Ej3FvDK4xuENy2Rk44AS-ANc7xnMa7A3RhpC0h17Xfg4GmLf0_W9fD08ugYHz_qVqAf36lEhWe8BxJKpSI6eu50avJvMD6hKaMg?purpose=inline)

1\. NeetCode Roadmap

Best structured problem sequence; includes explanations and Python solutions.

[Roadmap and practice problems](https://neetcode.io/roadmap?utm_source=chatgpt.com)

[Steven Kester Yuwono - National University of Singapore](https://images.openai.com/static-rsc-4/CBPWZEoAEIvC7ix2Ul5mhQG3ih0yE822kHaisyucrzOUcfL6kfnRiHW3gSB3-_0d_UeukBXkFCAQXFXstnNeW743j2uFWKxA8dpof4_vIMEK5q79bFqvhekS0duftKdSPFdrk8DDdOzkgP_3yvnhNkhlbZcVQYLQxzREu_zp0mM?purpose=inline)

2\. VisuAlgo

Visualize nodes, pointers and linked-list operations before coding.

[Linked-list visualization](https://visualgo.net/en/list?utm_source=chatgpt.com)

[PART-2: CODING PATTERN & TEMPLATE for LINEAR DS ( Personal Notes) - Discuss - LeetCode](https://images.openai.com/static-rsc-4/navAxe4O3hhu0tIlH6ZPTEe7aJmX5HPef1qxyAy_XMWAb_ov_Nkz5CwiUFn2aKT6Cvd7PdHxtoajl6_6BA5HqHb5IymfxVsa5tL7QA5japF--QmGHKLlwN7W6YaNWR4g0PC5HehqfP8JxfFr7qnHGAVszjIV0wjrtPRe89pSXI0?purpose=inline)

3\. LeetCode

Use for independent practice, edge cases and timed problem solving.

[All Linked List problems](https://leetcode.com/tag/linked-list/?utm_source=chatgpt.com)

## 4. Problem-solving order

Complete these in sequence:

1. Foundation: Reverse Linked List, Merge Two Sorted Lists, Linked List Cycle, Middle of the Linked List.
2. Pointer mastery: Remove Nth Node From End, Linked List Cycle II, Intersection of Two Linked Lists, Reverse Linked List II.
3. Medium patterns: Reorder List, Swap Nodes in Pairs, Partition List, Copy List with Random Pointer, Add Two Numbers.
4. Advanced: Sort List, Rotate List, Reverse Nodes in k-Group, LRU Cache, Merge k Sorted Lists.

## 5. When are you ready for Medium/Hard?

You should be able to:

- Trace every pointer change without guessing.
- Explain why your loop terminates and why edge cases work.
- Solve reversal, merging and fast/slow-pointer problems without looking up templates.
- Achieve \\(O(n)\\) time and \\(O(1)\\) auxiliary space when possible.
- Distinguish node identity from node value and avoid accidental cycles.

My recommendation: Since you're already practising linked-list problems, use NeetCode as your problem list and VisuAlgo only when pointer manipulation feels unclear. Don't wait until you've mastered every topic to begin Mediums.