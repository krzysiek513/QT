#ifndef MYWINDOW_H
#define MYWINDOW_H

#include <QRadioButton>
#include <QTextEdit>
#include <QFileDialog>

#include <QDebug>
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
    //void encrypt();
    //void decrypt();

private slots:
    void on_pathPB_clicked();

    void on_okPB_clicked();

    void on_deRB_clicked();

    void on_enRB_clicked();

private:
    bool crypt;

    Ui::MyWindow *ui;

    void write(QString FileName, QString text);
    QString read(QString FileName);

};

#endif // MYWINDOW_H
