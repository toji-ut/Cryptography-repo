#include <cctype>
#include <iostream>

using namespace std;

string shiftCipher(string sentence, int shiftVal) {
  string result_cipher = ""; // to return the cipher

  // convert to upper case, c++ can not convert the whole sentence at once :(
  for (int i = 0; i < sentence.length(); i++) {
    sentence[i] = toupper(sentence[i]);
  }

  for (int i = 0; i < sentence.length(); i++) {
    if (sentence[i] >= 'A' && sentence[i] <= 'Z') {
      // shift the letter from the sentence and mod 26 for alphabet
      result_cipher += (sentence[i] - 'A' + shiftVal) % 26 + 'A';
    } else {
      result_cipher += sentence[i];
    }
  }
  return result_cipher;
}

int main() {
  srand(time(0));             // plant a seed to have a random everytime
  int shiftVal = rand() % 26; // randomize the shift value

  cout << "Enter a text to apply the shift cipher: ";
  string inputText;
  getline(cin, inputText); // get the input sentence

  string ciphText = shiftCipher(inputText, shiftVal); // cipher using the func

  // display the output
  cout << "Original Text: " << inputText << endl;
  cout << "Shift Value: " << shiftVal << endl;
  cout << "Ciphered Text: " << ciphText << endl;

  return 0;
}
