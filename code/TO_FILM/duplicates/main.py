# pylint: disable-all


sample_list = ["cat", "pig", "cat"]

cleaned_list = [item 
                for index, item in
                enumerate(sample_list) 
                if item not in sample_list[:index]]

    
print(cleaned_list)