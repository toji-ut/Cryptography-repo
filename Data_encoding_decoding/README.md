Task:

Part 1:  Implement a function that simulates a cipher that takes a text written in standard US-English and performs the following operations:

Remove all whitespace
Remove all punctuation symbols
Perform a shift of +4 (wrapping around) on each character, and convert it to upper case
Create an output array/list that contains the numerical values of all characters at even positions (0, 2, 4, ...), followed by the numerical values of all characters at odd positions (1, 3, 5, ...)
Print the output array in groups of five characters. Values should be printed in hex values. Separate values by a single space, and separate letter groups by newlines

Part 2:  Write a function that decrypts the output created by the function you wrote for Part 1 by reversing the steps. NOTE: you won't be able to recover whitespace, punctuation symbols or original case this way!

So this function should:
Create a list of the numerical values in the correct order
Shift each character to the left by 4 (wrapping around)
Convert back to characters from the numerical values using UTF-8 encoding
You can test with the input "Hello, World!".  This should lead to an encoding of:

```
0x4C 0x50 0x53 0x53 0x50
0x49 0x50 0x41 0x56 0x48
```


and result in the following string after decoding:

```
H E L L O W O R L D
```
