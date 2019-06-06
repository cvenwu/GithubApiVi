# 查看键是否在字典中已经存在
data_dict = {
    '1' : 'java',
    '2' : 'python'
}
print('1' in data_dict.keys())

data_language = {
    'java' : 1,
    'python' : 2
}
print(data_language)
data_language['java'] += 1
print(data_language)


import numpy as np
data_array = np.array([[1, 2], [3, 4], [5, 6]])
print(data_array)
print(data_array.shape)
print(type(data_array.shape))

import matplotlib.pyplot as plt
arr1 = np.array([6, 6])
arr2 = np.array([1, 2])
plt.plot(arr1, arr2)
plt.show()