# Form implementation generated from reading ui file 'UI\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 868)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseFileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileBtn.setGeometry(QtCore.QRect(10, 10, 80, 27))
        self.chooseFileBtn.setObjectName("chooseFileBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(4, 46, 851, 781))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.successTable = QtWidgets.QTableView(self.tab)
        self.successTable.setGeometry(QtCore.QRect(0, 0, 851, 751))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.successTable.sizePolicy().hasHeightForWidth())
        self.successTable.setSizePolicy(sizePolicy)
        self.successTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.successTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.successTable.setObjectName("successTable")
        self.successTable.horizontalHeader().setCascadingSectionResizes(True)
        self.successTable.horizontalHeader().setStretchLastSection(True)
        self.successTable.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.toCheckTable = QtWidgets.QTableView(self.tab_2)
        self.toCheckTable.setGeometry(QtCore.QRect(0, 0, 851, 751))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toCheckTable.sizePolicy().hasHeightForWidth())
        self.toCheckTable.setSizePolicy(sizePolicy)
        self.toCheckTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.toCheckTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.toCheckTable.setObjectName("toCheckTable")
        self.toCheckTable.horizontalHeader().setCascadingSectionResizes(True)
        self.toCheckTable.horizontalHeader().setMinimumSectionSize(30)
        self.toCheckTable.horizontalHeader().setStretchLastSection(True)
        self.toCheckTable.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.ignoredTable = QtWidgets.QTableView(self.tab_3)
        self.ignoredTable.setGeometry(QtCore.QRect(-5, 1, 851, 761))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignoredTable.sizePolicy().hasHeightForWidth())
        self.ignoredTable.setSizePolicy(sizePolicy)
        self.ignoredTable.setObjectName("ignoredTable")
        self.ignoredTable.horizontalHeader().setCascadingSectionResizes(True)
        self.ignoredTable.horizontalHeader().setDefaultSectionSize(90)
        self.ignoredTable.horizontalHeader().setMinimumSectionSize(30)
        self.ignoredTable.horizontalHeader().setStretchLastSection(True)
        self.ignoredTable.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(859, 50, 171, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnExportSuccessTable = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExportSuccessTable.setObjectName("btnExportSuccessTable")
        self.verticalLayout.addWidget(self.btnExportSuccessTable)
        self.btnExportCheckTable = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExportCheckTable.setObjectName("btnExportCheckTable")
        self.verticalLayout.addWidget(self.btnExportCheckTable)
        self.btnExportIgnoreTable = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExportIgnoreTable.setObjectName("btnExportIgnoreTable")
        self.verticalLayout.addWidget(self.btnExportIgnoreTable)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 19, 151, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.totalLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.totalLabel.setObjectName("totalLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.totalLabel)
        self.convertedLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.convertedLabel.setObjectName("convertedLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.convertedLabel)
        self.convertedPercentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.convertedPercentLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.convertedPercentLabel.setObjectName("convertedPercentLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.convertedPercentLabel)
        self.lConvertedCount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lConvertedCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lConvertedCount.setReadOnly(True)
        self.lConvertedCount.setObjectName("lConvertedCount")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lConvertedCount)
        self.lConvertedPercent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lConvertedPercent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lConvertedPercent.setObjectName("lConvertedPercent")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lConvertedPercent)
        self.toCheckLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.toCheckLabel.setObjectName("toCheckLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.toCheckLabel)
        self.toCheckPercentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.toCheckPercentLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.toCheckPercentLabel.setObjectName("toCheckPercentLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.toCheckPercentLabel)
        self.lToCheckCount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lToCheckCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lToCheckCount.setReadOnly(True)
        self.lToCheckCount.setObjectName("lToCheckCount")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lToCheckCount)
        self.lToCheckPercent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lToCheckPercent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lToCheckPercent.setObjectName("lToCheckPercent")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lToCheckPercent)
        self.ignoredLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ignoredLabel.setObjectName("ignoredLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.ignoredLabel)
        self.ignoredPercentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ignoredPercentLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ignoredPercentLabel.setObjectName("ignoredPercentLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.ignoredPercentLabel)
        self.lIgnoredCount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lIgnoredCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lIgnoredCount.setReadOnly(True)
        self.lIgnoredCount.setObjectName("lIgnoredCount")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.lIgnoredCount)
        self.lIgnoredPercent = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lIgnoredPercent.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lIgnoredPercent.setObjectName("lIgnoredPercent")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lIgnoredPercent)
        self.lTotalRowCount = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lTotalRowCount.setFont(font)
        self.lTotalRowCount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lTotalRowCount.setReadOnly(True)
        self.lTotalRowCount.setObjectName("lTotalRowCount")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.lTotalRowCount)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1040, 300, 125, 223))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 19))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionHilfe = QtGui.QAction(MainWindow)
        self.actionHilfe.setObjectName("actionHilfe")
        self.actionDatei_ffnen = QtGui.QAction(MainWindow)
        self.actionDatei_ffnen.setObjectName("actionDatei_ffnen")
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.actionDatei_ffnen)
        self.menuMen.addAction(self.actionHilfe)
        self.menuMen.addAction(self.actionBeenden)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chooseFileBtn.setText(_translate("MainWindow", "Choose file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Converted Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "To Check Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Ignored Table"))
        self.btnExportSuccessTable.setText(_translate("MainWindow", "Export Converted-Table"))
        self.btnExportCheckTable.setText(_translate("MainWindow", "Export To-Check-Table"))
        self.btnExportIgnoreTable.setText(_translate("MainWindow", "Export Ignored-Table"))
        self.groupBox.setTitle(_translate("MainWindow", "Result"))
        self.totalLabel.setText(_translate("MainWindow", "Total rows:"))
        self.convertedLabel.setText(_translate("MainWindow", "Rows converted"))
        self.convertedPercentLabel.setText(_translate("MainWindow", "in %"))
        self.lConvertedCount.setText(_translate("MainWindow", "0"))
        self.lConvertedPercent.setText(_translate("MainWindow", "0"))
        self.toCheckLabel.setText(_translate("MainWindow", "Rows to check"))
        self.toCheckPercentLabel.setText(_translate("MainWindow", "in %"))
        self.lToCheckCount.setText(_translate("MainWindow", "0"))
        self.lToCheckPercent.setText(_translate("MainWindow", "0"))
        self.ignoredLabel.setText(_translate("MainWindow", "Ignored Rows"))
        self.ignoredPercentLabel.setText(_translate("MainWindow", "in %"))
        self.lIgnoredCount.setText(_translate("MainWindow", "0"))
        self.lIgnoredPercent.setText(_translate("MainWindow", "0"))
        self.lTotalRowCount.setText(_translate("MainWindow", "0"))
        self.menuMen.setTitle(_translate("MainWindow", "Menü"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))
        self.actionHilfe.setText(_translate("MainWindow", "Hilfe"))
        self.actionDatei_ffnen.setText(_translate("MainWindow", "Datei öffnen"))
