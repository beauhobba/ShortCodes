# pylint: disable-all


sample_list = ["cat", "pig", "cat"]

cleaned_list = [item for index, item in enumerate(sample_list) if item not in sample_list[:index]]

# print(sample_list[:0])
# print(sample_list[:1])
# print(sample_list[:2])

for index, item in enumerate(sample_list):
    print(item)
    print(sample_list[:index])
    
    
    
print(cleaned_list)