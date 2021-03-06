import csv
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math
import sys
import numpy as np


x = [] #Lista dei valori sull'asse x
y = [] #Lista dei valori sull'asse y
valori = [] #Lista dei valori esplorati
tests_list_ipfs = list() #Lista dei percorsi contenenti i test IPFS
tests_list_sia = list() #Lista dei percorsi contenenti i test SIA
deviazione_standard_ipfs=[] #Lista dei valori della deviazione standard per i test IPFS
latenza_accumulata_ipfs=[] #Lista dei valori della latenza accumulata per i test IPFS
latenza_media_ipfs=[] #Lista dei valori della latenza media per i test IPFS
deviazione_standard_sia=[] #Lista dei valori della deviazione standard per i test SIA
latenza_accumulata_sia=[] #Lista dei valori della latenza accumulata per i test SIA
latenza_media_sia=[] #Lista dei valori della latenza media per i test SIA
busVet=[] #Lista dei bus esplorati
testVet=[] #Lista dei test esplorati

#Deprecamento dei warning
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Calcolo percorso cartella test IPFS
for root, dirs, files in os.walk(".\\tests", topdown=False):
    for name in dirs:
        tests_list_ipfs.append(os.path.join(root, name))

#Calcolo percorso cartella test SIA
for root, dirs, files in os.walk(".\\testsSia", topdown=False):
    for name in dirs:
        tests_list_sia.append(os.path.join(root, name))

#Arrai dei bus
busConst = ['110', '226', '371', '426', '512', '639', '650', '889', '484', '422']

#Array dei bus utili per calcolare la deviazione standard
busConst1 = ['110', '226', '426', '512', '639', '650', '889', '484', '422']

#Set del font per la legenda dei grafici successivi
fontP = FontProperties()
fontP.set_size(7)

#Metodo per la rappresentazione del grafico delle latenze SIA con argomento il bus di riferimento (richiamato nel metodo ipfs_plot())
def sia_plot(bus):
    for test in tests_list_sia: 
        with open(test+'\\bus-'+bus+'.csv') as csv_file:
            x = []
            y = []
            #print("open"+test+'\\bus-'+bus+'.csv') 
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                x.append(int(row[0]))
                y.append(int(row[4]))
        plt.plot(x,y,'--o', label='Graph for: '+test)

#Metodo per la rappresentazione del grafico delle latenze IPFS
def ipfs_plot():
    for bus in busConst:
        for test in tests_list_ipfs: 
            with open(test+'\\bus-'+bus+'.csv') as csv_file:
                x = []
                y = []
                #print("open"+test+'\\bus-'+bus+'.csv') 
                csv_reader = csv.reader(csv_file, delimiter=',')
                next(csv_reader)
                for row in csv_reader:
                    x.append(int(row[0]))
                    y.append(int(row[4]))
            plt.subplot(1,2,1)
            plt.plot(x,y,'--o', label='Graph for: '+test)
            plt.title('--- TEST IPFS --- BUS: '+bus)
            plt.xlabel('ID')
            plt.ylabel('EXECUTION_TIME(ms)')
            plt.legend(loc='best', prop=fontP)
        plt.subplot(1,2,2)
        sia_plot(bus)
        plt.title('--- TEST SIA --- BUS: '+bus)
        plt.xlabel('ID')
        plt.ylabel('EXECUTION_TIME(ms)')
        legend=plt.legend(loc='best', prop=fontP)
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        export_legend(legend)
        plt.show()

#Metodo per esportare la legenda in formato png nella cartella del progetto
def export_legend(legend, filename="legend.png", expand=[-5,-5,5,5]):
    fig  = legend.figure
    fig.canvas.draw()
    bbox  = legend.get_window_extent()
    bbox = bbox.from_extents(*(bbox.extents + np.array(expand)))
    bbox = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(filename, dpi="figure", bbox_inches=bbox)

