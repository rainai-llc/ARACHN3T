# Author: Jeremiah Jackson-Williams
#
# Email: rainai.inc@gmail.com # distorted.corp@gmail.com
# Copyrights: Rainai Inc. @2025
#


import os
import subprocess
import sys
from time import sleep,time
from spectralComFreeVersion import vectorize

def main():
    def dashBuild(statsDat):
        statsDatOut={}
        if 'https://' in statsDat:
            statsDat=statsDat.replace('https://','')
        elif 'http://' in statsDat:
            statsDat=statsDat.replace('http://','')
        else:
            next
        statsDat=statsDat.split(':')
        statsDat[0]=statsDat[0].replace('[','').replace(']','')
        statsDat[1]=statsDat[1].replace(' ','').replace('[','').replace(']','')
        buildDash=statsDat[0]
        userTarget=statsDat[1]
        try:
            print(buildDash, userTarget)
            if userTarget in os.listdir():
                pass
            else:
                os.mkdir(userTarget)
        except:
            pass
        statsDatOut=vectorize(userTarget).shift0().reconMata()
        def patch():
            full=''
            for currStateSelf in statsDatOut.keys():
                patch=f'''
                <div class="stat-box">
                        <p id="vector{currStateSelf}">{statsDatOut[currStateSelf][:statsDatOut[currStateSelf].index("=")+1]}<stong>PAID-SERVICE</strong></p>
                    </div>
    '''
                full+=patch
            return full
        with open(userTarget+'/'+'profile.html','w') as profile:
            link0=patch()
            print(link0)
            try:
                if "PAID-SERVICE" in link0:
                    profile.write(f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Results</title>
            <link rel="stylesheet" href="/styles2.css">
        </head>
        <body>
            <!-- Header and Menu -->
            <header class="header">
                <div class="logo">
                    <h1 class="title"><h1 class="title"><img class="topBar" src=/images/backdrop.png></h1></h1>
                </div>

                <div class="logout-btn-container">
                    <button class="logout-btn">Logout</button>
                </div>

                <nav class="nav">
                    <ul class="nav-links">
                        <li><a href="/home">Home</a></li>
                        <li><a href="https://www.linkedin.com/in/rainaiinc/">Updates</a></li>
                        <li><a href="/settings">Settings</a></li>
                    </ul>
                </nav>
            </header>

            <!-- Main Content Layout: Video Gallery + Dashboard -->
            <div class="main-content">
                <!-- Dashboard Section -->
                <div class="dashboard">
                    <h2>{buildDash[:6]}:<br>{userTarget}</h2>
                    <div class="stats-container" id='memoryLink0'>
                    {link0}
                    </div>
                    <button class="arrow-btn" id="SendOff" name="send-Hacks"><img class="arrowButton" src="/images/send.png"></button>
                </div>
                <script src='/scripts/inject.js'>
                <div class="main-content">
                <!-- Video Gallery Section -->
                    <div class="video-gallery">
                        <h2>Company Updates!</h2>
                        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7346593019984277504?collapsed=1" height="551" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
                    </div>
                </div>
            </div>
        </body>
        <div class="copyrightNotice">
            <footer><p>Copyrights:<br> Rainai Inc. @2025</p></footer>
        </div>
        </html>
        ''')
                    sleep(0.7)
                    profile.close()
                else:
                    profile.write(f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Results</title>
            <link rel="stylesheet" href="/styles2.css">
        </head>
        <body>
            <!-- Header and Menu -->
            <header class="header">
                <div class="logo">
                    <h1 class="title"><h1 class="title"><img class="topBar" src=/images/backdrop.png></h1></h1>
                </div>

                <div class="logout-btn-container">
                    <button class="logout-btn">Logout</button>
                </div>

                <nav class="nav">
                    <ul class="nav-links">
                        <li><a href="/home">Home</a></li>
                        <li><a href="https://www.linkedin.com/in/rainaiinc/">Updates</a></li>
                        <li><a href="/settings">Settings</a></li>
                    </ul>
                </nav>
            </header>

            <!-- Main Content Layout: Video Gallery + Dashboard -->
            <div class="main-content">
                <!-- Dashboard Section -->
                <div class="dashboard">
                    <h2>{buildDash[:6]}:<br>{userTarget}</h2>
                    <div class="stats-container">
                    <img class="modern0" src='/images/No Results.gif'>
                    </div>
                </div>
                <div class="main-content">
                <!-- Video Gallery Section -->
                    <div class="video-gallery">
                        <h2>Company Insights/Awareness!</h2>
                        <h1 class="internalUpdate">Coming Soon!</h1>
                        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7346593019984277504?collapsed=1" height="551" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
                    </div>
                </div>
            </div>
        </body>
        <div class="copyrightNotice">
            <footer><p>Copyrights:<br> Rainai Inc. @2025</p></footer>
        </div>
        </html>
        ''')
                    sleep(0.7)
                    profile.close()
            except:
                profile.write(f'''<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Results</title>
            <link rel="stylesheet" href="/styles2.css">
        </head>
        <body>
            <!-- Header and Menu -->
            <header class="header">
                <div class="logo">
                    <h1 class="title"><h1 class="title"><img class="topBar" src=/images/backdrop.png></h1></h1>
                </div>

                <div class="logout-btn-container">
                    <button class="logout-btn">Logout</button>
                </div>

                <nav class="nav">
                    <ul class="nav-links">
                        <li><a href="/home">Home</a></li>
                        <li><a href="https://www.linkedin.com/in/rainaiinc/">Updates</a></li>
                        <li><a href="/settings">Settings</a></li>
                    </ul>
                </nav>
            </header>

            <!-- Main Content Layout: Video Gallery + Dashboard -->
            <div class="main-content">
                <!-- Dashboard Section -->
                <div class="dashboard">
                    <h2>{buildDash[:6]}:<br>{userTarget}</h2>
                    <div class="stats-container">
                    <img class="modern0" src='/images/No Results.gif'>
                    </div>
                </div>
                <div class="main-content">
                <!-- Video Gallery Section -->
                    <div class="video-gallery">
                        <h2>Company Insights and Awareness!</h2>
                        <h1 class="internalUpdate">Coming Soon!</h1>
                        <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7346593019984277504?collapsed=1" height="551" width="504" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>
                    </div>
                </div>
            </div>
        </body>
        <div class="copyrightNotice">
            <footer><p>Copyrights:<br> Rainai Inc. @2025</p></footer>
        </div>
        </html>
        ''')
    dashBuild(sys.argv[1])
main()
