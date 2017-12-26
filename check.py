#!/usr/bin/python3

import io
import sys
import subprocess
from subprocess import run, PIPE


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def check():
    inputString = io.StringIO( yourInput )

    try:
        goodProcess = run( [ './good' ], stdout = PIPE, input = yourInput, encoding = 'ascii' )
        goodOutput = io.StringIO( goodProcess.stdout )

        badProcess = run( [ './' + fileName ], stdout = PIPE, input = yourInput, encoding = 'ascii' )
        badOutput = io.StringIO( badProcess.stdout )


        for line in goodOutput:
            str = inputString.readline()

            if line == badOutput.readline():
                print( bcolors.OKGREEN + '[DOBRZE] ' + bcolors.ENDC + '{}'.format( str ), end = '' )
            else:
                print( bcolors.FAIL + '[ŹLE] ' + bcolors.ENDC + '{}'.format( str ), end = '' )

        goodOutput.close()
        badOutput.close()

    except FileNotFoundError:
        print( bcolors.FAIL + 'Nie znaleziono pliku!' + bcolors.ENDC )


try:
    fileName = sys.argv[ 1 ]
except IndexError:
    print( bcolors.WARNING + 'Brak nazwy pliku! Ustawiam domyślnie: main' + bcolors.ENDC )
    fileName = 'main'

print( bcolors.BOLD + 'ZADANIE F - TESTER' + bcolors.ENDC )
print( '[1] Testuj z plików' )
print( '[2] Własne' )

choice = input( ' >> ' )

if choice == '1':
    tests = [ 'fill', 'mov_w', 'pop', 'put', 'set', 'set_l', 'sum' ]

    for i in tests:
        inputFile = open( 'input_' + i + '.txt', 'r' )
        yourInput = inputFile.read()

        print( bcolors.ENDC + bcolors.BOLD + '\nSPRAWDZAM: ' + bcolors.ENDC + '{}'.format( i ) )
        check()

elif choice == '2':
    command = ''
    yourInput = ''

    while command != 'END':
        command = input( '' )
        yourInput += command + '\n'

    check()
else:
    print( '>:(' )


exit()