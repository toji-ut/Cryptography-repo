Task:

A ZIP file is provided containing:

5 RSA keypairs. The private keys are encoding using PEM encoding. The public keys are encoding using DER (ASN.1) encoding.
A pdf containing the Wizard of Oz
A pdf containing Bram Stoker's Dracula
1 digital signature (SHA1 with RSA)
SignatureAssignment.java -- a template file for the assignment
Your task is to complete the implementation of SignatureAssignment.java by filling in the code to complete the check() and the main() functions. Read over the materials on the Java Signature library from the Topic 12 notes that we covered in class -- the slides have links to the Java documentation for each.

When the program runs, it should try to verify the signature using each of the 5 public keys on each of the 2 book pdf files to see which key was used to sign which file. Your program should provide a clear output message stating the answer.

Notes:

The template includes 2 utility functions that will help you. You must use these in order to complete the assignment
loadFile() - will load the contents of the file with the specified file name and return a byte array of its contents. You can use this to get the contents of the pdf file and for the signature file
loadKey() - will return a PublicKey object representing the public key that was found in the public key with the specified file name
Review the functions relating to Signatures we discussed in class. Your code will be calls to the Signature class functions or the functions defined in SignatureAssignment.java
You MAY NOT write any addition functions. You MAY NOT write any substantive code that attempts to manually do any of the work required to verify the signature. You MUST use the provided library / utility functions to complete the task.
You will need to handle potential Exceptions thrown by the Signature library methods.
