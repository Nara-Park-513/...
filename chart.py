#파이선 시각화 사용하는데 명칭이 길어서 별칭으로 사용함
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])

plt.pie(y)
plt.show()