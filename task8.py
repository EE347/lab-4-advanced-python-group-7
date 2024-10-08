import numpy as np
import matplotlib.pyplot as plt

cosine = np.load('task7_cos.npy')
sine = np.load('task7_sin.npy')

plt.plot(cosine, label='Cosine Wave')
plt.plot(sine, label='Sine Wave')
plt.legend()
plt.show()
