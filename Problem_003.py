# Largest prime factor
# Largest prime factor of 600851475143

import math
pf = 600851475143

numb = pf
count = 2

while numb > 1:
    if  numb % count == 0: #if pf can be divided by count val
        highfact = count #count val is new highest factor
        numb = numb/count #pf is reduced by factor
        count = count - 1 #checks again for same factor (i.e. 4->2->1)
        print("The highest factor is:", highfact)
        print("Remaining value: ", numb)

    count = count + 1 # to next factor