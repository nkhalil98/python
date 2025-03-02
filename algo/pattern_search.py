def pattern_search(text, pattern):
    for i in range(len(text)):
        match_count = 0
        for j in range(len(pattern)):
            if pattern[j] == text[i + j]:
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print(f"{pattern} found at index {i}")
