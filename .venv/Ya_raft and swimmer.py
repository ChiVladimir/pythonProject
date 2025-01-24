# swimmer - x, y,
# corners - ”NW” - x_3, y_3 (unknown), ”NE” - x_2, y_2, ”SW” - x_1,y_1, ”SE” - x_4, y_4 (unknown)
# sides (all unknowns) - S - x_11, y_11, E - x_12, y_12, N - x_13, y_13, W - x_14, y_14
import math

def raft_corn_coord(x_1, y_1, x_2, y_2):
    return x_1, y_2, x_2, y_1,

def raft_side_coord(x_1, y_1, x_2, y_2):
    x_11 = x_2 - (x_2 + (-1 * x_1) / 2)
    y_11 = y_1
    x_12 = x_2
    y_12 = y_2 - (y_2 + (-1 * y_1) / 2)
    x_13 = x_2 - (x_2 + (-1 * x_1) / 2)
    y_13 = y_2
    x_14 = x_1
    y_14 = y_2 - (y_2 + (-1 * y_1) / 2)

    return x_11, y_11, x_12, y_12, x_13, y_13, x_14, y_14

def distance(x, y, x_n, y_n):
    return math.sqrt((x_n - x)** 2+(y_n - y)** 2)

def shortest_dist(dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
    if dist_SW == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "SW"
    elif dist_NE == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "NE"
    elif dist_NW == min(dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "NW"
    elif dist_SE == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "SE"

    elif dist_S == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "S"
    elif dist_E == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "E"
    elif dist_N == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "N"
    elif dist_W == min (dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W):
        return "W"
    else:
        return "Утонул"

x_1 = int(input())
y_1 = int(input())
x_2 = int(input())
y_2 = int(input())
x = int(input())
y = int(input())

x_3, y_3, x_4, y_4 = raft_corn_coord(x_1, y_1, x_2, y_2)
x_11, y_11, x_12, y_12, x_13, y_13, x_14, y_14 = raft_side_coord(x_1, y_1, x_2, y_2)


dist_SW = distance(x, y, x_1, y_1)
dist_NE = distance(x, y, x_2, y_2)
dist_NW = distance(x, y, x_3, y_3)
dist_SE = distance(x, y, x_4, y_4)
dist_S = distance(x, y, x_11, y_11)
dist_E = distance(x, y, x_12, y_12)
dist_N = distance(x, y, x_13, y_13)
dist_W = distance(x, y, x_14, y_14)

print(shortest_dist(dist_SW, dist_NE, dist_NW, dist_SE, dist_S, dist_E, dist_N, dist_W))
#shortest_dist(dist_SW, dist_NE, dist_NW, dist_SE)
