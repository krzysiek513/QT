#ifndef VERNAM_H
#define VERNAM_H

#include <QString>
#include <QDebug>

class Vernam
{
public:
    Vernam();
    std::string enc;

    QString encrypt(QString s, QString key);

    QString decrypt(QString s, QString key);
};

#endif // VERNAM_H
