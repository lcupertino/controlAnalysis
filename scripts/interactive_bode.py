import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
import control

# Parameters
try:
    plt.rcParams.update({
        "text.usetex": True
        })
except:
    print("TeX not found")

# Useful objects

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2, top=0.75)

f_d, = ax.plot([], [], linewidth=2.5)
temp = ax.text(1, 1, '', ha='right', va='top', fontsize=24)

# Data

num = [1.0, 1.0]
den = [1.0, 2.0, 1.2]
gain = 10.0

transfer_function = control.tf(num, den)
print(transfer_function)

w = np.logspace(-2, 2)
magnitude, phase, omega = control.bode(transfer_function, w, dB=True, deg=True)
#plt.plot(w, magnitude)
gain_values = np.linspace(1, 1000)
colors = plt.get_cmap('coolwarm', 10)


def animate(i, gain_values, transfer_function):
    w = np.logspace(-2, 2)
    magnitude, phase, omega = control.bode(gain_values[i]*transfer_function, w, dB=True, deg=True)
    y = magnitude
    f_d.set_data(w, y)
    f_d.set_color(colors(i))
    temp.set_text('K = ' + str(int(gain_values[i])))
    temp.set_color(colors(i))

"""
animation = FuncAnimation(fig, func=animate, frames=range(len(gain_values)), fargs=(gain_values, transfer_function,), interval=500, repeat = True)
fig.tight_layout()
animation.save('AnimatedPlot.gif', writer='Pillow', fps=10)
"""
# Slider

axis_slider = fig.add_axes([0.3, 0.85, 0.4, 0.05])
axis_slider.spines['top'].set_visible(True)
axis_slider.spines['right'].set_visible(True)

slider = Slider(ax=axis_slider, label='Gain', valmin=1.0, valmax=1000.0, valfmt='K =  %1.1f ', facecolor='#cc7000')

# Base Dataset
"""
w = np.logspace(-2, 2)
magnitude, phase, omega = control.tf(transfer_function, w, dB=True, deg=True)
"""
y = magnitude
fd, = ax.plot(w, y, linewidth=2.0)

# Update values

def update(val):
    num = [1.0, 1.0]
    den = [1.0, 2.0, 1.2]
    transfer_function = control.tf(num, den)
    gain = slider.val
    w = np.logspace(-2, 2)
    magnitude, phase, omega = control.bode(gain*transfer_function, w, dB=True, deg=True)
    f_d.set_data(w, magnitude)
    fig.canvas.draw_idle()
    
slider.on_changed(update)
plt.show()

class Interactive_Bode():
    def __init__(self, gain, num, den):
        self.gain = gain
        self.transfer_function = control.tf(num, den)
    
    def build_setup(self):
        pass

    def update(self):
        pass
    


