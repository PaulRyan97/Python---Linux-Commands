
    
  #!/usr/bin/env python3

from sys import argv

#Breaks the given number down into its prime factors.



for e in range( 1, len(argv)):
    factors = []
    primes = []
    nonprime = []
    for i in range( 1, int(argv[e]) + 1):
        if int(argv[e])%i == 0:
            factors += [i]
        else:
            continue

    for n in factors:
        for o in range( 2, n ):
            if n%o == 0:
                nonprime += [n]
                break

    for f in factors:
        if f not in nonprime and f > 1:
            primes += [f]
            
    print("%s: %s" % ( argv[e], primes ))

                
             
            

  

       
            
    
