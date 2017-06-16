#ifndef MYWINDOW_H
#define MYWINDOW_H

#include <QRadioButton>
#include <QTextEdit>

#include <QMainWindow>

namespace Ui {
class MyWindow;
}

class MyWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MyWindow(QWidget *parent = 0);
    ~MyWindow();
    void encrypt();
    void decrypt();

private:
    Ui::MyWindow *ui;
    QRadioButton *enRB;
    QRadioButton *deRB;
    QTextEdit  *cryText;
};

#endif // MYWINDOW_H
