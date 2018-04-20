#!/usr/bin/python
import socket

socket_server = socket.socket();
host_name = socket.gethostname();
socket_server.bind((host_name,9000));

socket_server.listen(2);

print "Server is listening";

while True:
    conn,addr = socket_server.accept();
    print "Server has accepted connection";

    if conn !=None:
        f = open("/home/prashanth/Desktop/p.img", "a+");
        buffer = conn.recv();
        while len(buffer) >0:
            if buffer =="$":
                print "Image file recieved";
                f.close()
                break;
            else:
                f.write(buffer);
                buffer = conn.recv();

        sf = open("/home/prashanth/Desktop/p_config.xml", "a+");
        buffer = conn.recv();
        while len(buffer) >0:
            if buffer== "#":
                print buffer;
                break;
            else:
                sf.write(buffer);
                buffer = conn.recv();
        print "File Transfer complete";
        conn.close();
    else:
        pass;
