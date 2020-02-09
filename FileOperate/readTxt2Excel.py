import os,time,xlrd
import xlsxwriter as xl

filename='test.xlsx'
i=0;j=0;b=0
f=open('ECLog.txt','r',encoding ='gbk')
line =f.readline()
Workbook=xl.Workbook(filename)
sheet1 = Workbook.add_worksheet('test')
starttime= time.time()
while(line != ''):
    for i in range(0,255):
        if line[i] ==(chr(32)):
            continue
        if line[i] >='0' and line[i] <='9':
            temp=int(line[i])
            sheet1.write_number(j,b,temp)
            #print(temp,end='')
        elif line[i] =='\n':
            break 
        else:
            temp=line
            sheet1.write_string(j,b,temp)
            #print(temp,end='')
            break
        b+=1
    #print('')
    line=f.readline()
    j+=1
    b=0
endtime=time.time()
print(" %f"%(endtime-starttime))
f.close
Workbook.close()
os.system(filename)