# File: DESModes.py
# Template for encrypting messages under different Modes of Operation
#  with our simplified DES-like algorithm
# Author: S. Kim

SBOX1 = [ [0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000],
          [0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011] ]

SBOX2 = [ [0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010],
          [0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100] ]

# des_round() - performs a single round of simplified DES on given input
#   pt, for round r, using masterkey)
def des_round(pt, masterkey, r):
    #isolate left and right halves of the input
    #use bitwise AND operation to isolate the bits we want
    l_in = (pt & 0b111111000000) >> 6 #need to shift so result is in lower 6 bits
    r_in = pt & 0b000000111111

    #FILL IN THE REST
    #Each round does the following:
    #  1. expands 6-bit r-input  to 8-bits
    #      The 8 bits should be:  (1) (2) (4) (3) (4) (3) (5) (6) of original 6-bit input
    #  2. generates round key based on the master key and round number
    #  3. passes the expanded_r and round key to f(), which:
    #     3a. XORs them together;
    #     3b. Splits result into two 4-bit sequences
    #     3c. Refer to the 2 S-Boxes (row = bit 1; column = bits 2-4) to get two 3-bit outputs
    #     3d. Concatenates together to single 6-bit output
    #  4. XORs result of f() with original left-input. This result is the right part of output
    #  5. Combine with original right-input (which is the left part of the output)

    #1. expand r_in to 8 bits
    expR = expand(r_in)

    #2. generate round key
    rk = roundKey(masterkey, r)

    #3. process and compute f() based on expR and rk
    fResult = f(expR, rk)

    #4. XOR result with original left_input to be next r
    rOut = fResult ^ l_in

    #5. Combine with original right_input
    lOut = r_in  #old r becomes next l

    result = (lOut << 6) | rOut

    return result

#enddef

#expand() - Take 6-bit input and expand to 8 bits according to set pattern
def expand(r_in):
    r = bin(r_in)
    r = r[2:]  # cut out 0b prefix

    #pad to 6 characters if needed
    while (len(r) < 6):
        r = "0"+ r;
    result = "" + r[0] + r[1] + r[3] + r[2] + r[3] + r[2] + r[4] + r[5]

    return int(result,2)
#enddef

#roundKey() - generates the round key from master key for round r
def roundKey(mk, r):
    key = bin(mk)
    key = key[2:]  #cut out 0b prefix

    #pad to 9 characters if needed
    while (len(key) < 9):
        key = "0" + key

    #rotate left (r - 1) times to get the string starting with char we nee
    for i in range(r-1):
        key = key[1:] + key[0]

    #slice to keep only first 8 bits
    rk = key[:8]
    return int(rk,2)
#enddef

#f() - return a 6-bit value according to f() based on expanded r and round key
def f(expR, rk):
    #XOR together
    xor = expR ^ rk

    #break into 4-bit halves
    input1 = (xor & 0b11110000) >> 4
    input2 = (xor & 0b00001111)

    #look up in S-Boxes
    #  row = 1st bit; column = bits 2-4
    output1 = SBOX1[(input1 & 0b1000) >> 3][input1 & 0b0111]
    output2 = SBOX2[(input2 & 0b1000) >> 3][input2 & 0b0111]

    #combine output into 6-bit value:  output1 shifts to bigs 1-3
    result = (output1 << 3) + output2

    return result
#enddef

#cbc() - Encrypts msg with simplified DES algorithm under Cipher Block Chaining mode
def cbc(msg, masterkey, iv):
    #FILL IN CODE
    to_hex = msg.encode('utf-8').hex()

    blocks = []
    for i in range(0, len(to_hex), 3):
        blocks.append(to_hex[i:i+3])

    encrypted = 0
    hex_string = ''

    for i, block in enumerate(blocks):
        block_int = int(block, 16)
        if i == 0:
            new_block = block_int ^ iv
        else:
            new_block = block_int ^ encrypted
        encrypted = des_round(new_block, masterkey, 1)
        hex_string += format(encrypted, 'x').zfill(3)

    return hex_string


#end def

#ofb() - Encrypts msg with simplified DES algorithm under Output Feedback mode
def ofb(msg, masterkey, iv):
    #FILL IN CODE
    to_hex = msg.encode('utf-8').hex()

    blocks = []
    for i in range(0, len(to_hex), 3):
        blocks.append(to_hex[i:i+3])

    encrypted = iv
    hex_string = ''

    for block in blocks:
        block_int = int(block, 16)
        encrypted = des_round(encrypted, masterkey, 1)
        new_block = block_int ^ encrypted
        hex_string += format(new_block, 'x').zfill(3)

    return hex_string

#enddef

#ctr() - Encrypts msg with simplified DES algorithm under Counter mode
def ctr(msg, masterkey, iv):
    #FILL IN CODE
    to_hex = msg.encode('utf-8').hex()

    blocks = []
    for i in range(0, len(to_hex), 3):
        blocks.append(to_hex[i:i+3])

    counter = iv
    hex_string = ''

    for block in blocks:
        block_int = int(block, 16)
        encrypted_counter = des_round(counter, masterkey, 1)
        new_block = block_int ^ encrypted_counter
        hex_string += format(new_block, 'x').zfill(3)
        counter += 1

    return hex_string

#enddef


def main():
    msg = "World!"
    masterkey = 421
    iv = 124

    cbc_result = cbc(msg, masterkey, iv)
    print("CBC:  " + cbc_result)

    ofb_result = ofb(msg, masterkey, iv)
    print("OFB:  " + ofb_result)

    ctr_result = ctr(msg, masterkey, iv)
    print("CTR:  " + ctr_result)


#enddef

if __name__ == "__main__":
    main()
