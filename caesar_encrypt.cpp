#include <iostream>
#include <ctype.h>

using namespace std;
 
string encrypt(string argc, int key_shift)
{
    string result = "";
 
    for (int i = 0; i < argc.length(); i++) {
        if (isupper(argc[i])){
            result += char(int(argc[i] + key_shift - 65) % 26 + 65);
        }
        else{
            result += char(int(argc[i] + key_shift - 97) % 26 + 97);
        }
    }
    return result;
}

int main()
{
    int ascChar;
    int key_shift;
    string argc;
    cout << "Masukkan character: " ;
    getline(cin,argc);
    cout << "Masukkan key-shift: " ;
    cin >> key_shift;

    for (int i=0;i<argc.length();i++)
    {
        ascChar = argc[i];
    }
    if (ascChar >= 50){
        cout << "Input text     : " << argc << "\n";
        cout << "Key Shift      : " << key_shift << "\n";
        cout << "Encrypted text : " << encrypt(argc, key_shift);
    }
    else{
        return 1;
    }
    return 0;
}