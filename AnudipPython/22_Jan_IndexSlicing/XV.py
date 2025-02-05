special_text = "Hello@$%& World!!!"

clean_text = ""
for char in special_text:
    if char.isalnum() or char == " ":
        clean_text += char
print("Cleaned text:", clean_text)
