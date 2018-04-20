import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def notify_by_email(vmname,attack):
    email_id = "imoss2k18@gmail.com"
    password = "ImossSVCE"
    mes = MIMEMultipart();
    if attack =="rootkit":
        message = "Potential %s attack on %s" % (attack, vmname);
    else:
        message ="Possible Kernel alteration on %s" %vmname;
    try:
        email_variable = smtplib.SMTP('smtp.gmail.com', 587);
        email_variable.starttls()
        #logging in
        email_variable.login(email_id,password);

        recv_email = fetch_mail(vmname);

        if recv_email == 0:
            return 0;
        else:
            mes['From'] = email_id;
            mes['To'] = recv_email;
            mes['Subject']= "Security Breach"
            mes.attach(MIMEText(message,'plain'));
            email_variable.sendmail("imoss2k18@gmail.com",recv_email,mes.as_string());
            email_variable.quit();
            return 1;
    except:
        return 0;

def fetch_mail(vmname):
    sender_det = open("./send_det.txt", "r");

    while 1:
        data_recv = sender_det.readline().split();
        if vmname in data_recv:
            recv_email = data_recv[1];
            break;
        else:
            continue;

    if recv_email == None:
        return 0;
    else:
        return recv_email;





