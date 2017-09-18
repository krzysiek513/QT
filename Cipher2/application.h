#ifndef APPLICATION_H
#define APPLICATION_H
#include<QApplication>
#include<QtWidgets>
#include"vernam.h"

class application : public QWidget
 {
    Q_OBJECT
public:
    application();
public slots:
    void keyPB();
    void pathPB();
    void okPB();
    void enRB();
    void crRB();


private:
    vernam *CryText;

    void write(QString FileName, QString text);
    QString read(QString FileName);


    bool crypt;
    bool showPass;
    // view
    QGroupBox *box;
    QRadioButton *crypting;
    QRadioButton *encrypting;

    QLineEdit *key;
    QLineEdit *path;

    QTextEdit *mainText;

    QPushButton *showkey;
    QPushButton *showpath;
    QPushButton *ok;

    ///layouts
    QGridLayout *grid;
    QFormLayout *form;
    QVBoxLayout *VBox;

    void Layout();

};
#endif // APPLICATION_H
