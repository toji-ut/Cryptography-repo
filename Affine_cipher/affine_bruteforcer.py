
# decripting function to decrypt each character
def decrypt(ciphertext, a, b):
    plaintext = ''
    for c in ciphertext:
        if c.isalpha():
            # use the inverse formula
            plaintext += (chr(((mod_inverse(a, 26) * (ord(c) - 65 - b)) % 26) + 65))
            # The ASCII code for the capital letters 'A' through 'Z' are 65 through 90, inclusive.
            # subtract 65 from the encoded value, to get the corresponding numerical code
            # we used for the Affine cipher (a = 0, b = 1, etc.)
        else:
            plaintext += c # just in case, genuinely probably useless

    return plaintext


#  helper method to find the mod inverse
def mod_inverse(a, n):
    for i in range(1, n):
        if (a * i) % n == 1:
            return i
    print("Mod inverse doesn't exist")


def bruteforcer(ciphertext):
    # bruteforce, try for each 12 alpha values {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25},
    # each of the 26 possible beta values {0 .. 25}
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            plaintext = decrypt(ciphertext, a, b)
            print("Key: alpha = " + str(a) + ", beta = " + str(b))
            print(plaintext)
            print()


def main():

    # Test your program using the ciphertext contained in the provided file ciphertext.txt.
    with open('ciphertext.txt', 'r') as file:
        ciphertext = file.read()

    # also probably useless since the ciphertext is already in upper case but just to be cautious
    ciphertext = ciphertext.upper()
    print(ciphertext)

    bruteforcer(ciphertext)
    # Key: alpha = 11, beta = 6
    # WETHEPEOPLEOFTHEUNITEDSTATESINORDERTOFORMAMOREPERFECTUNIONESTABLISHJUSTICEINSURE
    # DOMESTICTRANQUILITYPROVIDEFORTHECOMMONDEFENSEPROMOTETHEGENERALWELFAREANDSECURETHE
    # BLESSINGSOFLIBERTYTOOURSELVESANDOURPOSTERITYDOORDAINANDESTABLISHTHISCONSTITUTION
    # FORTHEUNITEDSTATESOFAMERICA

if __name__ == '__main__':
    main()
