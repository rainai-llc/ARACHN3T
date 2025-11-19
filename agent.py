#!/usr/bin/env python3

import subprocess as stack0
import os as ground
import re as skim
import urllib.request as web0
import urllib.error as web1
import sys
# import matplotlib.pyplot as vis0
# import plotly.express as vis1
# import plotly.graph_objects as vis2

class converse():
    def __init__(self,in0):
        self.in0=in0
        self.ou0=[]
        self.Mci={}
        self.ci=None
        punctutaions=[',',"'",'"','!','?','&','(',')']
    def digest(self):
        in3=self.in0.split('.')
        for in4 in in3:
            self.ou0.append(in4.split(' '))
        return self.ou0

    def initialUserNotice(self):
        userNotice = '\nGot it!\n\nLet\'s make sure we get things in order for immediately.\n\nProvide the following:\n\n[First-name Last-name]\n\n[Email]\n'
        print(userNotice)
        return True,(1,0,0)

    def userGen(self):
        userGen='\nAwesome!\n\nAnd the best email we can contact you by for communication regarding resolution?'
        return True,(1,1,0)
    def finalUserNotice(self):
        finalNotice = 'This chat is not for consultation.\n\nYou may email us for all other serious inqueries at rainaiincorporated@gmail.com\n\nWhat is your first & last name and email?\n'
        print(finalNotice)
        return True,(-1,0,0)

    def leadGen(self):
        leadGen='\nThank you!\n\nPlease explain your reason and I will have it sent to the team immediately to connect.\nA detailed summary of the trouble is preferred, as it can increase recovery time and odds.\n'
        print(leadGen)
        return True,(-1,1,0)

    def missedContact(self):
        missedUser="\nUhhhh...\n\nApologies, though it seems like your email is misssing.\nPlease make sure to provide it so we can move forward.\n\nIf you are looking to contact the Principal Engineer, you can do so here as well."
        print(missedUser)

    def closeChat(self):
        closeChat='\nSent to the team!\n\nYou will be contacted via email within the next hour.\n\n Self-Destructing in 3 seconds.\n'
        print(closeChat)
        return True,(1,1,1)

    def systemMaint(self):
        systemMain='\nThere has been a change somewhere on the internet that is preventing me from sending this message on your behalf.\nPlease reach out to us directly:\nEmail: rainaiincorporated@gmail.com\n\n-Thank You.'
    def initialUpdate(self):
        db=ground.getcwd()+'/datCluster/datRawHtml/datIngestLog.csv'
        outVis=[]
        with open(db,'r') as dat:
            outDat=dat.read()
            outDat=outDat.split('\n')
            outVal=""
            tmp=[]
            tmpLen={}
            base=0
            for rawDat in outDat:
                tmp.append(rawDat.split(','))
                tmpLen[outDat.index(rawDat)]=(len(rawDat))
            for i,m in tmpLen.items():
                if m<max(tmpLen.values()):
                    pass
                else:
                    outVal+='_'*tmpLen[i]+'\n'
                    base+=tmpLen[i]
            for curr1 in range(len(tmp)):
                if curr1==0:
                    for curr in tmp[curr1]:
                        if curr=='dID' or curr=="Localized" or curr=="Source":
                            outVal+='| '+curr+' '
                        else:
                            outVal+='|'+' '*72+curr+' '*72
                else:
                    for curr in tmp[curr1]:
                        if curr.isdigit():
                            outVal+='\n|  '+curr+'  '
                        elif 'True' in curr or 'False' in curr:
                            outVal+=' | '+curr
                        else:
                            formIt=72-len(curr)
                            outVal+='|'+' '+curr+' '*26

            print(outVal)
