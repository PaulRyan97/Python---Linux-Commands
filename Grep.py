#!/usr/bin/env python3

from sys import argv
#Searches the files for the given pattern and returns the lines that contain
#it. If the option "-n" is given it also prints the line number. If the option
#"-v" is given it prints the lines that do not contain that function.


n = 0
s = 2
p = 1
v = 0

if "-n" in argv:
    n = 1
    s += 1
    p += 1
if "-v" in argv:
    v += 1
    s += 1
    p += 1
for e in range(s, len(argv)):
    try:
        filehandle = open( argv[e], "r" )
    except IOError:
        print( "Grep: Cannot open %s"% ( argv[e] ) )

    linenumber = 0
    for line in filehandle:
        linenumber += 1
        if argv[p] in line and  n == 0 and v == 0:
                print ( "%s: %s" % ( argv[e], line ))
        elif argv[p] in line and n == 1 and v == 0:
            print ( "%s: %3i %s" % ( argv[e], linenumber, line))
        elif argv[p] not in line and v == 1 and n == 0:
            print ( "%s: %s" % ( argv[e], line ))
        elif argv[p] not in line and v == 1 and n == 1:
            print ( "%s: %3i %s" % ( argv[e], linenumber, line ))
        
        else:
            continue
                



