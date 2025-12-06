ids = open("solutions/day02/sample.txt").read().strip().split(",")
ids = open("solutions/day02/input.txt").read().strip().split(",")
invalid_ids = []

for r in ids:
    if not r:
        continue

    start_str, end_str = r.split("-")
    start = int(start_str)
    end = int(end_str)

    for id_num in range(start, end + 1):
        id_str = str(id_num)

        if len(id_str) % 2 != 0:
            continue

        mid = len(id_str) // 2
        first_half = id_str[:mid]
        second_half = id_str[mid:]

        if first_half == second_half:
            invalid_ids.append(id_num)
            print(f"Found invalid id: {id_num}")

print(f"Solution Day 1: {sum(invalid_ids)}")


def is_invalid_id(n):
    s = str(n)
    if len(s) <= 1:
        return False
    doubled = s + s
    return s in doubled[1:-1]


invalid_sum = 0
for r in ids:
    if not r:
        continue

    start, end = map(int, r.split("-"))
    for n in range(start, end + 1):
        if is_invalid_id(n):
            invalid_sum += n

print("Solution Day 2:", invalid_sum)
