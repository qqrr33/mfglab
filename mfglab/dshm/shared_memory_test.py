# Python
from multiprocessing import shared_memory
import numpy as np

from mfglab.config.log import logger


class WriteMemory:
    def __init__(self, name: str, size: int, data: list | np.ndarray) -> None:
        assert isinstance(size, int), "size should be integer"
        assert isinstance(data, (list, np.ndarray, tuple)), "data should be list or numpy array"
        
        self.shm = None
        self.name = name
        self.size = size
        self.data = data
        
    def write(self) -> None:
        self.shm = shared_memory.SharedMemory(name=self.name, create=True, size=self.size * np.int32().nbytes)
        np_array = np.ndarray((self.size,), dtype=np.int32, buffer=self.shm.buf)
        np_array[:] = self.data
        logger.info(f"write shared memory :\n{self.data}")
        
    def close(self) -> None:
        self.shm.close()
        self.shm.unlink()


class ReadMemory:
    def __init__(self, name: str, size: int) -> None:
        assert isinstance(size, int), "size should be integer"
        self.shm = None
        self.name = name
        self.size = size
    
    def read(self) -> np.ndarray:
        self.shm = shared_memory.SharedMemory(name=self.name)
        np_array = np.ndarray((self.size,), dtype=np.int32, buffer=self.shm.buf)
        
        return np_array
        
    def close(self) -> None:
        self.shm.close()