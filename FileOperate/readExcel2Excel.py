import xlrd
import xlwt

def set_style(name, height, bold ):
	style = xlwt.XFStyle()   #style init
	
	font = xlwt.Font()       #font init
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height
	
	style.font = font
	return style

data = xlrd.open_workbook('321.xlsx') # open xlsx
workbook = xlwt.Workbook() 
sheet1 = workbook.add_sheet('test')
table = data.sheets()[0] # open first sheet
data_=table.cell_value(0,1)
nrows = table.nrows # get row
j=0;p=0
skip=0
print("row=%d\n"%(nrows))
excelStyle=set_style('Times New Roman', 220, True)
#f=open("temp.txt",'w')
for i in range(nrows): # print 
    for q in range(table.ncols):
        print(table.cell_value(p,q),end='')
        sheet1.write(i,q,table.cell_value(p,q),excelStyle)
    print('')
    if j == 30:
        p+=5
       # print("...%d"%(p))
        j=0

    if skip != 1:
        p+=1
        skip=0
        j+=1
    else:
        skip=0

    if p>=nrows:
        break

workbook.save('test3.xls')
