import pyvmi

module=[];
def list_modules(vmname):
    vm = pyvmi.init(vmname,"complete");
    if vm == None:
        return 0;
    else:
        next_module = vm.translate_ksym2v("modules");
        list_head = next_module;
        while True:
            tmp_next = vm.read_addr_va(next_module,0);
            if list_head == tmp_next:
                break;
            else:
                if(vm.get_page_mode()=='ia32e'):
                    modname = vm.read_str_va(next_module+16,0);
                else:
                    modname = vm.read_str_va(next_module+8,0);

                print modname;
            next_module = tmp_next;



