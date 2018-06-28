'''
증명 : 
    https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf
'''
def solution(A):
    N = len(A)
    min_avg_slice = 10000
    start_of_slice = 0
    
    def start_and_avg_min_of_slice(s, n, current_start, current_min):
        temp_min = sum(A[s: s+n]) / n
        if temp_min < current_min:
            return (s, temp_min)
        else:
            return (current_start, current_min)
            
    for start in range(0, N - 1):
        start_of_slice, min_avg_slice = start_and_avg_min_of_slice(start, 2,
                                                                   start_of_slice, min_avg_slice)
        if start + 2 < N:
            start_of_slice, min_avg_slice = start_and_avg_min_of_slice(start, 3,
                                                                      start_of_slice, min_avg_slice)
            
    return start_of_slice
