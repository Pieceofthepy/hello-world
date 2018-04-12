#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 09:31:12 2018

@author: jackrusso
"""
"Jack Russo"

# Py Random Name Generator
import random,string
import pickle

print( "\n" + "Welcome to the Py Baby Name Generator.")


def add_another_first_use():
    DoNotNameList = []
    def Generator():    
        l1 = random.choice(string.ascii_lowercase)
        l2 = random.choice(string.ascii_lowercase)
        l3 = random.choice(string.ascii_lowercase)
        l4 = random.choice(string.ascii_lowercase)
        l5 = random.choice(string.ascii_lowercase)
        name = str(l1 + l2 + l3 + l4 + l5 ) 
        def Switch():
            if name in DoNotNameList:
                Generator()
            else:
                print("\n" + name + "\n")
        Switch() 
        def reload():
            addanother = input("You have named your child. Would you like to name another?: " + "\n" + "\n")    
            if addanother == 'Yes':
                add_another_first_use()
            elif addanother == 'yes':
                add_another_first_use()
            elif addanother == 'y':
                add_another_first_use()
            elif addanother == 'No':
                print("\n" + "Thank you for using Py Baby Name Generator. " + "\n" )
            elif addanother == 'no':
                print("\n" + "Thank you for using Py Baby Name Generator." + "\n" )
            elif addanother == 'n':
                print("\n" + "Thank you for using Py Baby Name Generator." + "\n")
            else:
                print("I'm sorry I didn't quite get that." + "\n" + "\n")
                reload()
        def User_Preference():
            preference = input("Do you like this Baby Name?:" + "\n" + "\n")
            if preference == 'Yes':
                reload()
            elif preference == 'yes':
                reload()
            elif preference == 'y':
                reload()
            elif preference == 'No':
                print("                                                                                                Ok, lets try something else:")
                DoNotNameList.append(name)
                add_another_first_use()
                
            elif preference == 'no':
                print("                                                                                                Ok, lets try something else:")
                DoNotNameList.append(name)
                add_another_first_use()
            elif preference == 'n':
                print("                                                                                                Ok, lets try something else:")
                DoNotNameList.append(name)
                add_another_first_use()
            else:
                print( "\n" + "I'm sorry, I didn't quite get that. " + "\n" )
                User_Preference()      
        User_Preference()
        with open('outfile', 'wb') as fp:
          pickle.dump(DoNotNameList, fp) 
    Generator()

def Main():
    DoNotNameList = []
    with open('outfile', 'rb') as fp:
        DoNotNameList = pickle.load(fp)
    def add_another_Prime():
        def Generator():    
            l1 = random.choice(string.ascii_lowercase)
            l2 = random.choice(string.ascii_lowercase)
            l3 = random.choice(string.ascii_lowercase)
            l4 = random.choice(string.ascii_lowercase)
            l5 = random.choice(string.ascii_lowercase)
            name = str(l1 + l2 + l3 + l4 + l5 ) 
            def Switch():
                if name in DoNotNameList:
                    Generator()
                else:
                    print("\n" + name + "\n")
            Switch() 
            def reload():
                addanother = input("You have named your child. Would you like to name another?: " + "\n" + "\n")    
                if addanother == 'Yes':
                    add_another_Prime()
                elif addanother == 'yes':
                    add_another_Prime()
                elif addanother == 'y':
                    add_another_Prime()
                elif addanother == 'No':
                    print("\n" + "Thank you for using Py Baby Name Generator. " + "\n" )
                elif addanother == 'no':
                    print("\n" + "Thank you for using Py Baby Name Generator." + "\n" )
                elif addanother == 'n':
                    print("\n" + "Thank you for using Py Baby Name Generator." + "\n")
                else:
                    print("I'm sorry I didn't quite get that." + "\n" + "\n")
                    reload()
            def User_Preference():
                preference = input("Do you like this Baby Name?:" + "\n" + "\n")
                if preference == 'Yes':
                    reload()
                elif preference == 'yes':
                    reload()
                elif preference == 'y':
                    reload()
                elif preference == 'No':
                    print("                                                                                                Ok, lets try something else:")
                    DoNotNameList.append(name)
                    add_another_Prime()
                    
                elif preference == 'no':
                    print("                                                                                                Ok, lets try something else:")
                    DoNotNameList.append(name)
                    add_another_Prime()
                elif preference == 'n':
                    print("                                                                                                Ok, lets try something else:")
                    DoNotNameList.append(name)
                    add_another_Prime()
                else:
                    print( "\n" + "I'm sorry, I didn't quite get that. " + "\n" )
                    User_Preference()      
            User_Preference()
            with open('outfile', 'wb') as fp:
              pickle.dump(DoNotNameList, fp)
        Generator()
    add_another_Prime()

def check():
    use = input( "\n" + "Is this your first time using this application?:"  + "\n")
    if use == 'Yes':
        print("\n" + "Welcome!:" + "\n")
        add_another_first_use()
    elif use == 'yes':
        print("\n" + "Welcome!:" + "\n")
        add_another_first_use()
    elif use == 'y':
        print("\n" + "Welcome!:" + "\n")
        add_another_first_use()
    elif use == 'No': 
        print("\n" + "Welcome back!:" + "\n")
        Main()
    elif use == 'no':
        print( "\n" + "Welcome back!:"  + "\n")
        Main()
    elif use == 'n':
        print( "\n" + "Welcome back!:"  + "\n")
        Main()
    else:
        print("\n" + "I'm sorry I didn't quite get that" "\n")
        check()
check()