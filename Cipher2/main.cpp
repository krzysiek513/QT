#include<QApplication>
#include"application.h"

int main(int argc, char *argv[])
{
    QApplication app(argc,argv);
    application test;
    //test.setLayout(form);
    test.show();
    return app.exec();
}
