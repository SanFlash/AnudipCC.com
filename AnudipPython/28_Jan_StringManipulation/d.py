def find_anagrams(word, lst):
    sorted_word = sorted(word)
    return [w for w in lst if sorted(w) == sorted_word]

word = "listen"
lst = ['enlist', 'google', 'inlets', 'banana']
print(find_anagrams(word, lst)) 
