#include "mywindow.h"
#include "ui_mywindow.h"

MyWindow::MyWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MyWindow)
{
    ui->setupUi(this);
    enRB = new QRadioButton(this);
    cryText = new QTextEdit();

    QObject::connect(enRB,SIGNAL(pressed()),qApp,SLOT(encrypt()));
}

MyWindow::~MyWindow()
{
    delete ui;
}

void MyWindow::encrypt()
{
    cryText->setText("dupa");
}
