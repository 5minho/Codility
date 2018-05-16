def solution(X, A):
    positions = {}
    for time, pos in enumerate(A):
        positions[pos] = True
        if len(positions) == X:
            return time
    else:
        return -1

