#ifndef APPLICATION_H
#define APPLICATION_H
#include<QApplication>
#include<QtWidgets>

class application : public QWidget
 {
public:
    application();
private:
    QGroupBox *box;

    QLineEdit *key;
    QLineEdit *path;

    QPushButton *showkey;
    QPushButton *showpath;

    ///layouts
    QGridLayout *grid;
    QFormLayout *form;
    QHBoxLayout Hlayout1;
    QHBoxLayout Hlayout2;
    QVBoxLayout Vlayout;

};
#endif // APPLICATION_H
