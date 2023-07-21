# pylint: disable-all

import numpy as np

sample_list = np.array(["cat", "pig", "cat"])


cleaned_array = np.unique(sample_list)


print(cleaned_array)