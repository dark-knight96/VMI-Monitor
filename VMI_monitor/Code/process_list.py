import pyvmi


def process_list(vmname):
    vmi = pyvmi.init(vmname, "complete")

    taskoffset, nameoffset, pidoffset, init_task_va = get_offsets(vmi);

    processes = vmi.read_addr_va(init_task_va + taskoffset, 0)
    current_process = processes

    while True:
        pid = vmi.read_32_va(current_process + pidoffset - taskoffset, 0)
        procname = vmi.read_str_va(current_process + nameoffset - taskoffset, 0)

        yield pid, procname

        current_process = vmi.read_addr_va(current_process, 0)

        if current_process == processes:
            break

    return;


def process_g(vmname):
    for pid, procname in process_list(vmname):
        print "%d, %s" % (pid, procname)
    return;


def get_offsets(vmi):
    tasksOffset = vmi.get_offset("linux_tasks")
    nameOffset = vmi.get_offset("linux_name")
    pidOffset = vmi.get_offset("linux_pid")
    init_task_va = vmi.translate_ksym2v("init_task")
    return tasksOffset, nameOffset, pidOffset, init_task_va

