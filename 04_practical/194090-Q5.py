def count_char_frequencies(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

s = "data structures and algorithms"
freqs = count_char_frequencies(s)

for char, count in freqs.items():
    print(f"'{char}': {count}")