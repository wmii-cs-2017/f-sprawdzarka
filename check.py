#!/usr/bin/python3

import io
import os
import sys
import subprocess
import time
import platform
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
        if platform.system().lower() in ('windows'):
            system_format = '.exe'
        elif platform.system().lower() in ('darwin'):
            system_format = 'mac' 
        else: # linux
            system_format = ''

        startGood = time.time()
        goodProcess = run( [ './good' + system_format ], stdout = PIPE, input = yourInput, encoding = 'ascii' )
        endGood = time.time()

        goodOutput = io.StringIO( goodProcess.stdout )

        startBad = time.time()
        badProcess = run( [ './' + fileName], stdout = PIPE, input = yourInput, encoding = 'ascii' )
        endBad = time.time()

        badOutput = io.StringIO( badProcess.stdout )


        for line in goodOutput:
            str = inputString.readline()
            badLine = badOutput.readline()

            if line == badLine:
                print( bcolors.OKGREEN + '[DOBRZE] ' + bcolors.ENDC + '{}'.format( badLine ), end = '' )
            else:
                print( bcolors.FAIL + '[ŹLE] ' + bcolors.ENDC + '{} ->'.format( badLine.rstrip() ) + bcolors.OKGREEN + ' {}'.format( line ) + bcolors.ENDC, end = '' )

        print( "Czas: {}".format( endGood - startGood ) )
        print( "Twój czas: {}".format( endBad - startBad ) )

        goodOutput.close()
        badOutput.close()

    except FileNotFoundError:
        print( bcolors.FAIL + 'Nie znaleziono pliku!' + bcolors.ENDC )


try:
    fileName = sys.argv[ 1 ]
except IndexError:
    print( bcolors.WARNING + 'Brak nazwy pliku! Ustawiam domyślnie: main' + bcolors.ENDC )
    fileName = 'main'

tests = [ 'set', 'put', 'pop', 'mov_w', 'set_l', 'fill', 'sum', 'custom' ]

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
            print( bcolors.ENDC + bcolors.BOLD + '\nSPRAWDZAM: ' + bcolors.ENDC + '{}'.format( test ) )
            inputFile = open( 'input_' + test + '.txt', 'r' ) 
            yourInput = inputFile.read()

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
        print( bcolors.ENDC + bcolors.BOLD + '\nSPRAWDZAM: ' + bcolors.ENDC + '{}'.format( tests[ choice - 3 ] ) )
        inputFile = open( 'input_' + tests[ choice - 3 ] + '.txt', 'r' )
        yourInput = inputFile.read()
        check()

    except FileNotFoundError:
        print( bcolors.FAIL + 'Nie znaleziono pliku!' + bcolors.ENDC )

else:
    print( '>:(' )


exit()
