sub_num, max_weight = tuple(map(lambda x: int(x), input().split()))
sub_weights = list(map(lambda x: int(x), input().split()))
sub_price = list(map(lambda x: int(x), input().split()))
processed_weights = list()
# (last_sub, price)
for_first_sub = [(-1, -1)] * (max_weight + 1)
for_first_sub[0] = (0, 0)
processed_weights.append(for_first_sub)

for sub_idx, sub_weight in enumerate(sub_weights):
    for current_weight, last_sub_number in enumerate(processed_weights[sub_idx][::-1]):
        current_weight = max_weight - current_weight
        if last_sub_number != -1:
            new_weight = current_weight + sub_weight
            if new_weight <= max_weight:
                if (
                    processed_weights[sub_idx][new_weight] == (-1, -1)
                    or sub_price[sub_idx]
                    + processed_weights[sub_idx][current_weight][1]
                    > processed_weights[sub_idx][new_weight][1]
                ):
                    processed_weights[sub_idx][new_weight] = (
                        sub_idx + 1,
                        sub_price[sub_idx]
                        + processed_weights[sub_idx][current_weight][1],
                    )
    if sub_idx < sub_num - 1:
        processed_weights.append(processed_weights[sub_idx].copy())

not_used_subs = list(range(1, sub_num + 1))
current_sub_idx = sub_num - 1
last_sub_idx, max_price = max(processed_weights[current_sub_idx], key=lambda x: x[1])
current_weight = processed_weights[last_sub_idx - 1].index((last_sub_idx, max_price))
result = list()

while last_sub_idx != 0:
    result.append(last_sub_idx)
    not_used_subs.remove(last_sub_idx)
    if not_used_subs:
        current_sub_idx = not_used_subs[-1]
    else:
        break
    c = processed_weights[current_sub_idx - 1][current_weight - sub_weights[last_sub_idx - 1]]

    current_weight = current_weight - sub_weights[last_sub_idx - 1]
    last_sub_idx = c[0]

for i in result[::-1]:
    print(i)
