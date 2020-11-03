import pypresence
import os
import sys
import time
import subprocess
import requests

from config import configs as c 

def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')

def starter(rame,filen,guiv):
    endramen = rame + "G"
    endfilen = filen + ".jar"
    print("Please, check all information you entered")
    print("-----------------------------------------")
    print("Size of RAM: " + endramen)
    print("Server file name: " + endfilen)
    print("Use original gui? " + guiv)
    print("-----------------------------------------")
    correct = input("All infomation is correct? (Y - Yes | N - No) ")
    if correct == "y" or correct == "Y" or correct == "yes" or correct == "Yes":
        print("Checking file in local folder...")
        time.sleep(2)
        realfile = os.path.isfile('./' + filen)
        if realfile == True:
            print("We found it!")
            if guiv == "n":
                for output_line in run_command('java -Xmx' + rame + ' -Xms' + rame + ' -jar ' + filen + ' --nogui'):
                    print(output_line)
            else:
                for output_line in run_command('java -Xmx' + rame + ' -Xms' + rame + ' -jar ' + filen):
                    print(output_line)

        if realfile == False:
            print("File named " + endfilen + " not found")
    if correct == "n" or correct == "N" or correct == "no" or correct == "No":
        print("Please restart this app")
        exit()
    else:
        print("What do you mean by this?")

print("Добро пожаловать в Minerunner v" + c.ver + "!")
gitver = str(requests.get(
    "https://nicksaltfoxu.ml/versions/" + c.appn + "/version").text[:4])
offwebsiten = "NickSaltFoxu Repos"
if c.ver != gitver:
    print("You haveold version of this app! At this moment stable version is " +
          offwebsiten + " = " + gitver + ". Update it here https://github.com/BlueBerrySans365/minerunner!") #https://git.io/nsissuse
else:
    print("You have stable version for now. Thanks for using Minerunner!")
print("-------------------------------------------")
print("Please enter command. [help - for commands]")
opt = input()
if opt == "run":
    rame = input("Please, enter size of ram to use for server (only number in GB): ")
    filen = input("Please, enter name of server file (without .jar): ")
    guiv = input("Please choose, do you want to see original gui? (Y - Yes | N - No): ")
    starter(rame,filen,guiv)

