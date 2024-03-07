# File:  RC4.py
# Template file for Assignment #05 (CSC 381 - Spring 2024)
# Author:  S. Kim

#encrypt() - Encrypt plaintext with the given key and place output
#   in ciphertext
#     DO NOT MODIFY!!
def encrypt(plaintext, key, ciphertext):
    #Ensure key length is between 5 to 16 bytes
    assert len(key) >= 5, "key is too short, must be between 5 to 16 bytes"
    assert len(key) <= 16, "key is too long, must be between 5 to 16 bytes"

    #create our state S and set key schedule
    s = []
    genKSA(key,s)

    #create a key stream and call genKeyStream() to create the key bytes
    #  according to the schedule s
    keyStream = []
    for i in range(256):
        keyStream.append(i)
    genKeyStream(s, keyStream, len(plaintext))

    #For debugging...
    print("keystream: ","\t")
    ks = []
    for i in range(len(plaintext)):
        ks.append(hex(keyStream[i]))
    print(ks)

    #encrypt the plaintext using the key stream
    # encryption does bitwise XOR of plaintext with keystream
    for i in range(len(plaintext)):
        ciphertext.append(plaintext[i] ^ keyStream[i])
#enddef


#decrypt() - Decrypt ciphertext with key.  Place output in plaintext
def decrypt(ciphertext, key, plaintext):

    #FILL IN CODE -- THINK CAREFULLY ABOUT THIS.  SHOULD BE 1 LINE

    encrypt(ciphertext, key, plaintext)


#enddef

#genKSA() - Generates the schedule S corresponding to the key
def genKSA(key,s):

    #FILL IN CODE -- Refer to algorithm from lecture slides or to the Wikipedia entry for RC4

    for i in range(256):
        s.append(i)

    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]

#enddef

#genKeyStream() - Generates a keyStream of numBytes bytes, using schedule s
def genKeyStream(s, keyStream, numBytes):
    #FILL IN CODE -- Refer to algorithm from lecture slides or to the Wikipedia entry for RC4

    i = 0
    j = 0
    for k in range(numBytes):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        keyStream.append(s[(s[i] + s[j]) % 256])
#enddef

#main() - Encrypt the phrase "Attack at dawn" using key "Secret"
#  Use the ciphertext and the key to recover the plaintext in order
#  to verify answer.
#     DO NOT MODIFY!!
def main():
    #Use "Secret" as the key
    key = []
    passphrase = "Secret"
    for c in passphrase:
        key.append(ord(c))

    #Set up plaintext "Attack at dawn"
    plain = []
    msg = "Attack at dawn"
    for c in msg:
        plain.append(ord(c))

    #Call encrypt() function and print out hex representation
    cipher = []
    encrypt(plain, key, cipher)
    print("Ciphertext:","\t")
    ciphertext = []
    for i in cipher:
        ciphertext.append(hex(i))
    print(ciphertext)

    #Call decrypt() function and reproduce original plaintext
    plain = []
    decrypt(cipher, key, plain)
    print("Recovered plaintext:", "\t")
    plaintext = ""
    for i in plain:
        plaintext += chr(i)
    print(plaintext)
#enddef

if __name__ == "__main__":
    main()
