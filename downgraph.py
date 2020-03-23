import csv
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
import sys

x = []
y = []
tests_list_ipfs = list()
tests_list_sia = list()

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

fontP = FontProperties()
fontP.set_size(7)

#Calcolo percorso cartella test ipfs
for root, dirs, files in os.walk(".\\downtests\\tests", topdown=False):
    for name in files:
        tests_list_ipfs.append(os.path.join(root, name))

#Calcolo percorso cartella test sia
for root, dirs, files in os.walk(".\\downtests\\testsSia", topdown=False):
    for name in files:
        tests_list_sia.append(os.path.join(root, name))

def sia_plot():
    turn=0
    count=0
    for test in tests_list_sia:
        with open(test) as csv_file1:
            valori =[]
            x = []
            y = []
            csv_reader1 = csv.reader(csv_file1, delimiter=',')
            next(csv_reader1)
            for row in csv_reader1:
                valori.append(int(row[1]))
                count+= 1
            for val in range(count/4):
                x.append("0")
                y.append(valori[turn+0])
                x.append("1")
                y.append(valori[turn+1])
                x.append("2")
                y.append(valori[turn+2])
                x.append("3")
                y.append(valori[turn+3])
                plt.plot(x,y,'--o',label='Graph for: Test '+str(val))
                x=[]
                y=[]
                turn+=4

def ipfs_plot():
    turn=0
    count=0
    for test in tests_list_ipfs:
        with open(test) as csv_file:
            valori =[]
            x = []
            y = [] 
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                valori.append(int(row[1]))
                count+= 1
            for val in range(count/4):
                x.append("0")
                y.append(valori[turn+0])
                x.append("1")
                y.append(valori[turn+1])
                x.append("2")
                y.append(valori[turn+2])
                x.append("3")
                y.append(valori[turn+3])
                plt.subplot(1,2,1)     
                plt.plot(x,y,'--o', label='Graph for: Test '+str(val))
                plt.title('--- TEST DOWNLOAD IPFS ---')
                plt.xlabel('FILE ID(row)')
                plt.ylabel('EXECUTION_TIME(ms)')
                plt.legend(loc='best',prop=fontP)
                x=[]
                y=[]
                turn+=4
    plt.subplot(1,2,2)
    sia_plot()
    plt.title('--- TEST DOWNLOAD SIA ---')
    plt.xlabel('FILE ID(row)')
    plt.ylabel('EXECUTION_TIME(ms)')
    plt.legend(loc='best',prop=fontP)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()

def main():
    ipfs_plot()
    print ("\n################################################\nESECUZIONE TERMINATA")

main()