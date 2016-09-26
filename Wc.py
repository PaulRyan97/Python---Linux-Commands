#!/usr/bin/env python3

from sys import argv
#Reads the given files and returns the number of lines, words & characters along
#with the filename. Will only return the number of lines if the option "-l"
#is given.

l = 0
s = 1
if "-l" in argv:
    l = 1
    s += 1
for e in range( s, len(argv)):
        try:
            filehandle = open( argv[e], "r" )
        except IOError:
            print( "Error Reading File '%s'"% ( e ) )

        lines = 0
        words = 0
        characters = 0

        for line in filehandle:
            lines +=1
            word = line.split()
            words += len(word)
            for n in line:
                characters +=1
        if l == 1:
            print( "%s" % ( lines ), end = "" )
            print()
        else:
            print("%s %s %s %s" % ( lines, words, characters, argv[e]), end ="")
            print()

