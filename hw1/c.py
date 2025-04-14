num_secs = int(input())
prices = [-1] * (num_secs + 1)
prices[0] = 0
rate_secs = list(map(lambda x: int(x), input().split()))[:num_secs]
for sec_idx, sec in enumerate(rate_secs):
    for secs, min_price in enumerate(prices):
        if min_price != -1:
            new_secs_num = secs + sec
            if new_secs_num > num_secs:
                new_secs_num = num_secs
            new_price = min_price + 2**sec_idx
            if prices[new_secs_num] > new_price or prices[new_secs_num] == -1:
                prices[new_secs_num] = new_price

print(prices[-1])
