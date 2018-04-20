import pyvmi
import hashlib

def root_kit_scan(name):
    if name == None:
        return 0;
    else:
        hash_file_read =open("./config/"+name+"_hash","r");
        read_data = hash_file_read.readlines();
        # initialize vm
        vm = pyvmi.init(name,"complete")
        if vm == None:
            return 0;
        else:
            kernel_start= vm.translate_ksym2v("_stext");
            kernel_end = vm.translate_ksym2v("_etext");
            count =0;
            for i in read_data:
                hash_val_array = i.split();
                sym_name = hash_val_array[0];
                hash_val = hash_val_array[1];
                sym_va = vm.read_addr_ksym(sym_name);
                if sym_va <=kernel_end or sym_va>=kernel_start:
                    string = vm.read_str_ksym(sym_name);
                    re_hash_val = hashlib.md5(string).hexdigest();
                    if (re_hash_val != hash_val):
                        count = count + 1;
                        continue;
                    else:
                        continue;
                else:
                    count= count+1;

            if count>0:
                return count;
            else:
                return count;






