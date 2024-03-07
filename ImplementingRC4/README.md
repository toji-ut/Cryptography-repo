Task:

In this assignment, use the provided template file and finish the implementation of the RC4 algorithm.  There is a template file for Java and another for Python.  Pick the language of your choice and copy/paste the appropriate file into the VPL to get started.

The main() function is already done.  It will use "Secret" as the key and attempt to encrypt the message "Attack at dawn" using RC4, and then decrypt the message back
The encrypt() function is already done.  It will ensure that the key is between 5 to 16 bytes, call the getKSA method to generate the key schedule, then call the genKeyStream method to generate the stream of key bytes.  Once the key stream is generated, the function will encrypt the plaintext based on the produced key stream (using bitwise XOR operation).
Your task is to provide the definitions for the three methods (headers already provided):

genKSA - generates the key schedule according to the algorithm provided on Slide 21 of the notes.
genKeyStream- generates the key stream of numBytes long using the created key schedule, according to the algorithm provided on Slide 23 of the notes [Note: You will not "output" key bytes as they are generated.  Instead add them to keyStream so it can be used when the function is finished executing.]
decrypt - decrypts the ciphertext according to the key.  Think carefully about an easy way to do this (should be only 1 line)!

Additional Notes/Instructions:

Check your output against the Wikipedia entry on RC4 to see if your generated keystream and ciphertext are correct.
You may NOT change the provided main() or encrypt() methods.
You may NOT change any of the provided headers.  Do not change function names.  Do not change parameters.  Do not change return types (for Java)
You may NOT add any additional functions.
