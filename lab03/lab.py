import numpy as np
import math
import matplotlib.pyplot as plt

N = 8   # Dimensiunea Matricei Fourier

F = np.zeros((N, N), dtype=complex)

# Construirea Matricei Fourier
for i in range(N):
    for j in range(N):
        F[i, j] = math.e ** ( -2j * np.pi * i * j / N)


# fig, axs = plt.subplots(N, 2, figsize=(10, 10))
# for i in range(N):
#     for j in range(2):
#         if j == 0:
#             axs[i, j].plot(F[i, :].real)
#             axs[i, j].set_title(f'Real part of line {i}')
#         else:
#             axs[i, j].plot(F[i, :].imag, linestyle='--', c='orange')
#             axs[i, j].set_title(f'Imaginary part of line {i}')
# plt.savefig("fourier.pdf")
# plt.show()

fig, axs = plt.subplots(N, figsize = (10, 10))

for i in range(N):
    axs[i].plot(F[i, :].real)
    axs[i].plot(F[i, :].imag, linestyle='--', c='orange')
    axs[i].set_title(f'Fourier line [{i}]')
plt.savefig("1.pdf")
plt.show()

    
# Verificați că matricea Fourier este unitară (complexă și ortogonală)

# Ortogonală: F * conj(F ^ T) = I, unde F este matricea Fourier,
# conj() este conjugata, F ^ T transpusa lui F, I matricea de identitate

# Complexă: Matricea Fourier este complexă

F_H = F.T.conj()
is_orthogonal = np.linalg.norm(np.abs(F_H @ F) - N * np.identity(N)) <= 1e-10
# is_orthogonal = np.allclose(np.dot(F_H, F), N * np.identity(N), atol=1e-10)
print(is_orthogonal)    # True

