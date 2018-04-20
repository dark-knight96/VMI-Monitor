import pyvmi
import hashlib

#Checks if kernel is compromised

def kernel_check(name):
    if name == None:
        return 0;
    else:
        string =""
        vm = pyvmi.init(name,"complete");
        kernel_start = vm.translate_ksym2v("_stext");
        kernel_end = vm.translate_ksym2v("_etext");
        i=kernel_start;
        while i<kernel_end:
            memory = vm.read_va(i,0,512);
            string = string +memory;
            i=i+512;

        # time to hash it
        final_hash = hashlib.md5(string).hexdigest();
        init_kernel = open("./config/"+name+"_kernel","r");
        while True:
            kernel_initial = init_kernel.readline().split();
            if kernel_initial[1]== name:
                init_hash =kernel_initial[2];
                break;
            else:
                continue;
        if(final_hash != init_hash):
            init_kernel.close()
            return 1;
        else:
            init_kernel.close()
            return 0;




