import numpy as np
import matplotlib.pyplot as plt


def x(t):
    return np.cos(520 * np.pi * t + np.pi/3)

def y(t):
    return np.cos(280 * np.pi * t - np.pi/3)

def z(t):
    return np.cos(120 * np.pi * t + np.pi/3)

# a)
t = np.arange(0, 0.03, 0.0005)

# b)
def b():
    plt.figure(0)
    plt.subplot(3, 1, 1)
    plt.plot(t, x(t))
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(t, y(t))
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, z(t))
    plt.grid()


# c)
def c():
    fs = 200    # Frecventa de Esantionare (200Hz)
    ts = 1/fs   # Perioada de esantionare

    N = np.arange(0, 0.03, ts)
    
    # plt.subplot(3, 1, 1)
    plt.figure(1)
    plt.stem(N, x(N))
    plt.plot(t, x(t))
    plt.grid()
    plt.ylabel('x(t)')

    plt.figure(2)
    plt.stem(N, y(N))
    plt.plot(t, y(t))
    plt.grid()
    plt.ylabel('y(t)')
    
    plt.figure(3)
    plt.stem(N, z(N))
    plt.plot(t, z(t))
    plt.grid()
    plt.ylabel('z(t)')

if __name__ == '__main__':
    b()
    c()
    plt.show()


