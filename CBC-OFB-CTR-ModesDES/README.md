Task:

In this assignment, you will be applying the simplified DES-like algorithm from assignment 6 to encrypt a message using the Cipher Block Chaining (CBC), Output Feedback (OFB), and Counter (CTR) modes of operation.

As a reminder, in CBC, the plaintext is XOR'ed with the initialization vector. That result is run through the block encryption (our simplified DES algorithm) and added to the ciphertext output. The result of the block encryption is then used for the next block, where it is XOR'ed with the next block of plaintext before the block encryption is applied. See the figure on Slide 17.

In OFB, the initialization vector is input to the block encryption algorithm. The output is then XOR'ed with the plaintext block to produce the ciphertext for that block. The output of the block encryption is also sent to be used in the next block, where it becomes the input to the block encryption algorithm. See the figure on Slide 26.

In CTR, the initialization vector (or nonce) plus the current counter value is input to the block encryption algorithm. The output is then XOR'ed with the plaintext block to produce the ciphertext for that block. The counter is incremented by 1 and the process is repeated for the next block. See the figure on Slide 29.

I have provided my sample solution for the DES implementation from assignment 6 in a template -- you are welcome to use this or use your own working version. The input string ("World!"), key (421), and initialization vector (124) are already defined. Encrypt the message using these parameters under the CBC, OFB, and CTR modes and output their results. Your output should be:

CBC: 29385252a2c5

OFB: a7ed4d9044a2

CTR: a7e03f949bea

IMPORTANT NOTES:

The DES algorithm operates on 12-bit blocks. You should be using full blocks. Each ASCII character can be represented as a byte (8 bits). This means each block should be made up of 1.5 ASCII characters. You will have to process the input String to split into 12-bit blocks for the encryption. I recommend using hex values, so each block would be made up of 3 hex digits.
Each block should only go through one round of the DES algorithm (round = 1). Do not run multiple rounds for a block, and use round # 1.
It may be easier to use hexadecimal values instead of individual bits. Each hex digit is 4 bits, and a hex literal is denoted by the prefix 0x. If you need to supply the radix, use 16.
Do not worry about the left shifting that is part of the different modes of operation. Just work on the full 12-bit block
