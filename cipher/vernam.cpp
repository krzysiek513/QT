#include "vernam.h"

Vernam::Vernam()
{

}

QString Vernam::encrypt(QString text, QString key)
{
    enc = "";
    std::string k = key.toStdString();
    std::string s = text.toStdString();
    char c;
    int i,j=0;
    for(i=0;i<s.size();i++)
    {
          c = s[i]^k[j];
          enc += c;
          j++;
          if(j>=k.size())
          {
                 j =0;
          }
    }

    return QString::fromStdString(enc);
}

QString Vernam::decrypt(QString text, QString key)
{
    std::string dec;
    std::string k = key.toStdString();
    std::string s = text.toStdString();
    int i,j=0;
    char c;
    for(i=0;i<s.size();i++)
    {
          c = s[i] ^ k[j];
          dec += c;
          j++;
          if(j>=k.size())
          {
                 j =0;
          }
    }
    return QString::fromStdString(dec);
}
