N_groups, M_rooms = tuple(map(lambda x: int(x), input().split()))
groups = list(map(lambda x: (x[0], int(x[1]) + 1), enumerate(input().split())))
rooms = list(map(lambda x: int(x), input().split()))

groups.sort(key=lambda x: x[1], reverse=True)
groups_in_rooms = [0] * N_groups


def find_room_for(st_num, free_rooms):
    for room_num, comp_num in enumerate(free_rooms, start=1):
        if comp_num >= st_num and comp_num != -1:
            return room_num
    return None


for group_num, st_num in groups:
    room_num = find_room_for(st_num, rooms)
    if room_num:
        groups_in_rooms[group_num] = room_num
        rooms[room_num - 1] = -1

print(len([room_num for room_num in groups_in_rooms if room_num != 0]))
print(" ".join(list(map(lambda x: str(x), groups_in_rooms))))
