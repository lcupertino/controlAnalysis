import numpy as np
import matplotlib.pyplot as plt
import os
import time
import control

class BodeDiagram:
    def __init__(self, gain, transfer_function, file_name):
        self.gain = gain
        self.transfer_function = transfer_function
        self.file_name = file_name
    
    def write_polynomial(self, coeficients):
        term=""
        num_of_terms=len(coeficients)
        for i, coeficient in enumerate(coeficients):
            if(i==len(coeficiente)-1):
                term+="+{}".format(str(coeficient))

            else:
                term+= term+"+{}".format(str(coeficient))+"s^{"+"{}".format(str(num_of_terms-i-1)) + "}"

        return term

    def generate_tex_code(self):
        den = self.write_polynomial(self.transfer_function.den[0][0])
        num = self.write_polynomial(self.transfer_function.num[0][0])

        return "$"+str(self.gain)+"\dfrac{"+num+"}{"+den+"}"
    
    def save_plot(self, save):
        if(save):
            plt.savefig(fname='{}.pdf'.format(self.file_name))
            plt.savefig(fname='{}.png'.format(self.file_name))
