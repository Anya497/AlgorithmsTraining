tests_num = int(input())


def cut_array(data):
    len_segments = list()
    current_segment_len, current_min_elem = 0, len(data)
    for elem in data:
        if (
            current_segment_len + 1 <= elem
            and current_segment_len + 1 <= current_min_elem
        ):
            current_segment_len += 1
            if elem < current_min_elem:
                current_min_elem = elem
        else:
            len_segments.append(current_segment_len)
            current_segment_len, current_min_elem = 1, elem
    len_segments.append(current_segment_len)
    return len_segments


for _ in range(tests_num):
    _ = input()
    data = list(map(lambda x: int(x), input().split()))
    len_segments = cut_array(data)
    print(len(len_segments))
    print(" ".join(list(map(lambda x: str(x), len_segments))))
