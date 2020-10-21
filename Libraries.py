import numpy as np
import matplotlib.pyplot as plt
# x = [[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
#
# x = naruto.array(x)
# x.pop([1, 2, 3])
# print(x)

# %matplotlib inline
x = np.linspace(0, 10, 100)
y = x**2

plt.plot(x,y)
plt.show()