#include"application.h"

application::application():QWidget()
{
    mainText=new QTextEdit(this);

    box=new QGroupBox(this);
    crypting=new QRadioButton("crypting",box);
    encrypting=new QRadioButton("decrypting",box);

    VBox=new QVBoxLayout();
    VBox->addWidget(crypting);
    VBox->addWidget(encrypting);

    box->setMaximumWidth(100);
    box->setWindowModified(false);
    box->setLayout(VBox);

    form=new QFormLayout();
    key=new QLineEdit;
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
