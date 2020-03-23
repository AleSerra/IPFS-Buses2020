import csv
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
import sys
import numpy as np

#Definizioni di alcune variabili utili all'interno dei metodi successivi
tests_list_ipfs = list() #Lista dei percorsi contenenti i test IPFS
tests_list_sia = list() #Lista dei percorsi contenenti i test SIA

#Deprecamento dei warning
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Set del font per la legenda dei grafici successivi
fontP = FontProperties()
fontP.set_size(7)

#Calcolo percorso cartella test IPFS
for root, dirs, files in os.walk(".\\downtests\\tests", topdown=False):
    for name in files:
        tests_list_ipfs.append(os.path.join(root, name))

#Calcolo percorso cartella test SIA
for root, dirs, files in os.walk(".\\downtests\\testsSia", topdown=False):
    for name in files:
        tests_list_sia.append(os.path.join(root, name))

#Metodo per la rappresentazione del grafico delle latenze SIA (richiamato nel metodo ipfs_plot())
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
                x.append("1")
                y.append(valori[turn+0])
                x.append("2")
                y.append(valori[turn+1])
                x.append("3")
                y.append(valori[turn+2])
                x.append("4")
                y.append(valori[turn+3])
                plt.plot(x,y,'--o',label='Graph for: Test '+str(val))
                x=[]
                y=[]
                turn+=4

#Metodo per la rappresentazione del grafico delle latenze IPFS
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
                x.append("1")
                y.append(valori[turn+0])
                x.append("2")
                y.append(valori[turn+1])
                x.append("3")
                y.append(valori[turn+2])
                x.append("4")
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

#Metodo per la rappresentazione del grafico delle aggregazioni SIA(richiamato nel metodo plot_risultati())
def plot_risultati_sia():
    print('RESULTS FROM TEST OF SIA NETWORK')
    turn=0
    count=0
    summs=0
    for test in tests_list_sia:
        with open(test) as csv_file:
            summs=0
            latenza_media_sia=[]
            latenza_accumulata_sia=[]
            deviazione_standard_sia=[]
            valori =[]
            values=[]
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                valori.append(int(row[1]))
                count+= 1
            print('QUI: ')
            print(valori)
            for turn in range(4):
                pos=0
                summs=0
                for val in range(count/4):
                    values.append(int(valori[turn+pos]))
                    summs = summs + int(valori[turn+pos])
                    pos+=4
                latenza_accumulata_sia.append(int(summs))
                mediams = summs/(float(count/4))
                latenza_media_sia.append(float('%.2f' % mediams))
                numdev = 0
                for value in values:
                    scarto = mediams - int(value)
                    scartoquad = pow(scarto, 2)
                    numdev = numdev + scartoquad
                devstd = math.sqrt(numdev / (float(count/4)))
                deviazione_standard_sia.append(float('%.2f' % devstd))
    pos = np.arange(1,len(latenza_media_sia)+1)
    var_one = np.array(deviazione_standard_sia)
    var_two = np.array(latenza_media_sia)
    plt.bar(pos, np.add(var_two, var_one), color='blue', edgecolor='blue', label='Latenza media')
    plt.bar(pos, var_one, color='orange', edgecolor='orange', label='Deviazione standard')

#Metodo per la rappresentazione delle aggregazioni IPFS
def plot_risultati():
    print('RESULTS FROM TEST OF IPFS NETWORK')
    turn=0
    count=0
    summs=0
    for test in tests_list_ipfs:
        with open(test) as csv_file:
            summs=0
            latenza_media_ipfs=[]
            latenza_accumulata_ipfs=[]
            deviazione_standard_ipfs=[]
            valori =[]
            values=[]
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                valori.append(int(row[1]))
                count+= 1
            print(valori)
            for turn in range(4):
                pos=0
                summs=0
                for val in range(count/4):
                    values.append(int(valori[turn+pos]))
                    summs = summs + int(valori[turn+pos])
                    pos+=4
                latenza_accumulata_ipfs.append(int(summs))
                mediams = summs/(float(count/4))
                latenza_media_ipfs.append(float('%.2f' % mediams))
                numdev = 0
                for value in values:
                    scarto = mediams - int(value)
                    scartoquad = pow(scarto, 2)
                    numdev = numdev + scartoquad
                devstd = math.sqrt(numdev / (float(count/4)))
                deviazione_standard_ipfs.append(float('%.2f' % devstd))
        plt.subplot(1,2,1)
        pos = np.arange(1,len(latenza_media_ipfs)+1)
        var_one = np.array(deviazione_standard_ipfs)
        var_two = np.array(latenza_media_ipfs)
        plt.bar(pos, np.add(var_two, var_one), color='blue', edgecolor='blue', label='Latenza media')
        plt.bar(pos, var_one, color='orange', edgecolor='orange', label='Deviazione standard')
        plt.xlabel('ID')
        plt.ylabel('ms')
        plt.title('--- TEST DOWNLOAD IPFS ---')
        plt.legend(loc='best')
        plt.xticks(np.arange(1, len(latenza_media_ipfs)+1, step=1))
        plt.subplot(1,2,2)
        plot_risultati_sia()
        plt.xlabel('ID')
        plt.ylabel('ms')
        plt.title('--- TEST DOWNLOAD SIA ---')
        plt.legend(loc='best')
        plt.xticks(np.arange(1, len(latenza_media_ipfs)+1, step=1))
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.show()

#Metodo principale. Richiama i metodi precedenti
def main():
    ipfs_plot()
    plot_risultati()
    print ("\n################################################\nESECUZIONE TERMINATA")

#Esecuzione del metodo principale
main()