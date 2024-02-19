Task:

Write a program in either Java, Python, C, or C++ (your choice) in the VPL that will apply a shift cipher (of a randomized amount) to a given input text.  In a shift cipher, each input letter will be encoded as a different letter by shifting by the determined number of spots wrapping back to the beginning (for example, a shift of 3 would mean:  A -> D, B->E, C->F, ... Z->C).  Case should be ignored, so it would be best to treat all letters as upper case (and convert the input text to upper case letters before performing the substitution).  Do not worry about any non-letter characters.

So in essence, your program will do the following:
Create a randomized shift value (only need to cover 0 through 25)
Take an input text string (can be via user input, or you can hardcode it into your stub).
Apply your shift cipher to your input text string to generate the output message.
Each time you run your program, the output should be different (because your program produces a randomized shift value).  Check to make sure whatever shift value was randomly chosen is applied consistently to the entire input message.
