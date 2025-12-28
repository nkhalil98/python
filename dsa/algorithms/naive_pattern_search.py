"""
Naive Pattern Search
"""

from __future__ import annotations


def pattern_search(text, pattern):
    if not text or not pattern:
        return -1

    n = len(text)
    m = len(pattern)

    if n < m:
        return -1

    for i in range(n - m + 1):
        for j in range(m):
            if pattern[j] != text[i + j]:
                break
        else:
            return i

    return -1


def pattern_search_chunk(text, pattern):
    if not text or not pattern:
        return -1

    n = len(text)
    m = len(pattern)

    if n < m:
        return -1

    for i in range(n - m + 1):
        chunk = text[i : i + m]
        if chunk == pattern:
            return i

    return -1
