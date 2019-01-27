"""
r	讀取模式
r+	讀寫模式
w	寫入模式。如果該檔案不存在，將建立一個新檔案。如果檔案存在，則會被覆蓋。
w+	讀寫模式。如果該檔案不存在，將建立一個用於讀寫的新檔案。如果檔案存在，則會被覆蓋。
a	追加模式。新資料將寫在檔案末尾。如果該檔案不存在，將建立一個用於寫入的新檔案。
a+	追加和讀寫模式。新資料將寫在檔案末尾。如果該檔案不存在，將建立一個用於讀寫的新檔案。
#readlines() 會把整個檔案讀出來第i行放在line[i]
#readline() 讀出一行(\n)第i個字放在line[i]
#readline(3) 讀出三個字第i字放在line[i]
"""
import os,time
MaxLine=100
QuitWord='q'

print("create a file.txt ")
writeBuff=list()
filename=input("press file name=")
for currenrLine in range(0,MaxLine):
    temp=input("line%d="%(currenrLine))
    if temp ==QuitWord:
        break
    writeBuff.append(temp);
#print(writeBuff)

f=open(filename+'.txt','w+')
for i in range(currenrLine):
    f.write(writeBuff[i]+'\n')
f.close
print("----------------------%s.txt----------------------"%(filename))
f=open(filename+'.txt','r')
line=f.readlines()
for i in range(currenrLine):
    print("%d:"%(i),line[i],end="")
f.close()
print("-------------------------------------------------------")
#os.rename("123.txt","test.txt")
#os.remove("test.txt")
#os.system("pause");
