import sys
from TableData import Stats, ConvertedTables
from qtpy import QtWidgets
from Converter.FileConverter import FileConverter
from ui.mainwindow import Ui_MainWindow
from FileBrowser import FileBrowser

#Todo add Top Menu in App
#ToDO add instructions to app
#ToDO add translation to program
#ToDo add custom invoice regex via appUI
#ToDo add custom colum name for transaction-Column in Bank-export

# Contains the UI-Elements of the application and the main functions,
# that are called by them
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileConverter = FileConverter()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ------------------------------------- EventListeners ---------------------------------------------------
        self.ui.chooseFileBtn.clicked.connect(self.loadTable)
        self.ui.btnMatchDTE.clicked.connect(self.matchExportWithDTE)
        # Export the converted table as Excel-file in the hard-drive
        self.ui.btnExportSuccessTable.clicked.connect(self.exportTableSuccess)
        self.ui.btnExportCheckTable.clicked.connect(self.exportTableCheck)
        self.ui.btnExportIgnoreTable.clicked.connect(self.exportTableIgnore)
        # ------------------------------------- EventListeners END-------------------------------------------------

        # ------------------------------------- UI-Elements -------------------------------------------------------
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

        self.msgBox = QtWidgets.QMessageBox()

        # ------------------------------------- UI-Elements END ---------------------------------------------------


    # Loads the Excel-file of the bank-transactions-export, converts it to the desired format needed to be recognized
    # by Desktop-Enterprise and displays the result-tables in the application-windows
    def loadTable(self):

        # TODO add check if file was succesfully opened and add errorhandling for cases if file is used by another programm or has password
        # open Excel-table
        file = FileBrowser.chooseFile("excel")
        # print(file.__str__())

        if file[0] != '':
            # convert table
            try:
                FileConverter.convertExcelBankExport(file[0])

            # Variant, using a QTableView as UI-Element
            # Convert the result tables from Dataframe to QTableView-type, to display the tables in the application
                successModel = FileConverter.toQtableModel(ConvertedTables.successTable)
                toCheckModel = FileConverter.toQtableModel(ConvertedTables.toCheckTable)
                ignoredModel = FileConverter.toQtableModel(ConvertedTables.ignoreTable)

                self.msgBox.information(self.msgBox, "Conversion successfull",
                                        "The file has been success parsed and split into different tables, depending on the grade of conversion. "
                                        "You can see the result in the different tables and export them with the corresponding buttons",
                                        self.msgBox.Ok)
            except Exception as e:
                self.showError(e)

            # Load the tables into the application
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
                # fill result statistics fields in the application
                self.rowTotal.setText(str(Stats.totalCount))
                self.convertTotal.setText(str(Stats.successCount))
                self.convertPerc.setText(str(Stats.calcSuccessPercent()))
                self.checkTotal.setText(str(Stats.checkCount))
                self.checkPerc.setText(str(Stats.calcCheckPercent()))
                self.ignoreTotal.setText(str(Stats.ignoreCount))
                self.ignorePerc.setText(str(Stats.calcIgnorePercent()))

                # Enable all UI-buttons for the further steps
                self.ui.btnMatchDTE.setEnabled(True)
                self.ui.btnExportSuccessTable.setEnabled(True)
                self.ui.btnExportCheckTable.setEnabled(True)
                self.ui.btnExportIgnoreTable.setEnabled(True)

            except Exception as e:
                self.showError(e)

    def exportTableSuccess(self):
        self.exportTable(ConvertedTables.successTable, 'success')

    def exportTableIgnore(self):
        self.exportTable(ConvertedTables.ignoreTable, 'ignore')

    def exportTableCheck(self):
        self.exportTable(ConvertedTables.toCheckTable, 'check')

    def exportTable(self, file, resultType: str):
        FileBrowser.exportFile(file, resultType)

    # Matches the converted bank-transfer table (check-table), where the transaction could not be entirely converted,
    # with a pdf transaction-export from Desktop-Enterprise. If there is a match with the customer- or delivery-Id AND
    # the invoice amount, the bank-transaction will be converted. If there´s only a match with the delivery-Id
    # a column with the corresponding invoice-Id will be added to the bank-check-table, so that these transactions can
    # be handled faster manually in Desktop enterprise
    def matchExportWithDTE(self):

        try:
            file = FileBrowser.chooseFile("pdf")
            print(file.__str__())
            if file[0] != '':
                self.fileConverter.convertDtePdfFile(file[0])

                try:
                    # Convert the updated result tables from Dataframe to QTableView-type, to display the tables in the application
                    successModel = self.fileConverter.toQtableModel(ConvertedTables.successTable)
                    toCheckModel = self.fileConverter.toQtableModel(ConvertedTables.toCheckTable)
                except Exception as e:
                    self.showError(e)

                # Load the tables into the application
                self.successTable.setModel(successModel)
                self.toCheckTable.setModel(toCheckModel)

                # Update result statistics fields in the application
                self.convertTotal.setText(str(Stats.successCount))
                self.convertPerc.setText(str(Stats.calcSuccessPercent()))
                self.checkTotal.setText(str(Stats.checkCount))
                self.checkPerc.setText(str(Stats.calcCheckPercent()))

                self.msgBox.information(self.msgBox, "Match with DTE-export successfull",
                                        "The match has been successfully finished. " + str(Stats.dteTotalCount) + " rows of the Desktop Enterprise export were matched witch the converted check-table."
                                        + str(Stats.rowsCorrected) + " rows with a full match on the customerId/deliveryId and the invoice amount have been converted and added to the success-table. "
                                        "For " + str(Stats.invoiceAddedCount) + " rows with a match on the deliveryId the invoiceId has been added to the transaction.", self.msgBox.Ok)

        except Exception as e:
            self.showError(e)

    # Display an alert-error-message in the application
    def showError(self, error):
        self.msgBox.critical(self.msgBox, "An unknown error occured",
                             "An unhandled error occured: "
                             + error +
                             "Please contact the stupid programmer who missed this.", self.msgBox.Close)
        print(error)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

