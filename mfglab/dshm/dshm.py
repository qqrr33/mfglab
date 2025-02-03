from multiprocessing import shared_memory
import numpy as np

from mfglab.config.log import logger

# 향 후에 3ch bmp파일을 위한 다차원 배열도 지원할 수 있도록 수정할 것

class WriteMemory:
    def __init__(self, name: str, data: np.ndarray) -> None:
        '''
        dynamic shared memory write\n
        name is shared memory address\n
        np.int64 is slow but it is the most stable and useful data type\n
        '''
        assert isinstance(data, np.ndarray), "data should be list or numpy array"
        
        self.shm = None
        self.name = name
        self.data = data
        self.size = len(self.data)
    
    def write(self) -> None:
        self.shm = shared_memory.SharedMemory(name=self.name, create=True, size=self.size * np.int64().nbytes)
        np_array = np.ndarray((self.size,), dtype=np.int64, buffer=self.shm.buf)
        np_array[:] = self.data
        logger.info(f"write shared memory: {self.name} (data array size: {self.size})")
        
    def close(self) -> None:
        self.shm.close()
        self.shm.unlink()
        logger.info(f"unlink shared memory: {self.name}")


class ReadMemory:
    def __init__(self, name: str, size: int) -> None:
        '''
        dynamic shared memory read\n
        name is shared memory address\n
        size is data array size
        '''
        assert isinstance(size, int), "size should be integer"
        self.name = name
        self.size = size
    
    def read(self) -> np.ndarray:
        shm = shared_memory.SharedMemory(name=self.name)
        np_array = np.ndarray((self.size,), dtype=np.int64, buffer=shm.buf)
        np_array = np.copy(np_array)    # copy to prevent shared memory delete at close shm
        shm.close()
        logger.info(f"read shared memory: {self.name}")
        return np_array
    