import pandas as pd


class ConvertedTables(object):
    # Table containing transactions with exact one invoice-Id
    successTable = pd.DataFrame()
    # Table containing transactions with several invoice-Id´s or a delivery-Id or/and a customer-Id
    toCheckTable = pd.DataFrame()
    # Table containing transactions with no invoice-Id, delivery or customer-Id
    ignoreTable = pd.DataFrame()
    # Table containing all open transactions in Desktop Enterprise with customer, delivery and invoice-Id
    dtePdfTable = pd.DataFrame()


class Stats:
    # Row Count of successTable
    successCount: int
    # Row Count of toCheckTable
    checkCount: int
    # Row Count of ignoreTable
    ignoreCount: int
    # Row Count of the Bank-Export
    totalCount: int
    # Row Count of the Desktop-Enterprise-Export
    dteTotalCount: int
    # Amount of rows that have been corrected by matching the Bank-Export with the Desktop-Enterprise-Export
    rowsCorrected: int
    # Amount of rows in the toCheckTable where an invoice-Id has been added
    # by matching the Bank-Export with the Desktop-Enterprise-Export
    invoiceAddedCount: int

    @staticmethod
    def calcSuccessPercent():
        return round(Stats.successCount * 100/Stats.totalCount)

    @staticmethod
    def calcCheckPercent():
        return round(Stats.checkCount * 100/Stats.totalCount)


    @staticmethod
    def calcIgnorePercent():
        return round(Stats.ignoreCount * 100/Stats.totalCount)



