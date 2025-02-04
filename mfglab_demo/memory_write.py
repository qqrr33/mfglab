from mfglab.dshm.dshm import WriteMemory

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
write_memory = WriteMemory(name="test_memory", data=data)
# write_memory.open()
write_memory.write()

input("if you want to close, press Enter...")

write_memory.close()



