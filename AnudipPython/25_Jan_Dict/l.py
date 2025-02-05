keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

zipped_dict = {k: v for k, v in zip(keys, values)}
print(zipped_dict)
