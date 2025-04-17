from collections import defaultdict


num_bricks, num_colors = tuple(map(int, input().split()))
bricks_color, bricks_len = list(), list()
for brick_num in range(num_bricks):
    length, color = tuple(map(int, input().split()))
    bricks_len.append(length)
    bricks_color.append(color)

max_len = sum(
    [
        length
        for brick_num, length in enumerate(bricks_len)
        if bricks_color[brick_num] == 1
    ]
)

possible_len_for_color = defaultdict(set)
possible_len_to_get_bricks_num = defaultdict(list)
for color_idx in range(1, num_colors + 1):
    possible_len_to_get_bricks_num[color_idx] = [-1] * (max_len + 1)
    possible_len_to_get_bricks_num[color_idx][0] = 0

for brick_idx, length in enumerate(bricks_len):
    for pl, last_brick in enumerate(
        possible_len_to_get_bricks_num[bricks_color[brick_idx]][::-1]
    ):
        current_l = max_len - pl
        if last_brick != -1:
            new_l = current_l + length
            if new_l <= max_len:
                if possible_len_to_get_bricks_num[bricks_color[brick_idx]][new_l] == -1:
                    possible_len_to_get_bricks_num[bricks_color[brick_idx]][new_l] = (
                        brick_idx + 1
                    )
                    possible_len_for_color[bricks_color[brick_idx]].add(new_l)

pos_lengths_intersection = possible_len_for_color[1]
for pos_lens in possible_len_for_color.values():
    pos_lengths_intersection = pos_lengths_intersection.intersection(pos_lens)


def get_bricks_nums(possible_lens: defaultdict[list], needed_len):
    bricks_nums = set()
    for color_num in possible_lens:
        current_len = needed_len
        last_needed_brick = possible_lens[color_num][current_len]
        while last_needed_brick != 0:
            bricks_nums.add(last_needed_brick)
            current_len -= bricks_len[last_needed_brick - 1]
            last_needed_brick = possible_lens[color_num][current_len]
    return bricks_nums


if len(pos_lengths_intersection) >= 2:
    print("YES")
    needed_bricks_nums = get_bricks_nums(
        possible_len_to_get_bricks_num, min(pos_lengths_intersection)
    )
    for num in needed_bricks_nums:
        print(num)
else:
    print("NO")
