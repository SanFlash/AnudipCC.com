my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sub_list = my_list[1:4]
print("Extracted Sublist:", sub_list)

my_list[3] = 'x'
print("List after replacing 'd' with 'x':", my_list)

my_list.remove('g')  
my_list.append('z') 

print("Final List:", my_list)
