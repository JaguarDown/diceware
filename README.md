# diceware
A python script to quickly and easily generate a truly random diceware passphrase. Can't generate a truly random number on a computer, you say? Nonsense! The source of randomness is obtained with the quantumrandom python library.  It communicates with a JSON API to download random numbers from the ANU Quantum Random Number Generator, which generates random numbers by measuring vacuum fluctuations in a particle accelerator. https://qrng.anu.edu.au/

It then simply extracts some numbers it can use with the EFF large diceware word list and nicely formats the words for you.

## Coming soon...
Additional instructions on installing libraries needed and tweaking the code to make it more community friendly.
