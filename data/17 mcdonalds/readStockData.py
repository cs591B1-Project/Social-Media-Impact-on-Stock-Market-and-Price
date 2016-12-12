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

    #print stockPrice
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

def readVolume(filename):
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

        volume=[]    
        for row in range(1, number_of_rows):
            col = 5
            value  = (sheet.cell(row,col).value)
            volume.append(float(value))

    #print volume
    # add interpolation data
    volume.insert(4, volume[4])
    volume.insert(5, volume[4])
    volume.insert(11, volume[11])
    volume.insert(12, volume[11])
    volume.insert(16, volume[16])
    volume.insert(18, volume[18])
    volume.insert(19, volume[18])
    volume.insert(25, volume[25])
    volume.insert(26, volume[25])

    return volume