# https://www.hackerrank.com/challenges/string-function-calculation/problem?isFullScreen=true

import os
from itertools import zip_longest, islice


def suffix_array_best(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),
                         fillvalue=-1)])
        k <<= 1
    return line

def inverse_array(l):
    n = len(l)
    ans = [0] * n
    for i in range(n):
        ans[l[i]] = i
    return ans


def to_int_keys_best(l):
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_matrix_best(s):
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    ans = [line]
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None), fillvalue=-1)])
        ans.append(line)
        k <<= 1
    return ans

def suffix_array_alternative_naive(s):
    return [rank for suffix, rank in sorted((s[i:], i) for i in range(len(s)))]

def lcp(sm, i, j):
    n = len(sm[-1])
    if i == j:
        return n - i
    k = 1 << (len(sm) - 2)
    ans = 0
    for line in sm[-2::-1]:
        if i >= n or j >= n:
            break
        if line[i] == line[j]:
            ans ^= k
            i += k
            j += k
        k >>= 1
    return ans


def maxValue(a):
    res = inverse_array(suffix_array_best(a))
    # res = suffix_array_alternative_naive(a)

    mtx = suffix_matrix_best(a)

    lcp_res = []
    for n in range(len(res) - 1):
        lcp_res.append(lcp(mtx, res[n], res[n+1]))
    lcp_res.append(0)

    max_score = len(a)

    lcp_res_len = len(lcp_res)

    for i, num in enumerate(res):

        if lcp_res[i] <= 1:
            continue

        lcp_res_i = lcp_res[i]

        cnt = 2
        for ii in range(i+1, lcp_res_len):
            if lcp_res[ii] >= lcp_res_i:
                cnt += 1
            else:
                break
        for ii in range(i-1, -1, -1):
            if lcp_res[ii] >= lcp_res_i:
                cnt += 1
            else:
                break

        max_score = max(cnt * lcp_res_i, max_score)

    return max_score
