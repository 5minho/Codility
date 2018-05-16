def solution(A):
    left_sum, right_sum = A[0], sum(A[1:])
    result = abs(left_sum - right_sum)
    for x in range(1, len(A) - 1):
        left_sum, right_sum = left_sum + A[x], right_sum - A[x]
        result = min(result, abs(left_sum - right_sum))
    return result
