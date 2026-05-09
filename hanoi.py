# ── RECURSION ─────────────────────────────────────────────────
def hanoi(n, source, target, auxiliary, step=None):
    if step is None:
        step = [0]

    if n == 1:                              # BASE CASE — stops recursion
        step[0] += 1
        print(f"  Step {step[0]:>3}: Move disk 1  {source} → {target}")
        return

    hanoi(n - 1, source, auxiliary, target, step)   # recursive call 1
    step[0] += 1
    print(f"  Step {step[0]:>3}: Move disk {n}  {source} → {target}")
    hanoi(n - 1, auxiliary, target, source, step)   # recursive call 2


# ── ITERATION ─────────────────────────────────────────────────
def hanoi_iterative(n):
    stack = [(n, 'A', 'C', 'B')]
    step = 0

    while stack:                            # ITERATIVE loop
        disks, src, tgt, aux = stack.pop()
        if disks == 1:
            step += 1
            print(f"  Step {step:>3}: Move disk 1  {src} → {tgt}")
        else:
            stack.append((disks - 1, aux, tgt, src))
            stack.append((1, src, tgt, aux))
            stack.append((disks - 1, src, aux, tgt))


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter number of disks (1–10): "))
            if 1 <= n <= 10:
                break
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    mode = input("Choose mode — (r)ecursive or (i)terative? [r/i]: ").strip().lower()

    print(f"\nSolving {n}-disk Tower of Hanoi ({2**n - 1} moves)...\n")

    if mode == 'i':
        hanoi_iterative(n)
    else:
        hanoi(n, 'A', 'C', 'B')

    print(f"\nDone! Total moves: {2**n - 1}")