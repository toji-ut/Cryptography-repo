In this assignment, use the provided template file and finish the implementation of the simplified DES-like algorithm from Section 4.2 of the textbook (also described below and in the comments). There is a template file for Java and another for Python. Pick the language of your choice and copy/paste the appropriate file into the VPL to get started.

The main() method is already done. It will follow the example from the textbook, inputting the plaintext = 0b011100100110 with master key = 0b010011001 and perform the 4th round of the DES-like encryption. This method is done and should not be modified.
Your task is to finish the implementation of the des_round() method, and implement the three helper definitions whose headers are provided: expand(), roundKey(), and f(). This method will perform a single round of the simplified DES algorithm, taking in as parameters (1) the input for this round, (2) the master key, and (3) the round number. Your method should perform the simplified DES algorithm as described in the book.

Each round does the following:

expands 6-bit r-input to 8-bits. The 8 bits should be: (1) (2) (4) (3) (4) (3) (5) (6) of original 6-bit input -- this is done by the expand() function
generates round key based on the master key and round number -- this is done by the roundKey() function.
The master key is 9 bits, while the round key is 8 bits. We get the round key for round i by starting at bit i (counting from 1) and taking the next 8 bits of the master key (wrapping around).
For example, if K = 010011001, then K4 = 01100101 (after bits 4 through 9, we reach the end of K, so the last 2 bits were obtained from the beginning of K).
passes the expanded_r and round key to f(), which:
3a. XORs them together;
3b. Splits result into two 4-bit sequences
3c. Refer to the 2 S-Boxes (row = bit 1; column = bits 2-4) to get two 3-bit outputs
3d. Concatenates together to single 6-bit output
This is done by the f() function
XORs result of f() with original left-input. This result is the right part of output
Combine with original right-input (which is the left part of the output)
Refer to the bit-wise operations.

Bitwise AND operator & -- can be used to select specific bits from a given binary string
Bitwise XOR operator ^
Shift operators >> or << -- shift bits to the right or left by the specified number of spots.
Once you're done, run and check the output to make sure it matches the book's example 0b100110011000.
