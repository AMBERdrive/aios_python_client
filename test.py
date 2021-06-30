import aios
import time
import threading
import numpy as np
import json
import struct

data = b'\xe7\xc0\xc0\x41'


print(data) 

print(struct.unpack('<i', data))
        