import java.io.*;
import java.security.*;
import java.security.interfaces.*;
import java.security.spec.*;

public class SignatureAssignment {

    /**
     * Loads filename into a byte array.
     * @param filename Name of file to be loaded
     * @return null on failure, or byte array on success
     */
    public byte[] loadFile(String filename) {
        byte[] data = null;
        FileInputStream fis = null;
        try {
            File f = new File(filename);
            fis = new FileInputStream(f);
            data = new byte[(int) f.length()];
            fis.read(data);
            fis.close();
        } catch (FileNotFoundException ex) {
            System.err.println("Unable to open " + filename);
            return null;
        } catch (IOException ex) {
            System.err.println("Unable to open " + filename);
            return null;
        } finally {
            if (fis != null) {
                try {
                    fis.close();
                } catch (Exception e) {
                    // ignore
                }
            }
        }
        return data;
    }

    /**
     * Loads public key from filename
     * @param filename Name of file to be loaded
     * @return null on failure, or a PublicKey on success
     */
    public PublicKey loadKey(String filename) {
        byte[] data = loadFile(filename);
        if (data == null) {
            System.err.println("Unable to load key file.");
            return null;
        }
        X509EncodedKeySpec x509 = new X509EncodedKeySpec(data);
        PublicKey pub = null;
        try {
            KeyFactory kf = KeyFactory.getInstance("RSA");
            pub = kf.generatePublic(x509);
        } catch (NoSuchAlgorithmException e) {
            System.err.println(e);
            return null;
        } catch (InvalidKeySpecException e) {
            System.err.println(e);
            return null;
        }
        return pub;
    }

    /**
     * Check if pdfFile was signed by keyFile, resulting in sigFile
     * @param keyFile File containing the DER-encoded key
     * @param sigFile File containing the signature
     * @param pdfFile File containing pdf
     * @return true of everything matches, false otherwise.
     */
    public boolean check(String keyFile, String sigFile, String pdfFile) {
        /* WRITE THIS CODE:
         * 	   1. load public key from file
         *     2. load signature from file
         * 	   3. Use Signature.getInstance() to get a new Signature object
         * 		  the signature was made as an RSA encoded SHA1 hash
         *     4. initialize the signature validation with the public key
         *     5. update the signature with the contents of the pdf
         *     6. check the signature
         */

        // load the public key, pdf file, and the signature
        PublicKey publicKey = loadKey(keyFile);
        byte[] signatureBytes = loadFile(sigFile);
        byte[] pdfBytes = loadFile(pdfFile);

        // if null, display an error
        if (publicKey == null || signatureBytes == null || pdfBytes == null) {
            System.err.println("Failed to load required files.");
            return false;
        }

        // try and catch block to verify the signature
        try {
            Signature signature = Signature.getInstance("SHA1withRSA");
            signature.initVerify(publicKey);
            signature.update(pdfBytes);
            return signature.verify(signatureBytes);
        } catch (
            NoSuchAlgorithmException
            | InvalidKeyException
            | SignatureException e
        ) {
            System.err.println(
                "Signature verification failed: " + e.getMessage()
            );
            return false;
        }
    }

    public static void main(String args[]) {
        SignatureAssignment sigTester = new SignatureAssignment();

        /* WRITE THIS CODE:
         *     check all combinations of PDF and key to determine if any
         *     were used to set the signature. If so, print a message to stdout.
         */

        // Load all key files and PDF files
        String[] keyFiles = {
            "key_pub_1.der",
            "key_pub_2.der",
            "key_pub_3.der",
            "key_pub_4.der",
            "key_pub_5.der",
        };

        String[] pdfFiles = {
            "the_wonderful_wizard_of_oz.pdf",
            "Dracula_NT.pdf",
        };

        String signatureFile = "signature.dat";

        // Iterate over all combinations of keys and PDFs to check signature
        for (String keyFile : keyFiles) {
            for (String pdfFile : pdfFiles) {
                // user the check function to determine which combination was used to set the signature
                if (sigTester.check(keyFile, signatureFile, pdfFile)) {
                    System.out.println(
                        "Signature in " +
                        signatureFile +
                        " is valid for " +
                        pdfFile +
                        " using key in " +
                        keyFile
                    );
                    return; // Exit after finding one valid signature
                }
            }
        }

        System.out.println("No valid signature found.");
    }
}
