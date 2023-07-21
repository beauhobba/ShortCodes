# pylint: disable-all


sample_list = ["cat", "pig", "cat"]


cleaned_list = list(dict.fromkeys(sample_list))


print(cleaned_list)