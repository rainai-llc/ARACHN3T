#!/usr/bin/env python3
#
# Scientist: Jeremiah Jackson-Williams
#
# Date of creation: 4/6/2025
#
# Contact: rainaiincorporated@gmail.com

import os as ground
import subprocess as stack0
import re as skim
from time import sleep
import urllib.request as web0
import urllib.error as web1
import urllib.response as web2
from .clusterMem import clusterMark
import json

class memlink:
    def __init__(self,in22):
        self.in22=in22
        self.mataDir='/Motion'
        self.cluster0={}
        self.cluster1=[]
    def synapse00(self) -> tuple:
        if type(self.in22)!=tuple:
            return ((type(self.in22)==tuple,1),(True,0),(False,-1))
        else:
            shiftName='rainaiSynapse0'
            print("Deployed Helper 3")
            print(self.in22[2])
            if 'motion' not in ground.getcwd().lower():
                ground.chdir(self.in22[1][0]+self.mataDir)
            tmpVal=0
            for currHandle0 in range(len(self.in22[2])):
                try:
                    if ".rainai" in self.in22[2][currHandle0] and tmpVal==0:
                        tmpVal+=1
                        stack0.run(['tmux','new-session','-d','-s',shiftName,'python3',self.in22[2][currHandle0]])
                        stack0.run(['tmux','split-window','-h','-t',shiftName])
                        print("Server initiated")
                    elif self.in22[2][currHandle0].endswith(".rainai") and tmpVal!=0:
                        stack0.run(['tmux','send-keys','-t',shiftName+'.'+str(currHandle0),'python3',self.in22[2][currHandle0],'C-m'])
                        stack0.run(['tmux','split-window','-v','-t',shiftName])
                        print("Session configured")
                    else:
                        pass
                    sleep(1)
                except:
                    return ((False,1),(True,0),(False,1))
        return ((type(self.in22)==tuple,1),(True,0),(False,-1)),ground.getcwd()
    def synapse01(self):
        # try:
        #     from .memCluster import memCluster,memSegment
        #     tmpRes=[]
        #     if len(memSegment)!=0 and len(memCluster)!=0:
        #         return ((type(self)==list,1),(True,0),(False,-1)),memCluster,memSegment
        # except:
        if 'motion' not in ground.getcwd():
            ground.chdir(self.in22[1][0]+self.mataDir)
        tmpHandle=skim.findall(r'[a-zA-Z0]{9}dat',str(self.in22[2]))
        print(tmpHandle)
        print(ground.getcwd())
        for currHandle1 in range(len(tmpHandle)):
            currHandle2=open(tmpHandle[currHandle1],'r')
            for currHandle3 in currHandle2.readlines():
                    try:
                        currHandle4=currHandle3.replace(' ','').split('|')
                        if int(currHandle4[0])>clusterMark:
                            print("Preparing "+currHandle4[0]+' | '+currHandle4[1]+" for mapping. . .")
                            self.cluster0[currHandle4[0]]=currHandle4[1].replace('\n','')
                            self.cluster1.append(currHandle4[1].replace('\n',''))
                            currHandle7=open(self.in22[1][0]+'/Memorylink/clusterMem.py','w')
                            currHandle7.write("""#!/usr/bin/env python3
#
# Scientist: Jeremiah Jackson-Williams
#
# Date of creation: 4/6/2025
#
# Contact: rainaiincorporated@gmail.com
clusterMark="""+str(currHandle4[0]))
                        else:
                            pass
                    except:
                        print("Some Error in Memlink Sysnapse01")
                        pass
        ground.chdir(self.in22[1][0]+'/Memorylink')
        print(ground.getcwd())
        currHandle8=open(self.in22[1][0]+'/Memorylink/memCluster.py','w')
        if len(self.cluster0)!=0:
            currHandle8.write("""#!/usr/bin/env python3
# Author: Jeremiah Jackson-Williams
#
# Copyright: Rainai Inc. @2025
memCluster="""+str(self.cluster0)+"\nmemSegment="+str(self.cluster1))
        return ((type(self)==list,1),(True,0),(False,-1)),self.cluster0,self.cluster1,ground.getcwd()
    def memTA00(self) -> tuple:
        if type(self.in22)==list:
            print("Missing links or dependencies for spectral")
        elif type(self.in22)==tuple:
            if type(self.in22[2])==list and len(self.in22[2])!=0:
                try:
                    #self.in22[0] is the working directory -> Motion for MATA on subdomains.
                    #Looking to map Ipv4z with respective domains and
                    ground.chdir(self.in22[0]+self.mataDir)
                    print("ACTIONS TAKEN:  \n"+ground.getcwd())
                    return True,self.in22,ground.listdir()
                except:
                    print("Error in Memorylink")
                    return False,self.in22
