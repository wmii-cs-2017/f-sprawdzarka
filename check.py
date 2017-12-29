#!/usr/bin/python3

import io
import os
import sys
import subprocess
from subprocess import run, PIPE


class bcolors:
    if os.name == 'posix':
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    else:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''


def check():
    inputString = io.StringIO( yourInput )

    try:
        if os.name == 'nt':
            windowsExt = '.exe'
        else:
            windowsExt = ''

        goodProcess = run( [ './good' + windowsExt ], stdout = PIPE, input = yourInput, encoding = 'ascii' )
        goodOutput = io.StringIO( goodProcess.stdout )

        badProcess = run( [ './' + fileName + windowsExt ], stdout = PIPE, input = yourInput, encoding = 'ascii' )
        badOutput = io.StringIO( badProcess.stdout )


        for line in goodOutput:
            str = inputString.readline()
            badLine = badOutput.readline()

            if line == badLine:
                print( bcolors.OKGREEN + '[DOBRZE] ' + bcolors.ENDC + '{}'.format( badLine ), end = '' )
            else:
                print( bcolors.FAIL + '[ŹLE] ' + bcolors.ENDC + '{} ->'.format( badLine.rstrip() ) + bcolors.OKGREEN + ' {}'.format( line ), end = '' )

        goodOutput.close()
        badOutput.close()

    except FileNotFoundError:
        print( bcolors.FAIL + 'Nie znaleziono pliku!' + bcolors.ENDC )


try:
    fileName = sys.argv[ 1 ]
except IndexError:
    print( bcolors.WARNING + 'Brak nazwy pliku! Ustawiam domyślnie: main' + bcolors.ENDC )
    fileName = 'main'

tests = [ 'fill', 'mov_w', 'pop', 'put', 'set', 'set_l', 'sum', 'custom' ]

print( bcolors.BOLD + 'ZADANIE F - TESTER' + bcolors.ENDC )
print( '[1] Testuj wszystkie' )
print( '[2] Wprowadź własne\n' )

i = 3;

for test in tests:
    print( '[{}] {}'.format( i, test ) )
    i = i + 1


choice = int( input( ' >> ' ) )

if choice == 1:

    for test in tests:
        try:
            inputFile = open( 'input_' + test + '.txt', 'r' )
            yourInput = inputFile.read()

            print( bcolors.ENDC + bcolors.BOLD + '\nSPRAWDZAM: ' + bcolors.ENDC + '{}'.format( test ) )
            check()

        except FileNotFoundError:
            print( bcolors.FAIL + 'Nie znaleziono pliku!' + bcolors.ENDC )

elif choice == 2:
    command = ''
    yourInput = ''

    while command != 'END':
        command = input( '' )
        yourInput += command + '\n'

    print( bcolors.ENDC + bcolors.BOLD + '\nSPRAWDZAM: ' + bcolors.ENDC )
    check()

    choice = input( "Zapisać input? [y/n] " )

    if choice == 'y':
        customInputFile = open( 'input_custom.txt', 'w' )
        customInputFile.write( yourInput )

elif choice >= 3 and choice <= 10:
    try:
        inputFile = open( 'input_' + tests[ choice - 3 ] + '.txt', 'r' )
        yourInput = inputFile.read()

        print( bcolors.ENDC + bcolors.BOLD + '\nSPRAWDZAM: ' + bcolors.ENDC + '{}'.format( tests[ choice - 3 ] ) )
        check()

    except FileNotFoundError:
        print( bcolors.FAIL + 'Nie znaleziono pliku!' + bcolors.ENDC )

else:
    print( '>:(' )


exit()
