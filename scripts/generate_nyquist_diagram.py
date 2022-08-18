import control
import matplotlib.pyplot as plt
plt.rcParams.update({
    "text.usetex": True
    })

num = [1.0, 1.0]
den = [1.0, 2.0, 3.0]

G = control.tf(num, den)

control.nyquist(G)
plt.plot(color="r")
plt.xlabel("Re(s)")
plt.ylabel("Im(s)")
plt.show()
