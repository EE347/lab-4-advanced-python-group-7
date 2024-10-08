import numpy as np


x = np.linspace(0, 10, 101)
print(x)
sine_wave = np.sin(x)
cosine_wave = np.cos(x)
np.save("task7_sin.npy", sine_wave)
np.save("task7_cos.npy", cosine_wave)