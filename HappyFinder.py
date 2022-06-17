#!/usr/bin/env python

"""Foobar.py: Description of what foobar does."""

__author__ = "Kartik Aggarwal(2002484) || Keshav(2002487)"
__copyright__ = "Copyright 2021, Planet Earth"
__version__ = "1.0"
"""
selenium==3.141.0
selenium-requests==1.3.3
text2emotion==0.0.5
pyfiglet==0.8.post1
matplotlib==3.5.0

"""
import argparse
import pyfiglet as pyfiglet
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import text2emotion as te
from matplotlib import pyplot as plt
import numpy as np

vars = {}
OPTIONS = ['Run Emotion Finder', 'Help', 'About']


def parsingopt():
    import chromedriver_autoinstaller
    chromedriver_autoinstaller.install()
    print(pyfiglet.figlet_format(text='Emotion Finder', font='standard'))
    print('Author: ' + __author__)
    print('Version: ' + __version__ + '\n')
    print('Copyright: ' + __copyright__ + '\n')
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-v', '--verbose',
                        action='store_true', help='Enable debugging')
    parser.add_argument('-i', required=True,
                        metavar='<wlan1>', dest='wnic', help='wlan int')
    parser.add_argument('-f', required=True,
                        metavar='<file>', dest='fd', help='Output file')
    if len(sys.argv) > 1:
        try:
            return parser.parse_args()
        except IOError as msg:
            parser.error(str(msg))

    for name in OPTIONS:
        print('[{}] {}'.format(OPTIONS.index(name) + 1, name))
    SELECTED = input("[*]Enter Your Choice : ")
    if SELECTED:
        if SELECTED.isnumeric():
            if int(SELECTED) == 1:
                username = input("\n\n\n[*]Enter the Username : ")
                print("\n\n[*] Running Emotion Finder ...\n\n")
                options = Options()
                options.headless = True
                driver = webdriver.Chrome(options=options,
                                          service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any',
                                                        '--web-security=false'])
                driver.set_window_size(1070, 800)
                driver.get("https://twitter.com/" + username + "")
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.XPATH, "//div[2]/div[2]/div/div/span")))
                vars["tweet1"] = driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/span").text
                # vars["tweet2"] = driver.find_element(By.XPATH, "//div[2]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div/div/span").text
                print("[*] Please Wait...")
                print(vars['tweet1'])
                # print(vars['tweet2'])
                driver.quit()
                labels = ['Happy', 'Angry', 'Surprise', 'Sad', 'Fear']
                data = []
                data_ = te.get_emotion(vars['tweet1'])
                # 			x = 0.333
                # print(str(int(data_['Fear']*100)) + "%)
                data.append(str(int(data_['Happy'] * 100)))
                data.append(str(int(data_['Angry'] * 100)))
                data.append(str(int(data_['Surprise'] * 100)))
                data.append(str(int(data_['Sad'] * 100)))
                data.append(str(int(data_['Fear'] * 100)))
                print(data, data_)
                explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
                fig1, ax1 = plt.subplots()
                ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.show()
            elif int(SELECTED) == 2:
                print("\n[1] :  Setup required Dependencies.")
                print("\n[2] :  Try using on cmd - pip install -r requirements.txt ")
                print("\n[3] :  For more information contact at 2002484.cse.cec@cgc.edu.in!")
            elif int(SELECTED) == 3:
                print("\n[*] : This is Kartik and We are in 2021.")
                print("\n[*] : __________Corona Literally Killed us then why Omnicron! 🥲 ____________")
            else:
                print("\n[*] : Invalid Option Selected. Please Try again.")
                print("\n[*] : _________That's really what we do When we choose Wrong Option._________")
        else:
            print("\n*****Invalid Input, Please Try again.*****")

    else:
        print("\n*****Thanks For Using this App.*****")


parsingopt()

input()