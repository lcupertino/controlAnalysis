import numpy as np
import matplotlib.pyplot as plt
import control
plt.rcParams.update({
    "text.usetex": True
})

import argparse

parser = argparse.ArgumentParser(description="Bode diagram with Python")
parser.add_argument("--K", action="store", nargs=1, default=1.0, type=float)
parser.add_argument("--num", action="store", nargs="*", default=1.0, type=float)
parser.add_argument("--den", action="store", nargs="*", default=1.0, type=float)
parser.add_argument("--tex", action="store", nargs=1, default=False, type=bool)
parser.add_argument("--name", action="store", nargs="*", default="bode_diagram", type=str)
parser.add_argument("--graph", action="store", nargs="*", default="$F(s)$", type=str)
args = parser.parse_args()

K = vars(args)["K"]
num = vars(args)["num"]
den = vars(args)["den"]
generate_tex = vars(args)["tex"]
file_name = vars(args)["name"]
graph_name = vars(args)["graph"]

print(K)
print(num)
print(den)

def generate_transfer_function(gain, num, den):
    return gain*control.tf(num, den)

G = generate_transfer_function(K, num, den)
print(G)

def write_numerator(transfer_function):
    str_num = ""
    num_of_terms = len(transfer_function.num[0][0])
    for i, elem in enumerate(transfer_function.num[0][0]):
        if(i==num_of_terms-1):
            str_num = str_num + "+{}".format(str(elem))
        else:
            str_num = str_num + "+{}".format(str(elem)) + "s^{}".format(str(num_of_terms-i-1))
    return str_num

def write_denominator(transfer_function):
    str_den = ""
    num_of_terms = len(transfer_function.den[0][0])
    for i, elem in enumerate(transfer_function.den[0][0]):
        if(i==num_of_terms-1):
            str_den = str_den + "+{}".format(str(elem))
        else:
            str_den = str_den + "+{}".format(str(elem)) + "s^{}".format(str(num_of_terms-i-1))
    return str_den    

def generate_tex_fraction(str_gain, str_num, str_den):
    pass

def obtain_tex_code(gain, transfer_function):
    if(generate_tex):
        str_gain = "{}".format(str(gain[0]))
        str_num = write_numerator(transfer_function)    
        str_den = write_denominator(transfer_function)
        return "$\dfrac{" + str_gain + " (" + str_num + ")}" + "{" + str_den + "}$"


# print(obtain_tex_code(K, G))
w = np.logspace(-2,2)
magnitude, phase, omega = control.bode(G,w)
# plt.title(label = graph_name)
# plt.savefig(fname='{}'.format(file_name), format="pdf")
# plt.savefig(fname='{}.png'.format(file_name))
plt.show()