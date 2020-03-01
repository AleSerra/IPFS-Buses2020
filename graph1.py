import csv
import os
import matplotlib.pyplot as plt
import math
import sys

x = []
y = []
valori = []
tests_list_ipfs = list()
tests_list_dataset = list()
tests_list_sia = list()

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

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

    busConst1 = [
  '110',
  '226',
  #'371',
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
        plt.title('--- TEST SIA --- BUS: '+bus)
        plt.xlabel('ID')
        plt.ylabel('EXECUTION_TIME(ms)')
        plt.legend(loc='best')
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
            plt.xlabel('ID')
            plt.ylabel('EXECUTION_TIME(ms)')
            plt.legend(loc='best')
        plt.subplot(1,2,2)
        sia_plot(bus)
        plt.xlabel('id')
        plt.ylabel('executionTime')  
        plt.legend(loc='best')
        #fig = plt.figure()
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())
        plt.show()

def calcolo_risultati_ipfs():
    print('RESULTS FROM TEST OF IPFS NETWORK')
    for test in tests_list_ipfs:
        print('\n################################################\nRESULTS FOR TEST IN: '+ test)
        totalms = 0
        for bus in busConst1:
            print('----------------------------------------------------\nLatenze per bus '+bus)
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
                print('Latenza accumulata: '+ str(summs)+' ms')
                mediams = summs/(line_count-1)
                print('Latenza media: {0:.2f}'.format(mediams)+' ms')
                totalms = totalms + summs

                numdev = 0
                for value in values:
                    scarto = mediams - int(value)
                    scartoquad = pow(scarto, 2)
                    numdev = numdev + scartoquad
                devstd = math.sqrt(numdev / (line_count-2))
                print('La deviazione standard del bus '+bus+' vale: {0:.2f}'.format(devstd)+' ms')
        print('----------------------------------------------------\nLatenza totale accumulata nel test: '+str(totalms)+' ms')
        print('Latenza media totale nel test: {0:.2f}'.format(totalms/79)+' ms\n\n')
        #plt.bar(totalms)
        #plt.show()

def calcolo_risultati_sia():
    print('RESULTS FROM TEST OF SKYNET NETWORK')
    for test in tests_list_sia:
        print('\n################################################\nRESULTS FOR TEST IN: '+ test)
        totalms = 0
        for bus in busConst1:
            print('----------------------------------------------------\nLatenze per bus '+bus)
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
                print('Latenza accumulata: '+ str(summs)+' ms')
                mediams = summs/(line_count-1)
                print('Latenza media: {0:.2f}'.format(mediams)+' ms')
                totalms = totalms + summs

                numdev = 0
                for value in values:
                    scarto = mediams - int(value)
                    scartoquad = pow(scarto, 2)
                    numdev = numdev + scartoquad
                devstd = math.sqrt(numdev / (line_count-2))
                print('La deviazione standard del bus '+bus+' vale: {0:.2f}'.format(devstd)+' ms')
        print('----------------------------------------------------\nLatenza totale accumulata nel test: '+str(totalms)+' ms')
        print('Latenza media totale nel test: {0:.2f}'.format(totalms/79)+' ms')

ipfs_plot()
calcolo_risultati_ipfs()
calcolo_risultati_sia()
print ("\n################################################\nESECUZIONE TERMINATA")