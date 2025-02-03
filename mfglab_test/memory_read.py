from mfglab.dshm.dshm import ReadMemory

read_memory = ReadMemory(name="test_memory", size=10)
data = read_memory.read()

print(data)


