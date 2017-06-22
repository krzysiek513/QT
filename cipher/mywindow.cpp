#include "mywindow.h"
#include "ui_mywindow.h"

MyWindow::MyWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MyWindow),
    crypt(false)
{
    ui->setupUi(this);
}

MyWindow::~MyWindow()
{
    delete ui;
}

void MyWindow::write(QString FileName, QString text)
{
    QFile mFile(FileName);

    if(!mFile.open(QFile::WriteOnly | QFile::Text))
    {
            qDebug() << "could not open file for write!";
            return;
    }
    QTextStream out(&mFile);
    out << text;

    mFile.flush();
    mFile.close();

}

QString MyWindow::read(QString FileName)
{
    QFile mFile(FileName);

    if(!mFile.open(QFile::ReadOnly | QFile::Text))
    {
            qDebug() << "could not open file for read!";
            return "error";
    }
    QTextStream in(&mFile);
    QString mText = in.readAll();
    //cry->decrypt(mText);
    ui->cryText->setText(mText);
    qDebug() << mText;

    mFile.close();
    return mText;


}

void MyWindow::on_pathPB_clicked()
{
    if(crypt)
    {
        QString file;
        QString filter ("text files (*.txt);;crypted (*.jok);;all files (*.*)");
        file = QFileDialog::getOpenFileName (this,"Open",".",filter);
        ui->pathLE -> setText(file);
    }
    else
    {
        QString file;
        QString filter ("crypted (*.jok);;text files (*.txt);;all files (*.*)");
        file = QFileDialog::getOpenFileName (this,"Open",".",filter);
        ui->pathLE -> setText(file);
    }
}

void MyWindow::on_okPB_clicked()
{
    if(crypt)
    {
        QString pathToRead = ui->pathLE->text();
      //  ui->cryText->setText("ok \n" + pathToRead);
     //   QString fileName = "file.txt";

        //cry->encrypt(pathToRead);
        //QString keys = ui->key->text();
        //cry->key  = keys.split(" ")[0].toInt();

       // ui->label->setText(QString::number(cry->x));

        QString filter ("crypted (*.jok)");
        QString file = QFileDialog::getSaveFileName (this,"Save",".",filter);


        write(file, read(pathToRead));
    }
    else
    {
        QString pathToRead = ui->pathLE->text();
        read(pathToRead);
        QString filter ("text files (*.txt)");
        QString file = QFileDialog::getSaveFileName (this,"Save",".",filter);

        write(file, read(pathToRead));

    }
}

void MyWindow::on_deRB_clicked()
{
    ui->deRB->setChecked(true);
    crypt = false;

}

void MyWindow::on_enRB_clicked()
{
    crypt = true;
    ui->enRB->setChecked(true);
}
