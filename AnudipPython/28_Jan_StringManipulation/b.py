def character_frequency_analysis(s):
    s = s.replace(" ", "").lower()  
    freq_dict = {} 
    
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1  
        else:
            freq_dict[char] = 1  
    most_common_char = max(freq_dict, key=freq_dict.get)
    return {'Character': most_common_char, 'Frequency': freq_dict[most_common_char]}

input_string = "This is a test sentence"
print(character_frequency_analysis(input_string))
