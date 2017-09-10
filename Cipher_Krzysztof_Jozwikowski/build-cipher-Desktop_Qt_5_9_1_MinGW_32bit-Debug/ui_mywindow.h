/********************************************************************************
** Form generated from reading UI file 'mywindow.ui'
**
** Created by: Qt User Interface Compiler version 5.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MYWINDOW_H
#define UI_MYWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MyWindow
{
public:
    QWidget *centralWidget;
    QGroupBox *groupBox;
    QRadioButton *enRB;
    QRadioButton *deRB;
    QLineEdit *keyLE;
    QLineEdit *pathLE;
    QLabel *label;
    QLabel *label_2;
    QTextEdit *cryText;
    QPushButton *okPB;
    QPushButton *pathPB;
    QPushButton *keyPB;
    QMenuBar *menuBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MyWindow)
    {
        if (MyWindow->objectName().isEmpty())
            MyWindow->setObjectName(QStringLiteral("MyWindow"));
        MyWindow->resize(400, 300);
        centralWidget = new QWidget(MyWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(9, 9, 81, 71));
        enRB = new QRadioButton(groupBox);
        enRB->setObjectName(QStringLiteral("enRB"));
        enRB->setGeometry(QRect(10, 10, 95, 20));
        enRB->setChecked(true);
        deRB = new QRadioButton(groupBox);
        deRB->setObjectName(QStringLiteral("deRB"));
        deRB->setGeometry(QRect(10, 40, 95, 20));
        deRB->setChecked(false);
        keyLE = new QLineEdit(centralWidget);
        keyLE->setObjectName(QStringLiteral("keyLE"));
        keyLE->setGeometry(QRect(182, 10, 201, 22));
        pathLE = new QLineEdit(centralWidget);
        pathLE->setObjectName(QStringLiteral("pathLE"));
        pathLE->setGeometry(QRect(182, 40, 201, 22));
        label = new QLabel(centralWidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(140, 10, 31, 21));
        QFont font;
        font.setPointSize(10);
        label->setFont(font);
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(94, 36, 81, 31));
        label_2->setFont(font);
        cryText = new QTextEdit(centralWidget);
        cryText->setObjectName(QStringLiteral("cryText"));
        cryText->setGeometry(QRect(13, 130, 371, 121));
        okPB = new QPushButton(centralWidget);
        okPB->setObjectName(QStringLiteral("okPB"));
        okPB->setGeometry(QRect(110, 90, 181, 28));
        pathPB = new QPushButton(centralWidget);
        pathPB->setObjectName(QStringLiteral("pathPB"));
        pathPB->setGeometry(QRect(380, 40, 16, 16));
        keyPB = new QPushButton(centralWidget);
        keyPB->setObjectName(QStringLiteral("keyPB"));
        keyPB->setGeometry(QRect(380, 10, 16, 16));
        MyWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MyWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 26));
        MyWindow->setMenuBar(menuBar);
        statusBar = new QStatusBar(MyWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MyWindow->setStatusBar(statusBar);

        retranslateUi(MyWindow);

        QMetaObject::connectSlotsByName(MyWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MyWindow)
    {
        MyWindow->setWindowTitle(QApplication::translate("MyWindow", "Cipher", Q_NULLPTR));
        groupBox->setTitle(QString());
        enRB->setText(QApplication::translate("MyWindow", "encrypt", Q_NULLPTR));
        deRB->setText(QApplication::translate("MyWindow", "decrypt", Q_NULLPTR));
        label->setText(QApplication::translate("MyWindow", " Key:", Q_NULLPTR));
        label_2->setText(QApplication::translate("MyWindow", "Path to file:", Q_NULLPTR));
        okPB->setText(QApplication::translate("MyWindow", "Ok", Q_NULLPTR));
        pathPB->setText(QApplication::translate("MyWindow", "<", Q_NULLPTR));
        keyPB->setText(QApplication::translate("MyWindow", "..", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MyWindow: public Ui_MyWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MYWINDOW_H
