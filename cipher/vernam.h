#ifndef VERNAM_H
#define VERNAM_H

#include <QString>

class Vernam
{
public:
    QString text;
    QString key;
    std::string enc;
    std::string dec;
    Vernam();

    QString encrypt(QString s, QString key);

    QString decrypt(QString s, QString key);
};

#endif // VERNAM_H
