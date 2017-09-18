#include"application.h"

application::application():QWidget(), crypt(true),showPass(true)
{
    CryText = new vernam();

    Layout();




    connect(crypting,SIGNAL(pressed()),this,SLOT(crRB()));
    connect(encrypting,SIGNAL(pressed()),this,SLOT(enRB()));
    connect(showkey,SIGNAL(pressed()),this,SLOT(keyPB()));
    connect(showpath,SIGNAL(pressed()),this,SLOT(pathPB()));
    connect(ok,SIGNAL(pressed()),this,SLOT(okPB()));

}
//control
void application::write(QString FileName, QString text)
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

QString application::read(QString FileName)
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

void application::keyPB()
{
    showPass = !showPass;
    if(showPass)
        key->setEchoMode(QLineEdit::Password);
    else
        key->setEchoMode(QLineEdit::Normal);
}
void application::pathPB()
{
    if(crypt)
    {
        QString file;
        QString filter ("text files (*.txt);;encrypted (*.jok);;all files (*.*)");
        file=QFileDialog::getOpenFileName (this,"Open",".",filter);
        path->setText(file);
    }
    else
    {
        QString file;
        QString filter ("encrypted (*.jok);;text files (*.txt);;all files (*.*)");
        file=QFileDialog::getOpenFileName (this,"Open",".",filter);
        path->setText(file);
    }
}
void application::okPB()
{
    if(crypt) //szyfrowanie
    {
        QString pathToRead =path->text();
        QString filter ("encrypted (*.jok)");
        QString file = QFileDialog::getSaveFileName (this,"Save",".",filter);
        QString Skey = key->text();
        QString text;
        if(pathToRead=="")
        {
            text=mainText->toPlainText();
        }
        else
        {
            text = read(pathToRead);
        }
        write(file, CryText->crypt(text, Skey));
        key->setText("");
        path->setText("");
    }
    else //odszyfrowanie
    {

        QString pathToRead =path->text();
        QString Skey =key->text();
        QString text = read(pathToRead);
        QString filter ("text files (*.txt)");
        QString file = QFileDialog::getSaveFileName (this,"Save",".",filter);
        QString plainText = CryText->encrypt(text, Skey);
        key->setText("");
        write(file, plainText);
        mainText->setText(plainText);
        path->setText("");

    }
}
void application::crRB()
{
    mainText->setText("");
    path->setText("");
    key->setText("");
    crypt = true;
    crypting->setChecked(crypt);
    crypting->setEnabled(!crypt);
    encrypting->setEnabled(crypt);
}
void application::enRB()
{
    mainText->setText("");
    path->setText("");
    key->setText("");
    encrypting->setChecked(crypt);
    crypting->setEnabled(crypt);
    crypt = false;
    encrypting->setEnabled(crypt);
}


//view
void application::Layout()
{
    mainText=new QTextEdit(this);

    box=new QGroupBox(this);
    crypting=new QRadioButton("crypting",box);
    crypting->setChecked(crypt);
    crypting->setEnabled(!crypt);
    encrypting=new QRadioButton("decrypting",box);

    VBox=new QVBoxLayout();
    VBox->addWidget(crypting);
    VBox->addWidget(encrypting);

    box->setMaximumWidth(100);
    box->setWindowModified(false);
    box->setLayout(VBox);

    form=new QFormLayout();
    key=new QLineEdit;
    key->setEchoMode(QLineEdit::Password);
    path=new QLineEdit;
    grid=new QGridLayout(this);

    ok=new QPushButton("ok");

    showkey=new QPushButton("..");
    showkey->setMaximumSize(16,16);
    showpath=new QPushButton("<");
    showpath->setMaximumSize(16,16);
    form->addRow("enter the key",key);
    form->addRow("enter path",path);
    form->setVerticalSpacing(15);
    form->setHorizontalSpacing(10);
    form->setMargin(5);


    grid->setMargin(10);
    grid->setHorizontalSpacing(0);
    grid->addWidget(showkey,0,6,1,1);
    grid->addWidget(showpath,1,6,1,1);
    grid->addWidget(box,0,0,2,2);
    grid->addLayout(form,0,2,2,4);
    grid->addWidget(ok,3,2,1,2);
    grid->addWidget(mainText,4,0,1,7);


    grid=new QGridLayout(this);

}
