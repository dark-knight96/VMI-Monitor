import write_hash
import kernel_config

def configure(name):
    status_array=[];
    if write_hash.write_sys_tab_hash(name):
        status_array.append(1);
    if kernel_config.kernel_config(name):
        status_array.append(1);

    stat = status_check(status_array)
    if stat:
        print "Configuration successful for "+ name;
        return 1;

    else:
        if stat == 1:
            print "Failed to configure systab hashes for "+name;
            return 0;
        elif stat == 2:
            print "Failed to configure kernel hash for" +name;
            return 0;

def status_check(status_array):
    for i in status_array:
        if i==1:
            continue
        else:
            return status_array.index(i);
    return 1;







