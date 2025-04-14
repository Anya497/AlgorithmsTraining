sub_num, max_weight = tuple(map(lambda x: int(x), input().split()))
sub_weights = list(map(lambda x: int(x), input().split()))
sub_price = list(map(lambda x: int(x), input().split()))
processed_weights = [-1] * (max_weight + 1)
processed_weights[0] = 0
for sub_idx, sub_weight in enumerate(sub_weights):
    for current_weight, last_sub_number in enumerate(processed_weights[::-1]):
        current_weight = max_weight - current_weight
        if last_sub_number != -1:
            new_weight = current_weight + sub_weight
            if new_weight <= max_weight:
                if (
                    processed_weights[new_weight] == -1
                    or sub_price[sub_idx] + processed_weights[current_weight]
                    > processed_weights[new_weight]
                ):
                    processed_weights[new_weight] = (
                        sub_price[sub_idx] + processed_weights[current_weight]
                    )

while processed_weights[max_weight] == -1:
    max_weight -= 1

print(max(processed_weights))
