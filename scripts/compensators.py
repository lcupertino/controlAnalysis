import matplotlib.pyplot as plt
import numpy as np
import control
plt.rcParams.update({
    "text.usetex":True
})

class Compensator:
    def __init__(self, gain, numerator, denominator):
        self.gain=gain
        self.numerator=numerator
        self.denominator=denominator

    def evaluate_nature(self):
        pass

    def plot_bode(self):
        pass
