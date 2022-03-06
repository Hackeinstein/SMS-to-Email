import os
import time

print("""
|||||||  |||   ||   |||   ||||||| 
|||  ||| |||  ||||  |||   |||  |||  
|||  |||  ||| |||| |||    |||  |||  
|||  |||   ||||||||||     |||  |||  
|||||||     |||  ||||     ||||||| 
""")

print(' ------------------------------  NUMBER TO EMAIL TOOL---------------------------             ')
print('')

print('Select services')
print('(1) verizon (2) AT&T wireless (3)AT&T mobility (4)Boost mobile (5)Cricket (6)Metro PCS (7)Sprint[pcs] ')
print('(8)Sprint[Nextel] (9)Straight talk (10)Tmobile (11)U.S cellular (12)Virgin Mobile')
print("")
input_value=input("Enter option  ")

if input_value == "1":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("verizon.txt","a")
        email=number+"@vtext.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "2":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("att_wireless.txt","a")
        email=number+"@txt.att.net"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "3":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("att_mobility.txt","a")
        email=number+"@cingularme.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")

if input_value == "4":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("boost.txt","a")
        email=number+"@myboostmobile.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "5":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("cricket.txt","a")
        email=number+"@sms.mycricket.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "6":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("metro(pcs).txt","a")
        email=number+"@mymetropcs.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")

if input_value == "7":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("sprint(pcs).txt","a")
        email=number+"@messaging.sprintpcs.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")

if input_value == "8":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("sprint(nextel).txt","a")
        email=number+"@page.nextel.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "9":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("straight_talk.txt","a")
        email=number+"@vtext.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "10":
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("t-mobile.txt","a")
        email=number+"@tmomail.net"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "11":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("us_cellular.txt","a")
        email=number+"@email.uscc.net"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")
if input_value == "12":
    print("")
    filename =input('Enter list name:')

    file = open(filename, 'r')
    lines = file.readlines()

    for index, line in enumerate(lines):
        number=("{}".format( line.strip()))
        f = open("virgin_mobile.txt","a")
        email=number+"@vmobl.com"
        f.write(email+"\n")
        f.close()
        status="Done"
        print(email+" => "+status)
    
    x=input("thanks")


