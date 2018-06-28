def solution(N, A):
    result = [0] * (N + 1)
    cur_max, prev_max = 0, 0
    for x in A:
        if x == N + 1:
            prev_max = cur_max
            continue
        result[x] = max(prev_max, result[x])
        result[x] += 1
        cur_max = max(cur_max, result[x])
    for i in range(N + 1):
        result[i] = max(prev_max, result[i])
    return result[1:]

'''
원래 prev_max 변수를 쓰지 않고 5번 라인에서 x 가 N+1이 되었을때 
result 리스트를 [cur_max] * (N + 1) 로 할당하여 새로운 리스트로 교체 했었음, 
그 결과 새로운 리스트를 생성하고 할당하는 작업 때문인지 퍼포먼스 점수가 80점이
나왔음 https://github.com/johnmee/codility 이 분께서 하신 코드를 참고해
prev_max 변수를 추가해 result 의 이전 최대값을 같이 저장해서,
마지막 한번만 result를 순회하는 방식으로 반복적인 result 할당을 막았더니
100점이 나왔음
'''
