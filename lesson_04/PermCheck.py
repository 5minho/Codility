def solution(A):
    occurs = {}
    maximum = len(A)
    minimum = 1
    for item in A:
        if item in occurs or (minimum <= item <= maximum) == False:
            return 0
        occurs[item] = True
    else:
        return 1
