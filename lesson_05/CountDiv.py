def solution(A, B, K):
    # (0 ~ B 까지 K 배수 개수) - (0 ~ (A - 1) 까지 K 배수 개수)
    return (B // K) - ((A - 1) // K)

