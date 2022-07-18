import numpy as np
import matplotlib.pyplot as plt
import control

import argparse

parser = argparse.ArgumentParser(description="Bode diagram with Python")
parser.add_argument("--K", action="store", nargs=1, default=1.0, type=float)
parser.add_argument("--num", action="store", nargs="*", default=1.0, type=float)
parser.add_argument("--den", action="store", nargs="*", default=1.0, type=float)

args = parser.parse_args()

K = vars(args)["K"]
num = vars(args)["num"]
den = vars(args)["den"]


print(K)
print(num)
print(den)

def generate_transfer_function(K, num, den):
    return K*control.tf(num, den)

G = generate_transfer_function(K, num, den)
print(G)

w = np.logspace(-2,2)
magnitude, phase, omega = control.bode(G,w)
plt.tight_layout()

