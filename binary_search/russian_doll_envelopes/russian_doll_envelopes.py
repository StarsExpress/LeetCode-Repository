from bisect import bisect_left


def count_max_envelopes(envelopes: list[list[int]]) -> int:  # LeetCode Q.354.
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    russian_doll_envelopes = []
    
    for _, height in envelopes:
        insertion_idx = bisect_left(russian_doll_envelopes, height)
        if insertion_idx == len(russian_doll_envelopes):
            russian_doll_envelopes.append(height)
            continue
        
        russian_doll_envelopes[insertion_idx] = height
        
    return len(russian_doll_envelopes)
