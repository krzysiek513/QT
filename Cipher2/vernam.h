#ifndef VERNAM_H
#define VERNAM_H
#include<QString>

class vernam
{
public:
    vernam();
    //std::string enc;

    QString crypt(QString s, QString key);

    QString encrypt(QString s, QString key);
private:

};

#endif // VERNAM_H
