import numpy as np
import matplotlib.pyplot as plt

# a)
def a():
    # Semnal sinusoidal de 400Hz
    # Frecventa de esantionare de 1600Hz

    timp = np.arange(0, 4, 1/1600)
    semnal = np.sin(2 * np.pi * 400 * timp)

    plt.plot(timp, semnal)
    plt.grid()
    plt.show()

def b():
    # Un semnal sinusoidal de frecventa 800Hz care sa dureze 3 secunde

    timp = np.arange(0, 3, 1/2400)
    semnal = np.sin(2 * np.pi * 800 * timp)

    plt.plot(timp, semnal)
    plt.grid()
    plt.show()

def c():
    # Un semnal de tip sawtooth de frecventa 240Hz
    pass

if __name__ == '__main__':
    # a()
    # b()
    c()

