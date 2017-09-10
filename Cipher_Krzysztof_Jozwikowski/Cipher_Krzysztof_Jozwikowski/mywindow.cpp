#include "mywindow.h"
#include "ui_mywindow.h"

MyWindow::MyWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MyWindow),
    crypt(true),
    showPass(false)
{
    ui->setupUi(this);
    encryping = new Vernam();
    ui->keyLE->setEchoMode(QLineEdit::Password);
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


    mFile.flush();
    mFile.close();
    return mText;


}

void MyWindow::on_pathPB_clicked()
{
    if(crypt)
    {
        QString file;
        QString filter ("text files (*.txt);;encrypted (*.jok);;all files (*.*)");
        file = QFileDialog::getOpenFileName (this,"Open",".",filter);
        ui->pathLE -> setText(file);
    }
    else
    {
        QString file;
        QString filter ("encrypted (*.jok);;text files (*.txt);;all files (*.*)");
        file = QFileDialog::getOpenFileName (this,"Open",".",filter);
        ui->pathLE -> setText(file);
    }
}

void MyWindow::on_okPB_clicked()
{
    if(crypt) //szyfrowanie
    {
        QString pathToRead = ui->pathLE->text();
        QString filter ("encrypted (*.jok)");
        QString file = QFileDialog::getSaveFileName (this,"Save",".",filter);
        QString key = ui->keyLE->text();
        QString text = read(pathToRead);
        write(file, encryping->encrypt(text, key));
        ui->keyLE->setText("");
        ui->pathLE->setText("");
    }
    else //odszyfrowanie
    {

        QString pathToRead = ui->pathLE->text();
        QString key = ui->keyLE->text();
        QString text = read(pathToRead);
        QString filter ("text files (*.txt)");
        QString file = QFileDialog::getSaveFileName (this,"Save",".",filter);
        QString plainText = encryping->decrypt(text, key);
        ui->keyLE->setText("");
        write(file, plainText);
        ui->cryText->setText(plainText);
        ui->pathLE->setText("");

    }
}

void MyWindow::on_deRB_clicked()
{
    ui->cryText->setText("");
    ui->pathLE->setText("");
    ui->keyLE->setText("");
    ui->deRB->setChecked(true);
    crypt = false;

}

void MyWindow::on_enRB_clicked()
{
    ui->cryText->setText("");
    ui->pathLE->setText("");
    ui->keyLE->setText("");
    crypt = true;
    ui->enRB->setChecked(true);
}

void MyWindow::on_keyPB_clicked()
{
    showPass = !showPass;
    if(showPass)
        ui->keyLE->setEchoMode(QLineEdit::Normal);
    else
        ui->keyLE->setEchoMode(QLineEdit::Password);
}
