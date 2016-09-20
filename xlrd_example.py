import os, xlrd, pprint
files = os.listdir(os.getcwd())
xl_file = filter(lambda x: x.endswith('.xls'),files)
print xl_file

if __name__ == '__main__':
    xl_file = xlrd.open_workbook(xl_file[0])
    ## View sheetnames
    print xl_file.sheet_names() ## Only 1 sheet
    ## Enter into sheet 2013
    sheet_2013 = xl_file.sheet_by_index(0)
    ## View NCols and NRows
    print '(NCols: %d, NRows:%d)' %(sheet_2013.ncols,sheet_2013.nrows)
    ## Check out column names
    print 'Column Names:'
    pprint.pprint(sheet_2013.row_values(0))
    ## Obtain all values for Hour_End and Coast as a list of tuples
    Hour_End_Col = sheet_2013.col_values(0,1,sheet_2013.nrows)
    Coast_Col = sheet_2013.col_values(1,1,sheet_2013.nrows)
    Data = zip(Hour_End_Col,Coast_Col)
    print Data[0]
    ## Obtain max values
    max_coast_time,max_coast = sorted(Data, key = lambda x: x[-1], reverse = True)[0]
    print max_coast, xlrd.xldate_as_tuple(max_coast_time,0)
    ## Obtain min values
    min_coast_time,min_coast = sorted(Data, key = lambda x: x[-1])[0]
    print min_coast, xlrd.xldate_as_tuple(min_coast_time,0)
    ## Obtain average coast
    print sum(Coast_Col) / len(Coast_Col)
