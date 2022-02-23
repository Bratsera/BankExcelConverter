import pandas as pd
import Converter.PdTableToQTableViewDatamodel as QModel
import Converter.PdfReader as DteConverter
import Converter.ExcelToDfContentFilter as BankConverter
from TableData import ConvertedTables, Stats


class FileConverter:

    @staticmethod
    def convertExcelBankExport(excelFile):
        BankConverter.convertFile(excelFile)

    def convertDtePdfFile(self, pdfFile):
        DteConverter.convertFile(pdfFile)
        self.__matchBankWithDTE(ConvertedTables.toCheckTable, ConvertedTables.dtePdfTable)

    # Convert a pandas Dataframe to a QTableView
    @staticmethod
    def toQtableModel(table: pd.DataFrame):
        return QModel.TableModel(table)

    # Matches the converted bank-transfer table (check-table), where the transaction could not be entirely converted,
    # with a pdf transaction-export from Desktop-Enterprise. If there is a match with the customer- or delivery-Id AND
    # the invoice amount, the bank-transaction will be converted. If there´s only a match with the delivery-Id
    # a column with the corresponding invoice-Id will be added to the bank-check-table, so that these transactions can
    # be handled faster manually in Desktop enterprise
    def __matchBankWithDTE(self, bankCheckTable, dteTable):

        toCheckTable = bankCheckTable
        try:
            # ------------------------------ Full matches to add to SuccessTable ---------------------------------------
            # Join tables Bank and DTE tables on delivery-/customer-Id and the invoice amount
            # to connect the transaction with the invoice-Id
            customerJoin = pd.merge(toCheckTable, dteTable, how="inner",
                                    left_on=["Verwendungszweck", "Betrag EUR"], right_on=["Kundennummer", "Betrag"])
            deliveryJoin = pd.merge(toCheckTable, dteTable, how="inner",
                                    left_on=["Verwendungszweck", "Betrag EUR"],
                                    right_on=["Lieferschein-Nr", "Betrag"])

            matchTable = pd.concat([customerJoin, deliveryJoin]).reset_index(drop=True)

            Stats.rowsCorrected = len(matchTable.index)
            # ------------------------------ Full matches to add to SuccessTable END -----------------------------------

            # ------------------------------ Add invoice-ID column to CheckTable ---------------------------------------
            # Outer-Join the Bank-export with the found matches with DTE (matchTable) to exclude them
            # from the Bank export in the next step.
            checkTableWithoutSuccessMatches = pd.merge(toCheckTable, matchTable, how="outer",
                                                       on=["Verwendungszweck", "Betrag EUR", "Wertstellung"],
                                                       indicator=True)
            # Exclude rows from the matchedTable by selecting rows which were only matched on one side
            checkTableWithoutSuccessMatches = checkTableWithoutSuccessMatches.loc[
                checkTableWithoutSuccessMatches["_merge"] == "left_only"].drop("_merge", axis=1)

            # Reformat table
            checkTableWithoutSuccessMatches = checkTableWithoutSuccessMatches[
                ["Fremdkontoinhaber_x", "Verwendungszweck", "Wertstellung", "Betrag EUR"]]
            checkTableWithoutSuccessMatches.columns = ["Fremdkontoinhaber", "Verwendungszweck", "Wertstellung",
                                                       "Betrag EUR"]

            # Join the resolved table with the DTE-Export to get the invoice-ID Column for matches on the delivery-ID
            checkTableWithoutSuccessMatches = \
                pd.merge(checkTableWithoutSuccessMatches, dteTable, how="left", left_on=["Verwendungszweck"],
                         right_on=["Lieferschein-Nr"])[["Fremdkontoinhaber", "Verwendungszweck", "Wertstellung",
                                                        "Betrag EUR", "Rechnungs-Nr"]]

            # ------------------------------ Add invoice-ID column to CheckTable END -----------------------------------

            # Create new table containing the full matched rows and the existing successTable
            successTable = matchTable[["Wertstellung", "Betrag EUR", "Name", "Rechnungs-Nr"]]
            successTable = pd.concat(
                [ConvertedTables.successTable, successTable.rename(columns={"Name": "Fremdkontoinhaber",
                                                                            "Rechnungs-Nr": "Verwendungszweck"
                                                                            })], ignore_index=True)

            # --------------------------------- Update tables and stats in TableData -----------------------------------
            ConvertedTables.successTable = successTable
            ConvertedTables.toCheckTable = checkTableWithoutSuccessMatches

            Stats.successCount = len(successTable.index)
            Stats.checkCount = len(checkTableWithoutSuccessMatches.index)
            # Drop empty rows
            invoiceAddedCount = checkTableWithoutSuccessMatches["Rechnungs-Nr"].dropna()
            Stats.invoiceAddedCount = len(invoiceAddedCount.index)

            # --------------------------------- Update tables and stats in TableData END -------------------------------
        except Exception as e:
            print(e)
