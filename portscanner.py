import pyfiglet
import socket
from threading import Thread

print("-" * 70)
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print("-" * 70)


def check_port_type(port, is_open):
    if(is_open == 'o'):
        port_status = "  OPEN     "
    else:
        port_status = "  CLOSED   "

    if(port == 25):
        print('%4s' % port, port_status + "SMTP (Simple Mail Transfer Protocol)")
    elif (port == 21):
        print('%4s' % port, port_status + "FTP (File Transfer Protocol)")
    elif (port == 22):
        print('%4s' % port, port_status + "SSH (Secure Shell)")
    elif (port == 23):
        print('%4s' % port, port_status + "Telnet")
    elif (port == 53):
        print('%4s' % port, port_status + "DNS (Domain Name System)")
    elif (port == 80):
        print('%4s' % port, port_status + "Hypertext Transfer Protocol (HTTP)")
    elif (port == 443):
        print('%4s' % port, port_status + "HTTP (Hypertext Transport Protocol) and HTTPS (HTTP over SSL)")
    elif (port == 110):
        print('%4s' % port, port_status + "POP3 (Post Office Protocol version 3)")
    elif (port == 119):
        print('%4s' % port, port_status + "Network News Transfer Protocol (NNTP)")
    elif (port == 135):
        print('%4s' % port, port_status + "Windows RPC")
    elif (port == 137) or (port == 138) or (port == 139):
        print('%4s' % port, port_status + "Windows NetBIOS over TCP/IP")
    elif (port == 143):
        print('%4s' % port, port_status + "Internet Message Access Protocol (IMAP)")
    elif (port == 465):
        print('%4s' % port, port_status + "URL Rendezvous Directory for SSM (Cisco protocol)")
    elif (port == 1433) or (port == 1434):
        print('%4s' % port, port_status + "Microsoft SQL Server")
    else:
        print('%4s' % port, port_status + "Unknown")
        pass



def pScan(port, ip_target, show_clport_opt):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con = s.connect_ex((ip_target, port))
        if con == 0:
            check_port_type(port, 'o')
        else:
            if(show_clport_opt == 'y'):
                check_port_type(port, 'c')
        con.close()
    except:
        pass



def final_message():
    print('==========================================')
    print("Done Scanning.")


def start_multithrd_scan(ip_target, show_clport_opt,  min_port, max_port):
    """If you get a "RuntimeError: can't start new thread", then you are running to many threads, consider
        lowering the min and max."""
    min_p = int(min_port)
    max_p = int(max_port)
    for x in range(min_p, max_p):
        t = Thread(target=pScan, args=(x, ip_target, show_clport_opt))
        num_thrd.append(t)


    for i in range(0, len(num_thrd)):
        num_thrd[i].start()


    for i in range(0, len(num_thrd)):
        num_thrd[i].join()


    final_message()



def program_start():
    print('Running Port Scanner...')
    ip_target = input("Target Link/IP: ")
    show_clport_opt = input("Show Closed ports? (y/n) ")
    min_port = input("Pick Min Range of Port: ")
    max_port = input("Pick Max Range of Port: ")
    print('----------------------------------------')
    print('PORT | STATE |  SERVICE')
    print('----------------------------------------')
    start_multithrd_scan(ip_target, show_clport_opt, min_port, max_port)



num_thrd = []


program_start()


input("Press any key to quit the program...")
