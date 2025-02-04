import numpy as np
from mfglab.dshm.dshm import WriteMemory

# setting data for ndarray
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = np.array(data, dtype=np.int32)

write_memory = WriteMemory(name="test_memory", data=data)
write_memory.write()

input("if you want to close, press Enter...")

# must be closed after using, because of leak memory
write_memory.close()



