def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print("Are 'listen' and 'silent' anagrams? :", are_anagrams("listen", "silent"))
