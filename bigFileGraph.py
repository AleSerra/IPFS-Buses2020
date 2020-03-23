import csv
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
import sys
import numpy as np

#Definizioni di alcune variabili utili all'interno dei metodi successivi
bigtests_list_ipfs = list() #Lista dei percorsi contenenti i test IPFS
bigtests_list_sia = list() #Lista dei percorsi contenenti i test SIA

fileConst=['0','1','2','3'] #Array dei file

#Deprecamento dei warning
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Set del font per la legenda dei grafici successivi
fontP = FontProperties()
fontP.set_size(7)

#Calcolo percorso cartella test IPFS
for root, dirs, files in os.walk(".\\bigfiletests\\tests", topdown=False):
    for name in dirs:
        bigtests_list_ipfs.append(os.path.join(root, name))

#Calcolo percorso cartella test SIA
for root, dirs, files in os.walk(".\\bigfiletests\\testsSia", topdown=False):
    for name in dirs:
        bigtests_list_sia.append(os.path.join(root, name))

#Metodo per la rappresentazione del grafico delle latenze SIA (richiamato nel metodo ipfs_plot())
def sia_plot():
    for test in bigtests_list_sia: 
        with open(test+'\\results.csv') as csv_file:
            x = []
            y = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                x.append(row[1]+str('\ndim:'+ str(int(row[3])/1000)+'kB'))
                y.append(int(row[4]))
        plt.plot(x,y,'--o', label='Graph for: '+test)

#Metodo per la rappresentazione del grafico delle latenze IPFS
def ipfs_plot():
    for test in bigtests_list_ipfs: 
        with open(test+'\\results.csv') as csv_file:
            x = []
            y = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                x.append(row[1]+str('\ndim:'+ str(int(row[3])/1000)+'kB'))
                y.append(int(row[4]))
        plt.subplot(1,2,1)
        plt.plot(x,y,'--o', label='Graph for: '+test)
        plt.title('--- TEST IPFS BIG FILE---')
        plt.xlabel('FILE')
        plt.ylabel('EXECUTION_TIME(ms)')
        plt.legend(loc='best',prop=fontP)
    plt.subplot(1,2,2)
    sia_plot()
    plt.title('--- TEST SIA BIG FILE---')
    plt.xlabel('FILE')
    plt.ylabel('EXECUTION_TIME(ms)')
    plt.legend(loc='best',prop=fontP)
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()

#Metodo per la rappresentazione del grafico delle aggregazioni SIA(richiamato nel metodo plot_risultati())
def plot_risultati_sia():
    print('RESULTS FROM TEST OF SIA NETWORK')
    summs=0
    latenza_media_sia=[]
    latenza_accumulata_sia=[]
    deviazione_standard_sia=[]
    summs=0
    for file in fileConst:
        summs=0
        values=[]
        for test in bigtests_list_sia:
            with open(test+'\\results.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    if(int(file)==int(row[0])):
                        values.append(int(row[4]))
                        summs = summs + int(row[4])
        latenza_accumulata_sia.append(int(summs))
        mediams = summs/len(values)
        latenza_media_sia.append(float('%.2f' % mediams))
        numdev = 0
        print(values)
        for value in values:
            scarto = mediams - int(value)
            scartoquad = pow(scarto, 2)
            numdev = numdev + scartoquad
        devstd = math.sqrt(numdev / len(values))
        deviazione_standard_sia.append(float('%.2f' % devstd))
    pos = np.arange(1,len(latenza_media_sia)+1)
    var_one_sia = np.array(deviazione_standard_sia)
    var_two_sia = np.array(latenza_media_sia)
    plt.bar(pos, np.add(var_two_sia, var_one_sia), color='orange', edgecolor='orange', label='Latenza media')
    plt.bar(pos, var_one_sia, color='blue', edgecolor='blue', label='Deviazione standard')

#Metodo per la rappresentazione delle aggregazioni IPFS
def plot_risultati():
    print('RESULTS FROM TEST OF IPFS NETWORK')
    summs=0
    latenza_media_ipfs=[]
    latenza_accumulata_ipfs=[]
    deviazione_standard_ipfs=[]
    summs=0
    for file in fileConst:
        summs=0
        values=[]
        for test in bigtests_list_ipfs:
            with open(test+'\\results.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    if(int(file)==int(row[0])):
                        values.append(int(row[4]))
                        summs = summs + int(row[4])
        latenza_accumulata_ipfs.append(int(summs))
        mediams = summs/len(values)
        latenza_media_ipfs.append(float('%.2f' % mediams))
        numdev = 0
        print(values)
        for value in values:
            scarto = mediams - int(value)
            scartoquad = pow(scarto, 2)
            numdev = numdev + scartoquad
        devstd = math.sqrt(numdev / len(values))
        deviazione_standard_ipfs.append(float('%.2f' % devstd))
    plt.subplot(1,2,1)
    pos = np.arange(1,len(latenza_media_ipfs)+1)
    var_one = np.array(deviazione_standard_ipfs)
    var_two = np.array(latenza_media_ipfs)
    plt.bar(pos, np.add(var_two, var_one), color='orange', edgecolor='orange', label='Latenza media')
    plt.bar(pos, var_one, color='blue', edgecolor='blue', label='Deviazione standard')
    plt.xlabel('ID')
    plt.ylabel('ms')
    plt.title('--- TEST BIG FILE IPFS ---')
    plt.legend(loc='best')
    plt.xticks(np.arange(1, len(latenza_media_ipfs)+1, step=1))
    plt.subplot(1,2,2)
    plot_risultati_sia()
    plt.xlabel('ID')
    plt.ylabel('ms')
    plt.title('--- TEST BIG FILE SIA ---')
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