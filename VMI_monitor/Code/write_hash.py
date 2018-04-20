import pyvmi
import hashlib
import sys


def write_sys_tab_hash(name):
    if name == None:
        return 0;
    else:
        vm = pyvmi.init(name, "complete")
        if (vm == None):
            print "Failed to start libvmi";
            return 0;
        else:
            # to create symbol file
            file = open("./guest_sysmap/"+name+"/"+name, "r");
            file2 = open("./config/"+name+"_hash", "w")
            sym_array = file.readlines();

            for i in sym_array:
                sym_split = i.split();
                sym_name = sym_split[2]
                sym_check = sym_name.split("_")
                if sym_check[0] =="sys":
                    content = vm.read_str_ksym(sym_name);
                    addr = vm.read_addr_ksym(sym_name);
                    hash = hashlib.md5(content).hexdigest();
                    file2.write(sym_name + " " + hash + "\n");
                elif sym_check == "":
                    sys.exit(0);
                else:
                    continue;

            file.close();
            file2.close();
        return 1;

