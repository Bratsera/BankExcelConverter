import pandas as pd
import re

pd.options.mode.chained_assignment = None  # default='warn'


# TODO split table in two: succesfull and notsuccessfull (and maybe modified/improved)
class TableConverter:
    __REGEX_CUSTOMER_ID = "1[0-2][0-9][0-9][0-9][^0-9]|1[0-2][0-9][0-9][0-9]$"
    __REGEX_INVOICE_ID = "10[0-4][0-9][0-9][0-9]"
    __REGEX_DELIVERY_ID = "50[0-4][0-9][0-9][0-9]"

    successTable = []
    toCheckTable = []
    ignoredTable = []

    def __init__(self, excelFile):
        self.table = pd.read_excel(excelFile)
        self.fileRowCount = len(self.table.index)
        self.conversionResult = self.convertFile()

        self.successTable = []
        self.toCheckTable = []
        self.ignoredTable = []

    def convertFile(self):
        transferDesc = self.table['Verwendungszweck']

        try:
            for index, line in enumerate(transferDesc):
                # A check if line is not a number NaN
                if line != line:
                    self.ignoredTable.append(self.table.loc[index])
                    continue
                result = re.findall(self.__REGEX_INVOICE_ID, line)

                match result:
                    # Match for one Invoice-id in reference-column
                    case result if len(result) == 1:

                        transferDesc.at[index] = result[0]
                        self.successTable.append(self.table.loc[index])

                    # Match for more than one Invoice-id´s in reference-column
                    case result if len(result) > 1:
                        # print('match RE ' + str(index))
                        customer = re.search(self.__REGEX_CUSTOMER_ID, line)
                        matches = ', '.join(result)
                        newDesc = 'Re-Nr: ' + matches
                        transferDesc.at[index] = newDesc + '; Kd-Nr: ' + customer.group()[0:5] if customer else newDesc
                        self.toCheckTable.append(self.table.loc[index])

                    # If no Invoice-id in reference-column, match for one delivery-id in reference-column
                    case result if len(result) == 0:
                        deliveryId = re.findall(self.__REGEX_DELIVERY_ID, line)
                        if len(deliveryId) == 0:
                            self.ignoredTable.append(self.table.loc[index])
                        else:
                            customer = re.search(self.__REGEX_CUSTOMER_ID, line)
                            # print('match LieferID ' + str(index))
                            matches = ', '.join(deliveryId)
                            newDesc = 'Lieferschein: ' + matches
                            transferDesc.at[index] = newDesc + \
                                                     '; Kd-Nr: ' + customer.group()[0:5] if customer else newDesc
                            self.toCheckTable.append(self.table.loc[index])

        except Exception as e:
            print(e)

        self.successTable = pd.DataFrame(self.successTable)
        self.toCheckTable = pd.DataFrame(self.toCheckTable)
        self.ignoredTable = pd.DataFrame(self.ignoredTable)

        try:
            return {
                'successTable': self.successTable,
                'toCheckTable': self.toCheckTable,
                'ignoredTable': self.ignoredTable,
                'rowsImproved': len(self.toCheckTable.index),
                'rowsConvertSuccess': len(self.successTable.index),
                'rowIgnored': len(self.ignoredTable.index),
                'totalRows': self.fileRowCount
            }
        except Exception as e:
            print(e)
        # print("Abgleich möglich: " + str(self.filesConvCounter))
        # print("Betreff verbessert: " + str(self.filesImprovedCounter))
    # print("Transaktionen gesamt: " + str(self.fileRowCount))
    # print("Abgleichquote %: " + str(self.successRatio))
