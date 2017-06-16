#include "crypt.h"

crypt::crypt()
{

}

void crypt::encrypt(QString text)
{
    encryptedText = text;
//    for(int i=0; i<=text.length(); i++)
//    {
//        text.at(i)+x;
////    if(text[i]>=65 && text[i]<=90-x) text[i]=int(text[i])+x; //wielkie liter
////    else if(text[i]>=91-x && text[i]<=90) text[i]=int(text[i])-26+x; // wielkie litery
////    else if(text[i]>=97 && text[i]<=122-x) text[i]=int(text[i])+x; //małe liter
////    else if(text[i]>=123-x && text[i]<=122) text[i]=int(text[i])-26+x; //małe litery
//    }
    return;
}

void crypt::decrypt(QString cryText)
{
    plainText = cryText;
    return;
}
