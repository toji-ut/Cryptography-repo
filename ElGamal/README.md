Task:

The message that is encrypted should be entered as a String. The String will be converted to a very large number consisting of the ASCII codes of each character concatenated together. This very large number will be the m that is encrypted.
Decryption should result in computing the same very large number m. Once you have m, then convert it back to a String and display the result.
HINT: In Java, you do not have to this manually. Both the String and the BigInteger class can work with byte[] byte arrays.
The BigInteger class has a constructor that can take a byte array as an argument and generate the number based on the provided array. There is also a toByteArray() (non-static) method that can convert itself to a byte array.
Meanwhile, the String class has a getBytes() method that returns a byte array containing the encodings for each character. The String class also has a constructor that can take a byte array as an argument and create a String where each character is decoded according to each byte in the array. The default encoding scheme is ASCII.
For Python implementations, you'll have to do some extra work.
You could, of course, use a for loop to return a list with each character's ascii code. But when concatenating (or joining) to a single long value, you need to be consistent with how many digits to use (in base 10, you can have 2 or 3 digit values). Otherwise, it will be impossible to parse it back to component characters.
Hint: You probably want to convert each char encoding to hex so you have a consistent 2-hex digit encoding for each character. (But be careful about the leading "0x" prefix Python automatically inserts.)
Any "creative" mathematical manipulation must be fully commented and explained and sourced.
Make sure that your program is generalized. You can test it out for the provided example below, BUT it should be work for ANY input prime number, secret number, message (shorter than your prime), and random message key.
Make any necessary changes to clean up the code and make it more user friendly (helpful prompt messages, output, etc). But don't add any unnecessary features.
Feel free to use the ElGamal.ZIP on the Moodle as a starting off point (but not required). Compartmentalize data as appropriate and define methods to perform major operations.

Test input:

p = 290249282772097489001037512744818724479 [128 bits]
alpha = 2
a = 1912062319540607
message = Cryptography!
k = 21205200308120525

Test output:

beta = 204425843808726574008313391612189709033
m = 5343714990652413231306415569185
r = 95362866958141345467790058284834141315
t = 202678883533677262297736902001266815564
