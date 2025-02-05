def string_compression(s):
    lis = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            lis.append(s[i-1] + str(count))
            count = 1
    lis.append(s[-1] + str(count))
    return ''.join(lis)

input_string = "aaabbccca"
print(string_compression(input_string)) 
