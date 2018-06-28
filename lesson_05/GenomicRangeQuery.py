'''
reference :
    https://github.com/johnmee/codility,
    https://github.com/michael-lazar/codility/blob/master/problems/Genomic-range-query.py

'''

def solution(S, P, Q):
    M = {
        'A' : 1,
        'C' : 2,
        'G' : 3,
        'T' : 4,
    }
    recent = [[-1] for i in range(4)]
    for i, s in enumerate(S):
        for j in range(4):
            if M[s] == j + 1:
                recent[j].append(i)
            else:
                recent[j].append(recent[j][-1])
    result = []
    for p, q in zip(P, Q):
        a = min(j for j in range(4) if recent[j][q + 1] >= p)
        result.append(a + 1)
    return result

