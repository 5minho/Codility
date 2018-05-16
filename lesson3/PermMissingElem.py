def solution(A):
    appear_set = set(range(1, len(A) + 2))
    return (appear_set - set(A)).pop()
