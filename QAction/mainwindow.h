#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "crypt.h"
#include <QMainWindow>
#include <QFileDialog>
#include <QWidget>
#include <QtGui>
#include <QTextEdit>
#include <QLabel>
#include <QFile>
#include <QDebug>
#include <QTextStream>
#include <QFileInfo>
#include <QMessageBox>
#include <QRadioButton>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();
    crypt *cry;

private slots:
    void on_OK_clicked();

    void on_pathToFile_clicked();

    void on_encrypt_clicked();

    void on_decrypt_clicked();

    void on_actionQuit_triggered();

    void on_actionOpen_triggered();

    void on_actionNew_triggered();

    void on_show_pressed();

    void message();



private:
    QString mFileName;
    Ui::MainWindow *ui;
    QLabel label;
    QPushButton *OK;
    QPushButton *pathToFile;
    QTextEdit *path;
    QRadioButton *encryptRb;
    bool encrypt;
    bool showPass;

    void write(QString FileName, QString text);
    void read(QString FileName);


};

#endif // MAINWINDOW_H
