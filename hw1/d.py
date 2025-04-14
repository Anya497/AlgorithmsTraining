gold_num, max_weight = tuple(map(lambda x: int(x), input().split()))
gold_weights = list(map(lambda x: int(x), input().split()))
processed_weights = [-1] * (max_weight + 1)
processed_weights[0] = 0
for gold_idx, gold_weight in enumerate(gold_weights):
    for current_weight, last_gold_number in enumerate(processed_weights[::-1]):
        current_weight = max_weight - current_weight
        if last_gold_number != -1:
            new_weight = current_weight + gold_weight
            if new_weight <= max_weight:
                if processed_weights[new_weight] == -1:
                    processed_weights[new_weight] = gold_idx
while processed_weights[max_weight] == -1:
    max_weight -= 1

print(max_weight)
