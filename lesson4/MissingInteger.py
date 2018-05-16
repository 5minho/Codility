def solution(A):
    should_occurs_elem_set = set(range(1, len(A) + 1))
    for elem in A:
        if elem in should_occurs_elem_set:
            should_occurs_elem_set.remove(elem)
    return min(should_occurs_elem_set) \
        if len(should_occurs_elem_set) != 0 \
        else len(A) + 1