#Metodo per la rappresentazione del grafico delle aggregazioni SIA con argomento il bus di riferimento(richiamato nel metodo plot_risultati())
def plot_risultati_sia(bus):
    print('RESULTS FROM TEST OF SKYNET NETWORK')
    testVet_sia=[]
    busVet=[]
    latenza_media_sia=[]
    latenza_accumulata_sia=[]
    deviazione_standard_sia=[]
    busVet.append(bus)
    print('\n################################################\nLatenze per bus '+bus)
    totalms = 0
    for test in tests_list_sia:
        testVet_sia.append(test)
        with open(test+'\\bus-'+bus+'.csv') as csv_file_sia:
            csv_reader_sia = csv.reader(csv_file_sia, delimiter=',')
            values_sia = list()
            line_count = 0
            summs = 0
            for row in csv_reader_sia:
                if line_count != 0:
                    summs = summs + int(row[4])
                    values_sia.append(row[4])
                line_count += 1
            latenza_accumulata_sia.append(int(summs))
            mediams = summs/(line_count-1)
            latenza_media_sia.append(float('%.2f' % mediams))
            totalms = totalms + summs
            numdev = 0
            for value in values_sia:
                scarto = mediams - int(value)
                scartoquad = pow(scarto, 2)
                numdev = numdev + scartoquad
            devstd = math.sqrt(numdev / (line_count-2))
            deviazione_standard_sia.append(float('%.2f' % devstd))
    pos_sia = np.arange(len(testVet_sia))
    var_one_sia = np.array(deviazione_standard_sia)
    var_two_sia = np.array(latenza_media_sia)
    var_three_sia = np.array(latenza_accumulata_sia)
    plt.bar(pos_sia, np.add(np.add(var_three_sia, var_two_sia), var_one_sia), color='orange', edgecolor='orange', label='Latenza accumulata')
    plt.bar(pos_sia, np.add(var_two_sia, var_one_sia), color='blue', edgecolor='blue', label='Latenza media')
    plt.bar(pos_sia, var_one_sia, color='green', edgecolor='green', label='Deviazione standard')
    print('----------------------------------------------------\nLatenza totale accumulata nel test: '+str(totalms)+' ms')
    print('Latenza media totale nel test: {0:.2f}'.format(totalms/79)+' ms')

#Metodo per la rappresentazione delle aggregazioni IPFS
def plot_risultati():
    print('RESULTS FROM TEST OF IPFS NETWORK')
    for bus in busConst1:
        testVet=[]
        busVet=[]
        latenza_media_ipfs=[]
        latenza_accumulata_ipfs=[]
        deviazione_standard_ipfs=[]
        busVet.append(bus)
        print('----------------------------------------------------\nLatenze per bus '+bus)
        totalms = 0
        for test in tests_list_ipfs:
            testVet.append(test)
            with open(test+'\\bus-'+bus+'.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                values = list()
                line_count = 0
                summs = 0
                for row in csv_reader:
                    if line_count != 0:
                        summs = summs + int(row[4])
                        values.append(row[4])
                    line_count += 1
                latenza_accumulata_ipfs.append(int(summs))
                mediams = summs/(line_count-1)
                latenza_media_ipfs.append(float('%.2f' % mediams))
                totalms = totalms + summs
                numdev = 0
                for value in values:
                    scarto = mediams - int(value)
                    scartoquad = pow(scarto, 2)
                    numdev = numdev + scartoquad
                devstd = math.sqrt(numdev / (line_count-2))
                deviazione_standard_ipfs.append(float('%.2f' % devstd))
        plt.subplot(1,2,1)
        pos = np.arange(len(testVet))
        var_one = np.array(deviazione_standard_ipfs)
        var_two = np.array(latenza_media_ipfs)
        var_three = np.array(latenza_accumulata_ipfs)
        plt.bar(pos, np.add(np.add(var_three, var_two), var_one), color='orange', edgecolor='orange', label='Latenza accumulata')
        plt.bar(pos, np.add(var_two, var_one), color='blue', edgecolor='blue', label='Latenza media')
        plt.bar(pos, var_one, color='green', edgecolor='green', label='Deviazione standard')
        plt.xlabel('ID')
        plt.ylabel('ms')
        plt.title('--- TEST IPFS --- BUS: '+bus)
        plt.legend(loc='best')
        plt.xticks(np.arange(0, len(testVet), step=1))
        print('----------------------------------------------------\nLatenza totale accumulata del bus'+bus+' : '+str(totalms)+' ms')
        print('Latenza media totale del bus '+bus+' : {0:.2f}'.format(totalms/79)+' ms\n\n')
        plt.subplot(1,2,2)
        plot_risultati_sia(bus)
        plt.xlabel('ID')
        plt.ylabel('ms')
        plt.title('--- TEST SIA --- BUS: '+bus)
        plt.legend(loc='best')
        plt.xticks(np.arange(0, len(testVet), step=1))
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