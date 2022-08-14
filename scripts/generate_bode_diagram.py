import numpy as np
import matplotlib.pyplot as plt
import control
import argparse

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

def write_polynomial(coeficients):
	term = ""
	num_of_terms=len(coeficients)
	for i, coeficient in enumerate(coeficients):
		if(i==len(coeficients)-1):
			term += "+{}".format(str(coeficient))
		else:
			term += term + "+{}".format(str(coeficient)) + "s^{"+"{}".format(str(num_of_terms-i-1)) + "}"			
	return term

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

def generate_tex_fraction(gain, num, den):
    return "$"+str(gain)+"\dfrac{"+str(num)+"}{"+str(den)+"}$"

def obtain_tex_code(gain, transfer_function):
    if(generate_tex):
        str_gain = "{}".format(str(gain[0]))
        str_num = write_numerator(transfer_function)    
        str_den = write_denominator(transfer_function)
        return "$\dfrac{" + str_gain + " (" + str_num + ")}" + "{" + str_den + "}$"

def save_plot(save, file_name):
    if(save):
        plt.savefig(fname='{}.pdf'.format(file_name))
        plt.savefig(fname='{}.png'.format(file_name))

G = generate_transfer_function(K, num, den)
plt.title(label=graph_name)
w = np.logspace(-2,2)
magnitude, phase, omega = control.bode(G,w,dB=True,deg=True)

# Tests
print(G)
print(K)
print(num)
print(den)
print(file_name[0])
print(graph_name)

save_plot(save, file_name[0])
plt.show()
