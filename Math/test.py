import numpy as np

a = np.array([0,1,2,3,4,5])
c = np.array([-5,-2,11,46,115,230])
b = np.polyfit(a, c,5)
print(b)
