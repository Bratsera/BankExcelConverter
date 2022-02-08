import sys
from qtpy import QtWidgets
from ExcelToDfContentFilter import TableConverter
from ui.mainwindow import Ui_MainWindow
from PdTableToQTableViewDatamodel import TableModel
from FileBrowser import FileBrowser


# Contains the UI-Elements of the application and the main functions,
# that are called by them
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.convertedFiles = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.chooseFileBtn.clicked.connect(self.loadTable)
        # Export the converted table as Excel-file in the hard-drive
        self.ui.btnExportSuccessTable.clicked.connect(self.exportTableSuccess)
        self.ui.btnExportCheckTable.clicked.connect(self.exportTableCheck)
        self.ui.btnExportIgnoreTable.clicked.connect(self.exportTableIgnore)

        self.setWindowTitle('MacGiro/DTE Excel Konverter')
        self.successTable = self.ui.successTable
        self.toCheckTable = self.ui.toCheckTable
        self.ignoredTable = self.ui.ignoredTable

        # statistic UI-Elements
        self.rowTotal = self.ui.lTotalRowCount
        self.convertTotal = self.ui.lConvertedCount
        self.convertPerc = self.ui.lConvertedPercent
        self.checkTotal = self.ui.lToCheckCount
        self.checkPerc = self.ui.lToCheckPercent
        self.ignoreTotal = self.ui.lIgnoredCount
        self.ignorePerc = self.ui.lIgnoredPercent



    # Loads an Excel-file, converts it and displays the result-table in the application
    def loadTable(self):

        # TODO add check if file was succesfully opened and add errorhandling for cases if file is used by another programm or has password
        # TODO implement saveFile-Method
        # open Excel-table
        file = FileBrowser.chooseFile()
        print(file.__str__())

        if file[0] != '':
            # convert table
            tableConverter = TableConverter(file[0])
            self.convertedFiles = tableConverter.convertFile()

            # Variant, using a QTableView as UI-Element
            # load table into application
            try:
                successModel = TableModel(self.convertedFiles['successTable'])
                toCheckModel = TableModel(self.convertedFiles['toCheckTable'])
                ignoredModel = TableModel(self.convertedFiles['ignoredTable'])
            except Exception as e:
                print(e)

            self.successTable.setModel(successModel)
            self.toCheckTable.setModel(toCheckModel)
            self.ignoredTable.setModel(ignoredModel)

            # Variant, using a QTableWidget as UI-Element
            # try:
            #    TableWidget(convertedFiles['successTable'],self.successTable)
            #    TableWidget(convertedFiles['toCheckTable'], self.toCheckTable)
            #    TableWidget(convertedFiles['ignoredTable'],self.ignoredTable)
            # except Exception as e:
            #    print(e)
            try:
            #fill result statistics field
                self.rowTotal.setText(str(self.convertedFiles['totalRows']))
                self.convertTotal.setText(str(self.convertedFiles['rowsConvertSuccess']))
                self.convertPerc.setText(str(round(self.convertedFiles['rowsConvertSuccess']*100/self.convertedFiles['totalRows'])))
                self.checkTotal.setText(str(self.convertedFiles['rowsImproved']))
                self.checkPerc.setText(str(round(self.convertedFiles['rowsImproved']*100/self.convertedFiles['totalRows'])))
                self.ignoreTotal.setText(str(self.convertedFiles['rowIgnored']))
                self.ignorePerc.setText(str(round(self.convertedFiles['rowIgnored']*100/self.convertedFiles['totalRows'])))
            except Exception as e:
                print(e)

    def exportTableSuccess(self):
        self.exportTable(self.convertedFiles['successTable'], 'success')

    def exportTableIgnore(self):
        self.exportTable(self.convertedFiles['ignoredTable'], 'check')

    def exportTableCheck(self):
        self.exportTable(self.convertedFiles['toCheckTable'], 'ignore')

    def exportTable(self, file, type):
        FileBrowser.exportFile(file, type)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

