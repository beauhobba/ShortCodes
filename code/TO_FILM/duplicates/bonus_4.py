# pylint: disable-all


sample_list = ["cat", "pig", "cat"]

cleaned_list = [] 
[cleaned_list.append(item)
 for item in sample_list
 if item not in cleaned_list]



print(cleaned_list)