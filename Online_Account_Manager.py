# Pi Password Generator / Online Account Manager
import random,string
import numpy as np

print("\n" + "Py Account Manager." + "\n")

def main_first_use():
    print("\n" + "If you would like to save your online account credentials, please log the following information:" + "\n")
    PyAccountsDictionary = {} 
    def Print_Credentials():
        print("\n" + str(PyAccountsDictionary) + "\n")   
    def add_another():
        WebsiteName = input("What is the website?:                                           ") 
        PyAccountsDictionary[str(WebsiteName)] = []
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
            print("                                                                                " + password)
            def User_Preference():
                preference = input("Do you like this password?:                          ")
                if preference == 'Yes':
                    PyAccountsDictionary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'yes':
                    PyAccountsDictionary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'y':
                    PyAccountsDictionary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'No':
                    print("                                                                                                Ok, lets try something else:")   
                    Generator()
                elif preference == 'no':
                    print("                                                                                                Ok, lets try something else:")
                    Generator()
                elif preference == 'n':
                    print("                                                                                                Ok, lets try something else:")
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
            main_first_use()
        elif addanother == 'yes':
            main_first_use()
        elif addanother== 'y':
            main_first_use()
        elif addanother == 'No':
            print("\n" + "Thank you for using Py Account Manager.")
        elif addanother == 'no':
            print("\n" + "Thank you for using Py Account Manager.")
        elif addanother == 'n':
            print("\n" + "Thank you for using Py Account Manager.")
        else:
            print("                                                        I'm sorry I didn't quite get that.")
            New_Entry()
    New_Entry()
    def Review_Credentials():
       review = input("\n" + "Would you like to review your credentials?" + "\n")
       if review == 'Yes':
           Print_Credentials()
       elif review == 'yes':
           Print_Credentials()
       elif review == 'y':
           Print_Credentials()
       elif review == 'No':
           print("\n" + "Ok. Have a nice day" + "\n")
       elif review == 'no':
           print("\n" + "Ok. Have a nice day" + "\n")
       elif review == 'n':
           print("\n" + "Ok. Have a nice day" + "\n")
       else:
        print("\n" + "I'm sorry I didn't quite get that" + "\n")
        Review_Credentials()
    np.save('PyAccountsDictonary.npy', PyAccountsDictionary)
    Review_Credentials()       
    


def main_Prime():
    print("\n" + "If you would like to save your online account credentials, please log the following information:" + "\n")
    PyAccountsDictionary = {}
    PyAccountsDictionary = np.load('PyAccountsDictonary.npy').item()
    def Print_Credentials_Prime():
        print("\n" + str(PyAccountsDictionary) + "\n")
    
    def add_another_Prime():
        WebsiteName = input("What is the website?:                                           ") 
        PyAccountsDictionary[str(WebsiteName)] = []
        URL = input("What is the URL?:                                                       ")
        UserName = input("What is your user name?:                                           ")
        Email = input("What email do you use with this account?:                             ")
        
        def Generator_Prime():    
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
            print("                                                                                " + password)
            def User_Preference_Prime():
                preference = input("Do you like this password?:                          ")
                if preference == 'Yes':
                    PyAccountsDictionary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'yes':
                    PyAccountsDictionary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'y':
                    PyAccountsDictionary[str(WebsiteName)] = [("URL: " + str(URL)), (("User Name: ") + str(UserName)),( "Email: " + str(Email)),( "Password: " + password)]
                elif preference == 'No':
                    print("                                                                                                Ok, lets try something else:")
                    Generator_Prime()
                elif preference == 'no':
                    print("                                                                                                Ok, lets try something else:")
                    Generator_Prime()
                elif preference == 'n':
                    print("                                                                                                Ok, lets try something else:")
                    Generator_Prime()
                else:
                    print("I'm sorry, I didn't quite get that.                                                            ")
                    User_Preference_Prime()
            User_Preference_Prime()
        Generator_Prime()
    add_another_Prime()    
    def New_Entry_Prime():
        addanother = input("You have added this account. Would you like to add another?: " + "\n" )
        if addanother == 'Yes':
            main_Prime()
        elif addanother == 'yes':
            main_Prime()
        elif addanother== 'y':
            main_Prime()
        elif addanother == 'No':
            print("\n" + "Thank you for using Py Account Manager.")
        elif addanother == 'no':
            print("\n" + "Thank you for using Py Account Manager.")
        elif addanother == 'n':
            print("\n" + "Thank you for using Py Account Manager.")
        else:
            print("                                                        I'm sorry I didn't quite get that.")
            New_Entry_Prime()
    New_Entry_Prime()
    def Review_Credentials_Prime():
       review = input("\n" + "Would you like to review your credentials?" + "\n")
       if review == 'Yes':
           Print_Credentials_Prime()
       elif review == 'yes':
           Print_Credentials_Prime()
       elif review == 'y':
           Print_Credentials_Prime()
       elif review == 'No':
           print("\n" + "Ok. Have a nice day" + "\n")
       elif review == 'no':
           print("\n" + "Ok. Have a nice day" + "\n")
       elif review == 'n':
           print("\n" + "Ok. Have a nice day" + "\n")
       else:
        print("\n" + "I'm sorry I didn't quite get that" + "\n")
        Review_Credentials_Prime()
    np.save('PyAccountsDictonary.npy', PyAccountsDictionary)
    Review_Credentials_Prime()       
    

def check():
    use = input( "\n" + "Is this your first time using this application?:"  + "\n")
    if use == 'Yes':
        print("\n" + "Welcome!:" + "\n")
        main_first_use()
    elif use == 'yes':
        print("\n" + "Welcome!:" + "\n")
        main_first_use()
    elif use == 'y':
        print("\n" + "Welcome!:" + "\n")
        main_first_use()
    elif use == 'No': 
        print("\n" + "Welcome back!:" + "\n")
        main_Prime()
    elif use == 'no':
        print( "\n" + "Welcome back!:"  + "\n")
        main_Prime()
    elif use == 'n':
        print( "\n" + "Welcome back!:"  + "\n")
        main_Prime()
    else:
        print("\n" + "I'm sorry I didn't quite get that" "\n")
        check()
check()
