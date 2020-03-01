import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

x = []
y = []
valori = []
tests_list_ipfs = list()
tests_list_dataset = list()
tests_list_sia = list()

#Calcolo percorso cartella test ipfs
for root, dirs, files in os.walk(".\\tests", topdown=False):
    for name in dirs:
        tests_list_ipfs.append(os.path.join(root, name))

#Calcolo percorso cartella test dataset
for root, dirs, files in os.walk(".\\dataset", topdown=False):
    for name in dirs:
        tests_list_dataset.append(os.path.join(root, name))

#Calcolo percorso cartella test sia
for root, dirs, files in os.walk(".\\testsSia", topdown=False):
    for name in dirs:
        tests_list_sia.append(os.path.join(root, name))

    busConst = [
    '110',
    '226',
    '371',
    '426',
    '512',
    '639',
    '650',
    '889',
    '484',
    '422'
    ]

'''def ipfs_dataset_bar(bus):
    with open('.\\dataset\\inputDataset'+bus+'.csv') as csv_file1:
        x = []
        y = []
        #print("open"+test+'\\bus-'+bus+'.csv') 
        csv_reader1 = csv.reader(csv_file1, delimiter=',')
        next(csv_reader1)
        for row in csv_reader1:
            x.append(int(row[4]))
            y.append(int(row[0]))
    plt.plot(x,y,'--o', label='Graph for: input')
    plt.xlabel('ID')
    plt.ylabel('EXECUTION_TIME')
    plt.plot
    plt.title('BUS: '+bus)
    plt.legend(loc='best')'''

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
    #fig = plt.figure()
    #plt.show()

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
            plt.xlabel('ID (counter)')
            plt.ylabel('EXECUTION_TIME (ms)')
            plt.legend(loc='best')
        plt.subplot(1,2,2)
        sia_plot(bus)
        plt.title('--- TEST SIA --- BUS: '+bus)
        plt.xlabel('ID (counter)')
        plt.ylabel('EXECUTIONTIME (ms)')  
        plt.legend(loc='best')
        #fig = plt.figure()
        plt.show()

ipfs_plot()
print ("ESECUZIONE TERMINATA")