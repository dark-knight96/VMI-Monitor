import pyvmi
import hashlib

def kernel_config(name):
    if(name == None):
        return 0;
    else:
        # get kernel hash value
        vm = pyvmi.init(name,"complete");
        if vm == None:
            return 0;
        else:
            kernel_start = vm.translate_ksym2v("_stext");
            kernel_end = vm.translate_ksym2v("_etext");
            file_input = open("./config/" + name+"_kernel", "w+");
            i = kernel_start;
            kernel_string = ""
            while i < kernel_end:
                memory = vm.read_va(i, 0, 512);
                kernel_string = kernel_string + memory;
                i = i + 512;

            hash = hashlib.md5(kernel_string).hexdigest();
            file_input.write("kernel_hash "+name+" "+ hash);
            file_input.close()
            print "Kernel_hash for "+name+" configured";
            return 1;
