"""
Naive Pattern Search
"""

from __future__ import annotations


def pattern_search(text, pattern):  # O(n*m): n = len(text), m = len(pattern)
    if not text or not pattern:
        return -1

    n = len(text)
    m = len(pattern)
    if n < m:
        return -1

    for i in range(n - m + 1):  # O(n)
        for j in range(m):  # O(m)
            if pattern[j] != text[i + j]:
                break
        else:
            return i  # return the index of the first match
    return -1
