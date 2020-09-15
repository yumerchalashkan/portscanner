from portscanner import *
import sys



def main():
    try:
        ip = input("Enter an ip address\n")
        scanner_object = PortScanner(ip)
        fake_control = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fake_control.settimeout(0.1)
        fake_control.connect_ex((ip,80))
    except:
        print("invalid ip address\n")
    else:
        argv = sys.argv[1]
        if argv != "-range" and argv != "-all":
            try:
                result = scanner_object.scan(int(argv))
            except:
                print("invalid port number")
            else:
                if result:
                    print(argv," : ","open")
                else:
                    print(argv," : ","closed")
        elif argv == "-all":
            result = scanner_object.scan_all_for_console()
            for i in result:
                print(i," : ","open")
            if not result:
                    print("all ports is closed")
        elif argv == "-range":
            try:
                first = int(sys.argv[2])
                last = int(sys.argv[3])
                result = scanner_object.scan_range(first,last)
            except:
                print("invalid port number")
            else:
                for i in result:
                    print(i," : ","open")
                if not result:
                    print("all ports is closed")
        else:
            print("invalid command")

if __name__ == "__main__":
    main()