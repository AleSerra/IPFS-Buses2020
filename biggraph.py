import csv
import os
import matplotlib.pyplot as plt
import math
import sys

x = []
y = []
bigtests_list_ipfs = list()
bigtests_list_sia = list()

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

#Calcolo percorso cartella test ipfs
for root, dirs, files in os.walk(".\\bigfiletests\\tests", topdown=False):
    for name in dirs:
        bigtests_list_ipfs.append(os.path.join(root, name))

#Calcolo percorso cartella test sia
for root, dirs, files in os.walk(".\\bigfiletests\\testsSia", topdown=False):
    for name in dirs:
        bigtests_list_sia.append(os.path.join(root, name))

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
        plt.legend(loc='best')
    plt.subplot(1,2,2)
    sia_plot()
    plt.title('--- TEST SIA BIG FILE---')
    plt.xlabel('FILE')
    plt.ylabel('EXECUTION_TIME(ms)')
    plt.legend(loc='best')
    manager = plt.get_current_fig_manager()
    manager.resize(*manager.window.maxsize())
    plt.show()

def main():
    ipfs_plot()
    print ("\n################################################\nESECUZIONE TERMINATA")

main()