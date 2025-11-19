# Author: Jeremiah Jackson-Williams
# Copy right: Rainai Inc. 2025

import os as ground
from time import sleep
import re as skim
import subprocess as stack0
import urllib.request as web0
import urllib.error as web2
import urllib.response as web3
import _thread as link0
import multiprocessing as link1

class mita:
    def __init__(self,in33):
        self.in33=in33
    def localizeIn0(self):
        passOut0=[]
        if type(self.in33)==list:
            print(ground.getcwd())
            for currHandle5 in self.in33:
                if "root" not in currHandle5 and "clean" in currHandle5 and "scope" not in currHandle5 and "main" not in currHandle5 and 'auto' not in currHandle5:
                    currHandle6=open(currHandle5,'r')
                    appOut0=currHandle6.readlines()
                    print("Batch available.. Type: "+str(type(appOut0))+' Size: '+str(len(appOut0)))
                    passOut0.append((currHandle5,str(appOut0).replace('\\n','').replace('\\t','|').replace('[','').replace(']','').replace(' ','').replace("'",'').split(',')))
                    sleep(0.7)
                else:
                    pass
        return passOut0
    def arachn3tLink0(self):
        print("Current Network Batch Size: ", len(source0))
        print("Current Domain Batch Size: ", len(source1))
    def segmentation0(self):
        source0=[]
        source1=[]
        source0Memlink={}
        source1Memlink={}
        print("Segmentation starting...")
        sleep(2)
        print(ground.getcwd())
        if type(self.in33)!=list:
            return False
        else:
            for currHandle7 in list(set(self.in33[0][1])):
                if "127.0.0.1" in currHandle7:
                    pass
                else:
                    currHandle8=currHandle7.split('|')
                    source0Memlink[currHandle8[0]]=currHandle8[1]
                    print(currHandle8, source0Memlink[currHandle8[0]])
    def datIngestion0(self):
        deadDat=[]
        tmpMarker=0
        tmpPivot=None
        if not 'datCluster' in ground.getcwd():
            try:
                tmpPivot=ground.chdir(ground.getcwd()+'/datCluster')
            except:
                ground.mkkdirs(ground.getcwd()+'/datCluster')
        else:
            tmpPivot=ground.getcwd()
        failedDat=open('datRawHtml/datIngestLog.csv','a')
        for datHandle0 in self.in33:
            for datHandle1 in datHandle0:
                if datHandle1.replace('https://','') in ground.listdir() and 'index.html' in str(ground.listdir(tmpPivot+'/'+datHandle1.replace('https://',''))):
                    pass
                elif datHandle1.replace('https://','') in ground.listdir() and not 'index.html' in ground.listdir(tmpPivot+'/'+datHandle1.replace('https://','')):
                    # ground.chdir(datHandle1.replace('https://',''))
                    try:
                        stack0.run(['wget','-t','1',datHandle1,'-T','7','-O',tmpPivot+'/'+datHandle1.replace('https://','')+'/index.html'])
                        failedDat.write(str(tmpMarker)+','+datHandle1+',True,'+'True\n')
                    except:
                        failedDat.write(str(tmpMarker)+','+datHandle1+',True,'+'False\n')
                        continue
                else:
                    tmpPivot
                    ground.makedirs(datHandle1.replace('https://',''))
                    print(datHandle1, " Localized as tangible...")
                    if datHandle1.replace('https://','') in tmpPivot:
                        try:
                            stack0.run(['wget','-t','1',datHandle1,'-T','7','-O',tmpPivot+'/'+datHandle1.replace('https://','')+'/index.html'])
                            failedDat.write(str(tmpMarker)+','+datHandle1+',True,'+'True\n')
                        except:
                            tmpPivot
                            failedDat.write(str(tmpMarker)+','+datHandle1+',True,'+'False\n')
                            deadDat.append(datHandle1)
                            print("Error within positioned states. Chech mark starting from line 59 Memorylink datIngestion0")
                tmpMarker+=1
    def segmentation1(self):
        currHandle9=[]
        if type(self.in33)!=list:
            return TypeError
        else:
            tmpMark=None
            projectedThreads=120
            endIngest=0
            clusterSize=len(self.in33)//projectedThreads
            while clusterSize<len(self.in33):
                currHandle9.append(self.in33[endIngest:clusterSize])
                endIngest=clusterSize
                tmpMark=endIngest
                clusterSize+=clusterSize
                print(len(self.in33[endIngest:clusterSize]))
                print('X'*75)
        return ((type(currHandle9)==list,1),(True,0),(False,-1)),currHandle9,ground.getcwd()
