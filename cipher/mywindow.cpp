#include "mywindow.h"
#include "ui_mywindow.h"

MyWindow::MyWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MyWindow)
{
    ui->setupUi(this);
//    enRB = new QRadioButton(this);
//    cryText = new QTextEdit();

//    QObject::connect(enRB,SIGNAL(pressed()),qApp,SLOT(encrypt()));
}

MyWindow::~MyWindow()
{
    delete ui;
}

void MyWindow::encrypt()
{
    ui->cryText->setText("dupa");
}

void MyWindow::read(QString FileName)
{
    QFile mFile(FileName);

    if(!mFile.open(QFile::ReadOnly | QFile::Text))
    {
            qDebug() << "could not open file for read!";
            return;
    }
    QTextStream in(&mFile);
    QString mText = in.readAll();
    //cry->decrypt(mText);
    ui->cryText->setText(mText);
    qDebug() << mText;

    mFile.close();

}

void MyWindow::on_pathPB_clicked()
{
    QString file;
    QString filter ("text files (*.txt);;crypted (*.ksz);;all files (*.*)");
    file = QFileDialog::getOpenFileName (this,"Otwieranie",".",filter);
    ui->pathLE -> setText(file);
}

void MyWindow::on_okPB_clicked()
{
//    if(encrypt)
//    {
//        QString pathToRead = ui->pathLE->text();
//        ui->cryText->setText("ok \n" + pathToRead);
//        QString fileName = "file.txt";

//        //cry->encrypt(pathToRead);
//        QString keys = ui->key->text();
//        //cry->key  = keys.split(" ")[0].toInt();

//       // ui->label->setText(QString::number(cry->x));
//        write(fileName, cry->encryptedText);
//    }
//    else
//    {
        QString pathToRead = ui->pathLE->text();
        ui->cryText->setText("ok \n" + pathToRead);
        QFileInfo dir(pathToRead);
        QString s = dir.absoluteFilePath();
        ui->cryText->setText("s \n" + s);
        read(s);

        //qDebug() << s;
        //ui->label->setText("dsf");
//    }
}
