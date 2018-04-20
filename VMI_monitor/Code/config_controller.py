from config import configure
from time import gmtime, strftime

import sys

import os.path
import time


def config_controller(vmlist):
    sys_open = open("./roots","r");
    hacked_vm = sys_open.readlines();
    config_final =list();
    configure_list = open("./config/config_list", "a+");
    config_lis = configure_list.readlines();
    config_list = list();
    for entry in config_lis:
        name = entry.split();
        name = name[0];
        config_list.append(name);

    for vm in vmlist:
        if vm in hacked_vm:
            #extract timestamp
            for v in hacked_vm:
                temp = v.split();
                if vm in v:
                    _time = temp[1];
                else:
                    continue;

            result = check_time_stamp(vm,_time);
            if result:
                config_result  = configure(vm);
                if config_result:
                    config_final.append(vm);
                    continue;
                else:
                    return 0;
            else:
                st = "change sysmap for %s" %vm;
                return st;
        else:
            #check configure list
            if vm in config_list:
                config_final.append(vm);
                continue;
            else:
                config_result = configure(vm);
            if config_result:
                config_final.append(vm);
                continue;
            else:
                return 0;
    configure_list.close();
    if len(config_final) == len(vmlist):
        configure_list = open("./config/config_list","a+");
        for vm in config_final:
            if vm in config_list:
                continue;
            else:
                configure_list.write("\n"+vm+" "+strftime("%Y-%m-%d %H:%M:%S", gmtime()));
        configure_list.close();
        return 1;

def check_time_stamp(vmname,_time):
    # to know if file exists
    if os.path.exists("./guest_sysmap/"+vmname):
        #check time stamp change
        new_time = time.ctime(os.path.getctime("./guest_sysmap"+vmname));
        if new_time > _time:
            return 1;
        else:
            return 0;






