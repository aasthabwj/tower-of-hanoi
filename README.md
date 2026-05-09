# Tower of Hanoi — Python Demo

A short Python demonstration of the classic **Tower of Hanoi** puzzle, implemented two ways to illustrate **recursion** and **iteration**.

## What is Tower of Hanoi?

Three pegs (A, B, C) hold a stack of disks of different sizes. The goal is to move all disks from peg A to peg C, following these rules:

- Only one disk can be moved at a time
- A disk can only be placed on top of a larger disk (or an empty peg)
- All disks start on peg A and must end on peg C

For `n` disks, the minimum number of moves required is always **2ⁿ − 1**.

## Files

| File | Description |
|------|-------------|
| `hanoi.py` | Main implementation — recursive + iterative versions |

## How to Run

Make sure Python 3 is installed, then:

```bash
python hanoi.py
```

### Sample output (3 disks)

```
=== Recursive solution (3 disks) ===
  Move disk 1:  A → C
  Move disk 2:  A → B
  Move disk 1:  C → B
  Move disk 3:  A → C
  Move disk 1:  B → A
  Move disk 2:  B → C
  Move disk 1:  A → C

=== Iterative solution (3 disks) ===
  Move disk 1:  A → C
  Move disk 2:  A → B
  Move disk 1:  C → B
  Move disk 3:  A → C
  Move disk 1:  B → A
  Move disk 2:  B → C
  Move disk 1:  A → C

Total moves required: 7
```

## Code Concepts Demonstrated

### Recursion (`hanoi` function)

The recursive solution expresses the problem in terms of itself:

1. Move the top `n-1` disks to the auxiliary peg ← *recursive call*
2. Move the largest disk directly to the target peg
3. Move the `n-1` disks from auxiliary to target ← *recursive call*

The **base case** (`n == 1`) stops the recursion — when there is only one disk, just move it directly.

```python
def hanoi(n, source, target, auxiliary):
    if n == 1:                                      # base case — stops recursion
        print(f"Move disk 1: {source} → {target}")
        return
    hanoi(n - 1, source, auxiliary, target)         # recursive call 1
    print(f"Move disk {n}: {source} → {target}")
    hanoi(n - 1, auxiliary, target, source)         # recursive call 2
```

### Iteration (`hanoi_iterative` function)

The iterative solution uses a `while` loop and an explicit stack to simulate the same logic that the call stack handles automatically in the recursive version.

```python
def hanoi_iterative(n):
    stack = [(n, 'A', 'C', 'B')]
    while stack:                        # iteration — runs until stack is empty
        n, src, tgt, aux = stack.pop()
        if n == 1:
            print(f"Move disk 1: {src} → {tgt}")
        else:
            stack.append((n-1, aux, tgt, src))  # step 3 (pushed first — LIFO)
            stack.append((1, src, tgt, aux))     # step 2
            stack.append((n-1, src, aux, tgt))  # step 1
```

Both versions produce **identical output**. The recursive version is cleaner and closer to the mathematical definition; the iterative version makes the stack mechanics explicit.

## Complexity

| Metric | Value |
|--------|-------|
| Time complexity | O(2ⁿ) |
| Space complexity | O(n) — call stack depth |
| Moves for 3 disks | 7 |
| Moves for 6 disks | 63 |


> Note: each extra disk doubles the number of moves, so large values (>20) will produce very long output.

## Author
Aastha
IIIT Delhi — B.Tech CSE, second year  
Submitted as part of a scripting and algorithms assignment.
