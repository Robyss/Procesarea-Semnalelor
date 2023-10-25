import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import sounddevice


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
    print(z)
    snr = [0.1, 1, 10, 100]

    for i, snr in enumerate(snr):
        # gamma^2  =  norma (x) ^ 2 / norma (z) ^ 2 * SNR
        gamma = np.sqrt(np.linalg.norm(semnale[i]) ** 2 / (np.linalg.norm(z) ** 2 * snr))
        semnal_zgomot = semnale[i] + gamma * z
        plt.subplot(4, 1, i + 1)
        plt.plot(t, semnal_zgomot)

    plt.grid()
    plt.show()


def ex3():
    rate = int(10e5)

    # Semnal sinusoidal de 400Hz cu frecventa de esantionare de 1600Hz
    t1 = np.arange(0, 4, 1/1600)
    s1 = np.sin(2 * np.pi * 400 * t1)

    scipy.io.wavfile.write('s1.wav', rate, s1)
    # rate, x = scipy.io.wavfile.read('s1.wav')

    # sounddevice.play(s1, 44100)
    # sounddevice.wait()

    # Un semnal sinusoidal de frecventa 800Hz care sa dureze 3 secunde
    t2 = np.arange(0, 3, 1/2400)
    s2 = np.sin(2 * np.pi * 800 * t2)

    # sounddevice.play(s2, 2400)
    # sounddevice.wait()

    # Un semnal de tip sawtooth de frecventa 240Hz

    # Parametrii semnalului
    frequency = 240  # Frecvența semnalului (Hz)
    amplitude = 1  # Amplitudinea semnalului
    duration = 1.0  # Durata semnalului (secunde)
    sample_rate = 2400  # Rata de eșantionare (esantioane pe secunda)

    t3 = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    s3 = amplitude * \
        (2 * (t3 * frequency - np.floor(t3 * frequency + 0.5)))
    
    # sounddevice.play(s3, 2400)
    # sounddevice.wait()


    # Un semnal de tip square de frecventa 300Hz

    # Parametrii semnalului
    frequency = 300
    amplitude = 2
    duration = 0.5
    sample_rate = 3000

    t4 = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    s4 = amplitude * np.sign(np.sin(2 * np.pi * frequency * t4))

    sounddevice.play(s4, 3000)
    sounddevice.wait()



def ex4():
    fr_cos = 400
    frequency = 240
    amplitude = 2
    duration = 0.05
    sample_rate = 2400


    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

    s1 = amplitude * np.cos(2 * np.pi * fr_cos * t)
    s2 = amplitude * 2 * (t * frequency - np.floor(t * frequency + 0.5))

    s = s1 + s2

    plt.subplot(3, 1, 1)
    plt.plot(t, s1)
    plt.grid()
    plt.title("Semnal sinusoidal")

    plt.subplot(3, 1, 2)
    plt.plot(t, s2, c='red')
    plt.title("Semnal sawtooth")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(t, s, c='purple')
    plt.grid()
    plt.title("Suma semnalelor")

    plt.show()


def ex5():
    freq1 = 400
    freq2 = 240
    amplitude = 2
    duration = 2
    sample_rate = 2400

    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    signal1 = amplitude * np.sin(2 * np.pi * freq1 * t)
    signal2 = amplitude * np.sin(2 * np.pi * freq2 * t)

    signal = np.append(signal1, signal2)

    sounddevice.play(signal, 2400)
    sounddevice.wait()


def ex6():

    # Observ ca nu am destule esantioane pentru a
    # reprezenta corect semnalul de frecventa fs/2. 
    # Semnalul fs/4 este reprezentat corect, iar semnalul
    # de frecventa 0 Hz este reprezentat ca o dreapta

    fs = 800   # Frecventa de esantionare
    durata = 1  # Durata semnalului
    amplitudine = 1

    t = np.linspace(0, durata, int(fs * durata), endpoint=False)

    frecventa1 = fs / 2
    frecventa2 = fs / 4
    frecventa3 = 0

    semnal1 = amplitudine * np.sin(2 * np.pi * frecventa1 * t)
    semnal2 = amplitudine * np.sin(2 * np.pi * frecventa2 * t)
    semnal3 = amplitudine * np.sin(2 * np.pi * frecventa3 * t)

    plt.figure(figsize=(12, 8))

    plt.subplot(311)
    plt.plot(t, semnal1)
    plt.title('f = fs/2')
    plt.xlabel('Timp (secunde)')
    plt.ylabel('Amplitudine')
    plt.grid(True)

    plt.subplot(312)
    plt.plot(t, semnal2)
    plt.title('f = fs/4')
    plt.xlabel('Timp (secunde)')
    plt.ylabel('Amplitudine')
    plt.grid(True)

    plt.subplot(313)
    plt.plot(t, semnal3)
    plt.title('f = 0 Hz')
    plt.xlabel('Timp (secunde)')
    plt.ylabel('Amplitudine')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def ex7():
    # Parametrii semnalului sinusoidal
    frecventa = 100 # Am ales o frecventa mai mica ca sa pot observa ceva
    durata = 1

    # Generare semnal sinusoidal
                        # am crescut numarul de esantioane
    t = np.linspace(0, durata, int(durata * frecventa * 10), endpoint=False)
    semnal_initial = np.sin(2 * np.pi * frecventa * t)

    # Decimare (păstrăm doar fiecare al patrulea eșantion)
    semnal_decimat = semnal_initial[::4]

    # Afișare semnale
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, semnal_initial)
    plt.title('Semnal inițial (1000 Hz)')
    plt.xlabel('Timp (secunde)')
    plt.grid(True)

    # Afisare semnal decimat
    t_decimat = np.linspace(0, durata, int(durata * frecventa / 4 * 10), endpoint=False)
    plt.subplot(3, 1, 2)
    plt.plot(t_decimat, semnal_decimat)
    plt.title('Semnal decimat (250 Hz)')
    plt.xlabel('Timp (secunde)')
    plt.grid(True)


    # b)
    semnal_decimat_2 = semnal_initial[1::4]
    
    plt.subplot(3, 1, 3)
    plt.plot(t_decimat, semnal_decimat_2)
    plt.title('Semnal decimat pornind de la al doilea element (250 Hz)')
    plt.xlabel('Timp (secunde)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def ex8():
    
    alpha = np.linspace(-np.pi/2, np.pi/2, 1000)
    semnal = np.sin(alpha)
    semnal_taylor = alpha

    error = np.abs(semnal - semnal_taylor)
        
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(alpha, semnal, label='sin(α)', color='blue')
    plt.plot(alpha, semnal_taylor, label='α (aproximare)', linestyle='--', color='red')
    plt.title('Compararea sin(α) cu α')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(alpha, error, label='Eroare', color='green')
    plt.title('Eroare între sin(α) și α (aproximare)')
    plt.legend()
    plt.grid(True)

    # plt.tight_layout()
    # plt.show()

    # Aproximarea Pade
    semnal_pade = (alpha - (7 * alpha**3 )/ 60) / (1 + (alpha**2) / 20)
    
    error_pade = np.abs(semnal - semnal_pade)

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(alpha, semnal, label='sin(α)', color='blue')
    plt.plot(alpha, semnal_pade, label='α (aproximare)', linestyle='--', color='red')
    plt.title('Compararea sin(α) cu Pade sin(α)')
    plt.legend()
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(alpha, error_pade, label='Eroare', color='green')
    plt.title('Eroare între sin(α) și Pade sin(α)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    # Aproximarea Pade este una mult mai apropriata de adevar
    # pentru toate valorile lui alpha din intervalul ales


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    ex8()
