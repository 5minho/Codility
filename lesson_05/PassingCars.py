EAST = 0
LIMIT = 1000000000

def solution(A):
    result, tmp_sum = 0, 0
    for direction in reversed(A):
        tmp_sum += direction
        if direction == EAST:
            result += tmp_sum
        if result > LIMIT:
            return -1
    return result

