from itertools import permutations

post_office = [(0, 2)]
points = [(2, 5), (5, 2), (6, 6), (8, 3)]


def distance(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


min_length = float('inf')
min_way = None

for perm in permutations(points):
    length = 0
    current_perm = post_office + list(perm) + post_office

    for i in range(len(current_perm) - 1):
        first_point = current_perm[i]
        second_point = current_perm[i + 1]
        length += distance(first_point, second_point)

    if min_length > length:
        min_length = length
        min_way = current_perm

length = 0
print(min_way[0], end=' -> ')

for i in range(len(min_way) - 1):
    first_point = min_way[i]
    second_point = min_way[i + 1]
    length += distance(first_point, second_point)

    if (i + 2) == len(min_way):
        end = ' = '
    else:
        end = ' -> '
    print(second_point, length, end=end)

print(min_length)
