#include "vernam.h"

Vernam::Vernam()
{

}

QString Vernam::encrypt(QString text, QString key)
{
    std::string k = key.toStdString();
    std::string s = text.toStdString();

    int i,j=0;
    for(i=0;i<s.size();i++)
    {
          enc[i] = s[i] ^ k[j];
          j++;
          if(j>=k.size())
          {
                 j =0;
          }
    }
    char c;
    std::string cale;
    for(i=0;i<s.size();i++)
    {
          c = enc[i];//%74 + 48
          cale+=c;
    }
    return QString::fromStdString(cale);
}

QString Vernam::decrypt(QString text, QString key)
{
    std::string k = key.toStdString();
    std::string s = text.toStdString();
    int i,j=0;
    for(i=0;i<s.size();i++)
    {
          dec[i] = enc[i] ^ k[j];
          j++;
          if(j>=k.size())
          {
                 j =0;
          }
    }
    return QString::fromStdString(dec);
}
