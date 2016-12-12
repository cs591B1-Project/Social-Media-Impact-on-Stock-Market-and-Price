from xlrd import open_workbook

def readClosingPrice(filename):
    wb = open_workbook(filename)
    for sheet in wb.sheets():
        number_of_rows = sheet.nrows
        number_of_columns = sheet.ncols

        items = []

        rows = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(number_of_columns):
                value  = (sheet.cell(row,col).value)
                #print col

                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
            #item = Arm(*values)
            #items.append(item)

        stockPrice=[]    
        for row in range(1, number_of_rows):
            col = 4
            value  = (sheet.cell(row,col).value)
            stockPrice.append(float(value))

    print stockPrice
    # add interpolation data
    stockPrice.insert(4, stockPrice[4])
    stockPrice.insert(5, stockPrice[4])
    stockPrice.insert(11, stockPrice[11])
    stockPrice.insert(12, stockPrice[11])
    stockPrice.insert(16, stockPrice[16])
    stockPrice.insert(18, stockPrice[18])
    stockPrice.insert(19, stockPrice[18])
    stockPrice.insert(25, stockPrice[25])
    stockPrice.insert(26, stockPrice[25])

    return stockPrice