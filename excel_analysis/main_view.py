# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from excel_oper import input_file, get_column_data, clicked_display_excel, common_merge_excel, merge_all_excel, \
    set_out_excel_dir, multi_excel_statistics, draw_grap, filter_excel_data


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 611)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.list_view = QtWidgets.QListView(self.centralwidget)
        self.list_view.setGeometry(QtCore.QRect(0, 0, 241, 441))
        self.list_view.setObjectName("list_view")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(243, 0, 591, 441))
        self.textEdit.setObjectName("textEdit")
        self.file_oper_label = QtWidgets.QLabel(self.centralwidget)
        self.file_oper_label.setGeometry(QtCore.QRect(10, 450, 81, 16))
        self.file_oper_label.setObjectName("file_oper_label")
        self.rButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton1.setGeometry(QtCore.QRect(10, 470, 141, 21))
        self.rButton1.setChecked(True)
        self.rButton1.setObjectName("rButton1")
        self.rButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rButton2.setGeometry(QtCore.QRect(10, 490, 91, 21))
        self.rButton2.setObjectName("rButton2")
        self.oput_file_dir = QtWidgets.QTextEdit(self.centralwidget)
        self.oput_file_dir.setGeometry(QtCore.QRect(70, 490, 441, 21))
        self.oput_file_dir.setObjectName("oput_file_dir")
        self.file_oper_btn = QtWidgets.QPushButton(self.centralwidget)
        self.file_oper_btn.setGeometry(QtCore.QRect(520, 490, 61, 21))
        self.file_oper_btn.setObjectName("file_oper_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(35, 35))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 878, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.button1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imag/图标-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button1.setIcon(icon)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/imag/图标-02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon1)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/imag/图标-03.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon2)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/imag/图标-04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button4.setIcon(icon3)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/imag/图标-05.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button5.setIcon(icon4)
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/imag/图标-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button6.setIcon(icon5)
        self.button6.setObjectName("button6")
        self.button7 = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/imag/图标-07.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button7.setIcon(icon6)
        self.button7.setObjectName("button7")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button5)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button6)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.button7)

        self.retranslateUi(MainWindow)
        # 导入文件
        self.button1.triggered.connect(lambda: input_file(self.list_view, MainWindow))
        # 筛选保存
        self.button2.triggered.connect(lambda: filter_excel_data(self.textEdit, self.rButton1,MainWindow))
        # 多表汇总
        self.button3.triggered.connect(lambda: get_column_data(self.textEdit, self.rButton1, MainWindow))
        # 多表分组
        self.button4.triggered.connect(lambda : merge_all_excel(self.textEdit, self.rButton1,MainWindow))
        # 多表数据排行
        self.button5.triggered.connect(lambda : multi_excel_statistics(self.textEdit, self.rButton1, MainWindow))
        # 生成图表
        self.button6.triggered.connect(lambda : draw_grap(self.rButton1, MainWindow))
        self.button7.triggered.connect(MainWindow.close)
        # 浏览文件按钮
        self.file_oper_btn.clicked.connect(lambda : set_out_excel_dir(self.oput_file_dir, MainWindow))
        # 单击QListView列表触发自定义的槽函数
        self.list_view.clicked['QModelIndex'].connect(lambda : clicked_display_excel(self.list_view, self.textEdit))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_oper_label.setText(_translate("MainWindow", "选择保存路径："))
        self.rButton1.setText(_translate("MainWindow", "保存到原来路径"))
        self.rButton2.setText(_translate("MainWindow", "另存为"))
        self.file_oper_btn.setText(_translate("MainWindow", "浏览"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.button1.setText(_translate("MainWindow", "导入文件"))
        self.button1.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p><p>导入文件</p></body></html>"))
        self.button2.setText(_translate("MainWindow", "筛选保存"))
        self.button3.setText(_translate("MainWindow", "多表汇总"))
        self.button4.setText(_translate("MainWindow", "多表分组统计"))
        self.button5.setText(_translate("MainWindow", "多表数据排行"))
        self.button6.setText(_translate("MainWindow", "生成图表"))
        self.button7.setText(_translate("MainWindow", "退出"))

import imag_rc
