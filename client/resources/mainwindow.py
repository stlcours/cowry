# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/aong/workspace/qt/cowry/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(756, 632)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.Host = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Host.sizePolicy().hasHeightForWidth())
        self.Host.setSizePolicy(sizePolicy)
        self.Host.setObjectName("Host")
        self.gridLayout.addWidget(self.Host, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.Port = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Port.sizePolicy().hasHeightForWidth())
        self.Port.setSizePolicy(sizePolicy)
        self.Port.setObjectName("Port")
        self.gridLayout.addWidget(self.Port, 0, 4, 1, 1)
        self.Infolist = QtWidgets.QListWidget(self.groupBox)
        self.Infolist.setObjectName("Infolist")
        self.gridLayout.addWidget(self.Infolist, 0, 5, 3, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.Username = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Username.sizePolicy().hasHeightForWidth())
        self.Username.setSizePolicy(sizePolicy)
        self.Username.setObjectName("Username")
        self.gridLayout.addWidget(self.Username, 1, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.Password = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Password.sizePolicy().hasHeightForWidth())
        self.Password.setSizePolicy(sizePolicy)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 1, 4, 1, 1)
        self.Login = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Login.sizePolicy().hasHeightForWidth())
        self.Login.setSizePolicy(sizePolicy)
        self.Login.setObjectName("Login")
        self.gridLayout.addWidget(self.Login, 2, 0, 1, 2)
        self.Reconnect = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Reconnect.sizePolicy().hasHeightForWidth())
        self.Reconnect.setSizePolicy(sizePolicy)
        self.Reconnect.setObjectName("Reconnect")
        self.gridLayout.addWidget(self.Reconnect, 2, 2, 1, 2)
        self.Logout = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logout.sizePolicy().hasHeightForWidth())
        self.Logout.setSizePolicy(sizePolicy)
        self.Logout.setObjectName("Logout")
        self.gridLayout.addWidget(self.Logout, 2, 4, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.Encrypts = QtWidgets.QComboBox(self.groupBox_3)
        self.Encrypts.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Encrypts.sizePolicy().hasHeightForWidth())
        self.Encrypts.setSizePolicy(sizePolicy)
        self.Encrypts.setObjectName("Encrypts")
        self.Encrypts.addItem("")
        self.Encrypts.addItem("")
        self.Encrypts.addItem("")
        self.Encrypts.addItem("")
        self.Encrypts.addItem("")
        self.Encrypts.addItem("")
        self.horizontalLayout_5.addWidget(self.Encrypts)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.Label_cipher = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_cipher.sizePolicy().hasHeightForWidth())
        self.Label_cipher.setSizePolicy(sizePolicy)
        self.Label_cipher.setObjectName("Label_cipher")
        self.horizontalLayout_5.addWidget(self.Label_cipher)
        self.Ciphercode = QtWidgets.QLineEdit(self.groupBox_3)
        self.Ciphercode.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ciphercode.sizePolicy().hasHeightForWidth())
        self.Ciphercode.setSizePolicy(sizePolicy)
        self.Ciphercode.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.Ciphercode.setObjectName("Ciphercode")
        self.horizontalLayout_5.addWidget(self.Ciphercode)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.Usepassword = QtWidgets.QCheckBox(self.groupBox_3)
        self.Usepassword.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Usepassword.setObjectName("Usepassword")
        self.horizontalLayout_5.addWidget(self.Usepassword)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.Button_encrypt = QtWidgets.QPushButton(self.groupBox_3)
        self.Button_encrypt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_encrypt.sizePolicy().hasHeightForWidth())
        self.Button_encrypt.setSizePolicy(sizePolicy)
        self.Button_encrypt.setObjectName("Button_encrypt")
        self.horizontalLayout_5.addWidget(self.Button_encrypt)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tab.setObjectName("tab")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Filetree_Private = QtWidgets.QTreeWidget(self.tab)
        self.Filetree_Private.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Filetree_Private.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Filetree_Private.setHeaderHidden(False)
        self.Filetree_Private.setObjectName("Filetree_Private")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Filetree_Private.headerItem().setFont(1, font)
        self.Filetree_Private.header().setDefaultSectionSize(114)
        self.Filetree_Private.header().setHighlightSections(False)
        self.Filetree_Private.header().setMinimumSectionSize(19)
        self.horizontalLayout_6.addWidget(self.Filetree_Private)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Filetree_Public = QtWidgets.QTreeWidget(self.tab_2)
        self.Filetree_Public.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Filetree_Public.setObjectName("Filetree_Public")
        self.Filetree_Public.header().setDefaultSectionSize(114)
        self.Filetree_Public.header().setHighlightSections(False)
        self.Filetree_Public.header().setMinimumSectionSize(19)
        self.horizontalLayout_3.addWidget(self.Filetree_Public)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setObjectName("Quit")
        self.horizontalLayout.addWidget(self.Quit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 22))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionFiles = QtWidgets.QAction(MainWindow)
        self.actionFiles.setObjectName("actionFiles")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.actionloadLoginInfo = QtWidgets.QAction(MainWindow)
        self.actionloadLoginInfo.setObjectName("actionloadLoginInfo")
        self.actiondeleteCertificate = QtWidgets.QAction(MainWindow)
        self.actiondeleteCertificate.setObjectName("actiondeleteCertificate")
        self.menuFiles.addAction(self.action1)
        self.menuAbout.addAction(self.action2)
        self.menuHelp.addAction(self.action3)
        self.menuHelp.addAction(self.actionloadLoginInfo)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.action3)
        self.toolBar.addAction(self.actionloadLoginInfo)
        self.toolBar.addAction(self.actiondeleteCertificate)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Login.clicked.connect(MainWindow.login)
        self.Quit.clicked.connect(MainWindow.quit)
        self.pushButton.clicked.connect(MainWindow.upload)
        self.pushButton_2.clicked.connect(MainWindow.download)
        self.pushButton_3.clicked.connect(MainWindow.refresh)
        self.Button_encrypt.clicked.connect(MainWindow.encrypt)
        self.Logout.clicked.connect(MainWindow.logout)
        self.Reconnect.clicked.connect(MainWindow.reconnect)
        self.Filetree_Private.customContextMenuRequested['QPoint'].connect(MainWindow.openmenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Logout, self.Encrypts)
        MainWindow.setTabOrder(self.Encrypts, self.Ciphercode)
        MainWindow.setTabOrder(self.Ciphercode, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.Quit)
        MainWindow.setTabOrder(self.Quit, self.Infolist)
        MainWindow.setTabOrder(self.Infolist, self.Host)
        MainWindow.setTabOrder(self.Host, self.Port)
        MainWindow.setTabOrder(self.Port, self.Username)
        MainWindow.setTabOrder(self.Username, self.Password)
        MainWindow.setTabOrder(self.Password, self.Login)
        MainWindow.setTabOrder(self.Login, self.Reconnect)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Info Of Login Cowry"))
        self.label.setText(_translate("MainWindow", "Host:"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "User:"))
        self.label_4.setText(_translate("MainWindow", "Password:"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.Reconnect.setText(_translate("MainWindow", "Reconnect"))
        self.Logout.setText(_translate("MainWindow", "Logout"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Method Of Encrypt Local Files"))
        self.label_5.setText(_translate("MainWindow", "Method:"))
        self.Encrypts.setItemText(0, _translate("MainWindow", "None"))
        self.Encrypts.setItemText(1, _translate("MainWindow", "AES-128-CBC"))
        self.Encrypts.setItemText(2, _translate("MainWindow", "DES"))
        self.Encrypts.setItemText(3, _translate("MainWindow", "3DES"))
        self.Encrypts.setItemText(4, _translate("MainWindow", "RC5"))
        self.Encrypts.setItemText(5, _translate("MainWindow", "IDEA"))
        self.Label_cipher.setText(_translate("MainWindow", "Cipher:"))
        self.Usepassword.setText(_translate("MainWindow", "Default"))
        self.Button_encrypt.setText(_translate("MainWindow", "Apply"))
        self.groupBox_2.setTitle(_translate("MainWindow", "User Files List"))
        self.Filetree_Private.headerItem().setText(0, _translate("MainWindow", "             Name"))
        self.Filetree_Private.headerItem().setText(1, _translate("MainWindow", "             Postfix"))
        self.Filetree_Private.headerItem().setText(2, _translate("MainWindow", "hash"))
        self.Filetree_Private.headerItem().setText(3, _translate("MainWindow", "             Size"))
        self.Filetree_Private.headerItem().setText(4, _translate("MainWindow", "          Encryption"))
        self.Filetree_Private.headerItem().setText(5, _translate("MainWindow", "        UploadTime"))
        self.Filetree_Private.headerItem().setText(6, _translate("MainWindow", "              Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Private"))
        self.Filetree_Public.headerItem().setText(0, _translate("MainWindow", "             Name"))
        self.Filetree_Public.headerItem().setText(1, _translate("MainWindow", "           Postfix"))
        self.Filetree_Public.headerItem().setText(2, _translate("MainWindow", "hash"))
        self.Filetree_Public.headerItem().setText(3, _translate("MainWindow", "           Size"))
        self.Filetree_Public.headerItem().setText(4, _translate("MainWindow", "           Encryption"))
        self.Filetree_Public.headerItem().setText(5, _translate("MainWindow", "        UploadTime"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Public"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))
        self.pushButton_3.setText(_translate("MainWindow", "Refresh"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionFiles.setText(_translate("MainWindow", "Files"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "saveLoginInfo"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.actionloadLoginInfo.setText(_translate("MainWindow", "loadLoginInfo"))
        self.actiondeleteCertificate.setText(_translate("MainWindow", "deleteCertificate"))

