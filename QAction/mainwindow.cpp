#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow), encrypt(true), showPass(false)
{
    ui->setupUi(this);
    cry = new crypt();
    ui->key->setEchoMode(QLineEdit::Password);
    //label = new QLabel;
    OK = new QPushButton;
    pathToFile = new QPushButton;
    path = new QTextEdit;
    mFileName = "dokument1.txt";

   // connect(encryptRb,SIGNAL(pressed(),this,SLOT(message());
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::write(QString FileName, QString text)
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

void MainWindow::read(QString FileName)
{
    QFile mFile(FileName);

    if(!mFile.open(QFile::ReadOnly | QFile::Text))
    {
            qDebug() << "could not open file for read!";
            return;
    }
    QTextStream in(&mFile);
    QString mText = in.readAll();
    cry->decrypt(mText);
    ui->label->setText(cry->plainText);
    qDebug() << mText;

    mFile.close();

}

void MainWindow::on_OK_clicked()
{
    if(encrypt)
    {
        QString pathToRead = ui->path->text();
        ui->label->setText("encrypting \n" + pathToRead);
        QString fileName = "file.txt";

        cry->encrypt(pathToRead);
        QString keys = ui->key->text();
        cry->key  = keys.split(" ")[0].toInt();

       // ui->label->setText(QString::number(cry->x));
        write(fileName, cry->encryptedText);
    }
    else
    {
        QString pathToRead = ui->path->text();
        QFileInfo dir(pathToRead);
        QString s = dir.absoluteFilePath();
        read(s);

        //qDebug() << s;
        //ui->label->setText("dsf");
    }


}

void MainWindow::message()
{
    int respond = QMessageBox::question(this, "Question", "Encrypt from file?",QMessageBox::Yes|QMessageBox::No);
    if(!respond)
    {

        ui->pathToFile->setEnabled(false);

    }

}

void MainWindow::on_pathToFile_clicked()
{
    QString file;
    QString filter ("text files (*.txt);;crypted (*.ksz);;all files (*.*)");
    file = QFileDialog::getOpenFileName (this,"Otwieranie",".",filter);
    ui->path -> setText(file);
}

void MainWindow::on_encrypt_clicked()
{
    encrypt = true;
    ui->encrypt->setChecked(true);
}

void MainWindow::on_decrypt_clicked()
{
    ui->decrypt->setChecked(true); // by wlaczyc przycisk musi byc true
    encrypt = false;
    ui->pathToFile->setEnabled(true);

}

void MainWindow::on_actionQuit_triggered()
{
    close();
}

void MainWindow::on_actionOpen_triggered()
{
    ui->pathToFile->setEnabled(true);
    ui->decrypt->setChecked(true);
    encrypt = false;
}

void MainWindow::on_actionNew_triggered()
{
    encrypt = true;
    ui->encrypt->setChecked(true);
    message();
}

void MainWindow::on_show_pressed()
{
    showPass = !showPass;
    if(showPass)
        ui->key->setEchoMode(QLineEdit::Normal);
    else
        ui->key->setEchoMode(QLineEdit::Password);
}
