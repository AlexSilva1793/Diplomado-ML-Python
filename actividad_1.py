#importamos numpy
import numpy as np

dias = np.arange(35, dtype=np.int64).reshape(5, 7)
referencias = np.arange(35, dtype=np.int64).reshape(5, 7)

for i in range(len(dias)):
    for t in range(7):
        dias[i, t]=0
        pass

for i in range(len(referencias)):
    for t in range(7):
        referencias[i, t]=0
        pass

if __name__=='__main__':
    pass

