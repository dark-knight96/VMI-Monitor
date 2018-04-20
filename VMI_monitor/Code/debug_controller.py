from process_list import process_g
from module_list import list_modules;
import sys

def debug_controller():
    print"Debug mode initiated";

    while True:
        vmname = raw_input("Enter vmname:");
        choice = input("1.Process list 2.Module list:");
        if choice == 1:
            process_g(vmname);
            option_cont = input("Do you like to continue? 1.Yes 2. No");
            if option_cont ==2:
                print "Good Bye!"
                sys.exit();
            else:
                pass;
        elif choice == 2:
            list_modules(vmname);
            option_cont = input("Do you like to continue? 1.Yes 2. No");
            if option_cont == 2:
                print "Good Bye!"
                sys.exit();
            else:
                pass;
        else:
            print "Incorrect option";
            sys.exit(0);
