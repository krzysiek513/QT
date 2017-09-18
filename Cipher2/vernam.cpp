#include"vernam.h"

vernam::vernam()
{

  //  connect(b1,SIGNAL(clicked()),qApp,SLOT(quit()));
}


QString vernam::crypt(QString text, QString key)
{
    std::string enc;
    std::string k = key.toStdString();
    std::string s = text.toStdString();
    char c;
    uint i,j=0;
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

QString vernam::encrypt(QString text, QString key)
{
    std::string dec;
    std::string k = key.toStdString();
    std::string s = text.toStdString();
    uint i,j=0;
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
