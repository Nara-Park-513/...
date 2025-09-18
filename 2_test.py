import matplotlib.pyplot as plt 
#파이플롯라이브러리를 불러옴 별칭 plt설정
import numpy as np

xpoints = np.array([0, 6])#x좌표
ypoints = np.array([0, 250])#y좌표

plt.plot(xpoints, ypoints)
plt.show()