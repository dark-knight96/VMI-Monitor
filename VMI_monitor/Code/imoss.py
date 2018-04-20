from operator import itemgetter
from config_controller import config_controller
from debug_controller import debug_controller
from root_kitscan import root_kit_scan
from kernel_check import kernel_check
from notify_via_mail import notify_by_email
from migrate_module import migrate


import sys
import multiprocessing
import time
import random
time_list =[];

def configure_main(cmd_param):
    vmlist= list();
#migrate vm names from cmdline
    for vm in cmd_param:
        vmlist.append(vm);
    vmlist.pop(0);
    vmlist.pop(0);
#to configure every vm
    config_stats = config_controller(vmlist);

    if config_stats == 1:
        print "Configuration Successfull";
        return 1;

    elif config_stats[0]=="c":
        print config_stats;
        sys.exit(0);

    else:
        print "Configuration error";
        sys.exit(0);

def hard_codeed_intervals(vmname):
    global time_list;

    while True:
        a = random.randint(0,100);
        if a in time_list:
            continue;
        else:
            time_list.append(a);
            return a;

def scan_call(vmname,delay):

    time.sleep(delay);
    root_res = root_kit_scan(vmname);
    kernel_res = kernel_check(vmname);
    if root_res ==1:
        root_dir = open("./roots", "a")
        root_dir.write(vmname+"\n");
        mail_res = notify_by_email(vmname,"rootkit");
        root_dir.close();               #Closed file pointer
        if mail_res ==0:
            print "Potential rootkit attack on %s"%(vmname)
    elif kernel_res == 1:
        mail_res = notify_by_email(vmname,"Kernel");
        if mail_res == 0:
            print "Possible Kernel modification on %s" %(vmname);
        else:
            return;
    else:
        print"%s is intact"%vmname;
        return;


if __name__ =="__main__":
    param_list = list(sys.argv);
    interval_array = {}
    if sys.argv[1] == "d":
        debug_controller();
    elif sys.argv[1] =="mig":
        name = raw_input("Enter vmname:")
        res = migrate(name);
        if res:
            print "%s migration successfull"%name;
        else:
            print "%s migration unsuccessfull"%name;
    elif sys.argv[1] == "m":
        config_result = configure_main(param_list);
        if config_result == 1:
            vmlist = list(param_list);
            vmlist = vmlist[2:];
            while 1:
                vm_l = list(vmlist);
                for vm in vm_l:
                    vm_interval = hard_codeed_intervals(vm);
                    vmname = vm;
                    vmname = multiprocessing.Process(target=scan_call,args=(vm,vm_interval,));
                    vmname.start();
                    vmname.join();
                    vm_l.pop(0);
                time.sleep(120);

        else:
            print "Scanner failed to start. Check LIBVMI configuration";
            sys.exit(0);
    else:
        print "Enter Valid mode.Good Bye!";
        sys.exit(0);
else:
    print "Invoke main properly";
    sys.exit(0);