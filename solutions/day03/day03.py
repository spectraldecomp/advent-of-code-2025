banks = open("solutions/day03/input.txt").read().splitlines()
banks = open("solutions/day03/input.txt").read().splitlines()

k = 12

total = 0

for bank in banks:
    digits = [int(x) for x in bank]
    n = len(digits)

    if k >= n:
        best_digits = digits
    else:
        remove = n - k
        stack = []
        for d in digits:
            while remove > 0 and stack and stack[-1] < d:
                stack.pop()
                remove -= 1
            stack.append(d)
        best_digits = stack[:k]

    number_value = int("".join(str(d) for d in best_digits))
    total += number_value

print("Solution:", total)
