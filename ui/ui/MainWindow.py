# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_input_dir = QLineEdit(self.groupBox_2)
        self.lineEdit_input_dir.setObjectName(u"lineEdit_input_dir")

        self.horizontalLayout.addWidget(self.lineEdit_input_dir)

        self.pushButton_input_dir = QPushButton(self.groupBox_2)
        self.pushButton_input_dir.setObjectName(u"pushButton_input_dir")

        self.horizontalLayout.addWidget(self.pushButton_input_dir)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_output_dir = QLineEdit(self.groupBox_2)
        self.lineEdit_output_dir.setObjectName(u"lineEdit_output_dir")

        self.horizontalLayout_2.addWidget(self.lineEdit_output_dir)

        self.pushButton_output_dir = QPushButton(self.groupBox_2)
        self.pushButton_output_dir.setObjectName(u"pushButton_output_dir")

        self.horizontalLayout_2.addWidget(self.pushButton_output_dir)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_shadow = QCheckBox(self.groupBox_3)
        self.checkBox_shadow.setObjectName(u"checkBox_shadow")

        self.horizontalLayout_8.addWidget(self.checkBox_shadow)

        self.checkBox_white_margin = QCheckBox(self.groupBox_3)
        self.checkBox_white_margin.setObjectName(u"checkBox_white_margin")

        self.horizontalLayout_8.addWidget(self.checkBox_white_margin)

        self.checkBox_use_equivalent_focal_length = QCheckBox(self.groupBox_3)
        self.checkBox_use_equivalent_focal_length.setObjectName(u"checkBox_use_equivalent_focal_length")

        self.horizontalLayout_8.addWidget(self.checkBox_use_equivalent_focal_length)

        self.checkBox_padding_with_original_ratio = QCheckBox(self.groupBox_3)
        self.checkBox_padding_with_original_ratio.setObjectName(u"checkBox_padding_with_original_ratio")

        self.horizontalLayout_8.addWidget(self.checkBox_padding_with_original_ratio)

        self.checkBox_logo_enable = QCheckBox(self.groupBox_3)
        self.checkBox_logo_enable.setObjectName(u"checkBox_logo_enable")

        self.horizontalLayout_8.addWidget(self.checkBox_logo_enable)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox_layout = QComboBox(self.groupBox_3)
        self.comboBox_layout.addItem("")
        self.comboBox_layout.addItem("")
        self.comboBox_layout.addItem("")
        self.comboBox_layout.addItem("")
        self.comboBox_layout.setObjectName(u"comboBox_layout")

        self.horizontalLayout_3.addWidget(self.comboBox_layout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBox_left_top = QComboBox(self.groupBox_3)
        self.comboBox_left_top.addItem("")
        self.comboBox_left_top.addItem("")
        self.comboBox_left_top.addItem("")
        self.comboBox_left_top.addItem("")
        self.comboBox_left_top.addItem("")
        self.comboBox_left_top.setObjectName(u"comboBox_left_top")

        self.horizontalLayout_4.addWidget(self.comboBox_left_top)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.comboBox_right_top = QComboBox(self.groupBox_3)
        self.comboBox_right_top.addItem("")
        self.comboBox_right_top.addItem("")
        self.comboBox_right_top.addItem("")
        self.comboBox_right_top.addItem("")
        self.comboBox_right_top.addItem("")
        self.comboBox_right_top.setObjectName(u"comboBox_right_top")

        self.horizontalLayout_6.addWidget(self.comboBox_right_top)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.comboBox_left_bottom = QComboBox(self.groupBox_3)
        self.comboBox_left_bottom.addItem("")
        self.comboBox_left_bottom.addItem("")
        self.comboBox_left_bottom.addItem("")
        self.comboBox_left_bottom.addItem("")
        self.comboBox_left_bottom.addItem("")
        self.comboBox_left_bottom.setObjectName(u"comboBox_left_bottom")

        self.horizontalLayout_5.addWidget(self.comboBox_left_bottom)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.comboBox_right_bottom = QComboBox(self.groupBox_3)
        self.comboBox_right_bottom.addItem("")
        self.comboBox_right_bottom.addItem("")
        self.comboBox_right_bottom.addItem("")
        self.comboBox_right_bottom.addItem("")
        self.comboBox_right_bottom.addItem("")
        self.comboBox_right_bottom.setObjectName(u"comboBox_right_bottom")

        self.horizontalLayout_7.addWidget(self.comboBox_right_bottom)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.pushButton_run = QPushButton(self.centralwidget)
        self.pushButton_run.setObjectName(u"pushButton_run")

        self.horizontalLayout_9.addWidget(self.pushButton_run)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textEdit_log = QTextEdit(self.groupBox)
        self.textEdit_log.setObjectName(u"textEdit_log")

        self.verticalLayout_2.addWidget(self.textEdit_log)


        self.verticalLayout_4.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8def\u5f84", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u8def\u5f84\uff1a", None))
        self.pushButton_input_dir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8f93\u5165\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u8def\u5f84\uff1a", None))
        self.pushButton_output_dir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8f93\u51fa\u6587\u4ef6\u5939", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u53c2\u6570", None))
        self.checkBox_shadow.setText(QCoreApplication.translate("MainWindow", u"\u9634\u5f71", None))
        self.checkBox_white_margin.setText(QCoreApplication.translate("MainWindow", u"\u767d\u8272\u8fb9\u6846", None))
        self.checkBox_use_equivalent_focal_length.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u6548\u7126\u8ddd", None))
        self.checkBox_padding_with_original_ratio.setText(QCoreApplication.translate("MainWindow", u"\u6309\u6bd4\u4f8b\u586b\u5145", None))
        self.checkBox_logo_enable.setText(QCoreApplication.translate("MainWindow", u"\u542f\u7528LOGO", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5e03\u5c40\uff1a", None))
        self.comboBox_layout.setItemText(0, QCoreApplication.translate("MainWindow", u"normal", None))
        self.comboBox_layout.setItemText(1, QCoreApplication.translate("MainWindow", u"normal(Logo \u5c45\u53f3)", None))
        self.comboBox_layout.setItemText(2, QCoreApplication.translate("MainWindow", u"normal(\u9ed1\u7ea2\u914d\u8272)", None))
        self.comboBox_layout.setItemText(3, QCoreApplication.translate("MainWindow", u"normal(\u9ed1\u7ea2\u914d\u8272\uff0cLogo \u5c45\u53f3)", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u4e0a\u89d2", None))
        self.comboBox_left_top.setItemText(0, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u578b\u53f7(eg. Nikon Z7)", None))
        self.comboBox_left_top.setItemText(1, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5382\u5546(eg. Nikon)", None))
        self.comboBox_left_top.setItemText(2, QCoreApplication.translate("MainWindow", u"\u955c\u5934\u578b\u53f7(eg. Nikkor 24-70 f/2.8)", None))
        self.comboBox_left_top.setItemText(3, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u53c2\u6570(eg. 50mm f/1.8 1/1000s ISO 100)", None))
        self.comboBox_left_top.setItemText(4, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4(eg. 2023-01-01 12:00)", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u4e0a\u89d2", None))
        self.comboBox_right_top.setItemText(0, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u578b\u53f7(eg. Nikon Z7)", None))
        self.comboBox_right_top.setItemText(1, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5382\u5546(eg. Nikon)", None))
        self.comboBox_right_top.setItemText(2, QCoreApplication.translate("MainWindow", u"\u955c\u5934\u578b\u53f7(eg. Nikkor 24-70 f/2.8)", None))
        self.comboBox_right_top.setItemText(3, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u53c2\u6570(eg. 50mm f/1.8 1/1000s ISO 100)", None))
        self.comboBox_right_top.setItemText(4, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4(eg. 2023-01-01 12:00)", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5de6\u4e0b\u89d2", None))
        self.comboBox_left_bottom.setItemText(0, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u578b\u53f7(eg. Nikon Z7)", None))
        self.comboBox_left_bottom.setItemText(1, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5382\u5546(eg. Nikon)", None))
        self.comboBox_left_bottom.setItemText(2, QCoreApplication.translate("MainWindow", u"\u955c\u5934\u578b\u53f7(eg. Nikkor 24-70 f/2.8)", None))
        self.comboBox_left_bottom.setItemText(3, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u53c2\u6570(eg. 50mm f/1.8 1/1000s ISO 100)", None))
        self.comboBox_left_bottom.setItemText(4, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4(eg. 2023-01-01 12:00)", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u53f3\u4e0b\u89d2", None))
        self.comboBox_right_bottom.setItemText(0, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u578b\u53f7(eg. Nikon Z7)", None))
        self.comboBox_right_bottom.setItemText(1, QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5382\u5546(eg. Nikon)", None))
        self.comboBox_right_bottom.setItemText(2, QCoreApplication.translate("MainWindow", u"\u955c\u5934\u578b\u53f7(eg. Nikkor 24-70 f/2.8)", None))
        self.comboBox_right_bottom.setItemText(3, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u53c2\u6570(eg. 50mm f/1.8 1/1000s ISO 100)", None))
        self.comboBox_right_bottom.setItemText(4, QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4(eg. 2023-01-01 12:00)", None))

        self.pushButton_run.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u65e5\u5fd7", None))
    # retranslateUi

