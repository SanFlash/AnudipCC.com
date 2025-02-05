mixed_string = "Python3.8 is awesome!"

digits = ""
for char in mixed_string:
    if char.isdigit() or char == ".":
        digits += char
print("Extracted digits:", digits)

letters = ""
for char in mixed_string:
    if char.isalpha():
        letters += char
print("Extracted letters:", letters)
