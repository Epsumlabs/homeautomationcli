from homeautomationcli.definations import (login, user_regd, profile, profile_edit, user_setting, user_setting_update,
                                           control_module,
                                           module_info, module_regd, module_config, forgot_1, forgot_2, password_update,
                                           history,
                                           regd_key, adminActions)
import sys


# Main Function
def entry():
    try:
        print("\n----------------------------------------------------")
        print("\n\nEpsum labs Home Automation Console App")
        print("Developed by Epsum labs Pvt. Ltd.")
        print("Authors : Suraj Kumar, Sai Prasad")
        print("Released Under MIT License")
        print("\n----------------------------------------------------")
        print("1- Login")
        print("Press any key to Register")
        choice = sys.stdin.readline()[:-1]
        assert choice == str(1)
        print("Enter your registered email with Epsumthings account : ")
        useremail = sys.stdin.readline()
        useremail = useremail[:-1]
        print("Enter you account password : ")
        userpass = sys.stdin.readline()
        userpass = userpass[:-1]
        print("\n")
        if useremail == "" or userpass == "":
            print("Please provide your username and password to login ...")
            entry()
        while (True):
            print("----------------------------------------------------")
            print("Logged In as : " + str(useremail) + "\n")
            print()
            print("Choose an option from the following menu : \n")
            print("1. Login ")
            print("2. User Registration")
            print("3. User Profile Display")
            print("4. User profile edit")
            print("5. Get User settings")
            print("6. Update user settings")
            print("7. Control modules")
            print("8. Module Info")
            print("9. Module registration")
            print("10. Module Configure")
            print("11. Forgot password step-1")
            print("12. Forgot password step-2")
            print("13. Update user password")
            print("14. Show History")
            print("15. Get Key for register")
            print("16. Admin Actions")
            print("0. Exit")
            choice = sys.stdin.readline()
            choice = int(choice[:-1])
            if choice == 1:
                login(useremail, userpass)
            elif choice == 2:
                user_regd()
            elif choice == 3:
                profile(useremail, userpass)
            elif choice == 4:
                profile_edit(useremail, userpass)
            elif choice == 5:
                user_setting(useremail, userpass)
            elif choice == 6:
                user_setting_update(useremail, userpass)
            elif choice == 7:
                control_module(useremail, userpass)
            elif choice == 8:
                module_info(useremail, userpass)
            elif choice == 9:
                module_regd(useremail, userpass)
            elif choice == 10:
                module_config(useremail, userpass)
            elif choice == 11:
                forgot_1(useremail, userpass)
            elif choice == 12:
                forgot_2(useremail, userpass)
            elif choice == 13:
                password_update(useremail, userpass)
            elif choice == 14:
                history(useremail, userpass)
            elif choice == 15:
                regd_key()
            elif choice == 16:
                adminActions()
            elif choice == 0:
                sys.exit()
            else:
                print("Invalid Choice")
            print("Press enter any key to continue")
            sys.stdin.readline()
    except KeyError:
        print(" You entered a wrong/invalid input.. Please enter a number from the menu... ")
        entry()
    except AssertionError:
        user_regd()
        entry()
    except KeyboardInterrupt:
        print("Exiting..")
        sys.exit(0)
    except ValueError:
        entry()
