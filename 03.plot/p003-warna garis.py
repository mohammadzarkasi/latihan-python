import numpy as np
import matplotlib.pyplot as plt

# koordinat pada sumbu x
x = np.array([1, 2, 3, 4, 5, 6])

# koordinat pada sumbu y
y = np.array([2, 10, 5, 8, 20, 50])
y2 = np.array([10, 5, 24, 87, 1, 4])

# gambar garis pertama ke plot dengan warna merah
plt.plot(x, y, 'r')

# gambar garis kedua ke plot dengan warna kuning
plt.plot(x, y2, 'y')

# tampilkan gambar
plt.show()