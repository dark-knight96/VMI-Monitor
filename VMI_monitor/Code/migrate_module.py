import hashlib
import socket
import libvirt
import sys

def migrate(vmname):
    host_ip = socket.gethostname();
    port = int(raw_input("Enter Port"));
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    #socket_client.connect((host_ip,port));
    config_file = open("./boot/" + vmname + ".txt", "r");
    img_file = open("./boot/" + vmname + ".img", "r");

    con = libvirt.open("xen:///");
    if con ==None:
        print "cannot migrate. libvirt error";
        sys.exit(0);
    else:
        pass;
    dom = con.lookupByName(vmname);
    if dom ==None:
        print "cannot migrate. Libvirt error";
        sys.exit(0);
    else:
        pass;
    if dom.isActive()== True:
        shut_down = dom.shutdown();
        if shut_down==0:
            print "Shut down successfull";
        else:
            shut_down = dom.destroy();
            if shut_down == None:
                print "Cannot stop VM";
                sys.exit(0);
            else:
                pass;
    else:
        print "Domain is not active";

    config_hash,img_hash = get_hashes(config_file,img_file);

    try:
        
        while img_file.readline():
            # send image file
            data = img_file.readline();
            print data;
            socket_client.send(data);
        socket_client.send(img_hash);
        socket_client.send("$");

        print "Image file transfer successfull"
        print "Starting config file transfer"

        while config_file.read():
            data = config_file.readline();
            socket_client.send(data);
        socket_client.send(config_hash);
        print "Config file transferred"
        socket_client.send("#");

        #close socket
        socket_client.close();
        config_file.close()
        img_file.close();
        return 1;
        
    except Exception as e:
        print e;
        return 0;


def get_hashes(config_file,img_file):
    config_hash = hashlib.md5();
    while config_file.readline():
        data = config_file.readline();
        config_hash.update(data);

    img_hash = hashlib.md5();
    while img_file.readline():
        data = img_file.readline();
        img_hash.update(data);
    return config_hash.hexdigest(),img_hash.hexdigest();

migrate("project5");


