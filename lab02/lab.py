import numpy as np
import matplotlib.pyplot as plt
import scipy


# x(t) = A sin (frecv * t + faza)
def ex1():

    t = np.arange(0, 1, 0.0005)

    def semnal1(timp):
        ampl = 2
        fs = 10
        faza = np.pi/2
        return ampl * np.sin(fs * np.pi * timp + faza)
    def semnal2(timp):
        ampl = 2
        fs = 10
        faza = 0
        return ampl * np.cos(fs * np.pi * timp + faza)

    plt.figure(1)
    plt.subplot(3, 1, 1)
    plt.plot(t, semnal1(t))
    plt.grid()
    plt.title("Semnal sinusoidal")

    plt.subplot(3, 1, 2)
    plt.plot(t, semnal2(t), c='red')
    plt.title("Semnal cosinusoidal")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, semnal1(t), c='blue')
    plt.plot(t, semnal2(t), c='purple')
    plt.grid()
    plt.title("Combinate")

    plt.show()


def ex2():
    t = np.arange(0, 1, 0.005)
    def f(faza):
        ampl = 2
        fs = 5
        return ampl * np.cos(fs * np.pi * t + faza)

    # Faze alese la alegere
    faze = [np.pi / 4, 2 * np.pi / 4, 3 * np.pi / 4, np.pi]

    # Construirea celor 4 semnale
    semnale = [f(faza) for faza in faze]

    # Generarea zgomotului folosind Distributia Gaussiana
    z = np.random.normal(0, 1, len(t))

    snr = [0.1, 1, 10, 100]

    for i, snr in enumerate(snr):
        # gamma^2  =  norma (x) ^ 2 / norma (z) ^ 2 * SNR
        gamma = np.sqrt(np.linalg.norm(semnale[i]) ** 2 / (np.linalg.norm(z) ** 2 * snr))
        semnal_zgomot = semnale[i] + gamma * z
        plt.subplot(4, 1, i + 1)
        plt.plot(t, semnal_zgomot)

    plt.grid()
    plt.show()


def ex4():
    pass


if __name__ == '__main__':
    # ex1()
    ex2()
