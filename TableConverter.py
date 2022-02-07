import pandas as pd
import re
pd.options.mode.chained_assignment = None  # default='warn'
#TODO split table in two: succesfull and notsuccessfull (and maybe modified/improved)
class TableConverter:
    __REGEX_CUSTOMER_ID = "1[0-2][0-9][0-9][0-9][^0-9]|1[0-2][0-9][0-9][0-9]$"
    __REGEX_INVOICE_ID = "10[0-4][0-9][0-9][0-9]"
    __REGEX_DELIVERY_ID = "50[0-4][0-9][0-9][0-9]"
    successRatio = None
    filesConvCounter = 0
    filesImprovedCounter = 0

    def __init__(self, excelFile):
        self.table = pd.read_excel(excelFile)
        self.fileRowCount = len(self.table.index)
        self.conversionResult = self.convertFile()

    def convertFile(self):
        transferDesc = self.table['Verwendungszweck']
        for index, line in enumerate(transferDesc):
            result = re.findall(self.__REGEX_INVOICE_ID, line)
            if len(line) > 0:
                match result:
                    case result if len(result) == 1:
                        transferDesc.at[index] = result[0]
                        self.filesConvCounter += 1

                    case result if len(result) > 1:
                        print('match RE ' + str(index))
                        customer = re.search(self.__REGEX_CUSTOMER_ID, line)
                        matches = ', '.join(result)
                        newDesc = 'Re-Nr: ' + matches
                        transferDesc.at[index] = newDesc + '; Kd-Nr: ' + customer.group()[0:5] if customer else newDesc
                        self.filesImprovedCounter += 1

                    case result if len(result) == 0:
                        deliveryId = re.findall(self.__REGEX_DELIVERY_ID, line)
                        if len(deliveryId) == 0:
                            continue
                        customer = re.search(self.__REGEX_CUSTOMER_ID, line)
                        print('match LieferID ' + str(index))
                        matches = ', '.join(deliveryId)
                        newDesc = 'Lieferschein: ' + matches
                        transferDesc.at[index] = newDesc + '; Kd-Nr: ' + customer.group()[0:5] if customer else newDesc
                        self.filesImprovedCounter += 1
        self.successRatio = round(self.filesConvCounter * 100 / self.fileRowCount, 2)

        return {'convertedFile': self.table,
                'successRatio': self.successRatio,
                'rowsImproved': self.filesImprovedCounter,
                'rowsConvertSuccess': self.filesImprovedCounter,
                'totalRows': self.fileRowCount
                }

        #print("Abgleich möglich: " + str(self.filesConvCounter))
        #print("Betreff verbessert: " + str(self.filesImprovedCounter))
       # print("Transaktionen gesamt: " + str(self.fileRowCount))
        #print("Abgleichquote %: " + str(self.successRatio))
