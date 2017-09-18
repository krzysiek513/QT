#ifndef APPLICATION_H
#define APPLICATION_H
#include<QApplication>
#include<QtWidgets>

class application : public QWidget
 {
public:
    application();
private:

    bool crypt;
    bool showPass;

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
//    QHBoxLayout Hlayout1;
//    QHBoxLayout Hlayout2;
    QVBoxLayout *VBox;

};
#endif // APPLICATION_H
