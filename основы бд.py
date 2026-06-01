import numpy as np
data = np.loadtxt("minutes_n_ingredients.csv", delimiter=",", dtype=np.int32, skiprows=1)
print(data[:5])



import numpy as np
np.set_printoptions(threshold=np.inf)
data = np.loadtxt("minutes_n_ingredients.csv", delimiter=",", dtype=np.int32, skiprows=1)
st_1 = np.array(data)
st_11 = st_1[:,0]
print(st_11)