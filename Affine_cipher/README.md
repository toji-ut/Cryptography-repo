Task:

Write a program in either Java or Python that will brute force crack an Affine cipher. In other words, it should try for each 12 alpha values {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}, each of the 26 possible beta values {0 .. 25}.  Your program should just decrypt the ciphertext according to all possible key values. You can manually skim the output from your program to determine the correct key and the decrypted message.

Test your program using the ciphertext contained in the provided file ciphertext.txt.  Identify the source of the original plaintext and what key was used to encrypt the message.  Add your answer to your code file as a comment!

Some hints/reminders:
Since the convention is to use all caps for ciphertext, you can just make sure by converting the input to uppercase first.
The ASCII/UTF code for the capital letters 'A' through 'Z' are 65 through 90, inclusive.  So if you subtract 65 from the encoded value, you get the corresponding numerical code we used for the Affine cipher (a = 0, b = 1, etc.)
The ASCII/UTF code for lower case letters 'a' through 'z' are 97 through 122, inclusive.  So after the decryption calculation, if you add 97 to the result, you should get the corresponding lowercase letter.
The multiplicative inverses for each of the possible alpha values are as follows (remember that inverses are reciprocal -- 3 is the inverse of 9, and vice versa): {1};  {3, 9};  {5, 21};  {7, 15};  {11, 19};  {17, 23};  {25}
