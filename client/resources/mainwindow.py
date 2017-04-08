# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 660)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(100000, 100000))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.centralWidget.setObjectName("centralWidget")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(120, 170, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 560, 781, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Upload = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Upload.setObjectName("Upload")
        self.horizontalLayout.addWidget(self.Upload)
        self.Download = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Download.setObjectName("Download")
        self.horizontalLayout.addWidget(self.Download)
        self.Refresh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Refresh.setObjectName("Refresh")
        self.horizontalLayout.addWidget(self.Refresh)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Quit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Quit.setObjectName("Quit")
        self.horizontalLayout.addWidget(self.Quit)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 781, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 431, 32))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Login = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Login.setObjectName("Login")
        self.horizontalLayout_2.addWidget(self.Login)
        self.Logout = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Logout.setObjectName("Logout")
        self.horizontalLayout_2.addWidget(self.Logout)
        self.Reconnect = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Reconnect.setObjectName("Reconnect")
        self.horizontalLayout_2.addWidget(self.Reconnect)
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 431, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 1, 2, 1, 1)
        self.Host = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Host.setObjectName("Host")
        self.gridLayout.addWidget(self.Host, 0, 1, 1, 1)
        self.Username = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Username.setObjectName("Username")
        self.gridLayout.addWidget(self.Username, 1, 1, 1, 1)
        self.Password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 1, 3, 1, 1)
        self.label_username = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_username.setObjectName("label_username")
        self.gridLayout.addWidget(self.label_username, 1, 0, 1, 1)
        self.label_port = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_port.setObjectName("label_port")
        self.gridLayout.addWidget(self.label_port, 0, 2, 1, 1)
        self.Port = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Port.setObjectName("Port")
        self.gridLayout.addWidget(self.Port, 0, 3, 1, 1)
        self.label_host = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_host.setObjectName("label_host")
        self.gridLayout.addWidget(self.label_host, 0, 0, 1, 1)
        self.sysScrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.sysScrollArea.setGeometry(QtCore.QRect(450, 30, 321, 131))
        self.sysScrollArea.setStyleSheet("")
        self.sysScrollArea.setWidgetResizable(True)
        self.sysScrollArea.setObjectName("sysScrollArea")
        self.statusPanel = QtWidgets.QWidget()
        self.statusPanel.setGeometry(QtCore.QRect(0, 0, 319, 129))
        self.statusPanel.setObjectName("statusPanel")
        self.Infolist = QtWidgets.QListWidget(self.statusPanel)
        self.Infolist.setGeometry(QtCore.QRect(0, 0, 321, 131))
        self.Infolist.setAutoScroll(True)
        self.Infolist.setObjectName("Infolist")
        self.sysScrollArea.setWidget(self.statusPanel)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 170, 781, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.fileScrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.fileScrollArea.setGeometry(QtCore.QRect(10, 30, 761, 341))
        self.fileScrollArea.setWidgetResizable(True)
        self.fileScrollArea.setObjectName("fileScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 759, 339))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.Filetree = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents_3)
        self.Filetree.setGeometry(QtCore.QRect(0, 0, 761, 341))
        self.Filetree.setObjectName("Filetree")
        self.fileScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menufile = QtWidgets.QMenu(self.menuBar)
        self.menufile.setObjectName("menufile")
        self.menutest = QtWidgets.QMenu(self.menuBar)
        self.menutest.setObjectName("menutest")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.Setdefaultinfo = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Downloads/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Setdefaultinfo.setIcon(icon)
        self.Setdefaultinfo.setObjectName("Setdefaultinfo")
        self.actionaaaa = QtWidgets.QAction(MainWindow)
        self.actionaaaa.setObjectName("actionaaaa")
        self.actionabout = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Downloads/fluidicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionabout.setIcon(icon1)
        self.actionabout.setObjectName("actionabout")
        self.actiontest = QtWidgets.QAction(MainWindow)
        self.actiontest.setObjectName("actiontest")
        self.Setlist = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Documents/tmp/icons/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Setlist.setIcon(icon2)
        self.Setlist.setObjectName("Setlist")
        self.Download_2 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Documents/tmp/icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Download_2.setIcon(icon3)
        self.Download_2.setObjectName("Download_2")
        self.menufile.addAction(self.Setdefaultinfo)
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionabout)
        self.menufile.addAction(self.actiontest)
        self.menutest.addSeparator()
        self.menutest.addAction(self.actionaaaa)
        self.menuBar.addAction(self.menufile.menuAction())
        self.menuBar.addAction(self.menutest.menuAction())
        self.mainToolBar.addAction(self.actionabout)
        self.mainToolBar.addAction(self.Setdefaultinfo)
        self.mainToolBar.addAction(self.Setlist)
        self.mainToolBar.addAction(self.Download_2)

        self.retranslateUi(MainWindow)
        self.Login.clicked.connect(MainWindow.login)
        self.Logout.clicked.connect(MainWindow.logout)
        self.Reconnect.clicked.connect(MainWindow.reconnect)
        self.Upload.clicked['bool'].connect(MainWindow.upload)
        self.Download.clicked['bool'].connect(MainWindow.download)
        self.Refresh.clicked['bool'].connect(MainWindow.refresh)
        self.Quit.clicked.connect(MainWindow.quit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Quit, self.Refresh)
        MainWindow.setTabOrder(self.Refresh, self.Infolist)
        MainWindow.setTabOrder(self.Infolist, self.Upload)
        MainWindow.setTabOrder(self.Upload, self.Host)
        MainWindow.setTabOrder(self.Host, self.Port)
        MainWindow.setTabOrder(self.Port, self.Username)
        MainWindow.setTabOrder(self.Username, self.Password)
        MainWindow.setTabOrder(self.Password, self.Login)
        MainWindow.setTabOrder(self.Login, self.Logout)
        MainWindow.setTabOrder(self.Logout, self.Reconnect)
        MainWindow.setTabOrder(self.Reconnect, self.Download)
        MainWindow.setTabOrder(self.Download, self.Filetree)
        MainWindow.setTabOrder(self.Filetree, self.sysScrollArea)
        MainWindow.setTabOrder(self.sysScrollArea, self.fileScrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cowry System"))
        self.Upload.setText(_translate("MainWindow", "上传"))
        self.Download.setText(_translate("MainWindow", "下载"))
        self.Refresh.setText(_translate("MainWindow", "刷新"))
        self.Quit.setText(_translate("MainWindow", "退出"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Control Panel"))
        self.Login.setText(_translate("MainWindow", "登录"))
        self.Logout.setText(_translate("MainWindow", "退出"))
        self.Reconnect.setText(_translate("MainWindow", "重连"))
        self.label_password.setText(_translate("MainWindow", "密码:"))
        self.label_username.setText(_translate("MainWindow", "用户名:"))
        self.label_port.setText(_translate("MainWindow", "端口:"))
        self.label_host.setText(_translate("MainWindow", "主机地址:"))
        self.groupBox.setTitle(_translate("MainWindow", "Files List"))
        self.Filetree.headerItem().setText(0, _translate("MainWindow", "            文件名"))
        self.Filetree.headerItem().setText(1, _translate("MainWindow", "格式"))
        self.Filetree.headerItem().setText(2, _translate("MainWindow", "大小"))
        self.Filetree.headerItem().setText(3, _translate("MainWindow", "上传时间"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menutest.setTitle(_translate("MainWindow", "test"))
        self.Setdefaultinfo.setText(_translate("MainWindow", "default"))
        self.Setdefaultinfo.setToolTip(_translate("MainWindow", "default"))
        self.Setdefaultinfo.setShortcut(_translate("MainWindow", "Meta+Q"))
        self.actionaaaa.setText(_translate("MainWindow", "aaaa"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actiontest.setText(_translate("MainWindow", "test"))
        self.Setlist.setText(_translate("MainWindow", "setlist"))
        self.Download_2.setText(_translate("MainWindow", "download"))

from resources import resources_rc