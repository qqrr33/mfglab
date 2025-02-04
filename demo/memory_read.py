import numpy as np
from mfglab.dshm.dshm import ReadMemory

dtype = np.int64
read_memory = ReadMemory(name="test_memory", dtype=dtype, arr_size=10)
data = read_memory.read()

print(type(data))
print(data)


