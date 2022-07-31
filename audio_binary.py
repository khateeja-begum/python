import os

from bitstring import BitArray

#os.chdir('filepath')
b=BitArray(bytes=open('voice.mp3','rb').read())

# Store result
with open('filename_bits.txt', 'w') as file1: 
    file1.write(b.bin)