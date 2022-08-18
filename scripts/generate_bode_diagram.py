import numpy as np
import matplotlib.pyplot as plt
import control
import argparse
from bode_diagram import BodeDiagram

plt.rcParams.update({
    "text.usetex": True
})

parser = argparse.ArgumentParser(description="Bode diagram with Python")
parser.add_argument("--K", action="store", nargs=1, default=1.0, type=float)
parser.add_argument("--num", action="store", nargs="*", default=1.0, type=float)
parser.add_argument("--den", action="store", nargs="*", default=1.0, type=float)
parser.add_argument("--tex", action="store", nargs=1, default=False, type=bool)
parser.add_argument("--name", action="store", nargs="*", default="bode_diagram", type=str)
parser.add_argument("--graph", action="store", nargs="*", default="$F(s)$", type=str)
parser.add_argument("--save", action="store", nargs=1, default=False, type=bool)
args = parser.parse_args()

K = vars(args)["K"]
num = vars(args)["num"]
den = vars(args)["den"]
generate_tex = vars(args)["tex"]
file_name = vars(args)["name"]
graph_name = vars(args)["graph"]
save = vars(args)["save"]

def generate_transfer_function(gain, num, den):
    return gain*control.tf(num, den)

def obtain_tex_code(gain, transfer_function, generate_tex):
    if(generate_tex):
        str_gain = "{}".format(str(gain[0]))
        str_num = write_numerator(transfer_function)    
        str_den = write_denominator(transfer_function)
        return "$\dfrac{" + str_gain + " (" + str_num + ")}" + "{" + str_den + "}$"

if __name__=="__main__":
    G = generate_transfer_function(K, num, den)
    bodeDiagram = BodeDiagram(K, G, file_name[0])
    print(bodeDiagram.write_polynomial(num))
    print(bodeDiagram.write_polynomial(den))
    print(bodeDiagram.generate_tex_code())
    bodeDiagram.plot_diagram("$F(s)$", save=True)

