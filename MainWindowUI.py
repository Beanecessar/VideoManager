# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(635, 586)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
		self.groupBox_2.setSizePolicy(sizePolicy)
		self.groupBox_2.setObjectName("groupBox_2")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
		self.checkBox.setObjectName("checkBox")
		self.horizontalLayout_2.addWidget(self.checkBox)
		self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
		self.checkBox_2.setObjectName("checkBox_2")
		self.horizontalLayout_2.addWidget(self.checkBox_2)
		self.horizontalLayout.addWidget(self.groupBox_2)
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setObjectName("groupBox")
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
		self.checkBox_3.setObjectName("checkBox_3")
		self.horizontalLayout_4.addWidget(self.checkBox_3)
		self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
		self.checkBox_4.setObjectName("checkBox_4")
		self.horizontalLayout_4.addWidget(self.checkBox_4)
		self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
		self.checkBox_5.setObjectName("checkBox_5")
		self.horizontalLayout_4.addWidget(self.checkBox_5)
		self.horizontalLayout.addWidget(self.groupBox)
		spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_3.addWidget(self.lineEdit)
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_3.addWidget(self.pushButton)
		self.verticalLayout.addLayout(self.horizontalLayout_3)
		self.widget = QtWidgets.QWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
		self.widget.setSizePolicy(sizePolicy)
		self.widget.setObjectName("widget")
		self.verticalLayout.addWidget(self.widget)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 23))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.groupBox_2.setTitle(_translate("MainWindow", "类型"))
		self.checkBox.setText(_translate("MainWindow", "视频"))
		self.checkBox_2.setText(_translate("MainWindow", "文件夹"))
		self.groupBox.setTitle(_translate("MainWindow", "评分"))
		self.checkBox_3.setText(_translate("MainWindow", "S"))
		self.checkBox_4.setText(_translate("MainWindow", "A"))
		self.checkBox_5.setText(_translate("MainWindow", "B"))
		self.pushButton.setText(_translate("MainWindow", "搜索"))
