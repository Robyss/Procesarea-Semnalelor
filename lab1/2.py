import numpy as np
import matplotlib.pyplot as plt

# a)
fs = 400    # Frecventa de Eșantionare (400Hz)
N = 1600    # Numărul de Eșantioane
ts = N / fs # Perioada de Eșantionare

t = np.arange(0, N/fs, 1/fs)
