# part 1

# should encode a the string passed as a param
# remove whitespace/punctuation symbols
# shift 4 to the right
# convert to upper case
# scramble into even index characters first and odd index chars next
# return an array
def encode(plaintext_str, SHIFT_VAL):
    cipher_text = []

    # remove white space and convert to upper case
    plaintext_str = plaintext_str.strip().upper()

    # index through and append only alphabetic characters to the array
    for i, c in enumerate(plaintext_str):
        if c.isalpha():
            cipher_text.append((ord(c) - 65 + SHIFT_VAL) % 26 + 65)
            # ord() https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character


    # scramble the array
    # numerical values of all characters at even positions (0, 2, 4, ...),
    # followed by the numerical values of all characters at odd positions (1, 3, 5, ...)
    even_chars = []
    odd_chars = []
    for i in range(len(cipher_text)):
        if i % 2 == 0:
            even_chars.append(cipher_text[i])
        else:
            odd_chars.append(cipher_text[i])

    output_array = even_chars + odd_chars

    # convert each letter in the array to hex
    hex_vals = []
    for val in output_array:
        hex_vals.append(hex(val))

    return hex_vals


# part 2

# decode the string passed as a param
# shift each 4 to the left
# convert from numerical vals to chars
def decode(cipher_text, SHIFT_VAL):
    num_vals = []

    # convert hex to numerical vals
    for val in cipher_text:
        num_vals.append(int(val, 16))
        # https://www.geeksforgeeks.org/python-program-to-convert-hex-string-to-decimal/

    # unscramble the array
    # the code in the comments is me trying to figure it out but it didn't work :(
    decoded_text = []
    # even_ptr = 0
    # odd_ptr = len(num_vals) // 2

    # for i in range(len(num_vals) // 2):
    #     decoded_text.append(num_vals[even_ptr])
    #     decoded_text.append(num_vals[odd_ptr])
    #     even_ptr += 1
    #     odd_ptr += 1


    # it finally works
    split_point = len(num_vals) // 2

    if len(num_vals) % 2 != 0: # work around the odd number numerical vals
        split_point += 1

    # Separate even and odd characters
    even_chars = num_vals[:split_point]
    odd_chars = num_vals[split_point:]

    for val in even_chars:
        decoded_text.append(val)

    # insert odd characters inbetween even characters in the array
    for i in range(len(odd_chars)):
        decoded_text.insert(2 * i + 1, odd_chars[i])

    # append unshifted characters to the result array
    result_array = []
    for val in decoded_text:
        result_array.append(chr((val - 65 - SHIFT_VAL) % 26 + 65))

    return result_array


def main():
    # defining the constant for the shifting
    SHIFT_VAL = 4

    # display the original string
    plaintext_str = input("Please enter a string: ")
    print("\nString entered: " + plaintext_str + "\n")

    # display the encoded version of the string
    cipher_text = encode(plaintext_str, SHIFT_VAL)
    print("String encoded:")

    # print in group of 5 and move to the next line
    count = 0
    for val in cipher_text:
        print(val, end=' ')
        count += 1
        if count % 5 == 0:
            print()


    # decode the array of characters and display
    print()
    unciphered_text = decode(cipher_text, SHIFT_VAL)
    print("\nString decoded:")
    for c in unciphered_text:
        print(c, end=' ')

# call the main function
if __name__ == '__main__':
    main()
