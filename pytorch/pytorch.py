import torch
import numpy as np
a = np.ones(6)
b = torch.from_numpy(a)
np.add(a,1,out=a)
print(a)
print(b)