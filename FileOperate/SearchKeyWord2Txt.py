import os,time
print("Search word in file.txt")

fileName=input("press file name=")
str=input("press your search word =")
writebuffer=list()
f=open(fileName,'r',encoding ='gbk')
#with open(r'C:\Users\user\Desktop\git\Python\FileOperate\123.txt', 'r',encoding='gbk') as f:
#with open(r'C:\Users\user\Desktop\git\Python\FileOperate\temp.txt','w',encoding='gbk') as fw:
i=0;j=0

starttime= time.time()

line=f.readline()
while(line !=""):
    if line.find(str) != -1:
         print("find the word in line%d,%d"%(i,line.find(str)))
         writebuffer.append(line)
    #if((i%10000==0) and (i !=0)):
        #fw=open(r'C:\Users\user\Desktop\git\Python\FileOperate\temp.txt','w')
        #fw.writelines(writebuffer)    
        #fw.close
        #writebuffer.clear
    line=f.readline()
    i+=1
f.close
fw=open(r'C:\Users\user\Desktop\git\Python\FileOperate\temp.txt','w')
fw.writelines(writebuffer)
fw.close


endtime=time.time()
print(" %f"%(endtime-starttime))

os.system('pause')


#fw=open(r'C:\Users\user\Desktop\git\Python\FileOperate\temp.txt','w')
#line=f.readline()
#while(line != ""):
#     #print(line)
#    if line.find(str) != -1:
#        print("find the word in line%d,%d"%(i,line.find(str)))
#        fw.write(line)
#    line=f.readline()
#    i+=1
