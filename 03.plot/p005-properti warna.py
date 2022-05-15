import numpy as np
import matplotlib.pyplot as plt

# koordinat pada sumbu x
x = np.array([1, 2, 3, 4, 5, 6])

# koordinat pada sumbu y
y = np.array([2, 10, 5, 8, 20, 50])
y2 = np.array([10, 5, 24, 87, 1, 4])


# buat plot
plot_1 = plt.plot(x,y)
plot_2 = plt.plot(x, y2)

# atur properti warna plot_1
plt.setp(plot_1, color='r')

# atur properti warna plot_2
plt.setp(plot_2, color='b')

# tampilkan gambar
plt.show()