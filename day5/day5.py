import math


def binary_search(boarding_pass):
    lower = 0
    upper = 2**len(boarding_pass)
    mid = math.floor((upper + lower) / 2)

    for letter in boarding_pass:
        if letter == 'F' or letter == 'L':
            upper = mid
        elif letter == 'B' or letter == 'R':
            lower = mid
        mid = math.floor((upper + lower) / 2)

    return mid


def get_seat_id(row, col):
    return row * 8 + col


with open('./day5/day5.txt', 'r') as f1:
    boarding_passes = f1.read().splitlines()


# part 1
max = 0
for boarding_pass in boarding_passes:
    row = binary_search(boarding_pass[:7])
    col = binary_search(boarding_pass[-3:])
    seat_id = get_seat_id(row, col)
    if seat_id > max:
        max = seat_id


# part 2
seat_ids = [0] * (max + 1)
for boarding_pass in boarding_passes:
    row = binary_search(boarding_pass[:7])
    col = binary_search(boarding_pass[-3:])
    seat_id = int(get_seat_id(row, col))
    seat_ids[seat_id] = seat_id

import numpy as np
seat_ids = np.asarray(seat_ids)
my_seat = np.argwhere(seat_ids == 0)[11:]
