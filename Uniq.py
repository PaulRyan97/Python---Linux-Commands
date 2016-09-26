#!/usr/bin/env python3

from sys import argv
#Prints all the unique lines in the file

for e in range( 1, len(argv)):
    try:
        filehandle = open( argv[e], "r" )
    except IOError:
        print( "Error Reading File '%s'"% ( argv[e]) )

    previous = ""

    for line in filehandle:
        if line in previous:
            continue
        else:
            previous += line
            print( line )
