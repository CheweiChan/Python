import os,time

print("Search word in file.txt")

str=input("press your search word =")
fileName=input("press file name=")
f=open(fileName+'.txt','r')

line=f.readlines()
for i in range(3):
    #print("%d:"%(i),line[i],end="") 
    if line[i].find(str) != -1:
        print("find the word in line%d,%d"%(i,line[i].find(str)))
f.close
