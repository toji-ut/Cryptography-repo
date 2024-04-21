p = 290249282772097489001037512744818724479
alpha = 2

# Asymmetric encryption
def encrypt(m, p, alpha, a, k):
    # Calculate beta
    beta = pow(alpha, a, p)
    # Compute r and t
    r = pow(alpha, k, p)
    t = (pow(beta, k, p) * m) % p
    return r, t

def decrypt(r, t, a):
    # Recover m
    m = (t * pow(r, -a, p)) % p
    return m

def string_to_large_number(string):
    # Convert each character to its ASCII code and concatenate
    large_number = 0
    for char in string:
        large_number = large_number * 256 + ord(char)
    return large_number

def large_number_to_string(number):
    # Convert the large number back to a string
    string = ""
    while number > 0:
        string = chr(number % 256) + string
        number //= 256
    return string

def main():
    msg = 'Cryptography!'
    print("Original Message:", msg)

    a = 1912062319540607
    k = 21205200308120525

    print("\nPublic key:")
    print("p =", p)
    print("alpha =", alpha)

    m = string_to_large_number(msg)
    print("m =", m)

    # Encrypt message
    r, t = encrypt(m, p, alpha, a, k)
    print("\nEncrypted message:")
    print("r =", r)
    print("t =", t)

    # Decrypt message
    decrypted_m = decrypt(r, t, a)
    print("\nDecrypted Message:", large_number_to_string(decrypted_m))

if __name__ == '__main__':
    main()
