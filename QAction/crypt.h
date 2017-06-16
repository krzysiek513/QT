#ifndef CRYPT_H
#define CRYPT_H
#include <QString>

class crypt
{
public:
    crypt();
    void encrypt(QString text);
    void decrypt(QString text);


    QString plainText;
    QString encryptedText;
    int key;


};

#endif // CRYPT_H
