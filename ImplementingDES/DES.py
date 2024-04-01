SBOX1 = [
    [0b101, 0b010, 0b001, 0b110, 0b011, 0b100, 0b111, 0b000],
    [0b001, 0b100, 0b110, 0b010, 0b000, 0b111, 0b101, 0b011]
]

SBOX2 = [
    [0b100, 0b000, 0b110, 0b101, 0b111, 0b001, 0b011, 0b010],
    [0b101, 0b011, 0b000, 0b111, 0b110, 0b010, 0b001, 0b100]
]

# des_round() - performs a single round of simplified DES on given input
#   pt, for round r, using masterkey)
def des_round(pt, masterkey, r):
    # isolate left and right halves of the input
    # use bitwise AND operation to isolate the bits we want
    l_in = (pt & 0b111111000000) >> 6  # need to shift so result is in lower 6 bits
    r_in = pt & 0b000000111111

    # Each round does the following:
    # 1. Call expand() to expand 6-bit r-input to 8-bits
    expR = expand(r_in)

    # 2. Call roundKey() to generate round key based on the master key and round number
    rk = roundKey(masterkey, r)

    # 3. Pass the expanded_r and round key to f():
    fResult = f(expR, rk)

    # 4. XORs result of f() with original left-input. This result is the right part of output
    xor_result = fResult ^ l_in

    # 5. Combine with original right-input (which is the left part of the output)
    result = (r_in << 6) + xor_result

    # Print out results of the round
    print("Round input: " + format(pt, '012b'))
    print("Round key: " + format(rk, '08b'))
    print("Round output: " + format(result, '012b'))

    # return the result of the round
    return result


# expand() - Take 6-bit input and expand to 8 bits according to set pattern
# USED IN STEP 1 of DES_ROUND
def expand(r_in):
    pattern = [1, 2, 4, 3, 4, 3, 5, 6] # pattern array

    # dictionary to get the bits
    positions = {
        1: (r_in & 0b100000) >> 5,
        2: (r_in & 0b010000) >> 4,
        3: (r_in & 0b001000) >> 3,
        4: (r_in & 0b000100) >> 2,
        5: (r_in & 0b000010) >> 1,
        6: (r_in & 0b000001),
    }

    result = 0

    # looping to fit this pattern (1) (2) (4) (3) (4) (3) (5) (6)
    for i in range(len(pattern)):
        result += positions[pattern[i]] << (7 - i)

    return result

# roundKey() - generates the round key from master key for round r
# USED IN STEP 2 of DES_ROUND
def roundKey(mk, r):
    start_bit = (r - 1) % 9

    rk = 0

    for i in range(8):
        bit_index = (start_bit + i) % 9
        rk |= (mk >> (8 - bit_index)) << (7 - i)

    return rk

# f() - return a 6-bit value according to f() based on expanded r and round key
# USED IN STEP 3 of DES_ROUND
def f(expR, rk):
    # XOR the expanded input with the round key
    xor_result = expR ^ rk
    # Split into two 4-bit halves
    left_half = (xor_result & 0b11110000) >> 4
    right_half = xor_result & 0b00001111
    # Use S-Boxes to transform the halves into 3-bit outputs
    # Row is determined by the most significant bit, column by the next 3 bits
    row1, col1 = left_half >> 3, left_half & 0b0111
    row2, col2 = right_half >> 3, right_half & 0b0111
    sbox1_result = SBOX1[row1][col1]
    sbox2_result = SBOX2[row2][col2]
    # Concatenate the 3-bit outputs from the S-Boxes
    fResult = (sbox1_result << 3) + sbox2_result
    return fResult


def main():
    msg = 0b011100100110
    masterkey = 0b010011001
    r = 4

    result = des_round(msg, masterkey, r)


if __name__ == "__main__":
    main()
