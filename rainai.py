#!/usr/bin/env python3

# Scientist: Jeremiah Jackson-Williams
#
# Copy right: Rainai Inc 2025
#
# Email: rainaiincorporated@gmail.com

# Recall CTA on session reset

from states import nState,stateZero,stateOne

def think(h) -> float|int:
    # Where h is message tokenized.
    import os as ground
    import subprocess as stack0
    # from nouns import nanv
    # from verbs import nanv
    # This is where all NTAMs will run to determing momentum
    # of value h
    s0=ground.getcwd()
    s0k0=ground.listdir()
    response=None
    hNk00=['.','?','!']
    hNk01=['who','what','when','why','how']
    hNk02=['yes','correct','yeah','yeah']
    h=str(h).lower()
    tmphNkMet={}
    def hNk0(h0) -> tuple:
        confirmType=None
        confirmConfirm=None
        for hNk01Token in hNk01:
            if hNk01Token in h0.lower():
                confirmType=True
                break
            else:
                confirmType=False
        for localH in hNk02:
            if localH in h:
                confirmConfirm=True
                break
            else:
                confirmConfirm=False
        return confirmType,confirmConfirm
    for localH in hNk00:
        tmphNkMet[localH]=h.count(localH)
    if tmphNkMet[hNk00[1]]!=0 and hNk0(h)==(True,True):
        return True,(1,1,1)
        tmphNkMet.clear()
    elif tmphNkMet[hNk00[1]]!=0 and hNk0(h)==(True,False):
        return True,(1,1,-1)
    elif tmphNkMet[hNk00[1]]!=0 and hNk0(h)==(False,False):
        return True,(1,-1,-1) #Analyze context prior to info sending message after info play.
    elif tmphNkMet[hNk00[1]]!=0 and hNk0(h)==(False,True):
        return True,(1,-1,1)
    else:
        if hNk0(h)==(True,True):
            return True,(1,1)
            tmphNkMet.clear()
        elif hNk0(h)==(True,False):
            return True,(1,-1)
        elif hNk0(h)==(False,True):
            return False,(-1,1)
        else:
            return False,(-1,-1)

    # for i in range(random(len(h))):
    #   if h{i} in k:
    #       response+=0.01
    # if response<-0.45:
    #   Respective certainty.
    #   speak(response)

class mya:
    def __init__(self,human,state=nState()):
        self.human=human
        self.state=state
        self.stateShift=-0.45
        self.stateCommit=-0.15
        self.stateAware=stateZero
        self.workReq=open('workReqTemp','a+')
        #
        # Security Model
        #
        #
        # Where certainty is met -> Awareness is held though bias is undetermined
        # Allow transparency by informing users this information is applicable for
        # learning, though, not accepted for security reasons. (Web app)
        # --->
        # Meeting compliance safety standards based off user choice.
        # Rainai Inc. has the right to refuse human prompts that do not align with out moral,
        # sociological, and economical beliefs. And will not be held responsible for any
        # activity or behavior derived from customer training choices. (Mobile App)
        #
    def knowSelf(self):
        # self is either aware of knowing of given (h) or knowingly aware of (h) certain
        # value
        # Map -1<=>0<=>1 to V (where V is v^n from C)
        return think(self.human)
        # while self.state!=self.stateAware:
        #     # Declare max M(emory) on the other end.
        #     self.State+=think()
    def editWorkRequest(self):
        self.workReq.write(self.human+'\n\n\n-[~ MYA ~] Rainai Inc. IAAI Systems:\t')
    def sendWorkRequest(self):
        import os
        import subprocess
        import json
        import sys
        import random
        import hashlib
        import re
        import smtplib
        from email.message import EmailMessage
        try:
                mail=EmailMessage()
                mail['Subject']="[~ MYA ~] - Work Request"
                self.workReq.seek(0)
                customerRequest=str(self.workReq.read())
                body=customerRequest
                mail.set_content(body, subtype='plain')
                mail['From']="rainaiincorporated@gmail.com"
                mail['To']="distorted.corp@gmail.com"
                try:
                    # Connect to the SMTP server
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        # Log in to your email account
                        smtp.login('rainaiincorporated@gmail.com', 'bdvz lqih wuuj zzhm')

                        # Send the email
                        smtp.send_message(mail)
                        print("Email sent successfully!")
                        self.workReq.close()
                        return True
                except Exception as e:
                    print(f"Error: {e}")
                    self.workReq.close()
        except:
            return False
    def selfManage(self,task=None):
        self.task=task
        tmpFileAuth=self.workReq.read()
    def sendPurchaseRequest(self):
            import os
            import subprocess
            import json
            import sys
            import random
            import hashlib
            import re
            import smtplib
            from email.message import EmailMessage
            try:
                    mail=EmailMessage()
                    mail['Subject']="[~ MYA ~] - Sale Made!"
                    customerRequest=str(self.human)
                    body=customerRequest
                    mail.set_content(body, subtype='plain')
                    mail['From']="rainaiincorporated@gmail.com"
                    mail['To']="distorted.corp@gmail.com"
                    try:
                        # Connect to the SMTP server
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            # Log in to your email account
                            smtp.login('rainaiincorporated@gmail.com', 'bdvz lqih wuuj zzhm')
                            # Send the email
                            smtp.send_message(mail)
                            print("Email sent successfully!")
                            return True
                    except Exception as e:
                        print(f"Error: {e}")
            except:
                return False


    # StateZero = 0
    # Setting applicable range by tens or hundredths based
    # based off sum.
    # In example 100.00 --> 50.00 --> 25.00 --> 5.00 --> 0.75
    # If h is valid increase from stateZero with all given
    # parameters where 1=100.
    # Base logic for algotithmically applying precision and accuracy scoring.
    # Said, False values reduce and are capable of reaching a negative score of StateOne itself.
    #
    # Lets say -1=-100.00
    # Current Tasks:
    # Default state for model is 0 or duality in a sense.
    # Knowing itself (definition in progress )and current state yet uknowing to fact h(s)needs.
    # The embedding.

    # After embedding and integration. Analysis summary should define purposes.
    #
    # Based on occupation, intuitively provide assistance that saves time.
    #
    # Example: Summary = Content Creator
    #
    # {"NTAM": {"Occupation":"Content-Creator,Director,Photographer,Streamer", "Action":"Sentify", "Token": "2c57d4b0297f7c7741ce8c738e0d54db8e925ec2a7c58e584e8513c014f9abef67aee2cac77bfbb78ddee6fe2572d3b17d9e89007d9a7442a48d4ed17024ddc6"}}
    #
    # mya(validate("Example message from authorized"), (validate(stateZero(-1))).
