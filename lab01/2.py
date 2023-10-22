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

    # Parametrii semnalului
    frequency = 240  # Frecvența semnalului (Hz)
    amplitude = 1  # Amplitudinea semnalului
    duration = 0.025  # Durata semnalului (secunde)
    sample_rate = 2400  # Rata de eșantionare (esantioane pe secunda)

    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    sawtooth_wave = amplitude * \
        (2 * (t * frequency - np.floor(t * frequency + 0.5)))

    plt.plot(t, sawtooth_wave)
    plt.grid()
    plt.show()


def d():
    # Un semnal de tip square de frecventa 300Hz

    # Parametrii semnalului
    frequency = 300
    amplitude = 2
    duration = 0.05
    sample_rate = 3000

    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    square_wave = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))

    plt.plot(t, square_wave)
    plt.grid()
    plt.show()


def e():
    # Un semnal 2D aleator

    x, y = 128, 128

    signal_2d = np.random.rand(x, y)
    print(signal_2d)

    plt.imshow(signal_2d)
    plt.colorbar()
    plt.title('Semnal 2D Aleator')
    plt.show()


def f():
    # Un semnal 2D la alegere

    x, y = 128, 128

    signal_2d = np.zeros((x, y))

    # Tabla de sah
    box_width = 16
    for i in range(x):
        for j in range(y):
            if (i // box_width) % 2 != (j // box_width) % 2:
                signal_2d[i, j] = 1.0

    # Afisarea semnalului
    plt.imshow(signal_2d, cmap='gray', origin='lower', extent=[0, x, 0, y])
    plt.colorbar()
    plt.title('Semnal 2D Personalizat')
    plt.show()


if __name__ == '__main__':
    # a()
    # b()
    # c()
    # d()
    # e()
    f()
