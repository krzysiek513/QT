#include"application.h"

application::application():QWidget()
{
    box=new QGroupBox();
    form=new QFormLayout();
    key=new QLineEdit;
    path=new QLineEdit;
    grid=new QGridLayout(this);
    showkey=new QPushButton("..");
    showpath=new QPushButton("<");
    form->addRow("enter the key",key);
    form->addRow("eter path",path);



    grid->addWidget(showkey,0,4,1,1);
    grid->addWidget(showpath,1,4,1,1);
    grid->addWidget(box,0,0,2,1);
    grid->addLayout(form,0,1,3,1);



    grid=new QGridLayout(this);


//    setLayout(grid);


//    Vlayout.addItem(&key);
//    Vlayout.addItem(&path);


//    setLayout(&Vlayout);
}
