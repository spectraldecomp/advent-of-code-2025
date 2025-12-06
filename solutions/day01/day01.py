def get_zero_crossings(data):
    zeroes = 0
    czeroes = 0
    position = 50

    for line in data:
        dist = abs(line)
        next_pos = position + line
        next_pos_cycled = next_pos % 100

        if next_pos_cycled == 0:
            zeroes += 1

        if position == 0 and next_pos_cycled == 0:
            rotation = dist // 100
            czeroes += rotation

        elif position != 0 and next_pos_cycled == 0:
            rotation = dist // 100 + 1
            czeroes += rotation

        elif position == 0 and next_pos_cycled != 0:
            rotation = dist // 100
            czeroes += rotation

        else:
            rotation = dist // 100
            left_over = (dist % 100 if line > 0 else (dist % 100) * -1)
            remaining_dist = position + left_over
            extra = remaining_dist < 0 or remaining_dist > 100
            if (next_pos < 0 or next_pos > 100) and dist < 100:
                czeroes += 1
            elif dist > 100:
                czeroes += rotation + extra

        position = next_pos_cycled

    return zeroes, czeroes


with open("solutions/day01/input.txt") as f:
    read_data = f.read().splitlines()
read_data = [int(x.replace("L", "-").replace("R", "")) for x in read_data]

print(f"Solution {get_zero_crossings(read_data)}")
