import csv
import os
import math

tests_list = list()
for root, dirs, files in os.walk(".\\testsSia", topdown=False):
    for name in dirs:
        tests_list.append(os.path.join(root, name))

busConst = [
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

print('RESULTS FROM TEST OF SKYNET NETWORK')
for test in tests_list:
    print('################################################\nRESULTS FOR TEST IN: '+ test)
    totalms = 0
    for bus in busConst:
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
