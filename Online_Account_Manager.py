#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:54:14 2018

@author: jackrusso

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"Jack Russo"

##
# Pi Password Generator / Online Account Manager
import random,string


print( "\n" + "Welcome to the Py Account Manager. If you would like to save your online account credentials, please log the following information:  ")

#strip dictionary file of strings, reload data
PyAccountsDictonary = {}
DoNotNamePasswordList = []

def main():
    def add_another():
        WebsiteName = input("What is the website?:                                           ") 
        PyAccountsDictonary[str(WebsiteName)] = []
        URL = input("What is the URL?:                                                       ")
        UserName = input("What is your user name?:                                           ")
        Email = input("What email do you use with this account?:                             ")
        
        def Generator():    
            l1 = random.choice(string.ascii_lowercase)
            l2 = random.choice(string.ascii_lowercase)
            l3 = random.choice(string.ascii_lowercase)
            l4 = random.choice(string.ascii_lowercase)
            l5 = random.choice(string.ascii_lowercase)
            l6 = random.choice(string.ascii_lowercase)
            l7 = random.choice(string.ascii_lowercase)
            l8 = random.choice(string.ascii_lowercase)
            l9 = random.choice(string.ascii_lowercase)
            l10 = random.choice(string.ascii_lowercase)
            l11 = random.choice(string.ascii_lowercase)
            l12 = random.choice(string.ascii_lowercase)
            password = str(l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10 + l11 + l12) 
            
            def Switch():
                if password in DoNotNamePasswordList:
                    Generator()
                else:
                    print("                                                                                " + password)
            Switch()
            
            def User_Preference():
                preference = input("Do you like this password?:                          ")
                if preference == 'Yes':
                    PyAccountsDictonary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'yes':
                    PyAccountsDictonary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'y':
                    PyAccountsDictonary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'No':
                    print("                                                                                                Ok, lets try something else:")
                    DoNotNamePasswordList.append(password)
                    Generator()
                elif preference == 'no':
                    print("                                                                                                Ok, lets try something else:")
                    DoNotNamePasswordList.append(password)
                    Generator()
                elif preference == 'n':
                    print("                                                                                                Ok, lets try something else:")
                    DoNotNamePasswordList.append(password)
                    Generator()
                else:
                    print("I'm sorry, I didn't quite get that.                                                            ")
                    User_Preference()
            User_Preference()
        Generator()
    add_another()    
    def New_Entry():
        addanother = input("You have added this account. Would you like to add another?: " + "\n" )
        if addanother == 'Yes':
            main()
        elif addanother == 'yes':
            main()
        elif addanother == 'y':
            main()
        elif addanother == 'No':
            print("                                                        Thank you for using Py Account Manager.")
        elif addanother == 'no':
            print("                                                        Thank you for using Py Account Manager.")
        elif addanother == 'n':
            print("                                                        Thank you for using Py Account Manager.")
        else:
            print("                                                        I'm sorry I didn't quite get that.")
            New_Entry()
    New_Entry()
main()


    
PyAccountsDictonary = str(PyAccountsDictonary)
PyAccountsDictonaryFile = open("PyAccountsDictonary.rtf", "w+")
PyAccountsDictonaryFile.write(PyAccountsDictonary)
PyAccountsDictonaryFile.close()

DoNotNamePasswordList = str(DoNotNamePasswordList)
DoNotNameListFile = open("DoNotNamePasswordAccounts.rtf", "w+")
DoNotNameListFile.write(DoNotNamePasswordList)
DoNotNameListFile.close()